# Copilot Instructions

このリポジトリは、UTR-S201シリーズ通信プロトコルの理解・実装支援・レビュー用ドキュメントです。

## 参照順

まず以下を確認してください。

1. `README.md`
2. `RELEASE_SCOPE.md`
3. `llms.txt`
4. `docs/current/V100_USAGE_GUIDE.md`
5. `docs/current/COMMAND_MASTER_V117.md`
6. `docs/current/RESPONSE_AND_NACK_MASTER.md`
7. `docs/current/RESPONSE_CLASSIFICATION_MATRIX.md`

対象コマンドがある場合は、`docs/current/commands/cards/` の該当カードを確認してください。

## 作業方針

- 公式PDFが一次情報です。
- 仕様値や技術的意味を推測で変更しないでください。
- 実装前に、機種、ROM、接続方式、対象コマンド、実機送信の有無を確認してください。
- 完成Hex、SUM計算済みコマンド、安全ガード解除コードを安易に生成しないでください。
- GitHubに実機ログ、顧客情報、実IPアドレス、raw EPC / UII / TID、認証情報、パスワードを含めないでください。
