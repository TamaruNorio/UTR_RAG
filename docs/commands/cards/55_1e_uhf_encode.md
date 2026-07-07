# UHF_Encode Command Card

## 1. Command Identity

- Command name: UHF_Encode
- Command group: UHF tag memory control
- Command code reference: 55/1E
- R8-7 catalog source: `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`

## 2. Purpose

タグのエンコード処理に関する整理用カードである。タグ内容を変更し得るため、R9-3では文書整理に限定する。

## 3. Safety Classification

- Safety class: `PROHIBITED`
- Risk: タグ識別情報またはメモリ内容の変更
- Default handling: 実行禁止

## 4. Operation Level

- Operation level: Level 4
- Approval: 個別承認、対象タグ、変更内容、復旧方針が必要

## 5. Parameters Overview

入力パラメータはタグ内容変更に直結するため、AI-readyカードでは概要のみ扱う。完成Hex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 6. Expected Response Overview

レスポンス仕様はPDF原本との照合対象である。応答の有無だけではタグ内容の妥当性を判断しない。

## 7. Real-device Test Status

- Status: `PROHIBITED`
- R8-8A: 未実施
- Reason: タグ内容変更リスクがあるため

## 8. Preconditions

- 通常の接続確認、読み取り確認、Inventory確認では使用しない
- 実施する場合は別プロセスで安全審査が必要

## 9. Prohibited Use

- AIによる自動送信
- タグ内容を変更するサンプル作成
- 本番タグ、顧客タグ、識別用タグへの実行

## 10. Related Documents

- `docs/commands/R8-7_COMMAND_COVERAGE_AUDIT.md`
- `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`
- `docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md`

## 11. AI Retrieval Tags

- command: UHF_Encode
- category: tag_memory_destructive
- safety: prohibited
- operation_level: 4
- test_status: prohibited

## 12. AI Handling Notes

AIはこのコマンドを実行可能候補にしない。利用相談ではタグ内容変更リスクと承認条件を先に提示する。

## 13. Current Decision

`PROHIBITED_DOCUMENT_ONLY`
