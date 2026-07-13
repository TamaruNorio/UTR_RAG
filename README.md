# UTR_RAG

UTR_RAG manages AI-ready RAG documents and no-PDF artifacts for UTR-S201 series protocol assistance.

Current package:

- `artifacts/utr_s201_ai_v009/utr_s201_ai_v009_v117_traceability_completed_no_pdf.zip`
- Source specification: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17
- Command cards: 54
- AI-assisted traceability completion
- ChatGPT AI specification review completed
- Includes command list / command format / ACK / NACK / device-ROM / RAM-FLASH / RF-safety references.

Previous package:

- v008 clean full coverage package: `artifacts/utr_s201_ai_v008/utr_s201_ai_v008_v117_full_coverage_no_pdf.zip`

Positioning:

- Japan domestic scope
- Japanese users
- no-PDF
- Not a formal external release
- Not a formal RC
- Not a customer release
- Not production-ready
- Not a replacement for the official PDF
- Not confirmed by individual real-device sends for all 54 commands

Main references:

- `docs/README.md`
- `docs/OPERATIONS.md`
- `docs/current/00_OVERVIEW.md`
- `docs/current/09_COMMAND_MASTER_V117.md`
- `docs/current/16_TRACEABILITY_INDEX_V117.md`
- `docs/current/commands/cards/`
- v008 review materials: `docs/review/v008/`
- `artifacts/README.md`

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

## v012 Stage 0 read-only real-device result package

- Latest package: v012 Stage 0 read-only real-device result no-PDF package
- ZIP: `artifacts/utr_s201_ai_v012/utr_s201_ai_v012_stage0_readonly_real_device_result_no_pdf.zip`
- v011 remains the Stage 0/1 read-only verification kit history.
- v012 is not a formal external release, not a formal RC, not a customer release, and not production-ready.
- v012 is not a replacement for the official PDF.
- v012 records a masked Stage 0 read-only real-device result summary.
- Raw runtime logs under `runtime_logs/` are not committed.
- If execution cannot complete, v012 records the HOLD result honestly.

## v013 Stage 0 ROM read frame adapter package

- Latest package: v013 Stage 0 ROM read frame adapter no-PDF package
- ZIP: `artifacts/utr_s201_ai_v013/utr_s201_ai_v013_stage0_rom_read_frame_adapter_no_pdf.zip`
- v012 remains the Stage 0 read-only result HOLD history.
- v013 is not a formal external release, not a formal RC, not a customer release, and not production-ready.
- v013 is not a replacement for the official PDF.
- v013 confirms the frame adapter for ROM version read only.
- v013 records ROM 2.052 / USM02 / UTR-SUN02-4CH from COMx / 115200bps as a masked summary.
- Runtime logs under `runtime_logs/` are not committed.
- Success, failure, or HOLD must be recorded honestly.

## v014 Stage 0 remaining read-only result package

- Latest package: v014 Stage 0 remaining read-only result no-PDF package
- ZIP: `artifacts/utr_s201_ai_v014/utr_s201_ai_v014_stage0_remaining_readonly_result_no_pdf.zip`
- v013 remains the ROM read frame adapter history.
- v014 is not a formal external release, not a formal RC, not a customer release, and not production-ready.
- v014 is not a replacement for the official PDF.
- v014 records Stage 0 read-only 3-command confirmation results.
- Runtime logs under `runtime_logs/` are not committed.
- Success, failure, or HOLD must be recorded honestly.
