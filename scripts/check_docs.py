#!/usr/bin/env python3
"""docs/current 配下の整合性チェック。

チェック内容:
- frontmatter の必須キーが揃っているか
- related_docs のリンク先が実在するか
- コマンドカード数が想定 (54) と一致するか
- verification_status の値を集計する

使い方（Thonnyでも、コマンドラインでもOK）:
    python scripts/check_docs.py

Thonnyで実行する場合:
1. Thonnyでこのファイルを開く
2. 緑の「実行」ボタン（F5）を押すだけ
   （引数は不要。カレントフォルダがどこでもリポジトリのルートを自動で見つけます）
"""
import sys
import pathlib

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML が必要です。\n"
        "Thonnyの場合: 上部メニュー『ツール』→『パッケージを管理』→ 検索欄に pyyaml と入力してインストール。\n"
        "コマンドラインの場合: pip install pyyaml",
        file=sys.stderr,
    )
    sys.exit(2)

# このファイル(scripts/check_docs.py)からリポジトリのルートを自動特定する。
# Thonnyでカレントフォルダがずれていても問題なく動くようにするため。
ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_ROOT = ROOT / "docs" / "current"
CARDS_ROOT = DOCS_ROOT / "commands" / "cards"
EXPECTED_CARD_COUNT = 54

# INDEX/README系はカード本体の枚数カウント・一覧生成の対象から除外する
NON_CARD_NAMES = {
    "README.md", "AI_RETRIEVAL_INDEX.md", "OPERATION_LEVEL_INDEX.md",
    "SAFETY_INDEX.md", "TEST_STATUS_INDEX.md",
}

REQUIRED_KEYS = {
    "title", "doc_type", "package_scope", "manual", "manual_version",
    "verification_status", "result_status", "related_docs", "tags",
}


def load_frontmatter(md_path: pathlib.Path):
    """1ファイルのfrontmatter(YAML部分)を辞書として読み込む。
    frontmatterが無いファイル(READMEなど)はNoneを返す。
    """
    text = md_path.read_text(encoding="utf-8")
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        return {"__yaml_error__": str(exc)}


def check_file(md_path: pathlib.Path, errors: list):
    """1ファイルのfrontmatterを検証し、辞書を返す(検証対象外ならNone)。"""
    fm = load_frontmatter(md_path)
    if fm is None:
        return None

    if "__yaml_error__" in fm:
        errors.append(f"{md_path}: YAML解析エラー: {fm['__yaml_error__']}")
        return None

    missing = REQUIRED_KEYS - fm.keys()
    if missing:
        errors.append(f"{md_path}: frontmatter必須キー欠落: {sorted(missing)}")

    related = fm.get("related_docs")
    if related is not None:
        if not isinstance(related, list):
            errors.append(f"{md_path}: related_docsが配列ではありません")
        else:
            for rel in related:
                if not isinstance(rel, str):
                    continue
                target = (md_path.parent / rel).resolve()
                if not target.exists():
                    errors.append(f"{md_path}: リンク切れ related_docs -> {rel}")

    return fm


def collect_cards(errors: list):
    """全コマンドカードのfrontmatterを読み込み、カード情報のリストを返す。
    check_docs.py と update_test_status_index.py の両方から使う共通処理。
    """
    if not CARDS_ROOT.exists():
        errors.append(f"{CARDS_ROOT} が見つかりません。")
        return [], []

    card_files = sorted(CARDS_ROOT.glob("*.md"))
    card_only_files = [f for f in card_files if f.name not in NON_CARD_NAMES]

    cards = []
    for md_path in card_only_files:
        fm = check_file(md_path, errors)
        if fm is None:
            continue
        cards.append({
            "title": fm.get("title", md_path.stem),
            "filename": md_path.name,
            "command_byte": fm.get("command_byte") or "-",
            "detail_command": fm.get("detail_command") or "-",
            "subcommand": fm.get("subcommand") or "-",
            "verification_status": fm.get("verification_status", "UNKNOWN"),
        })

    # カード以外のdocs/current配下のmdファイル(INDEX系・ガイド類)もリンク切れだけ確認する
    all_docs = list(DOCS_ROOT.rglob("*.md"))
    for md_path in all_docs:
        if md_path in card_only_files:
            continue
        check_file(md_path, errors)

    return cards, card_only_files


def main():
    errors: list[str] = []

    cards, card_only_files = collect_cards(errors)
    total_cards = len(card_only_files)

    verification_counts: dict[str, list] = {}
    for c in cards:
        verification_counts.setdefault(c["verification_status"], []).append(c)

    print("=== verification_status 集計 ===")
    for status, items in sorted(verification_counts.items()):
        print(f"{status}: {len(items)}件")
    print()

    print("=== 詳細一覧（frontmatterから抽出）===")
    for status, items in sorted(verification_counts.items()):
        print(f"\n## {status}")
        for c in sorted(items, key=lambda x: x["filename"]):
            print(f"- {c['title']} | {c['filename']} | {c['command_byte']}/{c['detail_command']}")

    print()
    print("=== カード枚数チェック ===")
    print(f"検出カード数: {total_cards} (想定: {EXPECTED_CARD_COUNT})")
    if total_cards != EXPECTED_CARD_COUNT:
        errors.append(
            f"カード数不一致: 検出{total_cards}件 / 想定{EXPECTED_CARD_COUNT}件"
        )

    print()
    if errors:
        print(f"=== NG: {len(errors)}件のエラー ===")
        for e in errors:
            print(f"ERROR: {e}")
        sys.exit(1)

    print("OK: docs check passed")
    print(f"cards: {total_cards}")
    print("broken_links: 0")


if __name__ == "__main__":
    main()
