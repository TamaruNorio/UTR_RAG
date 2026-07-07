# UHF_BlockErase Command Card

## 1. Command Identity

- Command name: UHF_BlockErase
- Command group: UHF tag memory control
- Command code reference: 55/1B
- R8-7 catalog source: `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`

## 2. Purpose

タグメモリの指定ブロック消去に関する整理用カードである。R9-3では仕様整理のみを行い、実機送信対象にはしない。

## 3. Safety Classification

- Safety class: `PROHIBITED`
- Risk: タグデータを不可逆に消去する可能性がある
- Default handling: 実行禁止

## 4. Operation Level

- Operation level: Level 4
- Approval: 個別承認、仕様根拠、復旧方針がない限り扱わない

## 5. Parameters Overview

詳細パラメータはPDF原本と既存RAG資料の照合対象である。完成Hex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 6. Expected Response Overview

レスポンスの詳細はPDF原本との再照合が必要である。成功応答をもってタグ内容の安全性を保証しない。

## 7. Real-device Test Status

- Status: `PROHIBITED`
- R8-8A: 未実施
- Reason: タグデータ破壊リスクがあるため

## 8. Preconditions

- 通常の社内pre-RC確認では実施しない
- 明示承認、対象タグ、復旧方針、ログ保存方針が必要

## 9. Prohibited Use

- AIによる自動実装
- サンプルコード生成
- 実機送信用コマンド生成
- 顧客環境または実運用タグでの実行

## 10. Related Documents

- `docs/commands/R8-7_COMMAND_COVERAGE_AUDIT.md`
- `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`
- `docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md`

## 11. AI Retrieval Tags

- command: UHF_BlockErase
- category: tag_memory_destructive
- safety: prohibited
- operation_level: 4
- test_status: prohibited

## 12. AI Handling Notes

AIはこのコマンドを実装候補として扱わない。必要性を問われた場合も、実行手順ではなく承認条件とリスクを説明する。

## 13. Current Decision

`PROHIBITED_DOCUMENT_ONLY`
