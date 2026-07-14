---
title: "拡張ポート値の読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.12"
command_group: "reader_setting"
command_name: "拡張ポート値の読み取り"
command_byte: "4Fh"
detail_command: "A0h"
subcommand: null
operation_stage: "Stage 1"
operation_level: "read-only"
rf_emission: false
write_operation: false
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
requires_tag: false
requires_access_password: false
requires_parameters: false
verification_status: "REAL_DEVICE_VERIFIED_WITH_NOTES"
result_status: "REAL_DEVICE_PASS_WITH_NOTES"
related_docs:
  - "../../09_COMMAND_MASTER_V117.md"
  - "../../16_TRACEABILITY_INDEX_V117.md"
  - "../../10_RESPONSE_AND_NACK_MASTER.md"
  - "../../11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "stage1"
  - "read-only"
  - "pass-with-notes"
---

# 拡張ポート値の読み取り

## 1. Command identity

- PDF section: 7.4.12
- Command name: 拡張ポート値の読み取り
- Category: リーダライタ設定
- Command byte: 4Fh
- Detail command byte: A0h
- Subcommand byte: -
- Command family: リーダライタ設定
- Read / Write / Control / RF tag / Mode: Read
- Source PDF: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17 (TDR-MNL-PRC-UTR-S201-117.pdf, 2025-06-16)
- Verification status: PDF Ver.1.17 desk review

## 2. Purpose

拡張ポート値を読み取る。

## 3. Usage status

- Status: NEEDS_DEVICE_OR_ROM_CHECK
- Reason: PDF Ver.1.17 lists this command in section 7.4.12. AI/RAG organizes device, ROM, parameter, impact, response, and recovery conditions instead of deciding arbitrary non-use.

## 4. Safety / impact classification

- RF emission: No or indirect
- Setting change: No
- RAM change: No
- FLASH change: Depends on write target
- Tag memory change: No
- External I/O change: Yes
- Persistent effect: Check whether the target field is RAM-only, FLASH-backed, or tag-memory persistent.
- Recovery note required: As needed
- Parameter confirmation required: Target device series, ROM version, connection address, timeout policy

## 5. Device / ROM support

- UTR-S201: Not supported for 8CH-only function
- UTR-SUN02-4CH: Not supported for 8CH-only function
- UTR-SHR201: Not supported for 8CH-only function
- UTR-SUN02V-8CH: Supported
- UTR-SUN02-8CH: Supported
- ROM/version notes: 8CH-class function. Read ROM version and series first.
- How to identify device:
  - Read ROM version first
  - Parse series name
  - Map USM01/USM02/USM05/USM06/USM08 to product type
- Unsupported cases: Treat as unsupported only when the PDF support table or ROM/version notes say so.

## 6. Required parameters

- Parameters: Target device series, ROM version, connection address, timeout policy
- Parameter constraints: Follow the field definitions in PDF section 7.4.12.
- Parameters that should be asked from user: Field conditions and values not obtainable from ROM.
- Parameters that can be read from device: ROM version number, series name, and applicable readable settings.
- Parameters that can be inferred from ROM/series: Product type, 4CH/8CH class, and ROM-dependent support.

## 7. Command format summary

- Command format overview: Use the common frame from chapter 5 and the command/detail/subcommand identifiers above.
- Do not include completed Hex: This card intentionally avoids a ready-to-send full frame.
- Do not include SUM-calculated command: This card intentionally avoids a SUM-calculated command.

## 8. ACK response

- ACK exists: Yes, unless the PDF section defines asynchronous, multiple-response, completion-response, or no-response behavior.
- ACK command: Use the command-specific ACK structure described in PDF section 7.4.12.
- Data length: See PDF section 7.4.12.
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
- Command-specific NACK notes: Check PDF section 7.4.12 and section 7.6 together.
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

- Decision: NEEDS_DEVICE_OR_ROM_CHECK
- Reason: Listed in PDF Ver.1.17 command master and classified by impact and required confirmation.
- Required parameter confirmation: Target device series, ROM version, connection address, timeout policy
- Required device/ROM check: Read ROM version first and consult the support table.
- Required recovery note: As needed
- Next action: Use this card with the command master, response/NACK master, ROM support document, and parameter confirmation guide before implementation.

## Traceability

- Command list source:
  - PDF 6.1.2
- Command format source:
  - PDF 7.4.12
- ACK response source:
  - PDF 7.4.12 ACK response
- NACK response source:
  - PDF 7.6 common NACK; PDF 7.4.12 NACK response
- Device/ROM support source:
  - PDF 6.2.2
- RAM/FLASH impact source:
  - PDF 7.4.12; docs/current/12_RAM_FLASH_IMPACT_MATRIX.md
- RF / carrier / antenna safety source:
  - NEEDS_RF_SAFETY_TRACE
- Traceability status:
  - TRACE_COMPLETE_WITH_NOTES
- Notes:
  - No completed Hex
  - No SUM-calculated command
  - No device-sendable code



## Real-device verification

- Verification stage:
  - Stage 1: Stage 0/1 read-only verification
- Initial status:
  - BLOCKED_BY_DEVICE_OR_ROM
- Required prior checks:
  - ROM version read first; confirm product/series/ROM and connection target before execution.
- Required parameters:
  - Explicit connection target, timeout policy, output directory, operator, and device/ROM applicability.
- Required log fields:
  - date_time, operator, command_card, pdf_section, command_name, device_series, product_type, rom_version, connection_type, port_or_ip, timeout_ms, elapsed_ms, actual_response_type, ack_summary, nack_error_code_1-4, result_status, notes
- Expected response type:
  - ACK/NACK/timeout/no-response
- Recovery note:
  - Read-only scope. No setting change is expected. Timeout/no-response requires connection and ROM/applicability review.
- Result status values:
  - READY_FOR_REAL_DEVICE_TEST
  - REAL_DEVICE_PASS
  - REAL_DEVICE_PASS_WITH_NOTES
  - REAL_DEVICE_FAIL
  - NEEDS_RETEST
  - BLOCKED_BY_DEVICE_OR_ROM
  - BLOCKED_BY_PARAMETER
  - NOT_APPLICABLE_TO_TARGET
- v011 notes:
  - 8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET
  - 外部I/O状態読み取り
- Related documents:
  - docs/current/17_REAL_DEVICE_VERIFICATION_FRAMEWORK.md
  - docs/current/18_REAL_DEVICE_LOG_SCHEMA.md
  - docs/current/19_VERIFICATION_STAGE_PLAN.md
  - docs/current/20_VERIFICATION_RESULT_STATUS.md
  - docs/current/21_STAGE01_READONLY_VERIFICATION_KIT.md
  - docs/current/22_STAGE01_READONLY_COMMAND_LIST.md
  - docs/current/23_STAGE01_READONLY_LOGGING_GUIDE.md

- v015 Stage 1 read-only configuration result:
  - docs/current/27_STAGE1_READONLY_CONFIGURATION_RESULT.md
- Latest result status:
  - NOT_APPLICABLE_TO_TARGET
- Latest result notes:
  - v015 did not send this command because it is 8CH-specific and the target is USM02 / UTR-SUN02-4CH.
