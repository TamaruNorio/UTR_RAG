# 06 Command Index

## 1. 概要

R8-7で抽出した38コマンドを、1コマンド1カード形式で整理している。インデックスは5件である。

## 2. 混同防止

- 55h/14h = UHF_InventoryRead
- 55h/15h = UHF_Read
- `55_14_uhf_read.md` は存在しない
- UHF_Read standalone はHOLD

## 3. インデックス

- `docs/current/commands/cards/README.md`
- `docs/current/commands/cards/AI_RETRIEVAL_INDEX.md`
- `docs/current/commands/cards/SAFETY_INDEX.md`
- `docs/current/commands/cards/TEST_STATUS_INDEX.md`
- `docs/current/commands/cards/OPERATION_LEVEL_INDEX.md`

## 4. コマンドカード

コマンドカードは `docs/current/commands/cards/` 配下に配置する。Level 4以上は明示確認、Level 5は明示承認と復旧手順なしではHOLDである。

## 5. 重要分類

- UHF_SetInventoryParam は自動送信禁止
- FLASH系はLevel 5またはHOLD/PROHIBITED
- 周波数/送信出力系はLevel 4以上