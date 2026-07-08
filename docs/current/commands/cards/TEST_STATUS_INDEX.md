# R9-3 Test Status Index

## TESTED_READ_ONLY

- [ROMバージョンの読み取り](rom_version_read.md)
- [UHF_GetInventoryParam](55_41_uhf_get_inventory_param.md)
- [送信出力設定の読み取り](55_43_01_read_output_power.md)
- [周波数設定の読み取り](55_43_02_read_frequency.md)

## TESTED_INVENTORY

- [UHF_Inventory](55_10_uhf_inventory.md)

## PASS_WITH_NOTES

- [ROMバージョンの読み取り](rom_version_read.md)
- [UHF_Inventory](55_10_uhf_inventory.md)

## TESTED_NO_SEND

- なし。R9-3では追加実機送信を行っていない。

## CONNECTION_ONLY

- R8-3/R8-3Cの接続確認結果を参照。

## NOT_TESTED

- [UHF_GetSelectParam](55_40_uhf_get_select_param.md)
- [UHF_GetExpandSelectParam](55_42_uhf_get_expand_select_param.md)
- [UHF_CheckAntenna](55_44_uhf_check_antenna.md)
- [使用アンテナ番号の読み取り](55_48_read_active_antenna.md)
- [各種設定読み取りカード](README.md)

## HOLD

- [UHF_InventoryRead](55_14_uhf_inventory_read.md)
- [UHF_Read](55_15_uhf_read.md)
- [リスタート](4e_9d_restart_reader.md)

## PROHIBITED

- 書き込み、FLASH、破壊的操作、任意コマンド系のカードを参照。
