---
title: "Stage 3+ First Batch Parameter Sheet"
doc_type: "schema"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "PLAN_ONLY"
result_status: "NOT_EXECUTED_IN_V021"
related_docs:
  - "39_STAGE3PLUS_FIRST_EXECUTION_BATCH_PLAN.md"
  - "37_STAGE3PLUS_EXECUTION_GATES.md"
tags:
  - "utr-s201"
  - "schema"
  - "stage3"
  - "stage4"
  - "needs-review"
---

# Stage 3+ First Batch Parameter Sheet

## 1. Purpose

This sheet defines the minimum information required before Stage 3+ real-device execution.

## 2. Common parameters

| Field | Value | Required |
|---|---|---|
| target_device | UTR-S201 series device name | yes |
| series | ROM series string | yes |
| rom_version | ROM version | yes |
| connection_type | serial / lan | yes |
| port_or_host | masked COMx or host | yes |
| baudrate_or_port | masked value | yes |
| timeout_ms | numeric value | yes |
| test_tag_only | true / false | yes |
| customer_tag_present | false required | yes |
| runtime_log_dir | runtime_logs/... | yes |

## 3. Command-specific parameters

| Command group | Required parameters |
|---|---|
| select/inventory parameter write | current value, new value, restore value, RAM/FLASH scope |
| antenna setting | current antenna config, new antenna config, restore config |
| RF carrier control | on/off value, expected duration, stop condition |
| restart | reason, expected recovery time, reconnect method |
| FLASH operation | address/value or init scope, backup value, rollback plan |
| tag write | target EPC/UII, memory bank, address, word count, data, test tag confirmation |
| lock/kill | explicit irreversible approval, target tag confirmation, reason |
| through command | exact protocol target, expected response, abort condition |

## 4. Status values

- PARAMETER_READY
- PARAMETER_BLOCKED
- NEEDS_PDF_CONFIRMATION
- NEEDS_OPERATOR_APPROVAL
- NOT_SELECTED_FOR_FIRST_BATCH
