---
title: "Stage 3+ Execution Gates"
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
  - "38_STAGE3PLUS_RECOVERY_AND_STOP_PLAN.md"
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

# Stage 3+ Execution Gates

## 1. Positioning

This document defines the gates required before any Stage 3+ high-impact real-device execution.
v020 does not execute Stage 3+ commands.

## 2. Gate table

| Gate | Name | Required condition | Evidence to record | If not satisfied |
|---:|---|---|---|---|
| 0 | Official PDF section confirmed | PDF section and command card are identified. | PDF section, command name, command bytes, card path. | Keep `READY_FOR_EXPLICIT_APPROVAL`; do not execute. |
| 1 | Device/ROM confirmed | ROM read identifies series, product type, and ROM version. | ROM raw, ROM version, series, product type. | Stop before command execution. |
| 2 | Target command selected | Command is selected as part of a reviewed Stage 3+ batch. | Batch name, selected command list, excluded commands. | Do not include in execution batch. |
| 3 | Parameters explicitly specified | Every required parameter is provided without guessing. | Parameter summary with no completed Hex or SUM-calculated command. | Block as `BLOCKED_BY_PARAMETER`. |
| 4 | Impact understood | RF, RAM, FLASH, tag memory, external I/O, and persistence impacts are reviewed. | Impact category and affected state. | Keep plan-only. |
| 5 | Recovery / rollback plan defined | Recovery action is documented before execution. | Backup, rollback, replacement tag, reconnect, or no-recovery statement. | Block as `BLOCKED_BY_RECOVERY_PLAN`. |
| 6 | Operator explicit approval | Operator approval is recorded for the exact batch and parameters. | Approval note, timestamp, operator role. | Do not execute. |
| 7 | Runtime logging enabled | Logs are enabled and storage path is outside Git-managed artifacts. | Runtime log directory and masking policy. | Do not execute. |
| 8 | Stop conditions defined | NACK, timeout, unknown response, LBT, antenna error, and operator stop rules are set. | Stop condition list. | Do not execute. |
| 9 | Execute single batch only | Batch scope is limited and unrelated high-impact categories are not mixed. | Batch ID and command count. | Split into a reviewed smaller batch. |

## 3. v020 CLI behavior

`tools/stage01_readonly_verify.py --command-set stage3plus-plan` is plan-only.

Even if `--execute` is provided, the tool prints the plan and exits without opening a serial or TCP connection.

## 4. Required result statuses

- `READY_FOR_EXPLICIT_APPROVAL`: command is protocol-defined and organized, but not approved for execution.
- `NOT_EXECUTED_IN_V020`: no Stage 3+ real-device send was performed in v020.
- `BLOCKED_BY_PARAMETER`: a future execution request lacks required parameters.
- `BLOCKED_BY_RECOVERY_PLAN`: a future execution request lacks recovery/rollback conditions.
