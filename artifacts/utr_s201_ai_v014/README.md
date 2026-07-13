# UTR-S201 AI Assistant Package v014 Stage 0 Remaining Read-only Result no-PDF

## 1. Positioning

- Stage 0 remaining read-only result package
- no-PDF
- Based on v013 ROM read frame adapter
- Focused on Stage 0 read-only commands
- Runtime logs are not committed
- Not a formal external release
- Not a formal RC
- Not a customer release
- Not production-ready
- Not a replacement for the official PDF

## 2. Scope

v014 target:

- ROM version read
- Chip version read
- Error information read

Out of v014 scope:

- Stage 1 read-only
- Write commands
- FLASH write/init
- Frequency change
- Output power change
- Antenna setting change
- Tag memory operation
- Lock / Kill / Encode / ThroughCmd

Out of scope does not mean prohibited by specification.

## 3. Safety and usage policy

- Stage 0 read-only only
- No write command
- No FLASH change
- No RF parameter change
- No tag memory change
- Runtime logs are ignored by Git
- Sensitive values must be masked
- No completed Hex in documents
- No SUM-calculated command examples in documents

## 4. Result

v014 result decision:

- V014_STAGE0_REMAINING_READONLY_PASS_WITH_NOTES

Stage 0 read-only summary:

- ROM version read: ACK; ROM 2.052; USM02; UTR-SUN02-4CH
- Chip version read: ACK; chip firmware 2.052; chip name UR201; subcommand 00h
- Error information read: ACK; error information 00h; normal
- Runtime logs: not committed

## 5. Remaining HOLD items

- Formal external release approval
- License/IP final confirmation
- Customer release decision
- Overseas use / overseas sales decision
- Stage 1 read-only real-device execution logs
- Stage 2 and later real-device verification
- Individual real-device send test for all 54 commands
