# Overview

Current package: v009 Ver.1.17 traceability completed no-PDF package.

This current clean RAG set covers 54 command cards, ACK/NACK handling, error codes, ROM-based product identification, device/ROM support, RAM/FLASH impact, RF safety, antenna switching, AI implementation guardrails, and AI-assisted traceability completion.

ChatGPT AI specification review completed. This package is not a formal external release, not a customer release, not production-ready, and not a replacement for the official PDF.

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
