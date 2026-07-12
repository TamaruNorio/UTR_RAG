# Real Device Log Schema

## 1. Positioning

v010では、実機確認時にACK/NACK/timeout/複数レスポンス/無応答を一貫して記録するための標準ログ項目を定義する。

## 2. Standard schema

| Field | Meaning | Required use | Masking / notes |
| --- | --- | --- | --- |
| log_id | log id | 実機確認ログで記録する標準項目 | |
| date_time | date time | 実機確認ログで記録する標準項目 | |
| operator | operator | 実機確認ログで記録する標準項目 | |
| repository_version | repository version | 実機確認ログで記録する標準項目 | |
| package_version | package version | 実機確認ログで記録する標準項目 | |
| command_card | command card | 実機確認ログで記録する標準項目 | |
| pdf_section | pdf section | 実機確認ログで記録する標準項目 | |
| command_name | command name | 実機確認ログで記録する標準項目 | |
| command_byte | command byte | 実機確認ログで記録する標準項目 | |
| detail_command | detail command | 実機確認ログで記録する標準項目 | |
| subcommand | subcommand | 実機確認ログで記録する標準項目 | |
| device_series | device series | 実機確認ログで記録する標準項目 | |
| product_type | product type | 実機確認ログで記録する標準項目 | |
| rom_version | rom version | 実機確認ログで記録する標準項目 | |
| connection_type | connection type | 実機確認ログで記録する標準項目 | |
| port_or_ip | port or ip | 実機確認ログで記録する標準項目 | |
| baudrate_or_socket | baudrate or socket | 実機確認ログで記録する標準項目 | |
| antenna_count | antenna count | 実機確認ログで記録する標準項目 | |
| active_antenna | active antenna | 実機確認ログで記録する標準項目 | |
| antenna_switching_mode | antenna switching mode | 実機確認ログで記録する標準項目 | |
| target_tag_count | target tag count | 実機確認ログで記録する標準項目 | |
| target_memory_bank | target memory bank | 実機確認ログで記録する標準項目 | |
| parameter_summary | parameter summary | 実機確認ログで記録する標準項目 | |
| ram_flash_impact | ram flash impact | 実機確認ログで記録する標準項目 | |
| rf_impact | rf impact | 実機確認ログで記録する標準項目 | |
| tag_memory_impact | tag memory impact | 実機確認ログで記録する標準項目 | |
| recovery_required | recovery required | 実機確認ログで記録する標準項目 | |
| pre_read_required | pre read required | 実機確認ログで記録する標準項目 | |
| expected_response_type | expected response type | 実機確認ログで記録する標準項目 | |
| actual_response_type | actual response type | 実機確認ログで記録する標準項目 | |
| ack_summary | ack summary | 実機確認ログで記録する標準項目 | |
| nack_error_code_1 | nack error code 1 | 実機確認ログで記録する標準項目 | |
| nack_error_code_2 | nack error code 2 | 実機確認ログで記録する標準項目 | |
| nack_error_code_3 | nack error code 3 | 実機確認ログで記録する標準項目 | |
| nack_error_code_4 | nack error code 4 | 実機確認ログで記録する標準項目 | |
| timeout_ms | timeout ms | 実機確認ログで記録する標準項目 | |
| elapsed_ms | elapsed ms | 実機確認ログで記録する標準項目 | |
| raw_log_file | raw log file | 実機確認ログで記録する標準項目 | |
| result_status | result status | 実機確認ログで記録する標準項目 | |
| notes | notes | 実機確認ログで記録する標準項目 | |

## 3. Response recording rules

- ACK, NACK, timeout, no-response, multiple response, and completion response must be recorded separately.
- Timeout is not NACK.
- No-response is not NACK.
- RF tag commands may require a receive loop and completion-response handling.
- NACK error code 1-4 should be recorded in separate fields.

## 4. Masking policy

実IPアドレス、タグ固有ID、顧客名、認証情報はそのまま記録しない。

Mask examples:

- IP: 192.168.xxx.xxx
- COM: COMx
- tag ID: EPC_xxxxxxxxxxxx
- customer: 株式会社XXXX

## 5. Storage policy

- Raw logs containing sensitive values should not be committed to GitHub.
- Store only masked summaries in RAG documents.
- Keep raw logs in controlled local or internal storage when required.
