---
title: "Stage 2 RF Read Command Plan"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:[]
tags:
  - "utr-s201"
  - "guide"
  - "stage2"
  - "rf-read"
---

# Stage 2 RF Read Command Plan

## 1. Positioning

This document defines the planned order and required checks for Stage 2 RF read operations.
v016 does not execute these commands on a real device.

## 2. Recommended execution order

1. ROM version read
2. Confirm required current settings from Stage 1 read-only results
3. UHF_CheckAntenna
4. UHF_GetHandle
5. UHF_Inventory
6. UHF_InventoryRead
7. UHF_Read

## 3. Command plan

| Execution order | Command name | Purpose | Required prior checks | Required parameters | Expected response | Stop conditions | Log fields | Next command if PASS | Next action if NACK | Next action if timeout |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | ROM version read | Identify device series, product type, and ROM version before RF operations. | Serial connection, timeout policy, no pending error condition. | Connection address, timeout. | ACK with ROM data. | ROM read fail, device identification fail, unexpected response. | device_series, product_type, rom_version, timeout_ms, actual_response_type. | Stage 1 current setting confirmation. | Stop and record NACK. | Stop and record timeout. |
| 2 | Stage 1 current setting confirmation | Confirm current settings without changing frequency, output, antenna, or InventoryParam. | v015 result availability and target device baseline. | Existing masked Stage 1 summary or read-only confirmation result. | Existing PASS/BLOCKED/NOT_APPLICABLE result summary. | Required current setting not known for planned RF test. | active_antenna, antenna_connection_status, parameter_summary. | UHF_CheckAntenna. | Stop and record missing setting. | Stop and record missing setting. |
| 3 | UHF_CheckAntenna | Confirm antenna connection before RF read. | ROM identified, target antenna selected, physical antenna connected. | Active antenna, timeout. | ACK/NACK/timeout. | Antenna error, unsupported command, unexpected response, consecutive timeout. | active_antenna, antenna_connection_status, nack_error_code_1..4, elapsed_ms. | UHF_GetHandle or UHF_Inventory. | Stop if antenna/LBT/unsupported/device mismatch; otherwise record supported NACK and decide. | Stop after timeout policy threshold. |
| 4 | UHF_GetHandle | Confirm tag handle behavior when a target tag is present. | Antenna check complete, tag-present condition decided, receive-loop policy defined. | Target tag condition, timeout, optional password policy if applicable. | ACK/NACK plus possible RF tag response handling. | No target tag condition, access password missing, unexpected response, antenna/LBT error. | tag_present, tag_type, tag_id_masked, expected_response_type, actual_response_type. | UHF_Inventory. | Stop or continue with notes only when NACK is expected under the test condition. | Stop after timeout policy threshold. |
| 5 | UHF_Inventory | Inventory RF tags using current settings. | Antenna confirmed, tag-present or no-tag condition defined, no InventoryParam change. | Timeout, active antenna, tag-present condition. | ACK/NACK, zero-tag result, or tag response depending on condition. | Antenna error, LBT error, unsupported command, unexpected response. | parsed_tag_count, parsed_epc_masked, rf_emission, timeout_ms, elapsed_ms. | UHF_InventoryRead if memory read target is defined. | Stop or continue with notes for expected no-tag/condition-specific NACK. | Stop after timeout policy threshold. |
| 6 | UHF_InventoryRead | Inventory and read selected memory using current settings. | Inventory result reviewed, memory bank selected, read range defined, access password policy decided. | Memory bank, read address, word count, access password if required. | ACK/NACK plus tag/read response handling. | Memory bank missing, read address missing, word count missing, access password missing, antenna/LBT error. | memory_bank, read_address, read_word_count, parsed_epc_masked, ack_summary. | UHF_Read if standalone read target is defined. | Stop unless NACK is expected and documented. | Stop after timeout policy threshold. |
| 7 | UHF_Read | Read memory from a selected target tag. | Target tag identified, memory bank/address/word count confirmed, password policy decided. | Target tag, memory bank, address, word count, access password if required. | ACK/NACK plus read data response handling. | Target tag missing, memory precondition missing, access password missing, unexpected response, antenna/LBT error. | tag_id_masked, memory_bank, read_address, read_word_count, actual_response_type. | End Stage 2 and record result. | Stop unless NACK is expected and documented. | Stop after timeout policy threshold. |

## 4. Command-specific notes

- UHF_Inventory is an RF read operation and requires a defined tag-present or no-tag condition.
- UHF_InventoryRead behaves like Inventory plus Read and requires target memory selection before execution.
- UHF_Read requires the target tag, memory bank, address, word count, and access password policy before execution.
- If an access password is required, ask the user for the policy and do not guess.
- Execute with the current settings only. Do not change frequency, output power, antenna settings, or InventoryParam as part of Stage 2.

## 5. v019 selected execution profile

v019 used the following explicit safe read-only profile for the Stage 2 completion run.

- Profile: `safe-tid`
- Target tag: first tag detected by `UHF_Inventory`
- Memory bank: TID(2)
- Start word address: 0
- Word count: 2
- Access password policy: default-zero
- Max tags summarized in Git-managed documents: 1
- Result document: `docs/current/34_STAGE2_READ_COMPLETION_RESULT.md`

The profile does not change InventoryParam, SelectParam, ExpandSelectParam, antenna settings, frequency, output power, FLASH, or tag memory.
