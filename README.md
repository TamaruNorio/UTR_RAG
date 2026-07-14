# UTR_RAG

## 目的

UTR_RAG は、タカヤ製 UTR-S201シリーズの通信プロトコル理解、実装支援、レビュー、段階的な実機確認を、AIとのペアプログラミングで進めやすくするためのドキュメントリポジトリです。

## 対象者

- AIを使ったペアプログラミング経験がある人
- Git / GitHub の基本操作を理解している人
- UTR-S201シリーズ制御プログラムを作成、移植、レビュー、検証する人
- 実装言語は限定しません。Python、C#、C++、JavaScriptなど、対象環境に合わせて利用できます。

## 最初に読むもの

1. `docs/current/V100_USAGE_GUIDE.md`
2. `docs/current/COMMAND_MASTER_V117.md`
3. `docs/current/commands/cards/`
4. 必要に応じて、レスポンス、ROM、RF安全、パラメータ確認の文書

## 公式PDFの扱い

公式PDFが一次情報です。このリポジトリは公式PDFの代替ではありません。PDF原本は、社内の正式な配布場所または管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

## GitHubにアップロードしない情報

runtime logs、実CSVログ、顧客情報、実IPアドレス、raw EPC / UII / TID、認証情報、完成Hex、SUM計算済み送信用コマンド例はGitHubにアップロードしません。
