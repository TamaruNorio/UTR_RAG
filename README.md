# UTR_RAG

UTR-S201シリーズの通信プロトコルを、生成AIとの実装・レビュー・検証で参照しやすく整理した公開ドキュメントです。

このリポジトリは、ベクトル検索APIや対話型RAGサービスそのものではありません。主な用途は、AIコーディングエージェントやAIレビュー支援が `git clone` 後にMarkdown文書群を直接参照し、実装・レビュー・実機確認の補助に使うことです。`rag_chunks/` は補助的生成物であり、主たる公開知識は `docs/current/` 配下の文書群です。目的は検索性能の競争ではなく、仕様理解の誤り、関連文書の読み飛ばし、実装時の危険な誤解を減らすことです。

## 目的

UTR_RAG は、タカヤ製 UTR-S201シリーズの通信プロトコル理解、実装支援、レビュー、段階的な実機確認を、AIとのペアプログラミングで進めやすくするためのドキュメントリポジトリです。

（本文中の「V100」は、社内検証を経た公開バージョン1.00を指します。）

このリポジトリは、通信仕様の理解と実装支援に使う資料を公開するものです。公式PDFの代替、実機送信の許可、完成Hexの無条件利用を保証するものではありません。公開範囲と注意点は `RELEASE_SCOPE.md` も確認してください。

公開版の作成手順と変更点記録の作法は `RELEASE_PROCESS.md` と `CHANGELOG_TEMPLATE.md` を確認してください。

## 対象者

メーカーSDKを必須とせず、公開通信プロトコルから実装できる資料を目指します。Windows専用SDKの有無に依存しない構成とし、USB/COMとLAN/TCPを区別します。各OSの接続手段・ドライバ・ライブラリの動作確認は別途必要です。

- AIを使ったペアプログラミング経験がある人
- Git / GitHub の基本操作を理解している人
- UTR-S201シリーズ制御プログラムを作成、移植、レビュー、検証する人
- 実装言語は限定しません。Python、C#、C++、JavaScriptなど、対象環境に合わせて利用できます。

## 最初に読むもの

用途が決まっている場合は、以下の共通資料と [用途別参照ガイド](docs/current/TASK_READING_GUIDE.md) から必要なカードへ進んでください。カードの `related_docs` は省略しません。

AIが作業する場合は、最初に [AGENTS.md](AGENTS.md) の必読順序・適用条件を確認してください。以下の案内だけで作業規則を読み終えた扱いにはしません。

まず全体像と公開範囲を確認し、その後にコマンド一覧やレスポンス分類へ進んでください。

1. `RELEASE_SCOPE.md` - 公開範囲、保証すること、保証しないこと
2. `docs/current/V100_USAGE_GUIDE.md` - V100ドキュメントの使い方
3. `docs/current/COMMAND_MASTER_V117.md` - コマンド一覧と参照導線
4. `docs/current/RESPONSE_AND_NACK_MASTER.md` - ACK/NACKとレスポンスの基本
5. `docs/current/RESPONSE_CLASSIFICATION_MATRIX.md` - レスポンス分類
6. `docs/current/commands/cards/TEST_STATUS_INDEX.md` - 実機確認状態の一覧
7. `docs/current/commands/cards/` - 個別コマンドカード
8. 必要に応じて、ROM、RF安全、パラメータ確認の文書

## AI/Codexで実装する場合の推奨参照順

AI/Codexに実装を依頼する場合は、接続方式を先に決めてから参照先を分けてください。

USB/COM接続で実装する場合は、まずこのリポジトリの `docs/current/AI_CONTEXT_INDEX.md`、`docs/current/AI_IMPLEMENTATION_GUARDRAILS.md`、`docs/current/COMMAND_MASTER_V117.md`、`docs/current/RESPONSE_AND_NACK_MASTER.md` を確認し、その後に対象コマンドカードと USB接続版サンプル `UTR_USB_Python_CodeX` を参照してください。

LAN/TCP接続で実装する場合は、まずこのリポジトリの `docs/current/AI_CONTEXT_INDEX.md`、`docs/current/AI_IMPLEMENTATION_GUARDRAILS.md`、`docs/current/COMMAND_MASTER_V117.md`、`docs/current/RESPONSE_AND_NACK_MASTER.md` を確認し、その後に対象コマンドカードと LAN(TCP)接続版サンプル `UTR_LAN_Python_CodeX` を参照してください。

複数アンテナ対応アプリを実装する場合は、個別コマンドカード単体だけを見て実装しないでください。特に `UHF_Inventory` の単純ループだけでアンテナ切替を実装せず、アンテナ番号、アンテナ自動切替、ACK/NACK、timeout、設定依存レスポンスを併せて確認してください。

機種を限定しないGUIアプリなど、複数の落とし穴がある実装をAI/Codexへ依頼する場合は、依頼文の実例として `docs/current/EXAMPLE_IMPLEMENTATION_REQUEST.md` も参照してください。

## 公式PDFの扱い

公式PDFが一次情報です。このリポジトリは公式PDFの代替ではありません。PDF原本は、社内の正式な配布場所または管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

## ライセンス

MIT Licenseの適用対象と、タカヤ公式マニュアル由来の内容の扱いは異なります。[LICENSE](LICENSE) と [公開範囲のライセンス説明](RELEASE_SCOPE.md) を確認してください。

## 文書整備の進め方と確認状態

2026-11-24の公開整備内容は [第2世代の公開範囲と確認結果](docs/GEN2_PUBLICATION_20261124.md) を参照してください。用途別の参照、仕様・試験状態の分離、18項目に対応した代表用途の設計をまとめています。別途作成したオフライン解析部品はローカル保存段階で、このリポジトリのcloneには含まれません。

現在はUTR_RAGの文書整備を先に進めています。USB/LANサンプル、GUI、通信ライブラリ等のプログラム改修は、RAG整備後の工程です。[整備計画・他社事例](docs/IMPROVEMENT_PLAN.md) に方針と到達点を記録します。

参照対象は [タカヤ公式の通信プロトコル説明書 Ver.1.17](https://www.product.takaya.co.jp/dcms_media/other/TDR-MNL-PRC-UTR-S201-117.pdf) です。版・節・ページと照合範囲は [原典照合一覧](docs/current/SOURCE_REVIEW_STATUS.md) で管理します。過去の制作記録やソフトウェア試験の成功を、仕様の根拠として優先しないでください。

54カードは `SPECIFICATION_REFERENCE`（仕様参照資料）として整理します。公式PDFを仕様上の期待結果の基準とし、全フィールドの再照合完了や実機試験の実施結果とは区別します。[確認状態の記録方針](docs/current/VERIFICATION_POLICY.md) と [確認状態索引](docs/current/commands/cards/TEST_STATUS_INDEX.md) を併せて確認してください。

PDF直接利用に対する一般的な正確さや利用量の改善は実証していません。[小規模比較](docs/SMALL_COMPARISON_REPORT.md)では関連抜粋を使った9問の回答を比較しましたが、PDF全体・資料探索・生成プログラムの動作を評価した結果ではありません。費用削減も確認していません。[評価手順](docs/QUALITY_EVALUATION_PLAN.md) に従い、正答性・参照量・実際の使用量を分けて扱います。

## 関連リポジトリ（サンプルコード）

本リポジトリはドキュメントのみを扱います。実際に動作するPythonサンプルコードは、以下の姉妹リポジトリを参照してください。

- [UTR_LAN_Python_CodeX](https://github.com/TamaruNorio/UTR_LAN_Python_CodeX) — LAN(TCP)接続版サンプル
- [UTR_USB_Python_CodeX](https://github.com/TamaruNorio/UTR_USB_Python_CodeX) — USB接続版サンプル

## GitHubにアップロードしない情報

runtime logs、実CSVログ、顧客情報、実IPアドレス、実機ログ由来のraw EPC / UII / TID、認証情報、パスワードはGitHubにアップロードしません。

公式PDFに掲載済みの完成Hex例は、仕様説明として記載できます。ただし、実機ログ由来のタグ固有値やパスワードを含むHexはマスクしてください。

機密情報、実機ログ、認証情報、raw EPC / UII / TID の詳しい扱いは `SECURITY.md` と `DATA_HANDLING.md` を確認してください。
