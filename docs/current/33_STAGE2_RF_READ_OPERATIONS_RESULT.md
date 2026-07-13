# Stage 2 RF Read Operations Result

## 1. Positioning

v018 records the Stage 2 RF read operations result after adding RF response receive-loop handling.

This document is a masked summary. Runtime CSV and raw logs under `runtime_logs/` are not committed.
No ZIP or GitHub Release is created in v018.

## 2. Execution environment

- repository commit: feature branch working tree before v018 merge
- package base: v017 Stage 2 RF read minimal result
- tool: `tools/stage01_readonly_verify.py`
- command set: `stage2-read`
- connection_type: USB serial
- port: COMx
- baudrate: 115200
- timeout_ms: 1500
- execution date/time: 2026-07-13 14:59:43 JST
- operator: masked

## 3. PDF specification confirmation

PDF Ver.1.17 references used for v018:

- UHF_Inventory: PDF 7.5.1
- UHF_InventoryRead: PDF 7.5.2
- UHF_Read: PDF 7.5.3
- NACK response and error code 1-4: PDF 7.6
- RF tag command processing notes: PDF 3.10.1, 3.10.2, 3.10.3

The v018 parser treats Inventory and InventoryRead as RF operations that may return multiple tag responses followed by a completion response.
Fields that are not fully interpreted are retained in runtime logs and summarized conservatively.

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
| Stage 2 | 7.5.1 | UHF_Inventory | docs/current/commands/cards/55_10_uhf_inventory.md | multi-frame | REAL_DEVICE_PASS_WITH_NOTES | frames=2; valid=2; completion=1; tag_frames=1; masked_epc=EPC_00B0xxxxxxxxxxxxxxxxxxxx | 1500 | v017 unknown-response was resolved as RF tag response plus completion response. |
| Stage 2 | 7.5.2 | UHF_InventoryRead | docs/current/commands/cards/55_14_uhf_inventory_read.md | not-sent | BLOCKED_BY_PARAMETER |  | 1500 | Read memory bank, address, and word count were not specified. |
| Stage 2 | 7.5.3 | UHF_Read | docs/current/commands/cards/55_15_uhf_read.md | not-sent | BLOCKED_BY_PARAMETER |  | 1500 | Read memory bank, address, and word count were not specified. |

## 6. Unknown-response analysis result

v017 recorded UHF_Inventory as `unknown-response`.
v018 added RF response receive-loop handling and parsed the response as:

- RF tag response frame: 1
- completion response: 1
- parsed tag count: 1
- masked EPC/UII summary: EPC_00B0xxxxxxxxxxxxxxxxxxxx

The raw response is stored only in runtime logs and is not committed.

## 7. Multiple / completion response handling result

- UHF_Inventory receive-loop handling: implemented
- Multiple response handling: implemented for conservative frame collection
- Completion response handling: implemented for Inventory completion count
- UHF_InventoryRead receive-loop handling: implemented, but not executed because read parameters were not specified
- UHF_Read conservative parser: implemented, but not executed because read parameters were not specified

## 8. Tag detection result

- tag detected: yes
- parsed tag count: 1
- EPC/UII masking policy: EPC/UII is masked in Git-managed documents
- raw EPC/UII: runtime log only, not committed

## 9. NACK / timeout / LBT / antenna error

- NACK: none recorded in the masked summary
- timeout: none recorded in the masked summary
- LBT-related error: none recorded in the masked summary
- antenna error: none recorded in the masked summary

## 10. BLOCKED / non-executed items

- UHF_InventoryRead: BLOCKED_BY_PARAMETER
- UHF_Read: BLOCKED_BY_PARAMETER

Reason:

- Read memory bank was not specified.
- Read start address was not specified.
- Read word count was not specified.
- The tool does not guess these values.

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

## 12. Runtime log files

Runtime files were saved under `runtime_logs/stage02_rf_read/` and are not committed.

- `stage01_readonly_20260713_145943_COMx_log.csv`
- `stage01_readonly_20260713_145943_COMx_result.md`

## 13. Result decision

V018_STAGE2_RF_READ_OPERATIONS_PARTIAL

## 14. Next action

- Decide explicit read parameters before executing UHF_InventoryRead or UHF_Read.
- Suggested required inputs: memory bank, read start word address, read word count, and access password policy.
- Keep write, setting-change, FLASH, Lock, Kill, Encode, and ThroughCmd operations outside the next read-only execution unless a separate reviewed scope is created.

## 15. v019 follow-up

v019 selected an explicit `safe-tid` read-only profile and completed `UHF_InventoryRead` and `UHF_Read` with notes.

- Result document: `docs/current/34_STAGE2_READ_COMPLETION_RESULT.md`
- Memory bank: TID(2)
- Start word address: 0
- Word count: 2
- Access password policy: default-zero
- Runtime logs: not committed
