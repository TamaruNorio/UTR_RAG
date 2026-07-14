# Release And Artifacts

Latest package: `artifacts/utr_s201_ai_v019/utr_s201_ai_v019_stage2_read_completion_no_pdf.zip`.

Current clean RAG baseline: `artifacts/utr_s201_ai_v009/utr_s201_ai_v009_v117_traceability_completed_no_pdf.zip`.

Previous package: `artifacts/utr_s201_ai_v008/utr_s201_ai_v008_v117_full_coverage_no_pdf.zip`.

v009 is the Ver.1.17 traceability completed package with AI-assisted traceability completion. It is no-PDF, not a formal external release, not a formal RC, not a customer release, not production-ready, and not a replacement for the official PDF.

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

## v015 Stage 1 read-only configuration result package

- Latest package: v015 Stage 1 read-only configuration result no-PDF package
- ZIP: `artifacts/utr_s201_ai_v015/utr_s201_ai_v015_stage1_readonly_configuration_result_no_pdf.zip`
- v014 remains the Stage 0 read-only result history.
- v015 is not a formal external release, not a formal RC, not a customer release, and not production-ready.
- v015 is not a replacement for the official PDF.
- v015 records ROM read plus Stage 1 read-only configuration results.
- Runtime logs under `runtime_logs/` are not committed.
- Success, failure, NOT_APPLICABLE, BLOCKED, or HOLD must be recorded honestly.

## v016 Stage 2 RF read preflight package

- Latest package: v016 Stage 2 RF read preflight no-PDF package
- ZIP: `artifacts/utr_s201_ai_v016/utr_s201_ai_v016_stage2_rf_read_preflight_no_pdf.zip`
- v015 remains the Stage 1 read-only configuration result history.
- v016 is not a formal external release, not a formal RC, not a customer release, and not production-ready.
- v016 is not a replacement for the official PDF.
- v016 does not execute Stage 2 RF read commands.
- v016 defines the Stage 2 RF read execution prerequisites, command plan, log template, and stop conditions.
- Runtime logs under `runtime_logs/` are not committed.

## v017 Stage 2 RF read minimal result

- Latest result: v017 Stage 2 RF read minimal result
- Result document: `docs/current/32_STAGE2_RF_READ_MINIMAL_RESULT.md`
- v016 remains the Stage 2 RF read preflight package history.
- v017 does not create a ZIP or GitHub Release.
- v017 executed ROM read, UHF_CheckAntenna, UHF_GetHandle, and UHF_Inventory only.
- UHF_InventoryRead and UHF_Read were not executed.
- Runtime logs under `runtime_logs/` are not committed.
- Write commands, FLASH, frequency changes, output changes, antenna setting changes, and tag memory operations were not executed.

## v018 Stage 2 RF read operations result

- Latest result: v018 Stage 2 RF read operations result
- Result document: `docs/current/33_STAGE2_RF_READ_OPERATIONS_RESULT.md`
- Artifact ZIP: not created in v018
- GitHub Release: not created in v018
- v018 resolved the v017 UHF_Inventory unknown-response as RF tag response plus completion response.
- v018 executed ROM read, UHF_CheckAntenna, UHF_GetHandle, and UHF_Inventory.
- UHF_InventoryRead and UHF_Read were not sent because read parameters were not specified.
- Runtime logs under `runtime_logs/` are not committed.
- Write commands, FLASH, frequency changes, output changes, antenna setting changes, and tag memory writes were not executed.

## v019 Stage 2 read completion package

- Latest package: v019 Stage 2 read completion no-PDF package
- ZIP: `artifacts/utr_s201_ai_v019/utr_s201_ai_v019_stage2_read_completion_no_pdf.zip`
- Result document: `docs/current/34_STAGE2_READ_COMPLETION_RESULT.md`
- v019 uses the explicit `safe-tid` read-only profile for UHF_InventoryRead and UHF_Read.
- v019 completed ROM read, UHF_CheckAntenna, UHF_GetHandle, UHF_Inventory, UHF_InventoryRead, and UHF_Read with notes.
- Runtime logs under `runtime_logs/` are not committed.
- Write commands, FLASH, frequency changes, output changes, antenna setting changes, InventoryParam/SelectParam/ExpandSelectParam changes, tag memory writes, Lock, Kill, Encode, and ThroughCmd were not executed.
- v019 is not a formal external release, not a formal RC, not a customer release, and not production-ready.

## v020 Stage 3+ high-impact readiness

- Latest plan-only readiness update: v020 Stage 3+ high-impact readiness
- Readiness document: `docs/current/35_STAGE3PLUS_HIGH_IMPACT_READINESS.md`
- Command matrix: `docs/current/36_STAGE3PLUS_COMMAND_MATRIX.md`
- Execution gates: `docs/current/37_STAGE3PLUS_EXECUTION_GATES.md`
- Recovery and stop plan: `docs/current/38_STAGE3PLUS_RECOVERY_AND_STOP_PLAN.md`
- v020 separates protocol support from execution permission.
- Stage 3+ real-device execution requires explicit approval, complete parameters, impact review, recovery plan, runtime logging, and stop conditions.
- Artifact ZIP: not created in v020
- GitHub Release: not created in v020
- Real-device command send: not performed in v020

## v021 Stage 3+ first batch planning

v021 adds a plan-only package for selecting the first Stage 3+ execution batch.

- Stage 3+ first execution batch plan
- Stage 3+ parameter sheet
- Stage 3+ operator approval template
- No real-device command send
- No ZIP or Release

## v022 Final RC package

v022 consolidates the current no-PDF UTR-S201 AI assistant package as a Final RC.

- Stage 2 read completion included
- Stage 3+ readiness included
- Stage 3+ first batch planning included
- AI context / frontmatter metadata included
- no PDF included
- no runtime logs included
- no real-device command sent by package creation
