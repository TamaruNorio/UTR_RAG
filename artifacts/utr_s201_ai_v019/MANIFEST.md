# v019 Manifest

## 1. Package

- Package name:
  utr_s201_ai_v019_stage2_read_completion_no_pdf.zip

- Package path:
  artifacts/utr_s201_ai_v019/utr_s201_ai_v019_stage2_read_completion_no_pdf.zip

- SHA256:
  AE8ECC63D1BD2E59CC2F29B312CCCBC295448EF023765DBDAFC94E227D10BF59

## 2. Package type

- Stage 2 read completion package
- no-PDF
- Japan domestic scope
- Japanese users
- Not formal external release
- Not formal RC
- Not customer release
- Not production-ready
- Not replacement for official PDF

## 3. Included files/directories

- README.md
- docs/README.md
- docs/OPERATIONS.md
- docs/current/
- docs/current/commands/cards/
- tools/stage01_readonly_verify.py
- templates/
- artifacts/README.md
- artifacts/utr_s201_ai_v019/README.md
- artifacts/utr_s201_ai_v019/MANIFEST.md

## 4. Excluded items

- PDF
- .git
- .github
- venv
- .venv
- __pycache__
- .pytest_cache
- node_modules
- runtime_logs
- actual CSV logs
- docs/audit
- docs/release
- docs/review
- old ZIPs
- v019 ZIP itself
- customer information
- tag unique IDs
- real IP addresses

## 5. Safety notes

- No write command performed
- No FLASH write/init performed
- No frequency change performed
- No output power change performed
- No antenna setting change performed
- No InventoryParam/SelectParam/ExpandSelectParam change performed
- No tag memory write performed
- No Lock / Kill / Encode / ThroughCmd performed
- No executable control code added beyond the existing reviewed verification helper
- No completed Hex added
- No SUM-calculated command added
- No PDF included
- Existing v004-v018 ZIP files not modified

## 6. Coverage notes

- Stage 2 target commands recorded: 6
- ROM read: REAL_DEVICE_PASS_WITH_NOTES
- UHF_CheckAntenna: REAL_DEVICE_PASS_WITH_NOTES
- UHF_GetHandle: REAL_DEVICE_PASS_WITH_NOTES
- UHF_Inventory: REAL_DEVICE_PASS_WITH_NOTES
- UHF_InventoryRead: REAL_DEVICE_PASS_WITH_NOTES
- UHF_Read: REAL_DEVICE_PASS_WITH_NOTES
- Runtime logs: excluded
- Raw EPC/UII/TID/read data: excluded from Git-managed summaries

## 7. Remaining HOLD items

- Formal external release approval
- License/IP final confirmation
- Customer release decision
- Overseas use / overseas sales decision
- Stage 3 and later real-device verification
- Individual real-device send test for all 54 commands
