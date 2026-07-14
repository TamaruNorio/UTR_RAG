# リリースと成果物

## 1. 現在版

現在版は V100 Final documentation package です。

V100では、過去の作業経緯ではなく、現在の利用入口を重視します。

## 2. 利用入口

- `README.md`: 最初に読む説明
- `llms.txt`: AIに読ませる入口
- `docs/current/45_V100_FINAL_USAGE_GUIDE.md`: V100の使い方
- `docs/current/09_COMMAND_MASTER_V117.md`: コマンド一覧
- `docs/current/commands/cards/`: 個別コマンドカード

## 3. PDF原本の扱い

公式PDFが一次情報です。

このリポジトリは公式PDFの代替ではありません。

PDF原本は、社内の正式な配布場所または管理場所から別途準備してください。

GitHubにはPDF原本をアップロードしないでください。

## 4. GitHubにアップロードしない情報

以下はGitHubにアップロードしません。

- PDF原本
- runtime logs
- 実CSVログ
- 顧客情報
- 実IPアドレス
- raw EPC / UII / TID
- 認証情報
- 完成Hex
- SUM計算済み送信用コマンド例

## 5. 過去成果物の扱い

過去のZIP成果物は、履歴確認が必要な場合にGitHub Release側で確認します。

V100で通常利用する入口は、mainブランチ上の現在版ドキュメントです。
