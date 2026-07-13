# UTR_RAG Documents

Current clean RAG set:

- `docs/current/00_OVERVIEW.md`
- `docs/current/09_COMMAND_MASTER_V117.md`
- `docs/current/10_RESPONSE_AND_NACK_MASTER.md`
- `docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
- `docs/current/12_RAM_FLASH_IMPACT_MATRIX.md`
- `docs/current/13_RF_SAFETY_AND_CARRIER_RULES.md`
- `docs/current/14_AI_IMPLEMENTATION_GUARDRAILS.md`
- `docs/current/15_PARAMETER_CONFIRMATION_GUIDE.md`
- `docs/current/16_TRACEABILITY_INDEX_V117.md`
- `docs/current/commands/cards/`
- v008 review materials: `docs/review/v008/`

The current set is based on UTR-S201 series communication protocol manual Ver.1.17 and contains 54 command cards. v009 adds AI-assisted traceability completion and is no-PDF. It is not a replacement for the official PDF.

## v010 real-device verification framework package

- Latest package: v010 real-device verification framework no-PDF package
- ZIP: `artifacts/utr_s201_ai_v010/utr_s201_ai_v010_real_device_verification_framework_no_pdf.zip`
- v009 remains the traceability completed package history.
- v010 is not a formal external release, not a formal RC, not a customer release, and not production-ready.
- v010 is not a replacement for the official PDF.
- v010 does not claim real-device send verification has been completed.
- v010 defines the framework for real-device verification.
- ChatGPT AI specification review completed.
- AI-assisted traceability completion completed.

## v011 Stage 0/1 read-only verification kit

- Latest package: v011 Stage 0/1 read-only verification kit no-PDF package
- ZIP: `artifacts/utr_s201_ai_v011/utr_s201_ai_v011_stage01_readonly_verification_kit_no_pdf.zip`
- v010 remains the real-device verification framework history.
- v011 is not a formal external release, not a formal RC, not a customer release, and not production-ready.
- v011 is not a replacement for the official PDF.
- v011 is a Stage 0/1 read-only verification kit.
- Real-device communication requires `--execute`.
- Default mode is dry-run.
- Write commands and setting-change commands are outside v011 scope.
