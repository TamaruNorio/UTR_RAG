# R9-3 AI Retrieval Index

## タグを読む

- [UHF_Inventory](55_10_uhf_inventory.md)
- [UHF_InventoryRead](55_14_uhf_inventory_read.md)
- [UHF_Read](55_15_uhf_read.md)

## Inventoryする

- [UHF_Inventory](55_10_uhf_inventory.md)
- [UHF_GetInventoryParam](55_41_uhf_get_inventory_param.md)
- [UHF_SetInventoryParam](55_31_uhf_set_inventory_param.md) は自動送信禁止。

## EPCを読む

- [UHF_Inventory](55_10_uhf_inventory.md)
- [UHF_Read](55_15_uhf_read.md) はstandalone HOLD。

## TIDを読む

- [UHF_InventoryRead](55_14_uhf_inventory_read.md)
- [UHF_Read](55_15_uhf_read.md)

## USER領域を読む

- [UHF_Read](55_15_uhf_read.md)。要仕様確認。

## RSSIを扱う

- [RSSIフィルタ設定の読み取り](55_49_read_rssi_filter.md)
- [RSSIフィルタ設定の書き込み](55_39_write_rssi_filter.md) はLevel 4。

## アンテナを扱う

- [UHF_CheckAntenna](55_44_uhf_check_antenna.md)
- [使用アンテナ番号の読み取り](55_48_read_active_antenna.md)
- [アンテナ切替設定の読み取り](55_43_00_read_antenna_switching.md)
- 書き込み系はLevel 4。

## 現在設定を読む

- [送信出力設定の読み取り](55_43_01_read_output_power.md)
- [周波数設定の読み取り](55_43_02_read_frequency.md)
- [FLASH設定値の読み取り](4f_b4_read_flash_settings.md)

## 読み取り条件を変更する

- [UHF_SetInventoryParam](55_31_uhf_set_inventory_param.md)
- [UHF_SetSelectParam](55_30_uhf_set_select_param.md)
- [UHF_SetExpandSelectParam](55_32_uhf_set_expand_select_param.md)

## 周波数を扱う

- [周波数設定の読み取り](55_43_02_read_frequency.md)
- [周波数設定の書き込み](55_33_02_write_frequency.md) はLevel 4。

## 送信出力を扱う

- [送信出力設定の読み取り](55_43_01_read_output_power.md)
- [送信出力設定の書き込み](55_33_01_write_output_power.md) はLevel 4。

## FLASHまたは永続設定を扱う

- [FLASH設定値の読み取り](4f_b4_read_flash_settings.md)
- [FLASH書き込み](4e_b4_flash_write.md)
- [FLASH初期化](4e_6f_flash_initialize.md)

## 初期化・再起動を扱う

- [リスタート](4e_9d_restart_reader.md)
- [FLASH初期化](4e_6f_flash_initialize.md)

## 禁止またはHOLDすべき操作

- FLASH系、破壊的タグ操作、任意コマンド系、RF条件変更、UHF_SetInventoryParam自動送信、UHF_Read standalone。
