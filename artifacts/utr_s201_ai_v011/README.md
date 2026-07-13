# UTR-S201 AI Assistant Package v011 Stage 0/1 Read-only Verification Kit no-PDF

## 1. Positioning

- Stage 0/1 read-only verification kit
- no-PDF
- Based on v010 real-device verification framework
- ROM version read first
- Product/series/ROM identification
- Read-only configuration verification
- Dry-run by default
- --execute required for real-device send
- No write commands included
- No FLASH write
- No frequency change
- No output power change
- No antenna setting change
- No tag memory operation
- Not a formal external release
- Not a formal RC
- Not a customer release
- Not production-ready
- Not a replacement for the official PDF

## 2. Main additions

- docs/current/21_STAGE01_READONLY_VERIFICATION_KIT.md
- docs/current/22_STAGE01_READONLY_COMMAND_LIST.md
- docs/current/23_STAGE01_READONLY_LOGGING_GUIDE.md
- tools/stage01_readonly_verify.py
- templates/stage01_readonly_log_template.csv
- templates/stage01_readonly_result_template.md
- runtime_logs/ ignored by Git

## 3. Safety and usage policy

- Protocol-defined commands are treated as usable commands
- v011 focuses only on Stage 0/1 read-only verification
- Default mode is dry-run
- --execute is required for real-device communication
- Connection target must be explicitly specified
- Runtime logs should not be committed
- No completed Hex in documents
- No SUM-calculated command examples in documents

## 4. Remaining HOLD items

- Formal external release approval
- License/IP final confirmation
- Customer release decision
- Overseas use / overseas sales decision
- Individual real-device send test for all 54 commands
- Stage 2 and later real-device verification
