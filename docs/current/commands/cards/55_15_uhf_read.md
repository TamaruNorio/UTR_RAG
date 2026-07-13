# UHF_Read

## 1. Command identity

- PDF section: 7.5.3
- Command name: UHF_Read
- Category: RFタグ通信
- Command byte: 55h
- Detail command byte: 15h
- Subcommand byte: -
- Command family: RFタグ通信
- Read / Write / Control / RF tag / Mode: RF tag
- Source PDF: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17 (TDR-MNL-PRC-UTR-S201-117.pdf, 2025-06-16)
- Verification status: PDF Ver.1.17 desk review

## 2. Purpose

RFタグメモリを読み取る。

## 3. Usage status

- Status: SUPPORTED_WITH_PARAMETERS
- Reason: PDF Ver.1.17 lists this command in section 7.5.3. AI/RAG organizes device, ROM, parameter, impact, response, and recovery conditions instead of deciding arbitrary non-use.

## 4. Safety / impact classification

- RF emission: Yes
- Setting change: No
- RAM change: No
- FLASH change: Depends on write target
- Tag memory change: Read-only RF access
- External I/O change: No
- Persistent effect: Check whether the target field is RAM-only, FLASH-backed, or tag-memory persistent.
- Recovery note required: As needed
- Parameter confirmation required: Target device series, ROM version, connection address, timeout policy, target tag, memory bank, word address, word count, Access password if required

## 5. Device / ROM support

- UTR-S201: Supported
- UTR-SUN02-4CH: Supported
- UTR-SHR201: Supported
- UTR-SUN02V-8CH: Supported
- UTR-SUN02-8CH: Supported
- ROM/version notes: Use the rightmost applicable ROM column in the support table.
- How to identify device:
  - Read ROM version first
  - Parse series name
  - Map USM01/USM02/USM05/USM06/USM08 to product type
- Unsupported cases: Treat as unsupported only when the PDF support table or ROM/version notes say so.

## 6. Required parameters

- Parameters: Target device series, ROM version, connection address, timeout policy, target tag, memory bank, word address, word count, Access password if required
- Parameter constraints: Follow the field definitions in PDF section 7.5.3.
- Parameters that should be asked from user: Field conditions and values not obtainable from ROM.
- Parameters that can be read from device: ROM version number, series name, and applicable readable settings.
- Parameters that can be inferred from ROM/series: Product type, 4CH/8CH class, and ROM-dependent support.

## 7. Command format summary

- Command format overview: Use the common frame from chapter 5 and the command/detail/subcommand identifiers above.
- Do not include completed Hex: This card intentionally avoids a ready-to-send full frame.
- Do not include SUM-calculated command: This card intentionally avoids a SUM-calculated command.

## 8. ACK response

- ACK exists: Yes, unless the PDF section defines asynchronous, multiple-response, completion-response, or no-response behavior.
- ACK command: Use the command-specific ACK structure described in PDF section 7.5.3.
- Data length: See PDF section 7.5.3.
- Data fields: Parse the fields documented in the command section.
- Multiple responses: RF tag and automatic-reading related commands may require a receive loop.
- Completion response: Required when the command section defines an end/completion response.
- No response: Treat only as specified by the command section or timeout policy.
- Notes: Always distinguish ACK, NACK, multiple response, completion response, and timeout.

## 9. NACK response

- NACK uses common 7.6 format: Yes.
- Error code 1 relevance: Check CRC, time-over, receive, RF tag no response, internal command error, UHF IC error, LBT, hardware, antenna, SUM, and format errors.
- Error code 2 relevance: Used mainly when Error code 1 is CMD_UHF_IC_ERROR.
- Error code 3 relevance: Important for UHF_Encode and UHF_BlockWrite2 partial-failure diagnostics.
- Error code 4 relevance: Important for UHF_BlockWrite2 when the code indicates RF tag access error.
- Command-specific NACK notes: Check PDF section 7.5.3 and section 7.6 together.
- Partial success risk: Relevant for write, erase, lock, kill, encode, and multi-word tag operations.
- Notes: Reserved bytes in NACK should be ignored unless the PDF assigns meaning.

## 10. Important errors and diagnostics

- CMD_LBT_ERROR
- CMD_ANT_ERROR
- CMD_RXBUSY_ERROR
- FORMAT_ERROR
- SUM_ERROR
- CMD_UHF_IC_ERROR
- Access password error
- Memory lock
- Tag not detected

## 11. Implementation notes for AI

- まずROMバージョン読み取りで機種とROMを自動判定する。
- AIが勝手に使用不可と決めない。
- 実行に必要なパラメータを整理する。
- 実機確認が必要な点と机上確認で可能な点を分ける。
- ログには送信目的、パラメータ、ACK/NACK、エラーコード、タイムアウト、復旧判断を残す。
- タイムアウト、受信ループ、複数レスポンス、完了レスポンス、無応答を区別する。

## 12. Current RAG decision

- Decision: SUPPORTED_WITH_PARAMETERS
- Reason: Listed in PDF Ver.1.17 command master and classified by impact and required confirmation.
- Required parameter confirmation: Target device series, ROM version, connection address, timeout policy, target tag, memory bank, word address, word count, Access password if required
- Required device/ROM check: Read ROM version first and consult the support table.
- Required recovery note: As needed
- Next action: Use this card with the command master, response/NACK master, ROM support document, and parameter confirmation guide before implementation.

## Traceability

- Command list source:
  - PDF 6.1.3
- Command format source:
  - PDF 7.5.3
- ACK response source:
  - PDF 7.5.3 ACK response
- NACK response source:
  - PDF 7.6 common NACK; PDF 7.5.3 NACK response
- Device/ROM support source:
  - PDF 6.2.3
- RAM/FLASH impact source:
  - NEEDS_RAM_FLASH_TRACE
- RF / carrier / antenna safety source:
  - PDF 3.1; PDF 7.5.3; docs/current/13_RF_SAFETY_AND_CARRIER_RULES.md
- Traceability status:
  - TRACE_COMPLETE_WITH_NOTES
- Notes:
  - No completed Hex
  - No SUM-calculated command
  - No device-sendable code


## Real-device verification

- Verification stage:
  - Stage 2: RF read operations
- Initial status:
  - BLOCKED_BY_SITE_CONDITION
- Required prior checks:
  - Stage 0完了、アンテナ構成、使用タグ、電波利用環境、timeout、受信ループ方針
- Required parameters:
  - ROM version, device/ROM support, connection condition, timeout policy, command-specific parameters, and field conditions not readable from ROM
- Required log fields:
  - antenna_count, active_antenna, target_tag_count, target_memory_bank, rf_impact, expected_response_type, actual_response_type, raw_log_file
- Expected response type:
  - ACK/NACK plus possible multiple RF tag responses and completion/no-response handling
- Recovery note:
  - RF送信とタグ応答を扱う。停止条件、timeout、複数レスポンス、完了レスポンスを記録する。
- Result status values:
  - NOT_TESTED
  - DESK_REVIEWED
  - AI_TRACE_REVIEWED
  - READY_FOR_REAL_DEVICE_TEST
  - REAL_DEVICE_PASS
  - REAL_DEVICE_PASS_WITH_NOTES
  - REAL_DEVICE_FAIL
  - NEEDS_RETEST
  - BLOCKED_BY_DEVICE_OR_ROM
  - BLOCKED_BY_PARAMETER
  - BLOCKED_BY_SITE_CONDITION
  - BLOCKED_BY_RECOVERY_PLAN
  - NOT_APPLICABLE_TO_TARGET
- Related documents:
  - docs/current/17_REAL_DEVICE_VERIFICATION_FRAMEWORK.md
  - docs/current/18_REAL_DEVICE_LOG_SCHEMA.md
  - docs/current/19_VERIFICATION_STAGE_PLAN.md
  - docs/current/20_VERIFICATION_RESULT_STATUS.md

## Stage 2 RF read preflight

- Preflight document:
  docs/current/28_STAGE2_RF_READ_PREFLIGHT.md
- Command plan:
  docs/current/29_STAGE2_RF_READ_COMMAND_PLAN.md
- Log template:
  docs/current/30_STAGE2_RF_READ_LOG_TEMPLATE.md
- Stop conditions:
  docs/current/31_STAGE2_STOP_CONDITIONS.md
- v016 status:
  READY_FOR_PREFLIGHT_REVIEW
- Real-device execution:
  NOT_EXECUTED_IN_V016

## v018 Stage 2 RF read operations result

- Result document:
  docs/current/33_STAGE2_RF_READ_OPERATIONS_RESULT.md
- v018 status:
  BLOCKED_BY_PARAMETER
- Actual response type:
  not-sent
- Reason:
  Read memory bank, read start word address, and read word count were not specified.
- Safety note:
  The command was not sent. The tool does not guess read parameters.
