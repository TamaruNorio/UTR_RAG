# Command Master Ver.1.17

Target specification: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17 (TDR-MNL-PRC-UTR-S201-117.pdf, 2025-06-16)

This command master follows PDF chapter 6.1:

- Reader/writer control commands: 12
- Reader/writer setting commands: 31
- RF tag communication commands: 11
- Total: 54

7.1 UHF continuous inventory mode and 7.2 UHF continuous inventory read mode are treated as operation modes/asynchronous-response behavior, not as ordinary host-sent commands.

| No | PDF section | Command name | Category | Command byte | Detail command byte | Read/Write/Control/RF tag | Usage status | Parameter confirmation required | Card path | Verification status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7.3.1 | エラー情報の読み取り | リーダライタ制御 | 4Fh | 80h | Read | SUPPORTED | As needed | docs/current/commands/cards/4f_80_read_error_info.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 2 | 7.3.2 | ブザーの制御 | リーダライタ制御 | 42h | - | Control | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/42_buzzer_control.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 3 | 7.3.3 | LED&ブザーの制御 | リーダライタ制御 | 4Eh | 57h | Control | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/4e_57_led_buzzer_control.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 4 | 7.3.4 | RF送信信号の制御 | リーダライタ制御 | 4Eh | 9Eh | Control | SUPPORTED_WITH_IMPACT_NOTICE | Yes | docs/current/commands/cards/4e_9e_rf_carrier_control.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 5 | 7.3.5 | UHF_CheckAntenna | リーダライタ制御 | 55h | 44h | Control | SUPPORTED_WITH_IMPACT_NOTICE | Yes | docs/current/commands/cards/55_44_uhf_check_antenna.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 6 | 7.3.6 | 使用アンテナ番号の読み取り | リーダライタ制御 | 55h | 48h | Read | NEEDS_DEVICE_OR_ROM_CHECK | As needed | docs/current/commands/cards/55_48_read_active_antenna.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 7 | 7.3.7 | 使用アンテナ番号の書き込み | リーダライタ制御 | 55h | 38h | Write | NEEDS_DEVICE_OR_ROM_CHECK | Yes | docs/current/commands/cards/55_38_write_active_antenna.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 8 | 7.3.8 | ROMバージョンの読み取り | リーダライタ制御 | 4Fh | 90h | Read | SUPPORTED | As needed | docs/current/commands/cards/rom_version_read.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 9 | 7.3.9 | チップバージョンの読み取り | リーダライタ制御 | 55h | 90h | Read | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_90_chip_version_read.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 10 | 7.3.10 | リスタート | リーダライタ制御 | 4Eh | 9Dh | Control | SUPPORTED_WITH_IMPACT_NOTICE | Yes | docs/current/commands/cards/4e_9d_restart_reader.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 11 | 7.3.11 | FLASH設定の初期化 | リーダライタ制御 | 4Eh | 6Fh | Control | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/4e_6f_flash_initialize.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 12 | 7.3.12 | UHF_GetHandle | リーダライタ制御 | 55h | 46h | RF tag | NEEDS_DEVICE_OR_ROM_CHECK | Yes | docs/current/commands/cards/55_46_uhf_get_handle.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 13 | 7.4.1 | リーダライタ動作モードの読み取り | リーダライタ設定 | 4Fh | 00h | Read | SUPPORTED | As needed | docs/current/commands/cards/4f_00_read_reader_mode.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 14 | 7.4.2 | UHF_GetSelectParam | リーダライタ設定 | 55h | 40h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_40_uhf_get_select_param.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 15 | 7.4.3 | UHF_GetInventoryParam | リーダライタ設定 | 55h | 41h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_41_uhf_get_inventory_param.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 16 | 7.4.4 | UHF_GetExpandSelectParam | リーダライタ設定 | 55h | 42h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_42_uhf_get_expand_select_param.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 17 | 7.4.5 | アンテナ切替設定の読み取り | リーダライタ設定 | 55h | 43h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_43_00_read_antenna_switching.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 18 | 7.4.6 | 出力設定の読み取り | リーダライタ設定 | 55h | 43h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_43_01_read_output_power.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 19 | 7.4.7 | 周波数設定の読み取り | リーダライタ設定 | 55h | 43h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_43_02_read_frequency.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 20 | 7.4.8 | RFタグ通信関連パラメータの読み取り | リーダライタ設定 | 55h | 43h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_43_04_read_rf_tag_comm_params.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 21 | 7.4.9 | EPC(UII)関連パラメータの読み取り | リーダライタ設定 | 55h | 43h | Read | SUPPORTED | As needed | docs/current/commands/cards/55_43_05_read_epc_uii_params.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 22 | 7.4.10 | 外部アンテナ自動切替設定の読み取り | リーダライタ設定 | 55h | 47h | Read | NEEDS_DEVICE_OR_ROM_CHECK | As needed | docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 23 | 7.4.11 | 汎用ポート値の読み取り | リーダライタ設定 | 4Fh | 9Fh | Read | SUPPORTED | As needed | docs/current/commands/cards/4f_9f_read_general_port.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 24 | 7.4.12 | 拡張ポート値の読み取り | リーダライタ設定 | 4Fh | A0h | Read | NEEDS_DEVICE_OR_ROM_CHECK | As needed | docs/current/commands/cards/4f_a0_read_extended_port.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 25 | 7.4.13 | FLASH設定値の読み取り(1バイトアクセス) | リーダライタ設定 | 4Fh | B4h | Read | SUPPORTED | As needed | docs/current/commands/cards/4f_b4_read_flash_settings.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 26 | 7.4.14 | RSSIフィルタ設定の読み取り | リーダライタ設定 | 55h | 49h | Read | NEEDS_DEVICE_OR_ROM_CHECK | As needed | docs/current/commands/cards/55_49_read_rssi_filter.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 27 | 7.4.15 | アンテナ個別送信出力設定の読み取り | リーダライタ設定 | 55h | 4Ah | Read | NEEDS_DEVICE_OR_ROM_CHECK | As needed | docs/current/commands/cards/55_4a_read_antenna_output_power.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 28 | 7.4.16 | リーダライタ動作モードの書き込み | リーダライタ設定 | 4Eh | 00h / 10h | Write | SUPPORTED_WITH_IMPACT_NOTICE | Yes | docs/current/commands/cards/4e_00_10_write_reader_mode.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 29 | 7.4.17 | UHF_SetSelectParam | リーダライタ設定 | 55h | 30h | Write | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_30_uhf_set_select_param.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 30 | 7.4.18 | UHF_SetInventoryParam | リーダライタ設定 | 55h | 31h | Write | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_31_uhf_set_inventory_param.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 31 | 7.4.19 | UHF_SetExpandSelectParam | リーダライタ設定 | 55h | 32h | Write | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_32_uhf_set_expand_select_param.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 32 | 7.4.20 | アンテナ切替設定の書き込み | リーダライタ設定 | 55h | 33h | Write | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_33_00_write_antenna_switching.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 33 | 7.4.21 | 出力設定の書き込み | リーダライタ設定 | 55h | 33h | Write | SUPPORTED_WITH_IMPACT_NOTICE | Yes | docs/current/commands/cards/55_33_01_write_output_power.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 34 | 7.4.22 | 周波数設定の書き込み | リーダライタ設定 | 55h | 33h | Write | SUPPORTED_WITH_IMPACT_NOTICE | Yes | docs/current/commands/cards/55_33_02_write_frequency.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 35 | 7.4.23 | Accessパスワードの書き込み | リーダライタ設定 | 55h | 33h | Write | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_33_03_write_access_password.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 36 | 7.4.24 | RFタグ通信関連パラメータの書き込み | リーダライタ設定 | 55h | 33h | Write | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_33_04_write_rf_tag_comm_params.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 37 | 7.4.25 | EPC(UII)関連パラメータの書き込み | リーダライタ設定 | 55h | 33h | Write | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_33_05_write_epc_uii_params.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 38 | 7.4.26 | 外部アンテナ自動切替設定の書き込み | リーダライタ設定 | 55h | 37h | Write | NEEDS_DEVICE_OR_ROM_CHECK | Yes | docs/current/commands/cards/55_37_write_external_antenna_auto_switch.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 39 | 7.4.27 | 汎用ポート値の書き込み | リーダライタ設定 | 4Eh | 9Fh | Write | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/4e_9f_write_general_port.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 40 | 7.4.28 | 拡張ポート値の書き込み | リーダライタ設定 | 4Eh | A0h | Write | NEEDS_DEVICE_OR_ROM_CHECK | Yes | docs/current/commands/cards/4e_a0_write_extended_port.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 41 | 7.4.29 | FLASH設定値の書き込み(1バイトアクセス) | リーダライタ設定 | 4Eh | B4h | Write | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/4e_b4_flash_write.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 42 | 7.4.30 | RSSIフィルタ設定の書き込み | リーダライタ設定 | 55h | 39h | Write | NEEDS_DEVICE_OR_ROM_CHECK | Yes | docs/current/commands/cards/55_39_write_rssi_filter.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 43 | 7.4.31 | アンテナ個別送信出力設定の書き込み | リーダライタ設定 | 55h | 3Ah | Write | NEEDS_DEVICE_OR_ROM_CHECK | Yes | docs/current/commands/cards/55_3a_write_antenna_output_power.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 44 | 7.5.1 | UHF_Inventory | RFタグ通信 | 55h | 10h | RF tag | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_10_uhf_inventory.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 45 | 7.5.2 | UHF_InventoryRead | RFタグ通信 | 55h | 14h | RF tag | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_14_uhf_inventory_read.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 46 | 7.5.3 | UHF_Read | RFタグ通信 | 55h | 15h | RF tag | SUPPORTED_WITH_PARAMETERS | Yes | docs/current/commands/cards/55_15_uhf_read.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 47 | 7.5.4 | UHF_Write | RFタグ通信 | 55h | 16h | RF tag | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_16_uhf_write.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 48 | 7.5.5 | UHF_Kill | RFタグ通信 | 55h | 17h | RF tag | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_17_uhf_kill.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 49 | 7.5.6 | UHF_Lock | RFタグ通信 | 55h | 18h | RF tag | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_18_uhf_lock.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 50 | 7.5.7 | UHF_BlockWrite | RFタグ通信 | 55h | 1Ah | RF tag | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_1a_uhf_block_write.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 51 | 7.5.8 | UHF_BlockErase | RFタグ通信 | 55h | 1Bh | RF tag | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_1b_uhf_block_erase.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 52 | 7.5.9 | UHF_BlockWrite2 | RFタグ通信 | 55h | 1Dh | RF tag | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_1d_uhf_block_write2.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 53 | 7.5.10 | UHF_Encode | RFタグ通信 | 55h | 1Eh | RF tag | SUPPORTED_WITH_RECOVERY_NOTE | Yes | docs/current/commands/cards/55_1e_uhf_encode.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |
| 54 | 7.5.11 | UHF_ThroughCmd | RFタグ通信 | 55h | FFh | RF tag | NEEDS_DEVICE_OR_ROM_CHECK | Yes | docs/current/commands/cards/55_ff_uhf_through_cmd.md | PDF Ver.1.17 desk review | No completed Hex or SUM-calculated command |


Traceability index reference: `docs/current/16_TRACEABILITY_INDEX_V117.md`
