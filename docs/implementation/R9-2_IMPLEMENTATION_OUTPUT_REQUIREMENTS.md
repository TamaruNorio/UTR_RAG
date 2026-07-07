# R9-2 Implementation Output Requirements

## 1. Purpose

This document defines output requirements for implementation assistance.

## 2. Required behavior

- Ask clarification questions before implementation when device, connection, scope, or operation level is unclear.
- Present implementation policy before code.
- Separate device-dependent checks from desk-checkable logic.
- Separate connection, send, receive, and close phases.
- Include timeout handling, error handling, and logging guidance.
- Externalize connection settings and file paths.
- Keep Japan domestic scope explicit.
- Do not treat this package as a formal external release or a replacement for the official PDF.

## 3. Safety boundaries

- Level 4 or higher operations require explicit confirmation.
- Level 5 operations require explicit approval and recovery procedure.
- Do not include completed Hex examples, checksum-calculated commands, or device-sendable code in this RAG repository.

## 4. Required checklists

### Before output

- Confirm target device.
- Confirm connection method.
- Confirm Japan domestic scope.
- Confirm read target and logging needs.
- Confirm whether setting changes are allowed.

### After output

- Connection, send, receive, and close are separated.
- Timeout, error handling, and logging are included.
- Settings are externalized.
- No completed command byte sequence is embedded.

### Before real-device verification

- Record device, connection, date, operator, and location.
- Confirm log masking policy.
- Confirm approval and recovery procedure for Level 4 or higher operations.

### External review

- Not a formal RC.
- Not a formal external release.
- Japan domestic scope only.
- Overseas use remains out of scope.
- SDK should be the first option where available.
