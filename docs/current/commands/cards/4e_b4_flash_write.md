# Flash Write Command Card

## 1. Command Identity

- Command name: Flash Write
- Command group: reader persistent settings
- Command code reference: 4E/B4
- R8-7 catalog source: `docs/current/06_COMMAND_INDEX.md`

## 2. Purpose

リーダ内部設定のFLASH書き込みに関する整理用カードである。永続設定変更を伴うため、R9-3では文書整理に限定する。

## 3. Safety Classification

- Safety class: `FLASH_WRITE_PROHIBITED`
- Risk: 永続設定変更、復旧困難な状態変更
- Default handling: 実行禁止

## 4. Operation Level

- Operation level: Level 5
- Approval: 明示承認、仕様根拠、復旧手順、作業責任者が必要

## 5. Parameters Overview

FLASH書き込み内容に関わるパラメータは記載しない。完成Hex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 6. Expected Response Overview

レスポンス仕様はPDF原本との照合対象である。応答確認のための実機送信も行わない。

## 7. Real-device Test Status

- Status: `PROHIBITED`
- R8-8A: 未実施
- Reason: FLASH書き込み禁止

## 8. Preconditions

- 通常のRAG整備、pre-RC確認、外部レビュー候補準備では実施しない
- 実施する場合は別プロセスの承認と復旧準備が必要

## 9. Prohibited Use

- 自動送信
- 実行サンプル生成
- 永続設定変更
- 周波数、送信出力、地域設定に影響する変更

## 10. Related Documents

- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/01_SCOPE_AND_POSITIONING.md`
- `docs/current/02_SAFETY_AND_HOLD_ITEMS.md`

## 11. AI Retrieval Tags

- command: Flash Write
- category: persistent_reader_setting
- safety: flash_write_prohibited
- operation_level: 5
- test_status: prohibited

## 12. AI Handling Notes

AIはFLASH書き込みを実行可能な実装候補として扱わない。問い合わせには禁止理由、承認条件、復旧準備の必要性を返す。

## 13. Current Decision

`PROHIBITED_DOCUMENT_ONLY`
