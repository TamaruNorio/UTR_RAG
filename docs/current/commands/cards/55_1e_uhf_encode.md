---
title: "UHF_Encode"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.10"
command_group: "rf_tag_communication"
command_name: "UHF_Encode"
command_byte: "55h"
detail_command: "1Eh"
subcommand: null
operation_stage: "Stage 3"
operation_level: "write/configuration"
rf_emission: true
write_operation: true
flash_operation: false
tag_memory_operation: true
requires_rom_check: true
requires_antenna: true
requires_tag: true
requires_access_password: false
requires_parameters: true
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
  - "rf-tag-communication"
  - "stage3"
  - "rf-emission"
  - "write-operation"
  - "tag-memory"
  - "requires-antenna"
  - "requires-tag"
  - "pass-with-notes"
---

# UHF_Encode

## 1. Command identity

- PDF section: 7.5.10
- Command name: UHF_Encode
- Category: RFタグ通信
- Command byte: 55h
- Detail command byte: 1Eh
- Subcommand byte: -
- Command family: RFタグ通信
- Read / Write / Control / RF tag / Mode: RF tag
- Source PDF: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17 (TDR-MNL-PRC-UTR-S201-117.pdf, 2025-06-16)
- Verification status: PDF Ver.1.17 desk review

## 2. Purpose

RFタグの複数領域書き込みやLockをまとめて行う。

## 3. Usage status

- Status: SUPPORTED_WITH_RECOVERY_NOTE
- Reason: PDF Ver.1.17 lists this command in section 7.5.10. AI/RAG organizes device, ROM, parameter, impact, response, and recovery conditions instead of deciding arbitrary non-use.

## 4. Safety / impact classification

- RF emission: Yes
- Setting change: No
- RAM change: No
- FLASH change: Depends on write target
- Tag memory change: Yes
- External I/O change: No
- Persistent effect: Check whether the target field is RAM-only, FLASH-backed, or tag-memory persistent.
- Recovery note required: Yes
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
- Parameter constraints: Follow the field definitions in PDF section 7.5.10.
- Parameters that should be asked from user: Field conditions and values not obtainable from ROM.
- Parameters that can be read from device: ROM version number, series name, and applicable readable settings.
- Parameters that can be inferred from ROM/series: Product type, 4CH/8CH class, and ROM-dependent support.

## 7. Command format summary

- Command format overview: Use the common frame from chapter 5 and the command/detail/subcommand identifiers above.
- Do not include completed Hex: This card intentionally avoids a ready-to-send full frame.
- Do not include SUM-calculated command: This card intentionally avoids a SUM-calculated command.

## 8. ACK response

- ACK exists: Yes, unless the PDF section defines asynchronous, multiple-response, completion-response, or no-response behavior.
- ACK command: Use the command-specific ACK structure described in PDF section 7.5.10.
- Data length: See PDF section 7.5.10.
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
- Command-specific NACK notes: Check PDF section 7.5.10 and section 7.6 together.
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

- Decision: SUPPORTED_WITH_RECOVERY_NOTE
- Reason: Listed in PDF Ver.1.17 command master and classified by impact and required confirmation.
- Required parameter confirmation: Target device series, ROM version, connection address, timeout policy, target tag, memory bank, word address, word count, Access password if required
- Required device/ROM check: Read ROM version first and consult the support table.
- Required recovery note: Yes
- Next action: Use this card with the command master, response/NACK master, ROM support document, and parameter confirmation guide before implementation.

## Traceability

- Command list source:
  - PDF 6.1.3
- Command format source:
  - PDF 7.5.10
- ACK response source:
  - PDF 7.5.10 ACK response
- NACK response source:
  - PDF 7.6 common NACK; PDF 7.5.10 NACK response
- Device/ROM support source:
  - PDF 6.2.3
- RAM/FLASH impact source:
  - NEEDS_RAM_FLASH_TRACE
- RF / carrier / antenna safety source:
  - PDF 3.1; PDF 7.5.10; docs/current/13_RF_SAFETY_AND_CARRIER_RULES.md
- Traceability status:
  - TRACE_COMPLETE_WITH_NOTES
- Notes:
  - No completed Hex
  - No SUM-calculated command
  - No device-sendable code


## Real-device verification

- Verification stage:
  - Stage 6: Tag memory operations
- Initial status:
  - BLOCKED_BY_PARAMETER
- Required prior checks:
  - Stage 0-2完了、対象タグ、メモリバンク、アドレス、長さ、書き込み値、復旧可否
- Required parameters:
  - ROM version, device/ROM support, connection condition, timeout policy, command-specific parameters, and field conditions not readable from ROM
- Required log fields:
  - target_tag_count, target_memory_bank, tag_memory_impact, parameter_summary, actual_response_type, raw_log_file
- Expected response type:
  - ACK/NACK with RF tag access error and timeout/no-response handling
- Recovery note:
  - タグメモリ変更を伴う。タグ固有IDはマスクし、変更前後の扱いと復旧可否を記録する。
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
