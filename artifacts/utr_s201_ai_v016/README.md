# UTR-S201 AI Assistant Package v016 Stage 2 RF Read Preflight no-PDF

## 1. Positioning

- Stage 2 RF read preflight package
- no-PDF
- Based on v015 Stage 1 read-only configuration result
- Focused on Stage 2 RF read planning
- No Stage 2 RF command execution in v016
- Runtime logs are not committed
- Not a formal external release
- Not a formal RC
- Not a customer release
- Not production-ready
- Not a replacement for the official PDF

## 2. Scope

v016 target:

- UHF_CheckAntenna preflight
- UHF_GetHandle preflight
- UHF_Inventory preflight
- UHF_InventoryRead preflight
- UHF_Read preflight
- RF read logging template
- Stop condition definition

Out of v016 scope:

- Actual Stage 2 RF command execution
- Setting writes
- InventoryParam writes
- Frequency changes
- Output power changes
- Antenna setting changes
- Tag memory writes
- Lock / Kill / Encode / ThroughCmd

Out of scope does not mean prohibited by specification.

## 3. Safety and usage policy

- No RF read command sent in v016
- No write command
- No FLASH change
- No frequency change
- No output power change
- No antenna setting change
- No tag memory change
- Sensitive values must be masked
- No completed Hex in documents
- No SUM-calculated command examples in documents

## 4. Remaining HOLD items

- Formal external release approval
- License/IP final confirmation
- Customer release decision
- Overseas use / overseas sales decision
- Stage 2 RF read real-device execution
- Stage 3 and later real-device verification
- Individual real-device send test for all 54 commands
