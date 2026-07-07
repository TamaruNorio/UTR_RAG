# UHF_Lock Command Card

## 1. Command Identity

- Command name: UHF_Lock
- Command group: UHF tag access control
- Command code reference: 55/18
- R8-7 catalog source: `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`

## 2. Purpose

タグメモリまたはアクセス制御のロックに関する整理用カードである。タグ運用状態を不可逆または復旧困難に変更し得るため、実施対象外とする。

## 3. Safety Classification

- Safety class: `PROHIBITED`
- Risk: タグアクセス制御の変更、復旧困難なロック
- Default handling: 実行禁止

## 4. Operation Level

- Operation level: Level 4
- Approval: 個別承認、対象タグ、解除可否、復旧方針が必要

## 5. Parameters Overview

ロック対象や権限に関わるパラメータは文書化しない。完成Hex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 6. Expected Response Overview

レスポンス仕様はPDF原本との照合対象である。応答確認のための送信も行わない。

## 7. Real-device Test Status

- Status: `PROHIBITED`
- R8-8A: 未実施
- Reason: タグアクセス制御を変更する可能性があるため

## 8. Preconditions

- 通常検証では実施不可
- 実施にはタグ所有者、対象、影響範囲、復旧方法の明示が必要

## 9. Prohibited Use

- 自動送信
- 実行例生成
- 顧客タグまたは本番タグでの実行
- 読み取り確認の代替としての使用

## 10. Related Documents

- `docs/commands/R8-7_COMMAND_COVERAGE_AUDIT.md`
- `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`
- `docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md`

## 11. AI Retrieval Tags

- command: UHF_Lock
- category: tag_access_control
- safety: prohibited
- operation_level: 4
- test_status: prohibited

## 12. AI Handling Notes

AIはこのコマンドを安全な読み取り系として扱わない。承認がない限り、候補化せずHOLDまたは禁止として返す。

## 13. Current Decision

`PROHIBITED_DOCUMENT_ONLY`
