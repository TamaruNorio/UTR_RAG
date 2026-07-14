---
title: "Stage 2 RF Read Log Template"
doc_type: "schema"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:[]
tags:
  - "utr-s201"
  - "schema"
  - "stage2"
  - "rf-read"
---

# Stage 2 RF Read Log Template

## 1. Positioning

This template defines the masked summary fields for future Stage 2 RF read verification.
v016 does not execute Stage 2 RF read commands and does not commit runtime logs.

## 2. Log fields

| Field | Description | Masking / recording policy |
|---|---|---|
| log_id | Unique log identifier | Use a non-sensitive run identifier. |
| date_time | Execution date and time | Use local time with timezone if available. |
| operator | Operator name or role | Avoid personal data when not required. |
| package_version | Package version | v016 or later execution package. |
| repository_commit | Git commit used for execution | Commit hash is allowed. |
| device_series | Device series | Example: USM02. |
| product_type | Product type | Example: UTR-SUN02-4CH. |
| rom_version | ROM version | Example: 2.052. |
| connection_type | Connection type | Example: USB serial. |
| port_masked | Port name | Use COMx format. |
| baudrate | Baudrate | Example: 115200bps. |
| antenna_count | Number of antennas | Use confirmed count. |
| active_antenna | Active antenna | Use logical antenna number. |
| antenna_connection_status | Antenna connection state | Connected, not connected, unknown, or error. |
| tag_present | Whether a tag is intentionally present | true, false, or unknown. |
| tag_type | Tag type | Use generic tag class if sensitive. |
| tag_id_masked | Masked tag identifier | Use EPC_xxxxxxxxxxxx format. |
| command_name | Command name | UHF_CheckAntenna, UHF_GetHandle, UHF_Inventory, UHF_InventoryRead, or UHF_Read. |
| command_card | Command card path | docs/current/commands/cards/... |
| pdf_section | PDF section | 7.3.5, 7.3.12, 7.5.1, 7.5.2, or 7.5.3. |
| parameter_summary | Parameter summary | Summarize without completed Hex or SUM-calculated command. |
| rf_emission | RF emission involved | yes/no. |
| expected_response_type | Expected response type | ACK, NACK, timeout, multiple response, completion response, or zero-tag result. |
| actual_response_type | Actual response type | Record observed response category. |
| ack_summary | ACK summary | Mask sensitive values. |
| parsed_tag_count | Parsed tag count | Numeric count only. |
| parsed_epc_masked | Parsed EPC/UII | Mask as EPC_xxxxxxxxxxxx. |
| memory_bank | Memory bank | EPC/UII, TID, user, reserved, or other documented value. |
| read_address | Read address | Record planned/read word address, not a completed command frame. |
| read_word_count | Read word count | Numeric word count. |
| nack_error_code_1 | NACK error code 1 | Record symbolic name when possible. |
| nack_error_code_2 | NACK error code 2 | Record symbolic name when possible. |
| nack_error_code_3 | NACK error code 3 | Record symbolic name when possible. |
| nack_error_code_4 | NACK error code 4 | Record symbolic name when possible. |
| timeout_ms | Timeout setting | Numeric milliseconds. |
| elapsed_ms | Elapsed time | Numeric milliseconds. |
| stop_condition_triggered | Stop condition | Link to docs/current/31_STAGE2_STOP_CONDITIONS.md. |
| result_status | Result status | PASS, PASS_WITH_NOTES, HOLD, FAIL, BLOCKED, or NOT_APPLICABLE. |
| notes | Notes | Include masked operational notes only. |

## 3. Masking policy

- EPC/UII is masked by default.
- TID/read data is masked or omitted from Git-managed summaries by default.
- Customer names are not recorded.
- Real IP addresses are not recorded.
- COM ports are recorded as COMx.
- Tag IDs are recorded as EPC_xxxxxxxxxxxx.
- Do not record completed Hex.
- Do not record SUM-calculated command examples.
- Do not commit runtime logs or actual CSV logs.

## 4. v019 read profile fields

When using the v019 `safe-tid` profile, record the following fields in masked summaries.

- read_profile: `safe-tid`
- memory_bank: `TID(2)`
- word_address: `0`
- word_count: `2`
- access_password_policy: `default-zero`
- max_tags: `1`

Do not record raw EPC/UII/TID/read-data values in Git-managed documents.
