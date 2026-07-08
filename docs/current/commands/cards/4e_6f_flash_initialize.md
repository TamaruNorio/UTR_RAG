# Flash Initialize Command Card

## 1. Command Identity

- Command name: Flash Initialize
- Command group: reader persistent settings
- Command code reference: 4E/6F
- R8-7 catalog source: `docs/current/06_COMMAND_INDEX.md`

## 2. Purpose

FLASH初期化に関する整理用カードである。永続設定の初期化や復旧困難な状態変更につながる可能性があるため、実施対象外とする。

## 3. Safety Classification

- Safety class: `FLASH_WRITE_PROHIBITED`
- Risk: 永続設定初期化、設定喪失、復旧困難
- Default handling: 実行禁止

## 4. Operation Level

- Operation level: Level 5
- Approval: 原則不可。必要時はメーカー仕様、復旧手順、明示承認が必要

## 5. Parameters Overview

初期化範囲や条件の詳細はPDF原本との照合対象である。完成Hex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 6. Expected Response Overview

レスポンス仕様はPDF原本との再照合が必要である。確認目的の送信は行わない。

## 7. Real-device Test Status

- Status: `PROHIBITED`
- R8-8A: 未実施
- Reason: FLASH初期化禁止

## 8. Preconditions

- 社内pre-RC、外部レビュー候補、AI-ready整備では実施しない
- 実施が必要な場合は別途HOLD解除判断が必要

## 9. Prohibited Use

- 自動送信
- 初期化手順の生成
- 実機送信用コード生成
- 復旧準備なしの確認

## 10. Related Documents

- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/02_SAFETY_AND_HOLD_ITEMS.md`

## 11. AI Retrieval Tags

- command: Flash Initialize
- category: persistent_reader_setting
- safety: flash_write_prohibited
- operation_level: 5
- test_status: prohibited

## 12. AI Handling Notes

AIはFLASH初期化を候補化しない。必要性を問われた場合も、実行ではなくHOLD事項と承認条件を説明する。

## 13. Current Decision

`PROHIBITED_DOCUMENT_ONLY_WITH_SPEC_HOLD`
