# UTR-S201 AI Assistant Package v013 Stage 0 ROM Read Frame Adapter no-PDF

## 1. Positioning

- Stage 0 ROM read frame adapter package
- no-PDF
- Based on v012 Stage 0 read-only result
- Focused only on ROM version read
- Implements common frame adapter for ROM version read
- Runtime logs are not committed
- Not a formal external release
- Not a formal RC
- Not a customer release
- Not production-ready
- Not a replacement for the official PDF

## 2. Scope

v013 target:

- ROM version read

Out of v013 scope:

- Chip version read
- Error information read
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

- ROM read only
- No write command
- No FLASH change
- No RF parameter change
- No tag memory change
- Runtime logs are ignored by Git
- Sensitive values must be masked
- No completed Hex in documents
- No SUM-calculated command examples in documents

## 4. Result

v013 result decision:

- V013_STAGE0_ROM_READ_REAL_DEVICE_PASS_WITH_NOTES

ROM read summary:

- actual_response_type: ACK
- ROM version: 2.052
- series name: USM02
- product type: UTR-SUN02-4CH
- connection: COMx / 115200bps
- runtime logs: not committed

## 5. Remaining HOLD items

- Formal external release approval
- License/IP final confirmation
- Customer release decision
- Overseas use / overseas sales decision
- Stage 0 chip version and error information execution
- Stage 1 read-only real-device execution logs
- Stage 2 and later real-device verification
- Individual real-device send test for all 54 commands
