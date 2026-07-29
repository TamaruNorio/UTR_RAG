# RAGチャンク生成手順

## 目的

`scripts/build_rag_chunks.py` は、`docs/current` 配下のMarkdownをベクトルDB登録用のJSONLへ分割するためのローカル生成ツールです。

## 前提

- Python 3 が実行できること
- PyYAML が利用できること
- 入力文書は `docs/current` 配下のMarkdownであること
- 生成物はローカルで都度作成し、GitHubへコミットしないこと

PyYAML がない場合は、スクリプトがエラーを表示します。

## 実行コマンド

```text
python scripts/build_rag_chunks.py
```

簡易説明を表示する場合:

```text
python scripts/build_rag_chunks.py --help
```

## 出力先

```text
rag_chunks/chunks.jsonl
```

`rag_chunks/` は `.gitignore` で除外されています。生成された `chunks.jsonl` はコミット対象外です。

## 想定入力範囲

対象は `docs/current/**/*.md` です。各チャンクには、元Markdownのfrontmatterから取得した `title`、`doc_type`、`command_byte`、`verification_status`、`tags` などのメタデータが付与されます。

分割は、`##` 見出し、`###` 見出し、段落、Markdown表の行、罫線なしフィールド列挙の行を順に使います。目標サイズは500字、ハード上限は1000字です。

## 失敗時の見方

- `PyYAML が必要です` と表示された場合は、PyYAMLをインストールしてください。
- `ハード上限(1000字)超のチャンク数` が0でない場合は、出力末尾に表示されるファイル名とchunk番号を確認してください。
- 入力Markdownのfrontmatterが壊れている疑いがある場合は、先に以下を実行してください。

```text
python scripts/validate_frontmatter.py
```

- Markdownリンクや `related_docs` の参照先が壊れている疑いがある場合は、以下を実行してください。

```text
python scripts/check_doc_links.py
```
