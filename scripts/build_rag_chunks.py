#!/usr/bin/env python3
"""docs/current 配下のMarkdownを、ベクトルDB登録用にチャンク分割する。

設計方針（汎用的な安全値。特定の埋め込みモデルに依存しない）:
    - 目標チャンクサイズ: 500字程度
    - ハード上限: 1000字（これを超える場合はさらに分割する）
    - 分割の優先順位:
        1. "## " 見出し単位（コマンドカードの節構成に対応）
        2. 上記がハード上限を超える場合、"### " 見出し単位でさらに分割
        3. それでも超える場合、空行区切りの段落単位で貪欲にまとめる
           （_raw.md のような見出しなしファイルは、最初からこの段階に入る）
    - 分割の基準は日本語の文字数（char）とする。埋め込みモデルによってトークン化は
      異なるため、厳密なトークン数ではなく、十分に安全側の文字数で管理する。
      日本語は1文字あたり1トークン相当になる場合があるため、500字は
      おおよそ500トークン相当（やや安全側）とみなせる。

各チャンクには、元カードのfrontmatter（command_byte, verification_status,
tags等）をメタデータとして付与する。これにより、チャンク単体を検索結果として
取得した際も、どのコマンド・どの節かが分かる。

使い方:
    python scripts/build_rag_chunks.py
    → rag_chunks/chunks.jsonl を生成する（生成物はコミット対象外。
      .gitignore で除外される想定。スクリプト自体をリポジトリの一部として
      利用者が手元で実行し、その時点のベクトルDB登録用データを作る）
"""
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML が必要です。`pip install pyyaml` を実行してください。", file=sys.stderr)
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_ROOT = ROOT / "docs" / "current"
OUTPUT_PATH = ROOT / "rag_chunks" / "chunks.jsonl"

TARGET_CHARS = 500
HARD_MAX_CHARS = 1000


def load_frontmatter_and_body(path: pathlib.Path):
    text = path.read_text(encoding="utf-8").lstrip("\ufeff")
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    fm = yaml.safe_load(parts[1]) or {}
    return fm, parts[2]


def split_by_heading(text: str, marker: str):
    """指定した見出しマーカー（"## " または "### "）で分割する。
    見出しが1つも無ければ、テキスト全体を1要素のリストとして返す。
    """
    pattern = re.compile(rf"\n(?=\{marker[0]}{{{len(marker) - 1}}} )")
    # markerは "## " や "### " を想定。正規表現を安全に組み立てる。
    hashes = marker.strip()
    pattern = re.compile(rf"\n(?=^{re.escape(hashes)} )", re.MULTILINE)
    parts = pattern.split(text.strip())
    return [p for p in parts if p.strip()]


def split_markdown_table(paragraph: str, hard_max: int, rows_per_chunk: int = 12):
    """Markdown表（| で始まる行の連続）を、ヘッダー行＋区切り行を
    各チャンクに複製しながら、行単位で分割する。
    表以外の場合はNoneを返す。
    """
    lines = paragraph.strip().splitlines()
    if len(lines) < 3:
        return None
    if not (lines[0].lstrip().startswith("|") and lines[1].lstrip().startswith("|")):
        return None
    if not re.match(r"^\|?[\s:|-]+\|?$", lines[1].strip()):
        return None

    header = lines[0]
    separator = lines[1]
    body_rows = lines[2:]
    if not body_rows:
        return None

    chunks = []
    for i in range(0, len(body_rows), rows_per_chunk):
        group = body_rows[i:i + rows_per_chunk]
        chunk_text = "\n".join([header, separator] + group)
        chunks.append(chunk_text)
    return chunks


def split_field_enumeration(paragraph: str, hard_max: int, lines_per_chunk: int = 10):
    """罫線(|)を使わない「ラベル名 バイト数 内容」形式のフィールド列挙
    （［コマンド］［ACKレスポンス］などの後に続く行の並び）を、
    先頭の見出し行（［...］や「ラベル名 バイト数 内容」ヘッダ）を
    各チャンクに複製しながら、行単位で分割する。
    該当しない場合はNoneを返す。
    """
    lines = paragraph.strip("\n").splitlines()
    if len(lines) < 6:
        return None

    # 先頭〜3行目までの範囲で「見出し」行を探す:
    #   ［コマンド］［ACK レスポンス］等のブラケット行、
    #   または「ラベル名」「バイト数」「内容」を含むヘッダ行
    # ヘッダ行の直前に短い説明文（①など）が挟まっている場合も、
    # まとめてheader_linesに含める。
    header_lines = []
    body_start = None
    scan_range = min(3, len(lines))
    for i in range(scan_range):
        stripped = lines[i].strip()
        is_bracket = stripped.startswith("［") or stripped.startswith("[")
        is_table_header = ("ラベル名" in stripped and "バイト数" in stripped)
        if is_bracket or is_table_header:
            header_lines = lines[: i + 1]
            body_start = i + 1
            break

    if not header_lines or body_start is None:
        return None

    body_lines = lines[body_start:]
    if len(body_lines) < 4:
        return None

    header_text = "\n".join(header_lines)
    chunks = []
    i = 0
    while i < len(body_lines):
        group = body_lines[i:i + lines_per_chunk]
        chunk_text = header_text + "\n" + "\n".join(group)
        # 1グループでも大きすぎる場合は、grouping数を段階的に減らす
        shrink = lines_per_chunk
        while len(chunk_text) > hard_max and shrink > 1:
            shrink -= 1
            group = body_lines[i:i + shrink]
            chunk_text = header_text + "\n" + "\n".join(group)
        chunks.append(chunk_text)
        i += len(group)
    return chunks


def split_paragraphs_greedy(text: str, target: int, hard_max: int):
    """見出しに頼らず、空行区切りの段落を貪欲にまとめてチャンク化する。
    _raw.md のような見出しなしファイルの最終手段として使う。
    Markdown表は行単位（ヘッダー行を複製）、罫線なしのフィールド列挙
    （［コマンド］等の後の一行一項目リスト）も行単位でさらに分割する。
    """
    paragraphs = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    if not paragraphs:
        return [text.strip()] if text.strip() else []

    chunks = []
    current = ""
    for p in paragraphs:
        if len(p) > hard_max:
            table_pieces = split_markdown_table(p, hard_max)
            if table_pieces:
                if current:
                    chunks.append(current)
                    current = ""
                chunks.extend(table_pieces)
                continue

            field_pieces = split_field_enumeration(p, hard_max)
            if field_pieces:
                if current:
                    chunks.append(current)
                    current = ""
                chunks.extend(field_pieces)
                continue

        candidate = (current + "\n\n" + p).strip() if current else p
        if len(candidate) <= target or not current:
            current = candidate
        else:
            chunks.append(current)
            current = p
        if len(current) > hard_max and current == p:
            chunks.append(current)
            current = ""
    if current:
        chunks.append(current)
    return chunks


def recursive_split(text: str, target: int, hard_max: int, depth: int = 0):
    """## → ### → 段落、の順で再帰的に分割する。"""
    if len(text) <= hard_max:
        return [text.strip()]

    if depth == 0:
        parts = split_by_heading(text, "## ")
        if len(parts) > 1:
            result = []
            for p in parts:
                result.extend(recursive_split(p, target, hard_max, depth=1))
            return result
        # ##見出しが無い（_raw.md等）場合は、段落分割に進む
        return recursive_split(text, target, hard_max, depth=2)

    if depth == 1:
        parts = split_by_heading(text, "### ")
        if len(parts) > 1:
            result = []
            for p in parts:
                result.extend(recursive_split(p, target, hard_max, depth=2))
            return result
        return recursive_split(text, target, hard_max, depth=2)

    # depth >= 2: 段落単位の貪欲分割（最終手段）
    return split_paragraphs_greedy(text, target, hard_max)


def extract_heading_title(chunk_text: str) -> str:
    first_line = chunk_text.strip().splitlines()[0] if chunk_text.strip() else ""
    m = re.match(r"^#{2,3}\s+(.*)", first_line)
    return m.group(1).strip() if m else first_line[:60]


def build_chunks():
    chunks = []
    over_hard_max = []

    md_files = sorted(DOCS_ROOT.rglob("*.md"))
    for path in md_files:
        fm, body = load_frontmatter_and_body(path)
        if fm is None:
            # frontmatterが無いファイル(READMEなど)もチャンク化はするが、
            # メタデータは最小限にする
            fm = {}

        rel_path = path.relative_to(ROOT).as_posix()
        pieces = recursive_split(body, TARGET_CHARS, HARD_MAX_CHARS)

        for i, piece in enumerate(pieces, start=1):
            chunk_id = f"{rel_path}#chunk{i}"
            char_count = len(piece)
            if char_count > HARD_MAX_CHARS:
                over_hard_max.append((chunk_id, char_count))

            chunk = {
                "chunk_id": chunk_id,
                "source_file": rel_path,
                "section_title": extract_heading_title(piece),
                "char_count": char_count,
                "text": piece,
                "metadata": {
                    "title": fm.get("title"),
                    "doc_type": fm.get("doc_type"),
                    "package_scope": fm.get("package_scope"),
                    "manual": fm.get("manual"),
                    "manual_version": fm.get("manual_version"),
                    "command_byte": fm.get("command_byte"),
                    "detail_command": fm.get("detail_command"),
                    "subcommand": fm.get("subcommand"),
                    "verification_status": fm.get("verification_status"),
                    "tags": fm.get("tags"),
                },
            }
            chunks.append(chunk)

    return chunks, over_hard_max


def main():
    chunks, over_hard_max = build_chunks()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    sizes = [c["char_count"] for c in chunks]
    print(f"生成チャンク数: {len(chunks)}")
    print(f"出力先: {OUTPUT_PATH.relative_to(ROOT)}")
    print(f"文字数 最小: {min(sizes)} / 最大: {max(sizes)} / 平均: {sum(sizes)//len(sizes)}")
    print(f"目標サイズ({TARGET_CHARS}字)超のチャンク数: {sum(1 for s in sizes if s > TARGET_CHARS)}")
    print(f"ハード上限({HARD_MAX_CHARS}字)超のチャンク数: {len(over_hard_max)}")
    if over_hard_max:
        print("\n=== ハード上限を超えたチャンク(段落分割でも割れなかったもの) ===")
        for chunk_id, size in sorted(over_hard_max, key=lambda x: -x[1])[:20]:
            print(f"  {size}字  {chunk_id}")


if __name__ == "__main__":
    main()