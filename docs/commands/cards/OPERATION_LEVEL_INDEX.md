# R9-3 Operation Level Index

Level 4以上は明示確認が必要である。Level 5は明示承認と復旧手順がなければHOLDである。

## Level 0: 文書参照のみ

- 本INDEXと各カードの参照。

## Level 1: 接続・状態取得・現在設定読み取り

- ROM/status/read-only系カード。

## Level 2: 既存設定のまま読み取り

- [UHF_Inventory](55_10_uhf_inventory.md)
- [UHF_InventoryRead](55_14_uhf_inventory_read.md)
- [UHF_Read](55_15_uhf_read.md)

## Level 3: 一時的な読み取り条件変更

- タイムアウト、リトライ、CSV保存、一時アンテナ指定など。R9-1文書を参照。

## Level 4: RF条件または読み取り動作条件の変更

- UHF_SetInventoryParam、周波数変更、送信出力変更、タグメモリ書き込み、リスタート、任意コマンド系。AIが勝手に実装しない。

## Level 5: 永続設定変更

- FLASH書き込み、FLASH初期化。明示承認と復旧手順がなければHOLDまたはPROHIBITED。
