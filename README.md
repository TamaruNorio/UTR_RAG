# UTR_RAG

UTR-S201シリーズの通信プロトコルを、生成AIとの実装・レビュー・検証で参照しやすく整理した公開ドキュメントです。

## 目的

UTR_RAG は、タカヤ製 UTR-S201シリーズの通信プロトコル理解、実装支援、レビュー、段階的な実機確認を、AIとのペアプログラミングで進めやすくするためのドキュメントリポジトリです。

（本文中の「V100」は、社内検証を経た公開バージョン1.00を指します。）

このリポジトリは、通信仕様の理解と実装支援に使う資料を公開するものです。公式PDFの代替、実機送信の許可、完成Hexの無条件利用を保証するものではありません。公開範囲と注意点は `RELEASE_SCOPE.md` も確認してください。

## 対象者

- AIを使ったペアプログラミング経験がある人
- Git / GitHub の基本操作を理解している人
- UTR-S201シリーズ制御プログラムを作成、移植、レビュー、検証する人
- 実装言語は限定しません。Python、C#、C++、JavaScriptなど、対象環境に合わせて利用できます。

## 最初に読むもの

まず全体像と公開範囲を確認し、その後にコマンド一覧やレスポンス分類へ進んでください。

1. `RELEASE_SCOPE.md` - 公開範囲、保証すること、保証しないこと
2. `docs/current/V100_USAGE_GUIDE.md` - V100ドキュメントの使い方
3. `docs/current/COMMAND_MASTER_V117.md` - コマンド一覧と参照導線
4. `docs/current/RESPONSE_AND_NACK_MASTER.md` - ACK/NACKとレスポンスの基本
5. `docs/current/RESPONSE_CLASSIFICATION_MATRIX.md` - レスポンス分類
6. `docs/current/commands/cards/TEST_STATUS_INDEX.md` - 実機確認状態の一覧
7. `docs/current/commands/cards/` - 個別コマンドカード
8. 必要に応じて、ROM、RF安全、パラメータ確認の文書

## 公式PDFの扱い

公式PDFが一次情報です。このリポジトリは公式PDFの代替ではありません。PDF原本は、社内の正式な配布場所または管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

## 関連リポジトリ（サンプルコード）

本リポジトリはドキュメントのみを扱います。実際に動作するPythonサンプルコードは、以下の姉妹リポジトリを参照してください。

- [UTR_LAN_Python_CodeX](https://github.com/TamaruNorio/UTR_LAN_Python_CodeX) — LAN(TCP)接続版サンプル
- [UTR_USB_Python_CodeX](https://github.com/TamaruNorio/UTR_USB_Python_CodeX) — USB接続版サンプル

## GitHubにアップロードしない情報

runtime logs、実CSVログ、顧客情報、実IPアドレス、実機ログ由来のraw EPC / UII / TID、認証情報、パスワードはGitHubにアップロードしません。

公式PDFに掲載済みの完成Hex例は、仕様説明として記載できます。ただし、実機ログ由来のタグ固有値やパスワードを含むHexはマスクしてください。
