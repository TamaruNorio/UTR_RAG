---
title: "Stage 3+ Operator Approval Template"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "PLAN_ONLY"
result_status: "NOT_EXECUTED_IN_V021"
related_docs:
  - "39_STAGE3PLUS_FIRST_EXECUTION_BATCH_PLAN.md"
  - "40_STAGE3PLUS_FIRST_BATCH_PARAMETER_SHEET.md"
tags:
  - "utr-s201"
  - "guide"
  - "stage3"
  - "stage4"
  - "needs-review"
---

# Stage 3+ Operator Approval Template

## 1. Approval statement

Before any Stage 3+ real-device execution, record the following approval in the issue, PR, or local execution record.

```text
I approve this bounded Stage 3+ real-device execution.

Target batch:
Target commands:
Target device:
ROM version:
Connection:
Test tag:
Customer tag present: no
Persistent setting change: yes/no
Tag memory change: yes/no
Irreversible operation: yes/no
Rollback plan confirmed: yes/no
Stop conditions confirmed: yes/no
Runtime logging confirmed: yes/no
```

## 2. Required confirmations

- The target is not a customer tag.
- The target command list is fixed.
- The execution is a bounded single batch.
- Parameters are explicit.
- The expected result is known.
- The rollback/restore method is known where applicable.
- Stop conditions are known.
- Raw logs remain outside Git.
- Masked summary only is committed.

## 3. Disallowed approval

Do not proceed with broad approval such as:

- "try everything"
- "run all writes"
- "change settings as needed"
- "use any tag"
- "continue even after NACK"
