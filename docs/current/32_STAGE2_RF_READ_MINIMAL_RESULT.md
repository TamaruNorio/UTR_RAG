# Stage 2 RF Read Minimal Result

## 1. Positioning

v017 records the minimal Stage 2 RF read real-device result.

This document is a masked summary. Runtime CSV and raw logs under `runtime_logs/` are not committed.

## 2. Execution scope

Executed:

- ROMバージョンの読み取り
- UHF_CheckAntenna
- UHF_GetHandle
- UHF_Inventory

Not executed in v017:

- UHF_InventoryRead
- UHF_Read
- 書き込み系
- FLASH write/init
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- InventoryParam変更
- SelectParam変更
- ExpandSelectParam変更
- タグメモリ操作
- Lock / Kill / Encode / ThroughCmd

Out of v017 scope does not mean prohibited by the protocol specification.
It means the operation was not executed in v017.

## 3. Execution environment

- repository commit: feature branch working tree before v017 merge
- package base: v016 Stage 2 RF read preflight
- tool: `tools/stage01_readonly_verify.py`
- command set: `stage2-minimal`
- connection_type: USB serial
- port: COMx
- baudrate: 115200
- timeout_ms: 1000
- execution date/time: 2026-07-13 14:43:27 JST
- operator: masked

## 4. Device identification

- ROM raw: 2052
- ROM version: 2.052
- series: USM02
- product type: UTR-SUN02-4CH
- result_status: REAL_DEVICE_PASS_WITH_NOTES

## 5. Command result summary

| Stage | PDF section | Command name | Card path | Actual response type | Result status | ACK summary | timeout_ms | Notes |
|---|---|---|---|---|---|---|---:|---|
| Stage 0 | 7.3.8 | ROMバージョンの読み取り | docs/current/commands/cards/rom_version_read.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | ROM raw=2052; ROM=2.052; series=USM02; product=UTR-SUN02-4CH | 1000 | ROM read was executed first. |
| Stage 2 minimal | 7.3.5 | UHF_CheckAntenna | docs/current/commands/cards/55_44_uhf_check_antenna.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | antenna check ACK; data_length=3 | 1000 | No antenna setting change. |
| Stage 2 minimal | 7.3.12 | UHF_GetHandle | docs/current/commands/cards/55_46_uhf_get_handle.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | handle response ACK; data_length=3 | 1000 | Tag-specific values are not committed. |
| Stage 2 minimal | 7.5.1 | UHF_Inventory | docs/current/commands/cards/55_10_uhf_inventory.md | unknown-response | REAL_DEVICE_FAIL |  | 1000 | Unexpected response category was returned by the current parser. This is not recorded as PASS. |

## 6. NACK / timeout / antenna error / LBT

- NACK: none recorded in the masked summary
- timeout: none recorded in the masked summary
- antenna error: none recorded in the masked summary
- LBT-related error: none recorded in the masked summary
- unexpected response: UHF_Inventory

## 7. Result decision

V017_STAGE2_RF_READ_MINIMAL_RESULT_WITH_NOTES

## 8. Runtime log files

Runtime files were saved under `runtime_logs/stage02_rf_read/` and are not committed.

- `stage01_readonly_20260713_144327_COMx_log.csv`
- `stage01_readonly_20260713_144327_COMx_result.md`

## 9. Next action

- Review UHF_Inventory response parsing before expanding Stage 2 execution.
- Do not mark UHF_Inventory as PASS until its response category is parsed and reviewed.
- Keep UHF_InventoryRead and UHF_Read outside the execution scope until Inventory behavior is understood.
