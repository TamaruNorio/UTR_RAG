# Stage 2 Read Completion Result

## 1. Positioning

v019 records the Stage 2 read completion result for the selected read-only RF operations.

This document is a masked summary. Runtime CSV and raw logs under `runtime_logs/` are not committed.
v019 uses an explicit safe read-only profile for `UHF_InventoryRead` and `UHF_Read`.

## 2. Execution environment

- repository commit: feature branch working tree before v019 merge
- package base: v018 Stage 2 RF read operations result
- tool: `tools/stage01_readonly_verify.py`
- command set: `stage2-read`
- read profile: `safe-tid`
- connection_type: USB serial
- port: COMx
- baudrate: 115200
- timeout_ms: 1500
- execution date/time: 2026-07-13 15:12:47 JST
- operator: masked

## 3. Read profile

| Item | Value | Notes |
|---|---|---|
| profile | safe-tid | Explicit read-only profile for v019. |
| target tag | First tag detected by `UHF_Inventory` | Tag identifier is masked in Git-managed documents. |
| memory bank | TID(2) | TID is selected as the safe read-only target. |
| start word address | 0 | Word address only; no completed command frame is documented. |
| word count | 2 | Minimal read range for Stage 2 completion. |
| access password policy | default-zero | `00000000` policy used by the tool; password value is not treated as a write operation. |
| max tags | 1 | Git-managed summary records at most one masked tag identifier. |

## 4. Device identification

- ROM raw: 2052
- ROM version: 2.052
- series: USM02
- product type: UTR-SUN02-4CH
- result_status: REAL_DEVICE_PASS_WITH_NOTES

## 5. Command result summary

| Stage | PDF section | Command name | Card path | Actual response type | Result status | Summary | timeout_ms | Notes |
|---|---|---|---|---|---|---|---:|---|
| Stage 0 | 7.3.8 | ROMバージョンの読み取り | docs/current/commands/cards/rom_version_read.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | ROM raw=2052; ROM=2.052; series=USM02; product=UTR-SUN02-4CH | 1500 | ROM read was executed first. |
| Stage 2 | 7.3.5 | UHF_CheckAntenna | docs/current/commands/cards/55_44_uhf_check_antenna.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | antenna check ACK; data_length=3 | 1500 | No antenna setting change. |
| Stage 2 | 7.3.12 | UHF_GetHandle | docs/current/commands/cards/55_46_uhf_get_handle.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | handle response ACK; data_length=3 | 1500 | Tag-specific values are not committed. |
| Stage 2 | 7.5.1 | UHF_Inventory | docs/current/commands/cards/55_10_uhf_inventory.md | multi-frame | REAL_DEVICE_PASS_WITH_NOTES | frames=2; valid=2; completion=1; tag_frames=1; masked_epc=EPC_00B0xxxxxxxxxxxxxxxxxxxx | 1500 | One tag was detected and masked. |
| Stage 2 | 7.5.2 | UHF_InventoryRead | docs/current/commands/cards/55_14_uhf_inventory_read.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | ACK; data_length=5; read_profile=safe-tid; memory_bank=TID(2); word_address=0; word_count=2; access_password_policy=default-zero; max_tags=1 | 1500 | Executed only after Inventory detected a tag. |
| Stage 2 | 7.5.3 | UHF_Read | docs/current/commands/cards/55_15_uhf_read.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | ACK; data_length=6; read_profile=safe-tid; memory_bank=TID(2); word_address=0; word_count=2; access_password_policy=default-zero; max_tags=1 | 1500 | Read data is not recorded unmasked in Git-managed documents. |

## 6. Read data masking

- EPC/UII is masked as `EPC_00B0xxxxxxxxxxxxxxxxxxxx`.
- TID/read data values are not recorded as raw values in this Git-managed summary.
- Runtime CSV may contain raw response details and must not be committed.
- Completed Hex and SUM-calculated commands are not documented.

## 7. NACK / timeout / parse error

- NACK: none recorded in the masked summary
- timeout: none recorded in the masked summary
- parse error: none recorded in the masked summary
- LBT-related error: none recorded in the masked summary
- antenna error: none recorded in the masked summary

## 8. BLOCKED / non-executed items

No v019 Stage 2 target command remained blocked.

The following operations remain outside v019 scope:

- UHF_SetInventoryParam
- UHF_SetSelectParam
- UHF_SetExpandSelectParam
- Write commands
- FLASH write/init
- Frequency change
- Output power change
- Antenna setting change
- External antenna auto-switch setting change
- Access password write
- Tag memory write
- Lock / Kill / Encode / ThroughCmd

Outside scope does not mean prohibited by the protocol specification.

## 9. Stage 2 overall status

Stage 2 read-only RF operations reached a completion point for the selected target and profile:

- ROM read: completed with notes
- UHF_CheckAntenna: completed with notes
- UHF_GetHandle: completed with notes
- UHF_Inventory: completed with notes
- UHF_InventoryRead: completed with notes using `safe-tid`
- UHF_Read: completed with notes using `safe-tid`

This is not an individual real-device send test for all 54 commands.

## 10. Runtime log files

Runtime files were saved under `runtime_logs/stage02_rf_read/` and are not committed.

- `stage01_readonly_20260713_151247_COMx_log.csv`
- `stage01_readonly_20260713_151247_COMx_result.md`

## 11. Safety confirmation

- UHF_SetInventoryParam: not executed
- UHF_SetSelectParam: not executed
- UHF_SetExpandSelectParam: not executed
- Write commands: not executed
- FLASH write/init: not executed
- Frequency change: not executed
- Output power change: not executed
- Antenna setting change: not executed
- External antenna auto-switch setting change: not executed
- Access password write: not executed
- Tag memory write: not executed
- Lock / Kill / Encode / ThroughCmd: not executed
- PDF: not added
- Runtime logs: not committed

## 12. Result decision

V019_STAGE2_READ_COMPLETION_PASS_WITH_NOTES

## 13. Next action

- Create and validate the v019 Stage 2 read completion no-PDF package.
- Continue later stages only under separately reviewed scopes.
- Keep write, setting-change, FLASH, Lock, Kill, Encode, and ThroughCmd operations outside Stage 2 read completion.
