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

- [文書整備計画](../docs/IMPROVEMENT_PLAN.md)に従い、RAG文書を先行し、プログラム改修は後工程にします。
- メーカーSDKを必須とせず、公開プロトコルから実装する前提です。USB/COMとLAN/TCPを区別します。
- [用途別参照ガイド](../docs/current/TASK_READING_GUIDE.md)で資料を選び、カードの関連文書を確認してください。
- [確認状態の記録方針](../docs/current/VERIFICATION_POLICY.md)と[原典照合一覧](../docs/current/SOURCE_REVIEW_STATUS.md)を確認し、過去の制作記録やPASSラベルだけで仕様・実機試験を断定しないでください。不明点は変更前に保守者へ確認します。

- 公式PDFが一次情報です。
- 仕様値や技術的意味を推測で変更しないでください。
- 実装前に、機種、ROM、接続方式、対象コマンド、実機送信の有無を確認してください。
- 完成Hex、SUM計算済みコマンド、安全ガード解除コードを安易に生成しないでください。
- GitHubに実機ログ、顧客情報、実IPアドレス、raw EPC / UII / TID、認証情報、パスワードを含めないでください。
