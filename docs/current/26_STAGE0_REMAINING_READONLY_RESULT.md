# Stage 0 Remaining Read-only Result

## 1. Positioning

v014では、v013でROMバージョン読み取りが成功した結果を前提に、Stage 0の残り2件であるチップバージョン読み取りとエラー情報読み取りを確認する。

この文書はマスク済みサマリであり、`runtime_logs/` の生ログはGit管理しない。

## 2. Execution scope

対象:

- ROMバージョンの読み取り
- チップバージョンの読み取り
- エラー情報の読み取り

v014でROMバージョン読み取りを先に実行する理由:

- 機種/ROMを自動判定するため
- 対象機種/ROMで残り2件を実行してよいか確認するため
- ログに実機条件を残すため

v014対象外:

- Stage 1 read-only
- 書き込み系
- FLASH
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- タグメモリ操作
- Lock / Kill / Encode / ThroughCmd

対象外は仕様上禁止ではなく、v014の実行対象外である。

## 3. Execution environment

- repository commit: aca2f7c
- package base: v013 Stage 0 ROM read frame adapter
- tool: `tools/stage01_readonly_verify.py`
- connection_type: USB serial
- port: COMx
- baudrate: 115200
- timeout_ms: 1000
- execution date/time: 2026-07-13 11:47:48 JST
- operator: masked

## 4. Device identification

- ROM raw: 2052
- ROM version: 2.052
- series: USM02
- product type: UTR-SUN02-4CH
- elapsed_ms: 15
- result_status: REAL_DEVICE_PASS_WITH_NOTES

## 5. Command result summary

| Stage | PDF section | Command name | Card path | Expected response type | Actual response type | Result status | ACK summary | NACK error code 1 | NACK error code 2 | NACK error code 3 | NACK error code 4 | timeout_ms | elapsed_ms | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stage 0 | 7.3.8 | ROMバージョンの読み取り | docs/current/commands/cards/rom_version_read.md | ACK/NACK/timeout/no-response | ACK | REAL_DEVICE_PASS_WITH_NOTES | ROM raw=2052; ROM=2.052; series=USM02; product=UTR-SUN02-4CH |  |  |  |  | 1000 | 15 | Raw response is retained only in runtime CSV. |
| Stage 0 | 7.3.9 | チップバージョンの読み取り | docs/current/commands/cards/55_90_chip_version_read.md | ACK/NACK/timeout/no-response | ACK | REAL_DEVICE_PASS_WITH_NOTES | chip raw=2052; chip firmware=2.052; chip name=UR201; subcommand=00h |  |  |  |  | 1000 | 16 | Serial-number subcommand 01h was not executed. Raw response is retained only in runtime CSV. |
| Stage 0 | 7.3.1 | エラー情報の読み取り | docs/current/commands/cards/4f_80_read_error_info.md | ACK/NACK/timeout/no-response | ACK | REAL_DEVICE_PASS_WITH_NOTES | error information=00h; status=normal; reserved=00h/00h |  |  |  |  | 1000 | 15 | Raw response is retained only in runtime CSV. |

## 6. Runtime log files

Runtime files were saved under `runtime_logs/stage01_readonly/` and are not committed.

- `stage01_readonly_20260713_114748_COMx_log.csv`
- `stage01_readonly_20260713_114748_COMx_result.md`

## 7. Result decision

V014_STAGE0_REMAINING_READONLY_PASS_WITH_NOTES

## 8. Next action

- Stage 1 read-only設定値読み取りへ進む。
- Stage 1でもROM 2.052 / USM02 / UTR-SUN02-4CHを前提条件として記録する。
- Runtime logs remain outside Git.
