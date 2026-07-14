---
title: "Stage 3+ First Execution Batch Plan"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "PLAN_ONLY"
result_status: "NOT_EXECUTED_IN_V021"
related_docs:
  - "35_STAGE3PLUS_HIGH_IMPACT_READINESS.md"
  - "36_STAGE3PLUS_COMMAND_MATRIX.md"
  - "37_STAGE3PLUS_EXECUTION_GATES.md"
  - "38_STAGE3PLUS_RECOVERY_AND_STOP_PLAN.md"
tags:
  - "utr-s201"
  - "guide"
  - "stage3"
  - "stage4"
  - "needs-real-device-test"
  - "needs-review"
---

# Stage 3+ First Execution Batch Plan

## 1. Positioning

This document defines the first execution candidate batches after v020 Stage 3+ high-impact readiness.

v021 is a planning package only. No real-device command is sent in v021.

## 2. Policy

Stage 3+ commands are not split one command at a time. They are grouped by operational risk, reversibility, required parameters, and recovery feasibility.

Protocol support and execution permission remain separate.

## 3. Batch groups

| Batch | Purpose | Candidate commands | Execution in v021 |
|---|---|---|---|
| Batch A | Volatile / recoverable reader control checks | RF carrier control, restart planning | Not executed |
| Batch B | Runtime parameter change planning | select/inventory/expand-select parameter writes | Not executed |
| Batch C | Persistent setting change planning | output, frequency, antenna, FLASH, RSSI, antenna output | Not executed |
| Batch D | Tag memory write planning | write/block write/block erase/encode | Not executed |
| Batch E | Irreversible tag operation planning | lock/kill | Not executed |
| Batch F | Through command planning | through command | Not executed |

## 4. Recommended first real-device candidate

The first real-device candidate should be selected from operations with the following properties:

- no permanent tag damage
- no irreversible tag state change
- no frequency or output power change
- no FLASH persistence unless rollback is explicit
- no customer tag
- test tag only
- single device, single session, operator present
- runtime logging enabled

Based on the current readiness, Batch A or a strictly parameterized subset of Batch B is the preferred first execution candidate.

## 5. Explicitly excluded from first execution

The following should not be included in the first execution batch:

- UHF_Kill
- UHF_Lock
- UHF_Encode
- UHF_ThroughCmd
- FLASH initialization
- frequency setting write
- output power setting write
- tag memory write to customer tags
- any command without explicit rollback/stop conditions

## 6. Completion criteria for moving beyond v021

To proceed from v021 to real execution:

1. target batch selected
2. target command list fixed
3. target device and ROM confirmed
4. target test tag confirmed
5. parameters explicitly written
6. rollback plan written
7. stop conditions written
8. operator explicit approval recorded
9. runtime log directory confirmed
10. command set remains single-session and bounded
