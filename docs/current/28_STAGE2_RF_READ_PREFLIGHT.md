---
title: "Stage 2 RF Read Preflight"
doc_type: "preflight"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:[]
tags:
  - "utr-s201"
  - "preflight"
  - "stage2"
  - "rf-read"
---

# Stage 2 RF Read Preflight

## 1. Positioning

v016 is the preflight package before Stage 2 RF read operations are executed on a real device.

v016 does not send real-device commands.
It organizes the execution prerequisites, confirmation items, stop conditions, and log items for Stage 2 commands.

## 2. Device baseline

The following baseline is carried forward from v015.

- product type: UTR-SUN02-4CH
- series: USM02
- ROM version: 2.052
- connection: USB serial
- baudrate: 115200bps
- Stage 0 status: completed with notes
- Stage 1 status: partial with notes

## 3. Stage 2 candidate commands

| PDF section | Command name | Card path | RF emission involved | Requires antenna | Requires tag | Requires memory bank | Requires access password | Device/ROM condition | Preflight status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 7.3.5 | UHF_CheckAntenna | docs/current/commands/cards/55_44_uhf_check_antenna.md | Yes or RF-adjacent antenna check | Yes | No | No | No | UTR-SUN02-4CH / USM02 / ROM 2.052 target baseline | READY_FOR_PREFLIGHT_REVIEW | Confirm antenna connection and active antenna before any RF read operation. |
| 7.3.12 | UHF_GetHandle | docs/current/commands/cards/55_46_uhf_get_handle.md | Yes | Yes | Yes | No | Depends on tag condition | ROM 2.050 or later; target ROM 2.052 satisfies the listed ROM baseline | READY_FOR_PREFLIGHT_REVIEW | Requires tag placement and receive-loop handling policy. |
| 7.5.1 | UHF_Inventory | docs/current/commands/cards/55_10_uhf_inventory.md | Yes | Yes | Conditional | No | No | Supported for target baseline unless a later site condition blocks execution | READY_FOR_PREFLIGHT_REVIEW | Define tag-present or no-tag test before execution. |
| 7.5.2 | UHF_InventoryRead | docs/current/commands/cards/55_14_uhf_inventory_read.md | Yes | Yes | Yes | Yes | Depends on memory bank and tag state | Supported for target baseline unless parameter conditions block execution | READY_FOR_PREFLIGHT_REVIEW | Inventory plus read behavior requires memory-bank and read-range decisions. |
| 7.5.3 | UHF_Read | docs/current/commands/cards/55_15_uhf_read.md | Yes | Yes | Yes | Yes | Depends on memory bank and tag state | Supported for target baseline unless parameter conditions block execution | READY_FOR_PREFLIGHT_REVIEW | Target tag, memory bank, address, word count, and access password policy must be decided first. |

## 4. Preflight checks

- [ ] アンテナが正しく接続されているか
- [ ] 使用アンテナ番号を確認したか
- [ ] タグを置くか、置かないか
- [ ] タグを置く場合、対象タグの種類を確認したか
- [ ] Inventoryのみか、InventoryRead/Readまで進むか
- [ ] Read対象メモリバンクを確認したか
- [ ] Access password要否を確認したか
- [ ] 現在の出力設定を変更しないことを確認したか
- [ ] 現在の周波数設定を変更しないことを確認したか
- [ ] InventoryParamを変更しないことを確認したか
- [ ] timeout値を決めたか
- [ ] NACK時の停止条件を決めたか
- [ ] LBT/antenna error時の停止条件を決めたか

## 5. Out of v016 scope

The following items are outside the v016 execution scope.

- Stage 2 RF command execution
- InventoryParam write
- SelectParam write
- ExpandSelectParam write
- Output power write
- Frequency write
- Antenna setting write
- Tag memory write
- Lock / Kill / Encode / ThroughCmd

Out of scope does not mean prohibited by the protocol specification.
It means the operation is not executed in v016.

## 6. v019 completion note

v019 executed the Stage 2 read target set after v016 preflight and v018 response-loop preparation.

- Result document: `docs/current/34_STAGE2_READ_COMPLETION_RESULT.md`
- Read profile: `safe-tid`
- Memory bank: TID(2)
- Start word address: 0
- Word count: 2
- ROM read, UHF_CheckAntenna, UHF_GetHandle, UHF_Inventory, UHF_InventoryRead, and UHF_Read completed with notes.
- Runtime logs remain outside Git management.
