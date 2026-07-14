---
title: "Stage 3+ Recovery And Stop Plan"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
operation_stage: "Stage 3+"
verification_status: "PLAN_ONLY"
result_status: "NOT_EXECUTED_IN_V020"
related_docs:
  - "35_STAGE3PLUS_HIGH_IMPACT_READINESS.md"
  - "36_STAGE3PLUS_COMMAND_MATRIX.md"
  - "37_STAGE3PLUS_EXECUTION_GATES.md"
tags:
  - "utr-s201"
  - "guide"
  - "stage3"
  - "stage4"
  - "stage5"
  - "write-operation"
  - "flash-operation"
  - "tag-memory"
  - "needs-real-device-test"
  - "needs-review"
---

# Stage 3+ Recovery And Stop Plan

## 1. Positioning

This document organizes recovery and stop planning for Stage 3+ high-impact commands.
v020 does not execute these commands on a real device.

## 2. Recovery considerations

| Impact area | Recovery / rollback viewpoint | Required prior record |
|---|---|---|
| FLASH change | Existing settings may need backup before write/init. Recovery may require restoring known values or reinitializing configuration. | Current FLASH/configuration snapshot, intended value, rollback value, operator approval. |
| Frequency change | Wrong frequency can affect legal/site operation. Recovery requires restoring known approved frequency settings. | Current frequency, approved target, site/legal confirmation, rollback value. |
| Output power change | Output changes can affect RF exposure, read range, and site behavior. Recovery requires restoring approved output settings. | Current output, approved target, antenna context, rollback value. |
| Antenna setting change | Wrong antenna routing can stop reads or route RF unexpectedly. Recovery requires known active antenna and wiring map. | Active antenna, antenna count, wiring map, rollback value. |
| Tag memory write/erase | Tag data may not be recoverable unless backed up externally. | Target tag, memory bank, address, word count, original data if readable, replacement-tag plan. |
| Lock/Kill | Lock may be irreversible depending on parameters; Kill is irreversible for the target tag. | Disposable target tag confirmation, access password policy, written approval. |
| Encode | Encode can modify multiple fields and lock state. | Target tag isolation, expected encoded state, replacement-tag plan. |
| ThroughCmd | Payload impact depends on command payload and can exceed normal card-level assumptions. | Payload review, expected RF/tag behavior, stop condition, recovery statement. |

## 3. Immediate stop conditions

Stop the batch immediately when any of the following occurs.

- ROM mismatch
- Device/product mismatch
- Missing parameter
- Missing explicit approval
- Missing recovery plan
- NACK that is not explicitly expected
- timeout
- unknown response
- parse error
- LBT-related error
- antenna error
- unexpected tag count
- unexpected target tag
- operator stop request

## 4. NACK / timeout / unknown-response handling

- Record NACK error code 1-4 when available.
- Do not continue into a stronger impact command after an unexpected NACK.
- Do not retry high-impact writes automatically.
- Treat timeout as a stop condition unless the reviewed batch explicitly defines a limited retry.
- Treat unknown response as a stop condition and preserve raw details only in runtime logs.

## 5. LBT / antenna error handling

- Stop immediately on LBT-related error.
- Stop immediately on antenna error.
- Do not change frequency, output power, antenna switching, or InventoryParam as a response to the error unless a separate reviewed recovery batch exists.

## 6. Logging and masking

- Runtime logs remain outside Git.
- Git-managed summaries must mask or omit EPC/UII/TID, customer information, real IP addresses, and raw response data.
- Do not document completed Hex or SUM-calculated command examples.
