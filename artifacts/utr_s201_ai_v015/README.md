# UTR-S201 AI Assistant Package v015 Stage 1 Read-only Configuration Result no-PDF

## 1. Positioning

- Stage 1 read-only configuration result package
- no-PDF
- Based on v014 Stage 0 read-only result
- Focused on ROM read plus Stage 1 read-only commands
- Runtime logs are not committed
- Not a formal external release
- Not a formal RC
- Not a customer release
- Not production-ready
- Not a replacement for the official PDF

## 2. Scope

v015 target:

- ROM version read
- Stage 1 read-only configuration reads

Out of v015 scope:

- Write commands
- FLASH write/init
- Frequency change
- Output power change
- Antenna setting change
- RF tag communication
- Tag memory operation
- Lock / Kill / Encode / ThroughCmd

Out of scope does not mean prohibited by specification.

## 3. Safety and usage policy

- ROM read first
- Stage 1 read-only only
- No write command
- No FLASH change
- No RF parameter change
- No tag memory change
- Runtime logs are ignored by Git
- Sensitive values must be masked
- No completed Hex in documents
- No SUM-calculated command examples in documents

## 4. Result

v015 result decision:

- V015_STAGE1_READONLY_CONFIGURATION_PARTIAL

Result summary:

- ROM read: ACK; ROM 2.052; USM02; UTR-SUN02-4CH
- Stage 1 PASS: 10 commands
- NOT_APPLICABLE_TO_TARGET: 2 commands
- BLOCKED_BY_PARAMETER: 1 command
- BLOCKED_BY_DEVICE_OR_ROM: 2 commands
- Runtime logs: not committed

## 5. Remaining HOLD items

- Formal external release approval
- License/IP final confirmation
- Customer release decision
- Overseas use / overseas sales decision
- Stage 1 blocked/not-applicable items review
- Stage 2 and later real-device verification
- Individual real-device send test for all 54 commands
