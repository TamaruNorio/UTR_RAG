# 使用アンテナ番号の読み取り

## 1. Command identity

- PDF section: 7.3.6
- Command name: 使用アンテナ番号の読み取り
- Category: リーダライタ制御
- Command byte: 55h
- Detail command byte: 48h
- Subcommand byte: -
- Command family: リーダライタ制御
- Read / Write / Control / RF tag / Mode: Read
- Source PDF: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17 (TDR-MNL-PRC-UTR-S201-117.pdf, 2025-06-16)
- Verification status: PDF Ver.1.17 desk review

## 2. Purpose

使用アンテナ番号を読み取る。

## 3. Usage status

- Status: NEEDS_DEVICE_OR_ROM_CHECK
- Reason: PDF Ver.1.17 lists this command in section 7.3.6. AI/RAG organizes device, ROM, parameter, impact, response, and recovery conditions instead of deciding arbitrary non-use.

## 4. Safety / impact classification

- RF emission: Yes
- Setting change: No
- RAM change: No
- FLASH change: Depends on write target
- Tag memory change: No
- External I/O change: No
- Persistent effect: Check whether the target field is RAM-only, FLASH-backed, or tag-memory persistent.
- Recovery note required: As needed
- Parameter confirmation required: Target device series, ROM version, connection address, timeout policy, connected antenna count, target antenna number, auto-switch range

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

- Parameters: Target device series, ROM version, connection address, timeout policy, connected antenna count, target antenna number, auto-switch range
- Parameter constraints: Follow the field definitions in PDF section 7.3.6.
- Parameters that should be asked from user: Field conditions and values not obtainable from ROM.
- Parameters that can be read from device: ROM version number, series name, and applicable readable settings.
- Parameters that can be inferred from ROM/series: Product type, 4CH/8CH class, and ROM-dependent support.

## 7. Command format summary

- Command format overview: Use the common frame from chapter 5 and the command/detail/subcommand identifiers above.
- Do not include completed Hex: This card intentionally avoids a ready-to-send full frame.
- Do not include SUM-calculated command: This card intentionally avoids a SUM-calculated command.

## 8. ACK response

- ACK exists: Yes, unless the PDF section defines asynchronous, multiple-response, completion-response, or no-response behavior.
- ACK command: Use the command-specific ACK structure described in PDF section 7.3.6.
- Data length: See PDF section 7.3.6.
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
- Command-specific NACK notes: Check PDF section 7.3.6 and section 7.6 together.
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
- Required parameter confirmation: Target device series, ROM version, connection address, timeout policy, connected antenna count, target antenna number, auto-switch range
- Required device/ROM check: Read ROM version first and consult the support table.
- Required recovery note: As needed
- Next action: Use this card with the command master, response/NACK master, ROM support document, and parameter confirmation guide before implementation.
