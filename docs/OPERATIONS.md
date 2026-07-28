# UTR_RAG 運用ルール

## 基本方針

- main直接変更禁止
- featureブランチ作業
- 小さな変更単位
- 変更前後の確認必須
- 実機依存内容と机上確認内容を分ける

## 標準作業手順

1. mainを最新化する
2. featureブランチを作成する
3. 変更する
4. git status --short を確認する
5. git diff を確認する
6. git diff --check を確認する
7. commitする
8. pushする
9. PRを作成する
10. レビュー後にmainへ反映する

## 禁止事項

- main直接commit
- 機密情報の追加
- PDF原本の追加
- 実機確認済みでない内容を実機確認済みと書くこと
- 正式RCでない成果物を正式RCと書くこと
- 完成Hex、SUM計算済みコマンド、実機送信用コードの安易な追加
- 安全ガードの削除・緩和
- 周波数、送信出力、FLASH、アンテナ設定に影響する変更を無断で入れること

## チェックコマンド

```text
git status --short
git diff
git diff --check
git log --oneline -5
git branch --show-current
```

## RAGチャンク生成

ベクトルDBへの登録用データを作る場合は、以下を実行してください。

    python scripts/build_rag_chunks.py

docs/current 配下の全Markdownを、frontmatterのメタデータ付きで
JSONL形式（rag_chunks/chunks.jsonl）に分割出力します。
生成物はコミット対象外です（.gitignoreで除外）。手元で都度生成してください。
