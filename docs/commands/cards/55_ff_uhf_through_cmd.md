# UHF_ThroughCmd Command Card

## 1. Command Identity

- Command name: UHF_ThroughCmd
- Command group: UHF passthrough control
- Command code reference: 55/FF
- R8-7 catalog source: `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`

## 2. Purpose

透過コマンド系の整理用カードである。実質的に任意の下位コマンド送信経路になり得るため、R9-3では実施対象外とする。

## 3. Safety Classification

- Safety class: `PROHIBITED`
- Risk: 安全分類を迂回した任意操作
- Default handling: 実行禁止

## 4. Operation Level

- Operation level: Level 4
- Approval: 原則不可。仕様、対象、下位コマンド、安全分類が確定した場合のみ別審査

## 5. Parameters Overview

透過ペイロードは任意操作になり得るため記載しない。完成Hex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 6. Expected Response Overview

レスポンスは下位コマンドに依存するため、一般化して安全とは判断できない。

## 7. Real-device Test Status

- Status: `PROHIBITED`
- R8-8A: 未実施
- Reason: 安全ガードを迂回する可能性があるため

## 8. Preconditions

- 通常検証では使用しない
- 下位コマンドが明確で、個別カードの安全分類を通過していることが最低条件

## 9. Prohibited Use

- 安全分類が不明な操作の送信
- 実行コード生成
- 任意Hex送信の案内
- SUM計算済みコマンドの生成

## 10. Related Documents

- `docs/commands/R8-7_COMMAND_COVERAGE_AUDIT.md`
- `docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md`
- `docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md`

## 11. AI Retrieval Tags

- command: UHF_ThroughCmd
- category: passthrough
- safety: prohibited
- operation_level: 4
- test_status: prohibited

## 12. AI Handling Notes

AIは透過コマンドを安全な汎用手段として提案しない。不明操作の送信要求はHOLDにする。

## 13. Current Decision

`PROHIBITED_DOCUMENT_ONLY`
