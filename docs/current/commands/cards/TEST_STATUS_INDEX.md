---
title: "Test Status Index"
doc_type: "index"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../AI_IMPLEMENTATION_GUARDRAILS.md"
tags:
  - "utr-s201"
  - "guide"
  - "result-summary"
---

# 実機確認ステータス索引

この索引は、`scripts/check_docs.py` と同じロジック（`scripts/update_test_status_index.py`）で、各コマンドカードのfrontmatterから自動生成したものです。
全54コマンドを個別に実機送信済みであることを示すものではありません。各カードの詳細な確認内容は、カード本体の「9. 実機確認」を参照してください。

最終更新時点のカード枚数: 54件

## REAL_DEVICE_VERIFIED_WITH_NOTES（54件）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `42h` | [ブザーの制御](42_buzzer_control.md) | `-` | `-` |
| `4Eh` | [リーダライタ動作モードの書き込み](4e_00_10_write_reader_mode.md) | `00h` | `10h` |
| `4Eh` | [LED&ブザーの制御](4e_57_led_buzzer_control.md) | `57h` | `-` |
| `4Eh` | [FLASH設定の初期化](4e_6f_flash_initialize.md) | `6Fh` | `-` |
| `4Eh` | [リスタート](4e_9d_restart_reader.md) | `9Dh` | `-` |
| `4Eh` | [RF送信信号の制御](4e_9e_rf_carrier_control.md) | `9Eh` | `-` |
| `4Eh` | [汎用ポート値の書き込み](4e_9f_write_general_port.md) | `9Fh` | `-` |
| `4Eh` | [拡張ポート値の書き込み](4e_a0_write_extended_port.md) | `A0h` | `-` |
| `4Eh` | [FLASH設定値の書き込み(1バイトアクセス)](4e_b4_flash_write.md) | `B4h` | `-` |
| `4Fh` | [リーダライタ動作モードの読み取り](4f_00_read_reader_mode.md) | `00h` | `-` |
| `4Fh` | [エラー情報の読み取り](4f_80_read_error_info.md) | `80h` | `-` |
| `4Fh` | [汎用ポート値の読み取り](4f_9f_read_general_port.md) | `9Fh` | `-` |
| `4Fh` | [拡張ポート値の読み取り](4f_a0_read_extended_port.md) | `A0h` | `-` |
| `4Fh` | [FLASH設定値の読み取り(1バイトアクセス)](4f_b4_read_flash_settings.md) | `B4h` | `-` |
| `55h` | [UHF_Inventory](55_10_uhf_inventory.md) | `10h` | `-` |
| `55h` | [UHF_InventoryRead](55_14_uhf_inventory_read.md) | `14h` | `-` |
| `55h` | [UHF_Read](55_15_uhf_read.md) | `15h` | `-` |
| `55h` | [UHF_Write](55_16_uhf_write.md) | `16h` | `-` |
| `55h` | [UHF_Kill](55_17_uhf_kill.md) | `17h` | `-` |
| `55h` | [UHF_Lock](55_18_uhf_lock.md) | `18h` | `-` |
| `55h` | [UHF_BlockWrite](55_1a_uhf_block_write.md) | `1Ah` | `-` |
| `55h` | [UHF_BlockErase](55_1b_uhf_block_erase.md) | `1Bh` | `-` |
| `55h` | [UHF_BlockWrite2](55_1d_uhf_block_write2.md) | `1Dh` | `-` |
| `55h` | [UHF_Encode](55_1e_uhf_encode.md) | `1Eh` | `-` |
| `55h` | [UHF_SetSelectParam](55_30_uhf_set_select_param.md) | `30h` | `-` |
| `55h` | [UHF_SetInventoryParam](55_31_uhf_set_inventory_param.md) | `31h` | `-` |
| `55h` | [UHF_SetExpandSelectParam](55_32_uhf_set_expand_select_param.md) | `32h` | `-` |
| `55h` | [アンテナ切替設定の書き込み](55_33_00_write_antenna_switching.md) | `33h` | `00h` |
| `55h` | [出力設定の書き込み](55_33_01_write_output_power.md) | `33h` | `01h` |
| `55h` | [周波数設定の書き込み](55_33_02_write_frequency.md) | `33h` | `02h` |
| `55h` | [Accessパスワードの書き込み](55_33_03_write_access_password.md) | `33h` | `03h` |
| `55h` | [RFタグ通信関連パラメータの書き込み](55_33_04_write_rf_tag_comm_params.md) | `33h` | `04h` |
| `55h` | [EPC(UII)関連パラメータの書き込み](55_33_05_write_epc_uii_params.md) | `33h` | `05h` |
| `55h` | [外部アンテナ自動切替設定の書き込み](55_37_write_external_antenna_auto_switch.md) | `37h` | `-` |
| `55h` | [使用アンテナ番号の書き込み](55_38_write_active_antenna.md) | `38h` | `-` |
| `55h` | [RSSIフィルタ設定の書き込み](55_39_write_rssi_filter.md) | `39h` | `-` |
| `55h` | [アンテナ個別送信出力設定の書き込み](55_3a_write_antenna_output_power.md) | `3Ah` | `-` |
| `55h` | [UHF_GetSelectParam](55_40_uhf_get_select_param.md) | `40h` | `-` |
| `55h` | [UHF_GetInventoryParam](55_41_uhf_get_inventory_param.md) | `41h` | `-` |
| `55h` | [UHF_GetExpandSelectParam](55_42_uhf_get_expand_select_param.md) | `42h` | `-` |
| `55h` | [アンテナ切替設定の読み取り](55_43_00_read_antenna_switching.md) | `43h` | `00h` |
| `55h` | [出力設定の読み取り](55_43_01_read_output_power.md) | `43h` | `01h` |
| `55h` | [周波数設定の読み取り](55_43_02_read_frequency.md) | `43h` | `02h` |
| `55h` | [RFタグ通信関連パラメータの読み取り](55_43_04_read_rf_tag_comm_params.md) | `43h` | `04h` |
| `55h` | [EPC(UII)関連パラメータの読み取り](55_43_05_read_epc_uii_params.md) | `43h` | `05h` |
| `55h` | [UHF_CheckAntenna](55_44_uhf_check_antenna.md) | `44h` | `-` |
| `55h` | [UHF_GetHandle](55_46_uhf_get_handle.md) | `46h` | `-` |
| `55h` | [外部アンテナ自動切替設定の読み取り](55_47_read_external_antenna_auto_switch.md) | `47h` | `-` |
| `55h` | [使用アンテナ番号の読み取り](55_48_read_active_antenna.md) | `48h` | `-` |
| `55h` | [RSSIフィルタ設定の読み取り](55_49_read_rssi_filter.md) | `49h` | `-` |
| `55h` | [アンテナ個別送信出力設定の読み取り](55_4a_read_antenna_output_power.md) | `4Ah` | `-` |
| `55h` | [チップバージョンの読み取り](55_90_chip_version_read.md) | `90h` | `-` |
| `55h` | [UHF_ThroughCmd](55_ff_uhf_through_cmd.md) | `FFh` | `-` |
| `4Fh` | [ROMバージョンの読み取り](rom_version_read.md) | `90h` | `-` |

## 更新方法

この表は手動で行を書き写さず、`python scripts/update_test_status_index.py` を実行して更新してください。カードのfrontmatterに`verification_status`を追加・変更した場合は、このスクリプトを再実行するだけで表が更新されます。

公式PDFが一次情報です。この索引は公式PDFの代替ではありません。
