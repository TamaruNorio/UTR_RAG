# UTR_RAG ドキュメント

このディレクトリには、UTR-S201 シリーズ制御プログラムをAIと一緒に設計・実装・レビューするための no-PDF ドキュメントを格納します。

現在版は **V100 Final documentation package** です。

## 1. 対象者

- AIを使ったペアプログラミング経験がある人
- Git / GitHub の基本操作を理解している人
- UTR-S201 シリーズの制御プログラムを作成、移植、レビュー、検証したい人

実装言語は限定しません。Python、C#、C++、JavaScriptなど、必要な言語で利用できます。

## 2. 最初に読む文書

1. `../README.md`
2. `../llms.txt`
3. `current/AI_CONTEXT_INDEX.md`
4. `current/00_OVERVIEW.md`
5. `current/45_V100_FINAL_USAGE_GUIDE.md`

## 3. コマンドを調べるとき

1. `current/09_COMMAND_MASTER_V117.md` で対象コマンドを確認する。
2. `current/16_TRACEABILITY_INDEX_V117.md` で参照関係を確認する。
3. `current/commands/cards/` 配下のコマンドカードを読む。
4. `current/10_RESPONSE_AND_NACK_MASTER.md` で応答、ACK、NACK、timeoutを確認する。
5. `current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md` でROMと機種差分を確認する。

## 4. 実機確認を考えるとき

- `current/17_REAL_DEVICE_VERIFICATION_FRAMEWORK.md`
- `current/19_VERIFICATION_STAGE_PLAN.md`
- `current/20_VERIFICATION_RESULT_STATUS.md`
- `current/37_STAGE3PLUS_EXECUTION_GATES.md`
- `current/38_STAGE3PLUS_RECOVERY_AND_STOP_PLAN.md`

実機送信は、対象コマンド、パラメータ、復旧方法、停止条件が揃ってから行います。

## 5. 注意

このディレクトリの文書は公式PDFの代替ではありません。公式PDFを一次情報とし、AI実装支援用の補助資料として使用します。
