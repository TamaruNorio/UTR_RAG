# Stage 0 Read-only Real-device Result

## 1. Positioning

v012では、v011 Stage 0/1 read-only verification kitを使い、Stage 0 read-onlyコマンドの実機確認結果を記録する。

この文書はマスク済みサマリであり、runtime_logs/ の生ログはGit管理しない。

## 2. Execution scope

対象:

- ROMバージョンの読み取り
- チップバージョンの読み取り
- エラー情報の読み取り

対象外:

- 書き込み系
- FLASH
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- タグメモリ操作
- Lock / Kill / Encode / ThroughCmd

対象外は仕様上禁止ではなく、v012の実行対象外である。

## 3. Execution environment

- repository commit: 40daa86 base main before v012 branch
- package base: v011 Stage 0/1 read-only verification kit
- tool: tools/stage01_readonly_verify.py
- connection_type: serial
- port: COMx
- baudrate: 115200
- timeout_ms: 1000
- execution date/time: 2026-07-13 10:15:56 JST
- operator: masked

## 4. Device identification result

- ROM version: not obtained
- series name: not obtained
- product type: not determined
- mapping source: docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md
- result: v011 tool reached Stage 0 execute path with COMx, but the read-only frame adapter was not encoded and no real-device command was sent.
- pyserial: available
- connection note: COMx was specified. No alternate port scan was performed.

## 5. Command result summary

| Stage | PDF section | Command name | Card path | Expected response type | Actual response type | Result status | ACK summary | NACK error code 1 | NACK error code 2 | NACK error code 3 | NACK error code 4 | timeout_ms | elapsed_ms | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stage 0 | 7.3.8 | ROMバージョンの読み取り | docs/current/commands/cards/rom_version_read.md | ACK/NACK/timeout/no-response | not-sent | BLOCKED_BY_PARAMETER |  |  |  |  |  | 1000 |  | v011 execution adapter did not encode the common frame; no real-device command was sent and ROM was not obtained. |
| Stage 0 | 7.3.9 | チップバージョンの読み取り | docs/current/commands/cards/55_90_chip_version_read.md | ACK/NACK/timeout/no-response | not-sent | NEEDS_RETEST |  |  |  |  |  | 1000 |  | Not executed after the Stage 0 adapter guard; retry after read-only frame adapter is confirmed. |
| Stage 0 | 7.3.1 | エラー情報の読み取り | docs/current/commands/cards/4f_80_read_error_info.md | ACK/NACK/timeout/no-response | not-sent | NEEDS_RETEST |  |  |  |  |  | 1000 |  | Not executed after the Stage 0 adapter guard; retry after read-only frame adapter is confirmed. |

## 6. Log files

Runtime files were saved under `runtime_logs/stage01_readonly/` and are not committed.

- `stage01_readonly_20260713_101556_COMx_log.csv`
- `stage01_readonly_20260713_101556_COMx_result.md`

## 7. Result decision

V012_STAGE0_REAL_DEVICE_HOLD_BY_CONNECTION

## 8. Next action

- Confirm the Stage 0 read-only frame adapter against the protocol common frame.
- Re-run only Stage 0 read-only commands after adapter confirmation.
- Keep runtime logs outside Git.
- Do not proceed to Stage 1 until ROM version read is actually completed or a reviewed equivalent identification path is available.

## 9. v013 follow-up

v013 adds a ROMバージョン読み取り専用フレームアダプタ and records the masked result in:

- `docs/current/25_STAGE0_ROM_READ_FRAME_ADAPTER_RESULT.md`

This does not rewrite the v012 result. v012 remains a HOLD result because the v011 tool stopped before real-device command send. v013 narrows the execution scope to ROMバージョン読み取り only; チップバージョン読み取り and エラー情報の読み取り are not executed in v013.

## 10. v014 follow-up

v014 uses the v013 ROM result as the first device-identification step and proceeds to the remaining Stage 0 read-only commands. The masked result is recorded in:

- `docs/current/26_STAGE0_REMAINING_READONLY_RESULT.md`

This does not rewrite the v012 result. v012 remains the original HOLD record for the pre-adapter execution attempt.
