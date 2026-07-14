# Artifacts

このディレクトリでは、UTR-S201 AI補助ドキュメントの成果物を管理します。

現在版は **V100 Final documentation package** です。

## 1. V100の位置づけ

V100は、UTR_RAGをAIペアプログラミングで利用するための最終版ドキュメントセットです。

- 公式PDFの代替ではありません。
- PDF原本は、社内の正式な管理場所から別途準備します。
- GitHubにはPDF原本をアップロードしません。
- runtime logs、実CSVログ、顧客情報、実IPアドレス、raw EPC / UII / TID はアップロードしません。
- 実装言語は限定しません。
- Python、C#など任意の言語で実装するための参照資料として使います。

## 2. 主な参照先

- `../README.md`
- `../llms.txt`
- `../docs/current/45_V100_FINAL_USAGE_GUIDE.md`
- `../docs/current/09_COMMAND_MASTER_V117.md`
- `../docs/current/commands/cards/`
- `../docs/current/10_RESPONSE_AND_NACK_MASTER.md`
- `../docs/current/20_VERIFICATION_RESULT_STATUS.md`

## 3. ZIP成果物について

既存の `artifacts/utr_s201_ai_v022/utr_s201_ai_v022_final_rc_no_pdf.zip` は、V100整理前のFinal RC成果物として残します。

V100での最新利用入口は、リポジトリ上のREADME、`llms.txt`、`docs/current/` 配下の現在版ドキュメントです。PDF原本や実ログはZIPにもGitにも含めません。

## 4. 安全方針

Artifacts配下に、PDF原本、runtime logs、実CSVログ、顧客情報、完成Hex、SUM計算済み送信用コマンド例を追加しないでください。
