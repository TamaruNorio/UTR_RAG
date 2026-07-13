# Stage 1 Read-only Configuration Result

## 1. Positioning

v015では、v014でStage 0 read-onlyが成功した結果を前提に、Stage 1 read-only設定値読み取り系を確認する。

この文書はマスク済みサマリであり、`runtime_logs/` の生ログはGit管理しない。

## 2. Execution scope

対象:

- ROMバージョンの読み取り
- Stage 1 read-only設定値読み取り系15件

v015でROMバージョン読み取りを先に実行する理由:

- 機種/ROMを自動判定するため
- USM02 / ROM 2.052 / UTR-SUN02-4CHを前提条件として記録するため
- 8CH専用、ROM 2.100以降、追加パラメータが必要な項目を送信前に止めるため

v015対象外:

- 書き込み系
- FLASH write/init
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- RFタグ通信
- タグメモリ操作
- Lock / Kill / Encode / ThroughCmd

対象外は仕様上禁止ではなく、v015の実行対象外である。

## 3. Execution environment

- repository commit: 6e90593
- package base: v014 Stage 0 remaining read-only result
- tool: `tools/stage01_readonly_verify.py`
- connection_type: USB serial
- port: COMx
- baudrate: 115200
- timeout_ms: 1000
- execution date/time: 2026-07-13 13:20:55 JST
- operator: masked

## 4. Device identification

- ROM raw: 2052
- ROM version: 2.052
- series: USM02
- product type: UTR-SUN02-4CH
- result_status: REAL_DEVICE_PASS_WITH_NOTES

## 5. Command result summary

| Stage | PDF section | Command name | Card path | Actual response type | Result status | ACK summary | timeout_ms | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stage 0 | 7.3.8 | ROMバージョンの読み取り | docs/current/commands/cards/rom_version_read.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | ROM raw=2052; ROM=2.052; series=USM02; product=UTR-SUN02-4CH | 1000 | ROM read was executed first. |
| Stage 1 | 7.4.1 | リーダライタ動作モードの読み取り | docs/current/commands/cards/4f_00_read_reader_mode.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | reader mode=command mode; data_length=9 | 1000 | Raw response is retained only in runtime CSV. |
| Stage 1 | 7.4.2 | UHF_GetSelectParam | docs/current/commands/cards/55_40_uhf_get_select_param.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | parameter kind=00h; data_length=9 | 1000 | Command-mode parameter kind was used. |
| Stage 1 | 7.4.3 | UHF_GetInventoryParam | docs/current/commands/cards/55_41_uhf_get_inventory_param.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | parameter kind=00h; data_length=11 | 1000 | Command-mode parameter kind was used. |
| Stage 1 | 7.4.4 | UHF_GetExpandSelectParam | docs/current/commands/cards/55_42_uhf_get_expand_select_param.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | parameter kind=00h; data_length=25 | 1000 | Command-mode parameter kind and mask count 1 were used. |
| Stage 1 | 7.4.5 | アンテナ切替設定の読み取り | docs/current/commands/cards/55_43_00_read_antenna_switching.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | subcommand=00h; parameter kind=00h; data_length=8 | 1000 | Read-only. No antenna setting change. |
| Stage 1 | 7.4.6 | 出力設定の読み取り | docs/current/commands/cards/55_43_01_read_output_power.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | subcommand=01h; parameter kind=00h; data_length=11 | 1000 | Read-only. No output power change. |
| Stage 1 | 7.4.7 | 周波数設定の読み取り | docs/current/commands/cards/55_43_02_read_frequency.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | subcommand=02h; parameter kind=00h; data_length=12 | 1000 | Read-only. No frequency change. |
| Stage 1 | 7.4.8 | RFタグ通信関連パラメータの読み取り | docs/current/commands/cards/55_43_04_read_rf_tag_comm_params.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | subcommand=04h; parameter kind=00h; data_length=6 | 1000 | Read-only. No RF tag communication was executed. |
| Stage 1 | 7.4.9 | EPC(UII)関連パラメータの読み取り | docs/current/commands/cards/55_43_05_read_epc_uii_params.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | subcommand=05h; parameter kind=00h; data_length=4 | 1000 | Read-only. |
| Stage 1 | 7.4.10 | 外部アンテナ自動切替設定の読み取り | docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md | not-sent | NOT_APPLICABLE_TO_TARGET |  | 1000 | 8CH-specific command; target is USM02 / UTR-SUN02-4CH. |
| Stage 1 | 7.4.11 | 汎用ポート値の読み取り | docs/current/commands/cards/4f_9f_read_general_port.md | ACK | REAL_DEVICE_PASS_WITH_NOTES | general port values read; data_length=5 | 1000 | Raw response is retained only in runtime CSV. |
| Stage 1 | 7.4.12 | 拡張ポート値の読み取り | docs/current/commands/cards/4f_a0_read_extended_port.md | not-sent | NOT_APPLICABLE_TO_TARGET |  | 1000 | 8CH-specific command; target is USM02 / UTR-SUN02-4CH. |
| Stage 1 | 7.4.13 | FLASH設定値の読み取り(1バイトアクセス) | docs/current/commands/cards/4f_b4_read_flash_settings.md | not-sent | BLOCKED_BY_PARAMETER |  | 1000 | Read address is required and was not specified for v015. |
| Stage 1 | 7.4.14 | RSSIフィルタ設定の読み取り | docs/current/commands/cards/55_49_read_rssi_filter.md | not-sent | BLOCKED_BY_DEVICE_OR_ROM |  | 1000 | Command requires ROM 2.100 or later; target ROM is 2.052. |
| Stage 1 | 7.4.15 | アンテナ個別送信出力設定の読み取り | docs/current/commands/cards/55_4a_read_antenna_output_power.md | not-sent | BLOCKED_BY_DEVICE_OR_ROM |  | 1000 | Command requires ROM 2.100 or later; target ROM is 2.052. |

## 6. PASS results

- ROMバージョンの読み取り
- リーダライタ動作モードの読み取り
- UHF_GetSelectParam
- UHF_GetInventoryParam
- UHF_GetExpandSelectParam
- アンテナ切替設定の読み取り
- 出力設定の読み取り
- 周波数設定の読み取り
- RFタグ通信関連パラメータの読み取り
- EPC(UII)関連パラメータの読み取り
- 汎用ポート値の読み取り

## 7. NOT_APPLICABLE / BLOCKED results

- NOT_APPLICABLE_TO_TARGET:
  - 外部アンテナ自動切替設定の読み取り
  - 拡張ポート値の読み取り
- BLOCKED_BY_PARAMETER:
  - FLASH設定値の読み取り(1バイトアクセス)
- BLOCKED_BY_DEVICE_OR_ROM:
  - RSSIフィルタ設定の読み取り
  - アンテナ個別送信出力設定の読み取り

## 8. Runtime log files

Runtime files were saved under `runtime_logs/stage01_readonly/` and are not committed.

- `stage01_readonly_20260713_132054_COMx_log.csv`
- `stage01_readonly_20260713_132054_COMx_result.md`

## 9. Result decision

V015_STAGE1_READONLY_CONFIGURATION_PARTIAL

## 10. Next action

- Stage 1のうち、対象機種/ROM/パラメータ不足で未送信となった項目の扱いを整理する。
- FLASH設定値読み取りは、読み取りアドレスを指定して別工程で確認する。
- Stage 2以降へ進む前に、v015のPARTIAL結果を前提条件として扱う。
