# Stage 2 Stop Conditions

## 1. Immediate stop conditions

Stop Stage 2 execution immediately when any of the following occur.

- Consecutive timeout
- Antenna error
- LBT-related error
- NACK error code indicating unsupported command
- Device/ROM mismatch
- Unexpected response format
- Tag memory read precondition missing
- Access password missing
- User-specified stop condition

## 2. Continue-with-notes conditions

Continue only with notes when the condition is intentional, controlled, and recorded.

- No tag detected when tag_present=false
- No tag detected during intentional empty-field test
- Command returns supported NACK that is expected under test condition
- Inventory returns zero tags in controlled no-tag test

## 3. Do-not-continue conditions

Do not continue into the next Stage 2 command when any of the following are true.

- ROM読み取り失敗
- 機種判定不能
- アンテナ未接続
- 対象タグ条件未確定
- Read対象メモリ未指定
- 復旧条件未定義
- 実行者が停止判断した場合

## 4. Safety notes

- v016 does not execute Stage 2 RF read commands.
- Frequency, output power, antenna settings, and InventoryParam are not changed as part of v016.
- Stop decisions must be logged as masked summaries.
