---
title: "Verification Stage Plan"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:[]
tags:
  - "utr-s201"
  - "guide"
  - "real-device-test"
---

# Verification Stage Plan

v010では、全54コマンドを実機確認の影響範囲と前提条件で段階分けする。

## Stage 0: Connection and identification

- 目的: 接続と機種/ROM識別を確立する。
- 主な確認対象: ROM/チップ/エラー情報の読み取り
- 実行前に必要な情報: 接続方式、port/IP、timeout、ログ保存先
- ログ項目: ROM、series、product、ACK/NACK、timeout
- 復旧観点: 接続条件の見直し
- 先に完了しておくべきStage: なし

Commands:

- エラー情報の読み取り (docs/current/commands/cards/4f_80_read_error_info.md)
- ROMバージョンの読み取り (docs/current/commands/cards/rom_version_read.md)
- チップバージョンの読み取り (docs/current/commands/cards/55_90_chip_version_read.md)

## Stage 1: Read-only configuration

- 目的: 設定状態を読み取り、後続stageの前提を作る。
- 主な確認対象: 設定値読み取り、アンテナ/出力/周波数/RSSI/FLASH/ポート読み取り
- 実行前に必要な情報: Stage 0、対象機種/ROM
- ログ項目: 読み取り結果、ACK/NACK、timeout
- 復旧観点: 原則不要
- 先に完了しておくべきStage: Stage 0

Commands:

- 使用アンテナ番号の読み取り (docs/current/commands/cards/55_48_read_active_antenna.md)
- リーダライタ動作モードの読み取り (docs/current/commands/cards/4f_00_read_reader_mode.md)
- UHF_GetSelectParam (docs/current/commands/cards/55_40_uhf_get_select_param.md)
- UHF_GetInventoryParam (docs/current/commands/cards/55_41_uhf_get_inventory_param.md)
- UHF_GetExpandSelectParam (docs/current/commands/cards/55_42_uhf_get_expand_select_param.md)
- アンテナ切替設定の読み取り (docs/current/commands/cards/55_43_00_read_antenna_switching.md)
- 出力設定の読み取り (docs/current/commands/cards/55_43_01_read_output_power.md)
- 周波数設定の読み取り (docs/current/commands/cards/55_43_02_read_frequency.md)
- RFタグ通信関連パラメータの読み取り (docs/current/commands/cards/55_43_04_read_rf_tag_comm_params.md)
- EPC(UII)関連パラメータの読み取り (docs/current/commands/cards/55_43_05_read_epc_uii_params.md)
- 外部アンテナ自動切替設定の読み取り (docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md)
- 汎用ポート値の読み取り (docs/current/commands/cards/4f_9f_read_general_port.md)
- 拡張ポート値の読み取り (docs/current/commands/cards/4f_a0_read_extended_port.md)
- FLASH設定値の読み取り(1バイトアクセス) (docs/current/commands/cards/4f_b4_read_flash_settings.md)
- RSSIフィルタ設定の読み取り (docs/current/commands/cards/55_49_read_rssi_filter.md)
- アンテナ個別送信出力設定の読み取り (docs/current/commands/cards/55_4a_read_antenna_output_power.md)

## Stage 2: RF read operations

- 目的: RF読取系の応答と受信ループを確認する。
- 主な確認対象: Inventory、InventoryRead、Read、CheckAntenna、GetHandle
- 実行前に必要な情報: Stage 0、アンテナ、タグ、電波環境
- ログ項目: RF影響、タグ応答、複数レスポンス、完了レスポンス
- 復旧観点: 停止条件、timeout条件
- 先に完了しておくべきStage: Stage 0-1の必要項目

Commands:

- UHF_CheckAntenna (docs/current/commands/cards/55_44_uhf_check_antenna.md)
- UHF_GetHandle (docs/current/commands/cards/55_46_uhf_get_handle.md)
- UHF_Inventory (docs/current/commands/cards/55_10_uhf_inventory.md)
- UHF_InventoryRead (docs/current/commands/cards/55_14_uhf_inventory_read.md)
- UHF_Read (docs/current/commands/cards/55_15_uhf_read.md)

## Stage 3: Antenna and runtime parameter operations

- 目的: 実行時パラメータとアンテナ切替を確認する。
- 主な確認対象: Select/Inventory/ExpandSelect、アンテナ切替、RSSI、RFタグ通信パラメータ
- 実行前に必要な情報: 設定前値、設定値、戻し手順
- ログ項目: RAM/FLASH影響、RF影響、設定前後値
- 復旧観点: 設定戻し
- 先に完了しておくべきStage: Stage 0-2の該当項目

Commands:

- 使用アンテナ番号の書き込み (docs/current/commands/cards/55_38_write_active_antenna.md)
- UHF_SetSelectParam (docs/current/commands/cards/55_30_uhf_set_select_param.md)
- UHF_SetInventoryParam (docs/current/commands/cards/55_31_uhf_set_inventory_param.md)
- UHF_SetExpandSelectParam (docs/current/commands/cards/55_32_uhf_set_expand_select_param.md)
- アンテナ切替設定の書き込み (docs/current/commands/cards/55_33_00_write_antenna_switching.md)
- RFタグ通信関連パラメータの書き込み (docs/current/commands/cards/55_33_04_write_rf_tag_comm_params.md)
- EPC(UII)関連パラメータの書き込み (docs/current/commands/cards/55_33_05_write_epc_uii_params.md)
- 外部アンテナ自動切替設定の書き込み (docs/current/commands/cards/55_37_write_external_antenna_auto_switch.md)
- RSSIフィルタ設定の書き込み (docs/current/commands/cards/55_39_write_rssi_filter.md)

## Stage 4: RF condition and reader operation settings

- 目的: RF条件とリーダ動作設定を確認する。
- 主な確認対象: RFキャリア、出力、周波数、動作モード、リスタート、ブザー、LED、I/O
- 実行前に必要な情報: 現場RF条件、外部I/O条件、戻し手順
- ログ項目: RF影響、外部I/O影響、ACK/NACK
- 復旧観点: 設定戻し/再接続
- 先に完了しておくべきStage: Stage 0、必要に応じStage 1

Commands:

- ブザーの制御 (docs/current/commands/cards/42_buzzer_control.md)
- LED&ブザーの制御 (docs/current/commands/cards/4e_57_led_buzzer_control.md)
- RF送信信号の制御 (docs/current/commands/cards/4e_9e_rf_carrier_control.md)
- リスタート (docs/current/commands/cards/4e_9d_restart_reader.md)
- リーダライタ動作モードの書き込み (docs/current/commands/cards/4e_00_10_write_reader_mode.md)
- 出力設定の書き込み (docs/current/commands/cards/55_33_01_write_output_power.md)
- 周波数設定の書き込み (docs/current/commands/cards/55_33_02_write_frequency.md)
- 汎用ポート値の書き込み (docs/current/commands/cards/4e_9f_write_general_port.md)
- 拡張ポート値の書き込み (docs/current/commands/cards/4e_a0_write_extended_port.md)
- アンテナ個別送信出力設定の書き込み (docs/current/commands/cards/55_3a_write_antenna_output_power.md)

## Stage 5: FLASH and persistent settings

- 目的: 永続設定とFLASH操作を確認する。
- 主な確認対象: FLASH書き込み/初期化、Accessパスワード、アンテナ個別出力
- 実行前に必要な情報: 事前読み取り、復旧手順、承認
- ログ項目: FLASH影響、復旧要否、設定前後値
- 復旧観点: 復旧手順必須
- 先に完了しておくべきStage: Stage 0-1

Commands:

- FLASH設定の初期化 (docs/current/commands/cards/4e_6f_flash_initialize.md)
- Accessパスワードの書き込み (docs/current/commands/cards/55_33_03_write_access_password.md)
- FLASH設定値の書き込み(1バイトアクセス) (docs/current/commands/cards/4e_b4_flash_write.md)

## Stage 6: Tag memory operations

- 目的: タグメモリ操作を確認する。
- 主な確認対象: Write、BlockWrite、BlockErase、BlockWrite2、Encode
- 実行前に必要な情報: 対象タグ、メモリ、アドレス、長さ、復旧可否
- ログ項目: タグメモリ影響、RF応答、NACK詳細
- 復旧観点: タグ状態の復旧可否確認
- 先に完了しておくべきStage: Stage 0-2

Commands:

- UHF_Write (docs/current/commands/cards/55_16_uhf_write.md)
- UHF_BlockWrite (docs/current/commands/cards/55_1a_uhf_block_write.md)
- UHF_BlockErase (docs/current/commands/cards/55_1b_uhf_block_erase.md)
- UHF_BlockWrite2 (docs/current/commands/cards/55_1d_uhf_block_write2.md)
- UHF_Encode (docs/current/commands/cards/55_1e_uhf_encode.md)

## Stage 7: Irreversible or advanced tag operations

- 目的: 不可逆または高度なタグ操作を確認する。
- 主な確認対象: Lock、Kill、ThroughCmd
- 実行前に必要な情報: 承認、対象タグ、不可逆影響、復旧不可条件
- ログ項目: タグ影響、承認、ACK/NACK、timeout
- 復旧観点: 復旧不可条件の明記
- 先に完了しておくべきStage: Stage 0-2、必要に応じStage 6

Commands:

- UHF_Kill (docs/current/commands/cards/55_17_uhf_kill.md)
- UHF_Lock (docs/current/commands/cards/55_18_uhf_lock.md)
- UHF_ThroughCmd (docs/current/commands/cards/55_ff_uhf_through_cmd.md)

## Policy

- Stage分類は実行順序と必要な準備を示す。
- Stageが後段であることは、仕様上禁止という意味ではない。
- 実機確認時は対象機器、ROM、接続方式、アンテナ構成、ログ、復旧方法を記録する。
