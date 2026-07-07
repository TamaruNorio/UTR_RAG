# R9-3 Structured Command Cards

R8-7で抽出した38件のコマンドを、AIが誤読しにくい1コマンド1カード形式へ整理した。

- 現時点でのカード件数: 38
- R8-7抽出ベース
- PDF原本との全件再照合は未完了
- 正式社外公開版ではない
- 日本国内仕様前提
- 海外利用は対象外
- 完成Hex、SUM計算済みコマンド、実機送信用コードを含まない

| No | Command name | Command identifier | Card file | Safety class | Operation level | Real device test status | Current decision | Notes |
|---:|---|---|---|---|---:|---|---|---|
| 1 | ROMバージョンの読み取り | 4F/90 | [rom_version_read.md](rom_version_read.md) | READ_ONLY | 1 | PASS_WITH_NOTES | READY_FOR_REFERENCE | R8-8AでROM/status read確認 |
| 2 | UHF_Inventory | 55/10 | [55_10_uhf_inventory.md](55_10_uhf_inventory.md) | INVENTORY_RF_EMISSION | 2 | TESTED_INVENTORY | READY_FOR_REFERENCE | R8-8AでInventory 1回確認 |
| 3 | UHF_InventoryRead | 55/14 | [55_14_uhf_inventory_read.md](55_14_uhf_inventory_read.md) | INVENTORY_RF_EMISSION | 2 | HOLD | PARTIAL_WITH_NOTES | 55h/14hの正対応 |
| 4 | UHF_GetInventoryParam | 55/41 | [55_41_uhf_get_inventory_param.md](55_41_uhf_get_inventory_param.md) | READ_ONLY | 1 | TESTED_READ_ONLY | READY_FOR_REFERENCE | R8-8Aで取得確認 |
| 5 | UHF_GetSelectParam | 55/40 | [55_40_uhf_get_select_param.md](55_40_uhf_get_select_param.md) | READ_ONLY | 1 | NOT_TESTED | PARTIAL_WITH_NOTES | 仕様確認候補 |
| 6 | UHF_GetExpandSelectParam | 55/42 | [55_42_uhf_get_expand_select_param.md](55_42_uhf_get_expand_select_param.md) | READ_ONLY | 1 | NOT_TESTED | PARTIAL_WITH_NOTES | 仕様確認候補 |
| 7 | UHF_SetInventoryParam | 55/31 | [55_31_uhf_set_inventory_param.md](55_31_uhf_set_inventory_param.md) | DEVICE_SETTING_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 自動送信禁止 |
| 8 | UHF_SetSelectParam | 55/30 | [55_30_uhf_set_select_param.md](55_30_uhf_set_select_param.md) | DEVICE_SETTING_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | Select条件変更 |
| 9 | UHF_SetExpandSelectParam | 55/32 | [55_32_uhf_set_expand_select_param.md](55_32_uhf_set_expand_select_param.md) | DEVICE_SETTING_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | Select条件変更 |
| 10 | UHF_CheckAntenna | 55/44 | [55_44_uhf_check_antenna.md](55_44_uhf_check_antenna.md) | NEEDS_SPEC_CONFIRMATION | 1 | NOT_TESTED | HOLD_NEEDS_SPEC_CONFIRMATION | trace item不足 |
| 11 | 使用アンテナ番号の読み取り | 55/48 | [55_48_read_active_antenna.md](55_48_read_active_antenna.md) | NEEDS_SPEC_CONFIRMATION | 1 | NOT_TESTED | HOLD_NEEDS_SPEC_CONFIRMATION | trace item不足 |
| 12 | 使用アンテナ番号の書き込み | 55/38 | [55_38_write_active_antenna.md](55_38_write_active_antenna.md) | DEVICE_SETTING_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | trace item不足 |
| 13 | 送信出力設定の読み取り | 55/43/01 | [55_43_01_read_output_power.md](55_43_01_read_output_power.md) | READ_ONLY | 1 | TESTED_READ_ONLY | READY_FOR_REFERENCE | R8-8Aで読取確認 |
| 14 | アンテナ切替設定の読み取り | 55/43/00 | [55_43_00_read_antenna_switching.md](55_43_00_read_antenna_switching.md) | READ_ONLY | 1 | NOT_TESTED | PARTIAL_WITH_NOTES | 設定確認 |
| 15 | 外部アンテナ自動切替設定の読み取り | 55/47 | [55_47_read_external_antenna_auto_switch.md](55_47_read_external_antenna_auto_switch.md) | READ_ONLY | 1 | NOT_TESTED | PARTIAL_WITH_NOTES | 8CH注意 |
| 16 | アンテナ個別送信出力設定の読み取り | 55/4A | [55_4a_read_antenna_output_power.md](55_4a_read_antenna_output_power.md) | READ_ONLY | 1 | NOT_TESTED | PARTIAL_WITH_NOTES | 出力値確認 |
| 17 | RSSIフィルタ設定の読み取り | 55/49 | [55_49_read_rssi_filter.md](55_49_read_rssi_filter.md) | READ_ONLY | 1 | NOT_TESTED | PARTIAL_WITH_NOTES | 設定確認 |
| 18 | FLASH設定値の読み取り | 4F/B4 | [4f_b4_read_flash_settings.md](4f_b4_read_flash_settings.md) | READ_ONLY | 1 | NOT_TESTED | PARTIAL_WITH_NOTES | 読み取りのみ |
| 19 | 送信出力設定の書き込み | 55/33/01 | [55_33_01_write_output_power.md](55_33_01_write_output_power.md) | RF_PARAM_CHANGE_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 送信出力変更 |
| 20 | 周波数設定の読み取り | 55/43/02 | [55_43_02_read_frequency.md](55_43_02_read_frequency.md) | READ_ONLY | 1 | TESTED_READ_ONLY | READY_FOR_REFERENCE | R8-8Aで読取確認 |
| 21 | 周波数設定の書き込み | 55/33/02 | [55_33_02_write_frequency.md](55_33_02_write_frequency.md) | RF_PARAM_CHANGE_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 周波数変更 |
| 22 | アンテナ切替設定の書き込み | 55/33/00 | [55_33_00_write_antenna_switching.md](55_33_00_write_antenna_switching.md) | DEVICE_SETTING_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 設定変更 |
| 23 | Accessパスワードの書き込み | 55/33/03 | [55_33_03_write_access_password.md](55_33_03_write_access_password.md) | TAG_MEMORY_WRITE_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 認証条件 |
| 24 | 外部アンテナ自動切替設定の書き込み | 55/37 | [55_37_write_external_antenna_auto_switch.md](55_37_write_external_antenna_auto_switch.md) | DEVICE_SETTING_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 8CH自動切替 |
| 25 | RSSIフィルタ設定の書き込み | 55/39 | [55_39_write_rssi_filter.md](55_39_write_rssi_filter.md) | DEVICE_SETTING_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 読取条件変更 |
| 26 | アンテナ個別送信出力設定の書き込み | 55/3A | [55_3a_write_antenna_output_power.md](55_3a_write_antenna_output_power.md) | RF_PARAM_CHANGE_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 送信出力変更 |
| 27 | UHF_Read | 55/15 | [55_15_uhf_read.md](55_15_uhf_read.md) | READ_WITH_RF | 2 | HOLD | PARTIAL_WITH_NOTES | 55h/15hの正対応、standalone HOLD |
| 28 | UHF_Write | 55/16 | [55_16_uhf_write.md](55_16_uhf_write.md) | TAG_MEMORY_WRITE_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | タグ書き込み |
| 29 | UHF_BlockWrite | 55/1A | [55_1a_uhf_block_write.md](55_1a_uhf_block_write.md) | TAG_MEMORY_WRITE_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | タグ書き込み |
| 30 | UHF_BlockWrite2 | 55/1D | [55_1d_uhf_block_write2.md](55_1d_uhf_block_write2.md) | TAG_MEMORY_WRITE_RESTRICTED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | タグ書き込み |
| 31 | UHF_BlockErase | 55/1B | [55_1b_uhf_block_erase.md](55_1b_uhf_block_erase.md) | PROHIBITED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 破壊的操作 |
| 32 | UHF_Encode | 55/1E | [55_1e_uhf_encode.md](55_1e_uhf_encode.md) | PROHIBITED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 破壊的操作 |
| 33 | UHF_Kill | 55/17 | [55_17_uhf_kill.md](55_17_uhf_kill.md) | PROHIBITED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 破壊的操作 |
| 34 | UHF_Lock | 55/18 | [55_18_uhf_lock.md](55_18_uhf_lock.md) | PROHIBITED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 破壊的操作 |
| 35 | UHF_ThroughCmd | 55/FF | [55_ff_uhf_through_cmd.md](55_ff_uhf_through_cmd.md) | PROHIBITED | 4 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 任意コマンド系 |
| 36 | FLASH書き込み | 4E/B4 | [4e_b4_flash_write.md](4e_b4_flash_write.md) | FLASH_WRITE_PROHIBITED | 5 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | 永続設定変更 |
| 37 | FLASH初期化 | 4E/6F | [4e_6f_flash_initialize.md](4e_6f_flash_initialize.md) | FLASH_WRITE_PROHIBITED | 5 | PROHIBITED | PROHIBITED_DOCUMENT_ONLY | RAG/trace不足 |
| 38 | リスタート | 4E/9D | [4e_9d_restart_reader.md](4e_9d_restart_reader.md) | DEVICE_SETTING_RESTRICTED | 4 | HOLD | HOLD_NEEDS_SPEC_CONFIRMATION | trace item不足 |
