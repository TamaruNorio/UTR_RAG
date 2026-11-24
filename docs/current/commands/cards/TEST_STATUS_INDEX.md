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

# 仕様参照・確認状態索引

2026-09-07の保守者方針に従い、公式PDFを仕様上の期待結果の基準とします。54カードは `SPECIFICATION_REFERENCE`、結果は `NOT_AN_EXECUTION_RESULT` として整理します。PDFとの全項目再照合完了、実機合格、試験未実施のいずれも表しません。[確認状態の記録方針](../../VERIFICATION_POLICY.md)と[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)を参照してください。

この索引は、各コマンドカードのfrontmatterに記載された `verification_status` をもとに、現在有効な確認状態を整理したものです。
全54コマンドを個別に実機送信済みであることを示すものではありません。各カードの詳細な確認内容は、カード本体の「9. 実機確認」を参照してください。

整理対象のカード枚数: 54件

2026-09-14: GetHandle・ThroughCmdまで主要条件を部分照合しました。累計54カードで、全カードに照合記録があります。各カードの残項目・未解決仕様があり、全仕様の照合完了ではありません。詳細は[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)を参照してください。確認状態ラベルは変更していません。

## SPECIFICATION_REFERENCE（54件）

### ブザー・LEDと動作モード（一覧順1–3）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `42h` | [ブザーの制御](42_buzzer_control.md) | `-` | `-` |
| `4Eh` | [リーダライタ動作モードの書き込み](4e_00_10_write_reader_mode.md) | `00h / 10h` | `-` |
| `4Eh` | [LED&ブザーの制御](4e_57_led_buzzer_control.md) | `57h` | `-` |

### 初期化・再起動とRF制御（一覧順4–6）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `4Eh` | [FLASH設定の初期化](4e_6f_flash_initialize.md) | `6Fh` | `-` |
| `4Eh` | [リスタート](4e_9d_restart_reader.md) | `9Dh` | `-` |
| `4Eh` | [RF送信信号の制御](4e_9e_rf_carrier_control.md) | `9Eh` | `-` |

### ポート・FLASH書込み（一覧順7–9）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `4Eh` | [汎用ポート値の書き込み](4e_9f_write_general_port.md) | `9Fh` | `-` |
| `4Eh` | [拡張ポート値の書き込み](4e_a0_write_extended_port.md) | `A0h` | `-` |
| `4Eh` | [FLASH設定値の書き込み(1バイトアクセス)](4e_b4_flash_write.md) | `B4h` | `-` |

### 動作モード・状態・設定読取り（一覧順10–14）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `4Fh` | [リーダライタ動作モードの読み取り](4f_00_read_reader_mode.md) | `00h` | `-` |
| `4Fh` | [エラー情報の読み取り](4f_80_read_error_info.md) | `80h` | `-` |
| `4Fh` | [汎用ポート値の読み取り](4f_9f_read_general_port.md) | `9Fh` | `-` |
| `4Fh` | [拡張ポート値の読み取り](4f_a0_read_extended_port.md) | `A0h` | `-` |
| `4Fh` | [FLASH設定値の読み取り(1バイトアクセス)](4f_b4_read_flash_settings.md) | `B4h` | `-` |

### タグ検出と読取り（一覧順15–17）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [UHF_Inventory](55_10_uhf_inventory.md) | `10h` | `-` |
| `55h` | [UHF_InventoryRead](55_14_uhf_inventory_read.md) | `14h` | `-` |
| `55h` | [UHF_Read](55_15_uhf_read.md) | `15h` | `-` |

### タグ書込み・Kill・Lock（一覧順18–20）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [UHF_Write](55_16_uhf_write.md) | `16h` | `-` |
| `55h` | [UHF_Kill](55_17_uhf_kill.md) | `17h` | `-` |
| `55h` | [UHF_Lock](55_18_uhf_lock.md) | `18h` | `-` |

### Block処理とEncode（一覧順21–24）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [UHF_BlockWrite](55_1a_uhf_block_write.md) | `1Ah` | `-` |
| `55h` | [UHF_BlockErase](55_1b_uhf_block_erase.md) | `1Bh` | `-` |
| `55h` | [UHF_BlockWrite2](55_1d_uhf_block_write2.md) | `1Dh` | `-` |
| `55h` | [UHF_Encode](55_1e_uhf_encode.md) | `1Eh` | `-` |

### Select・Inventory条件の設定（一覧順25–27）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [UHF_SetSelectParam](55_30_uhf_set_select_param.md) | `30h` | `-` |
| `55h` | [UHF_SetInventoryParam](55_31_uhf_set_inventory_param.md) | `31h` | `-` |
| `55h` | [UHF_SetExpandSelectParam](55_32_uhf_set_expand_select_param.md) | `32h` | `-` |

### アンテナ・RF・EPC関連設定（一覧順28–33）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [アンテナ切替設定の書き込み](55_33_00_write_antenna_switching.md) | `33h` | `00h` |
| `55h` | [出力設定の書き込み](55_33_01_write_output_power.md) | `33h` | `01h` |
| `55h` | [周波数設定の書き込み](55_33_02_write_frequency.md) | `33h` | `02h` |
| `55h` | [Accessパスワードの書き込み](55_33_03_write_access_password.md) | `33h` | `03h` |
| `55h` | [RFタグ通信関連パラメータの書き込み](55_33_04_write_rf_tag_comm_params.md) | `33h` | `04h` |
| `55h` | [EPC(UII)関連パラメータの書き込み](55_33_05_write_epc_uii_params.md) | `33h` | `05h` |

### 外部アンテナ・RSSI・個別出力設定（一覧順34–37）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [外部アンテナ自動切替設定の書き込み](55_37_write_external_antenna_auto_switch.md) | `37h` | `-` |
| `55h` | [使用アンテナ番号の書き込み](55_38_write_active_antenna.md) | `38h` | `-` |
| `55h` | [RSSIフィルタ設定の書き込み](55_39_write_rssi_filter.md) | `39h` | `-` |
| `55h` | [アンテナ個別送信出力設定の書き込み](55_3a_write_antenna_output_power.md) | `3Ah` | `-` |

### Select・Inventory条件の読取り（一覧順38–40）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [UHF_GetSelectParam](55_40_uhf_get_select_param.md) | `40h` | `-` |
| `55h` | [UHF_GetInventoryParam](55_41_uhf_get_inventory_param.md) | `41h` | `-` |
| `55h` | [UHF_GetExpandSelectParam](55_42_uhf_get_expand_select_param.md) | `42h` | `-` |

### アンテナ・RF・EPC関連設定の読取り（一覧順41–45）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [アンテナ切替設定の読み取り](55_43_00_read_antenna_switching.md) | `43h` | `00h` |
| `55h` | [出力設定の読み取り](55_43_01_read_output_power.md) | `43h` | `01h` |
| `55h` | [周波数設定の読み取り](55_43_02_read_frequency.md) | `43h` | `02h` |
| `55h` | [RFタグ通信関連パラメータの読み取り](55_43_04_read_rf_tag_comm_params.md) | `43h` | `04h` |
| `55h` | [EPC(UII)関連パラメータの読み取り](55_43_05_read_epc_uii_params.md) | `43h` | `05h` |

### 診断・Handleと個別設定の読取り（一覧順46–51）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [UHF_CheckAntenna](55_44_uhf_check_antenna.md) | `44h` | `-` |
| `55h` | [UHF_GetHandle](55_46_uhf_get_handle.md) | `46h` | `-` |
| `55h` | [外部アンテナ自動切替設定の読み取り](55_47_read_external_antenna_auto_switch.md) | `47h` | `-` |
| `55h` | [使用アンテナ番号の読み取り](55_48_read_active_antenna.md) | `48h` | `-` |
| `55h` | [RSSIフィルタ設定の読み取り](55_49_read_rssi_filter.md) | `49h` | `-` |
| `55h` | [アンテナ個別送信出力設定の読み取り](55_4a_read_antenna_output_power.md) | `4Ah` | `-` |

### 機器識別と透過通信（一覧順52–54）

| コマンド | カード | detail | sub |
|---|---|---|---|
| `55h` | [チップバージョンの読み取り](55_90_chip_version_read.md) | `90h` | `-` |
| `55h` | [UHF_ThroughCmd](55_ff_uhf_through_cmd.md) | `FFh` | `-` |
| `4Fh` | [ROMバージョンの読み取り](rom_version_read.md) | `90h` | `-` |

## 更新方法

### 表示変更の履歴

2026-09-07以前は54件とも `REAL_DEVICE_VERIFIED_WITH_NOTES` / `REAL_DEVICE_PASS_WITH_NOTES` でした。この旧表示は、全54コマンドの個別実機試験を示すものではないという注記と併存していました。PDFを基準とする仕様参照資料であることが伝わるよう、表示を変更しました。過去の実績を否定したり、新たな試験を実施したりした変更ではありません。

この表は手動で行を書き写さず、手元管理の検証ツールで更新してください。検証ツールはリポジトリには含めません。カードのfrontmatterに`verification_status`を追加・変更した場合は、検証ツールで表を再生成してください。

公開cloneには、この索引を再生成するツールはありません。ツールを利用できない場合はカードと索引の対応変更案を保守者へ渡し、再生成と差分確認を依頼してください。再生成済みとは報告しません。公開scriptsのFront Matter検査とリンク検査は、索引の全行とカードの状態が一致することまで検査しないため、件数・重複・対象カード・状態の対応を別途確認します。

公式PDFが一次情報です。この索引は公式PDFの代替ではありません。
