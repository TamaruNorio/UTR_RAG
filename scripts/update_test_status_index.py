#!/usr/bin/env python3
"""TEST_STATUS_INDEX.md を、実際のコマンドカードのfrontmatterから自動生成し直す。

このスクリプトが解決する問題:
    verification_status（実機確認状態）の一覧表を、
    54行を手で書き写して作ると、どこかで1文字ズレる。
    このスクリプトは、各コマンドカードのfrontmatterを機械的に読んで
    表を組み立てるので、手作業のミスが起きない。

Thonnyでの使い方:
1. Thonnyでこのファイルを開く
2. 緑の「実行」ボタン（F5）を押すだけ
3. 「更新しました」というメッセージが出れば完了
4. 念のため scripts/check_docs.py も実行して OK になることを確認する

このスクリプトは TEST_STATUS_INDEX.md の frontmatter（先頭の---で
囲まれた部分）はそのまま残し、本文（表の部分）だけを作り直します。
"""
import sys
import pathlib

# 同じ scripts フォルダにある check_docs.py の関数を再利用する
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_docs  # noqa: E402

TARGET = check_docs.CARDS_ROOT / "TEST_STATUS_INDEX.md"


def extract_frontmatter_block(text: str) -> str:
    """既存ファイルの先頭にある ---...--- の frontmatter ブロックをそのまま取り出す。
    frontmatterが見つからない場合は空文字を返す(呼び出し側でエラー表示)。
    """
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    return f"---{parts[1]}---\n"


def build_body(cards: list) -> str:
    by_status: dict[str, list] = {}
    for c in cards:
        by_status.setdefault(c["verification_status"], []).append(c)

    lines = []
    lines.append("\n# 実機確認ステータス索引")
    lines.append("")
    lines.append(
        "この索引は、`scripts/check_docs.py` と同じロジック"
        "（`scripts/update_test_status_index.py`）で、"
        "各コマンドカードのfrontmatterから自動生成したものです。"
    )
    lines.append(
        "全54コマンドを個別に実機送信済みであることを示すものではありません。"
        "各カードの詳細な確認内容は、カード本体の「9. 実機確認」を参照してください。"
    )
    lines.append("")
    lines.append(f"最終更新時点のカード枚数: {len(cards)}件")
    lines.append("")

    for status in sorted(by_status):
        items = by_status[status]
        lines.append(f"## {status}（{len(items)}件）")
        lines.append("")
        lines.append("| コマンド | カード | detail | sub |")
        lines.append("|---|---|---|---|")
        for c in sorted(items, key=lambda x: x["filename"]):
            lines.append(
                f"| `{c['command_byte']}` | [{c['title']}]({c['filename']}) | "
                f"`{c['detail_command']}` | `{c['subcommand']}` |"
            )
        lines.append("")

    lines.append("## 更新方法")
    lines.append("")
    lines.append(
        "この表は手動で行を書き写さず、"
        "`python scripts/update_test_status_index.py` を実行して更新してください。"
        "カードのfrontmatterに`verification_status`を追加・変更した場合は、"
        "このスクリプトを再実行するだけで表が更新されます。"
    )
    lines.append("")
    lines.append("公式PDFが一次情報です。この索引は公式PDFの代替ではありません。")
    lines.append("")

    return "\n".join(lines)


def main():
    errors: list[str] = []
    cards, _ = check_docs.collect_cards(errors)

    if errors:
        print("=== 先にこのエラーを直してください ===")
        for e in errors:
            print(f"ERROR: {e}")
        sys.exit(1)

    if not TARGET.exists():
        print(f"ERROR: {TARGET} が見つかりません。", file=sys.stderr)
        sys.exit(2)

    existing_text = TARGET.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter_block(existing_text)
    if not frontmatter:
        print(f"ERROR: {TARGET} にfrontmatterが見つかりませんでした。", file=sys.stderr)
        sys.exit(2)

    new_text = frontmatter + build_body(cards)
    TARGET.write_text(new_text, encoding="utf-8")

    print(f"更新しました: {TARGET}")
    print(f"カード枚数: {len(cards)}")
    print("次に scripts/check_docs.py を実行してOKになることを確認してください。")


if __name__ == "__main__":
    main()
