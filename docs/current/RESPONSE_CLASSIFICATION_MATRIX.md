---
title: "レスポンス分類マトリクス"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs:
  - "COMMAND_MASTER_V117.md"
  - "RESPONSE_AND_NACK_MASTER.md"
  - "commands/cards/"
tags:
  - "utr-s201"
  - "guide"
  - "response"
  - "matrix"
  - "ai-implementation"
---

# レスポンス分類マトリクス

## 1. 目的

この文書は、全54コマンドを横断して、AI実装時に必要なレスポンス分類を一覧化します。詳細なbyte offset、ACK例、NACK例は各コマンドカードの `7.4 AI実装用レスポンス定義` を参照してください。

## 2. 先に読む順番

1. `RESPONSE_AND_NACK_MASTER.md` で共通フレーム、NACK、設定スナップショットを確認する。
2. このマトリクスで対象コマンドのレスポンス分類を確認する。
3. `commands/cards/<card>.md` の `7.4 AI実装用レスポンス定義` でoffset表と疑似コードを読む。

## 3. レスポンス分類の意味

| 分類 | 意味 | 実装上の注意 |
|---|---|---|
| `ACK_SIMPLE_OR_PAYLOAD` | `CMD=30h` の通常ACKまたはPDF定義payload | `DATA[0]` だけで固定せずPDF該当節を読む |
| `ACK_WITH_READ_DATA` | ACK内に読み取り長と読み取りデータを含む | タグ固有値はログ公開時にマスクする |
| `ACK/RF_ASYNC_AWARE` | 通常ACKと非同期RF応答が混在し得る | 自動読み取り中の `CMD=6Ch` を要求ACKと混同しない |
| `RF_TAG_DATA + COMPLETION` | タグ応答が複数返り、設定により完了ACK等が続く | 読取完了応答、ANT切替応答、キャリア検知応答のON/OFFをスナップショットで判断する |
| `ACK_THEN_READBACK` | 設定書き込みACK後に読戻し確認が必要 | RAM/FLASH、復元要否、再起動保持を別管理する |
| `ACK_THEN_TAG_VERIFY` | タグメモリ操作のACK後にタグ状態確認が必要 | NACK時はUHF ICエラー詳細も確認する |
| `NO_RESPONSE` | 正常系でACK/NACKを期待しない | Restart後は待機し、ROM読出し等で復帰確認する |

## 4. 全54コマンド分類

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 1 | [`ブザーの制御`](commands/cards/42_buzzer_control.md) | `42h` | `-` | `-` | `needs-metadata-confirmation` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 2 | [`リーダライタ動作モードの書き込み`](commands/cards/4e_00_10_write_reader_mode.md) | `4Eh` | `00h` | `10h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 3 | [`LED&ブザーの制御`](commands/cards/4e_57_led_buzzer_control.md) | `4Eh` | `57h` | `-` | `needs-metadata-confirmation` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 4 | [`FLASH設定の初期化`](commands/cards/4e_6f_flash_initialize.md) | `4Eh` | `6Fh` | `-` | `needs-metadata-confirmation` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, FLASH | ACK/NACK/timeout/invalid frameを共通処理 |
| 5 | [`リスタート`](commands/cards/4e_9d_restart_reader.md) | `4Eh` | `9Dh` | `-` | `needs-metadata-confirmation` | `NO_RESPONSE` | ROM/機種 | ACK待ちしない。再起動待機後にROM読出しで復帰確認 |
| 6 | [`RF送信信号の制御`](commands/cards/4e_9e_rf_carrier_control.md) | `4Eh` | `9Eh` | `-` | `needs-metadata-confirmation` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 7 | [`汎用ポート値の書き込み`](commands/cards/4e_9f_write_general_port.md) | `4Eh` | `9Fh` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 8 | [`拡張ポート値の書き込み`](commands/cards/4e_a0_write_extended_port.md) | `4Eh` | `A0h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 9 | [`FLASH設定値の書き込み(1バイトアクセス)`](commands/cards/4e_b4_flash_write.md) | `4Eh` | `B4h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, FLASH, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 10 | [`リーダライタ動作モードの読み取り`](commands/cards/4f_00_read_reader_mode.md) | `4Fh` | `00h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 11 | [`エラー情報の読み取り`](commands/cards/4f_80_read_error_info.md) | `4Fh` | `80h` | `-` | `rom-identification` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 12 | [`汎用ポート値の読み取り`](commands/cards/4f_9f_read_general_port.md) | `4Fh` | `9Fh` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 13 | [`拡張ポート値の読み取り`](commands/cards/4f_a0_read_extended_port.md) | `4Fh` | `A0h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 14 | [`FLASH設定値の読み取り(1バイトアクセス)`](commands/cards/4f_b4_read_flash_settings.md) | `4Fh` | `B4h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, FLASH, 読戻し | ACK/NACK/timeout/invalid frameを共通処理 |
| 15 | [`UHF_Inventory`](commands/cards/55_10_uhf_inventory.md) | `55h` | `10h` | `-` | `rf-read` | `RF_TAG_DATA + COMPLETION` | ROM/機種, ANT, Tag, ANT-ID出力, TID付加, 読取完了応答, ANT切替応答, キャリア検知応答 | 複数フレーム受信。タグ応答、完了ACK、ANT切替、キャリア検知を分類 |
| 16 | [`UHF_InventoryRead`](commands/cards/55_14_uhf_inventory_read.md) | `55h` | `14h` | `-` | `rf-read` | `RF_TAG_DATA + COMPLETION` | ROM/機種, ANT, Tag, ANT-ID出力, TID付加, 読取完了応答, ANT切替応答, キャリア検知応答 | 複数フレーム受信。タグ応答、完了ACK、ANT切替、キャリア検知を分類 |
| 17 | [`UHF_Read`](commands/cards/55_15_uhf_read.md) | `55h` | `15h` | `-` | `rf-read` | `ACK_WITH_READ_DATA` | ROM/機種, ANT, Tag, ANT-ID出力, キャリア検知応答 | ACK内の読取長と読取データを可変長解析 |
| 18 | [`UHF_Write`](commands/cards/55_16_uhf_write.md) | `55h` | `16h` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, ANT-ID出力, キャリア検知応答, 読戻し | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 19 | [`UHF_Kill`](commands/cards/55_17_uhf_kill.md) | `55h` | `17h` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, AP, ANT-ID出力, キャリア検知応答, 読戻し | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 20 | [`UHF_Lock`](commands/cards/55_18_uhf_lock.md) | `55h` | `18h` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, AP, ANT-ID出力, キャリア検知応答, 読戻し | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 21 | [`UHF_BlockWrite`](commands/cards/55_1a_uhf_block_write.md) | `55h` | `1Ah` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, AP, ANT-ID出力, キャリア検知応答, 読戻し | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 22 | [`UHF_BlockErase`](commands/cards/55_1b_uhf_block_erase.md) | `55h` | `1Bh` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, AP, ANT-ID出力, キャリア検知応答, 読戻し | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 23 | [`UHF_BlockWrite2`](commands/cards/55_1d_uhf_block_write2.md) | `55h` | `1Dh` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, AP, ANT-ID出力, キャリア検知応答, 読戻し | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 24 | [`UHF_Encode`](commands/cards/55_1e_uhf_encode.md) | `55h` | `1Eh` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, ANT-ID出力, キャリア検知応答, 読戻し | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 25 | [`UHF_SetSelectParam`](commands/cards/55_30_uhf_set_select_param.md) | `55h` | `30h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 26 | [`UHF_SetInventoryParam`](commands/cards/55_31_uhf_set_inventory_param.md) | `55h` | `31h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 27 | [`UHF_SetExpandSelectParam`](commands/cards/55_32_uhf_set_expand_select_param.md) | `55h` | `32h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 28 | [`アンテナ切替設定の書き込み`](commands/cards/55_33_00_write_antenna_switching.md) | `55h` | `33h` | `00h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 29 | [`出力設定の書き込み`](commands/cards/55_33_01_write_output_power.md) | `55h` | `33h` | `01h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 30 | [`周波数設定の書き込み`](commands/cards/55_33_02_write_frequency.md) | `55h` | `33h` | `02h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 31 | [`Accessパスワードの書き込み`](commands/cards/55_33_03_write_access_password.md) | `55h` | `33h` | `03h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, AP, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 32 | [`RFタグ通信関連パラメータの書き込み`](commands/cards/55_33_04_write_rf_tag_comm_params.md) | `55h` | `33h` | `04h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 33 | [`EPC(UII)関連パラメータの書き込み`](commands/cards/55_33_05_write_epc_uii_params.md) | `55h` | `33h` | `05h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 34 | [`外部アンテナ自動切替設定の書き込み`](commands/cards/55_37_write_external_antenna_auto_switch.md) | `55h` | `37h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 35 | [`使用アンテナ番号の書き込み`](commands/cards/55_38_write_active_antenna.md) | `55h` | `38h` | `-` | `needs-metadata-confirmation` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, 読戻し | ACK/NACK/timeout/invalid frameを共通処理 |
| 36 | [`RSSIフィルタ設定の書き込み`](commands/cards/55_39_write_rssi_filter.md) | `55h` | `39h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 37 | [`アンテナ個別送信出力設定の書き込み`](commands/cards/55_3a_write_antenna_output_power.md) | `55h` | `3Ah` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 38 | [`UHF_GetSelectParam`](commands/cards/55_40_uhf_get_select_param.md) | `55h` | `40h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 39 | [`UHF_GetInventoryParam`](commands/cards/55_41_uhf_get_inventory_param.md) | `55h` | `41h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 40 | [`UHF_GetExpandSelectParam`](commands/cards/55_42_uhf_get_expand_select_param.md) | `55h` | `42h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 41 | [`アンテナ切替設定の読み取り`](commands/cards/55_43_00_read_antenna_switching.md) | `55h` | `43h` | `00h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 42 | [`出力設定の読み取り`](commands/cards/55_43_01_read_output_power.md) | `55h` | `43h` | `01h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 43 | [`周波数設定の読み取り`](commands/cards/55_43_02_read_frequency.md) | `55h` | `43h` | `02h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 44 | [`RFタグ通信関連パラメータの読み取り`](commands/cards/55_43_04_read_rf_tag_comm_params.md) | `55h` | `43h` | `04h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 45 | [`EPC(UII)関連パラメータの読み取り`](commands/cards/55_43_05_read_epc_uii_params.md) | `55h` | `43h` | `05h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 46 | [`UHF_CheckAntenna`](commands/cards/55_44_uhf_check_antenna.md) | `55h` | `44h` | `-` | `rf-read` | `ACK/RF_ASYNC_AWARE` | ROM/機種, ANT, ANT-ID出力, キャリア検知応答 | 通常ACKと自動読み取り中の非同期RF応答を分離 |
| 47 | [`UHF_GetHandle`](commands/cards/55_46_uhf_get_handle.md) | `55h` | `46h` | `-` | `rf-read` | `ACK/RF_ASYNC_AWARE` | ROM/機種, ANT, ANT-ID出力, キャリア検知応答 | 通常ACKと自動読み取り中の非同期RF応答を分離 |
| 48 | [`外部アンテナ自動切替設定の読み取り`](commands/cards/55_47_read_external_antenna_auto_switch.md) | `55h` | `47h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 49 | [`使用アンテナ番号の読み取り`](commands/cards/55_48_read_active_antenna.md) | `55h` | `48h` | `-` | `needs-metadata-confirmation` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 50 | [`RSSIフィルタ設定の読み取り`](commands/cards/55_49_read_rssi_filter.md) | `55h` | `49h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 51 | [`アンテナ個別送信出力設定の読み取り`](commands/cards/55_4a_read_antenna_output_power.md) | `55h` | `4Ah` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 52 | [`チップバージョンの読み取り`](commands/cards/55_90_chip_version_read.md) | `55h` | `90h` | `-` | `rom-identification` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 53 | [`UHF_ThroughCmd`](commands/cards/55_ff_uhf_through_cmd.md) | `55h` | `FFh` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, ANT-ID出力, キャリア検知応答 | ACK後、タグ状態・UHF ICエラー詳細を確認 |
| 54 | [`ROMバージョンの読み取り`](commands/cards/rom_version_read.md) | `4Fh` | `90h` | `-` | `rom-identification` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |

## 5. 実装時の判定順序

全コマンドで、まず共通フレームを検証し、その後に次の順で分類してください。

| 順序 | 判定 | 条件 |
|---:|---|---|
| 1 | `INVALID_FRAME` | `STX/ETX/CR/SUM` または総長 `LEN + 7` が不正 |
| 2 | `TIMEOUT` | 受信期限内に有効フレームなし |
| 3 | `NACK` | `CMD=31h` |
| 4 | `RF_TAG_DATA` | `CMD=6Ch` |
| 5 | `ACK` | `CMD=30h` |
| 6 | `NO_RESPONSE` | 対象カードが `NO_RESPONSE` 分類で、仕様上ACK/NACKなし |

`CMD=30h` の中には、通常ACK、読取完了ACK、アンテナ切替完了ACK、キャリア検知ACKが含まれます。コマンド名だけで固定せず、DATA offsetと設定スナップショットで判断してください。

## 6. 数量確認

- command_card件数: `54`
- このマトリクスは、旧工程や過去経緯ではなく、現在版V100の実装入口として使います。
