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

この文書は、全54コマンドを横断して、AI実装時に必要なレスポンス分類を一覧化します。詳細なbyte offset、ACK例、NACK例は各コマンドカードの `AI実装用レスポンス定義` を参照してください。

## 2. 先に読む順番

1. `RESPONSE_AND_NACK_MASTER.md` で共通フレーム、NACK、設定スナップショットを確認する。
2. このマトリクスで対象コマンドのレスポンス分類を確認する。
3. `commands/cards/<card>.md` の `AI実装用レスポンス定義` でoffset表と判定手順を読む。

共通フレーム・SUM・固定長NACKは[共通マスタ](RESPONSE_AND_NACK_MASTER.md)を確認します。未照合カードの汎用説明や疑似コードが共通マスタと矛盾する場合、無条件にカードを優先しません。[照合範囲](SOURCE_REVIEW_STATUS.md)を確認し、原典へ戻ります。

## 3. レスポンス分類の意味

| 分類 | 意味 | 実装上の注意 |
|---|---|---|
| `ACK_SIMPLE_OR_PAYLOAD` | `CMD=30h` の通常ACKまたはPDF定義payload | `DATA[0]` だけで固定せずPDF該当節を読む |
| `ACK_ONLY_NO_READBACK` | 値を返さないACKで、設定値の読戻し手段がない | Access設定のACKをタグ認証成功と同一視しない |
| `ACK_THEN_KILLED` | Kill成功ACK後、対象タグは応答しなくなる | 読戻し不可。無応答単独で成功を証明しない |
| `ACK_WITH_READ_DATA` | ACK内に読み取り長と読み取りデータを含む | タグ固有値はログ公開時にマスクする |
| `ACK/RF_ASYNC_AWARE` | 通常ACKと非同期RF応答が混在し得る | 自動読み取り中の `CMD=6Ch` を要求ACKと混同しない |
| `RF_TAG_DATA + COMPLETION` | タグ応答と、そのコマンドに定義された完了応答 | 単発コマンドの完了と自動読み取りのサイクル通知を分ける。[モード別適用範囲](RESPONSE_MODE_APPLICABILITY.md)を参照 |
| `ACK_THEN_READBACK` | 設定書き込みACK後に読戻し確認が必要 | RAM/FLASH、復元要否、再起動保持を別管理する |
| `ACK_THEN_TAG_VERIFY` | タグメモリ操作のACK後にタグ状態確認が必要 | NACK時はUHF ICエラー詳細も確認する |
| `NO_RESPONSE` | 正常系でACK/NACKを期待しない | Restart後は待機し、ROM読出し等で復帰確認する |
| `ACK_OR_NO_RESPONSE_BY_REQUEST` | 応答要求パラメータによりACKあり/なしが変わる | 送信DATAの応答要求値を受信判定へ渡す |

## 4. 全54コマンド分類

### ブザー・LEDと動作モード（一覧順1–3）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 1 | [`ブザーの制御`](commands/cards/42_buzzer_control.md) | `42h` | `-` | `-` | `reader-control` | `ACK_OR_NO_RESPONSE_BY_REQUEST` | ポート7機能, 応答要求 | 01hはLEN=00h ACK、00hは正常無応答。異常NACKあり |
| 2 | [`リーダライタ動作モードの書き込み`](commands/cards/4e_00_10_write_reader_mode.md) | `4Eh` | `00h/10h` | `-` | `settings-change` | `ACK_THEN_READBACK` | 対象, モード | LEN=00h。読戻しは00hモード時 |
| 3 | [`LED&ブザーの制御`](commands/cards/4e_57_led_buzzer_control.md) | `4Eh` | `57h` | `-` | `reader-control` | `ACK_SIMPLE_OR_PAYLOAD` | 機能, 方向, 動作値 | LEN=01h・57h。実動作を別確認 |

### 初期化・再起動とRF制御（一覧順4–6）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 4 | [`FLASH設定の初期化`](commands/cards/4e_6f_flash_initialize.md) | `4Eh` | `6Fh` | `-` | `settings-change` | `ACK_THEN_READBACK` | FLASH | LEN=01h・6Fh。再起動後に反映確認 |
| 5 | [`リスタート`](commands/cards/4e_9d_restart_reader.md) | `4Eh` | `9Dh` | `-` | `reader-control` | `NO_RESPONSE` | 保存モード | ACKなし。2秒以上後に通信・設定確認 |
| 6 | [`RF送信信号の制御`](commands/cards/4e_9e_rf_carrier_control.md) | `4Eh` | `9Eh` | `-` | `reader-control` | `ACK_SIMPLE_OR_PAYLOAD` | 制御値・RF | LEN=02h・9Eh、予約1 byte |

### ポート・FLASH書込み（一覧順7–9）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 7 | [`汎用ポート値の書き込み`](commands/cards/4e_9f_write_general_port.md) | `4Eh` | `9Fh` | `-` | `settings-change` | `ACK_THEN_READBACK` | 機能, 方向, 指示 | LEN=01h・9Fh。対象bitを読戻す |
| 8 | [`拡張ポート値の書き込み`](commands/cards/4e_a0_write_extended_port.md) | `4Eh` | `A0h` | `-` | `settings-change` | `ACK_THEN_READBACK` | 8CH, 方向, 指示 | LEN=01h・A0h。対象bitを読戻す |
| 9 | [`FLASH設定値の書き込み(1バイトアクセス)`](commands/cards/4e_b4_flash_write.md) | `4Eh` | `B4h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種・アドレス | LEN=01h・B4h。読戻しと実動作は別 |

### 動作モード・状態・設定読取り（一覧順10–13）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 10 | [`リーダライタ動作モードの読み取り`](commands/cards/4f_00_read_reader_mode.md) | `4Fh` | `00h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | モード | LEN=09h。連続中は受付保証なし |
| 11 | [`エラー情報の読み取り`](commands/cards/4f_80_read_error_info.md) | `4Fh` | `80h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | 状態 | LEN=04h・80h。非ゼロ情報もACK |
| 12 | [`汎用ポート値の読み取り`](commands/cards/4f_9f_read_general_port.md) | `4Fh` | `9Fh` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | LEN=05h・9Fh。現在値と設定を分離 |
| 13 | [`拡張ポート値の読み取り`](commands/cards/4f_a0_read_extended_port.md) | `4Fh` | `A0h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | 8CH | LEN=05h・A0h。機能は0固定 |

### 動作モード・状態・設定読取り（一覧順14–14）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 14 | [`FLASH設定値の読み取り(1バイトアクセス)`](commands/cards/4f_b4_read_flash_settings.md) | `4Fh` | `B4h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種・アドレス | LEN=02h・B4h、値1 byte。要求に対応 |

### タグ検出と読取り（一覧順15–17）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 15 | [`UHF_Inventory`](commands/cards/55_10_uhf_inventory.md) | `55h` | `10h` | `-` | `rf-read` | `RF_TAG_DATA + COMPLETION` | ROM/機種, ANT, Tag, ANT-ID出力, コマンドモード用設定 | 単発のタグ応答と完了を分類。正常0枚も完了応答。自動読み取り用通知OFFを流用しない |
| 16 | [`UHF_InventoryRead`](commands/cards/55_14_uhf_inventory_read.md) | `55h` | `14h` | `-` | `rf-read` | `RF_TAG_DATA + COMPLETION` | ROM/機種, ANT, Tag, ANT-ID出力, コマンド内のTID付加・読取領域指定 | 単発の複数フレームと完了を対象節で確認。自動読み取りの通知条件とは分ける |
| 17 | [`UHF_Read`](commands/cards/55_15_uhf_read.md) | `55h` | `15h` | `-` | `rf-read` | `ACK_WITH_READ_DATA` | ROM/機種, ANT, Tag, AP条件, ANT-ID出力, 要求bank・Word位置・m | CMD=30h・詳細15h、n=2×m byte、LEN=n+2。完了通知設定で省略しない |

### タグ書込み・Kill・Lock（一覧順18–20）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 18 | [`UHF_Write`](commands/cards/55_16_uhf_write.md) | `55h` | `16h` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, AP条件, 要求bank・Word位置・値, 読戻し条件 | CMD=30h・LEN=01h・詳細16h、総8 byte。値は返らず、読戻し確認を別記録 |
| 19 | [`UHF_Kill`](commands/cards/55_17_uhf_kill.md) | `55h` | `17h` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_KILLED` | ROM/機種, ANT, 対象1枚, Kill Password, AP設定条件 | CMD=30h・LEN=01h・詳細17h。成功後は応答せず読戻し不可。無応答単独では成功を証明しない |
| 20 | [`UHF_Lock`](commands/cards/55_18_uhf_lock.md) | `55h` | `18h` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, 対象1枚, 非ゼロで一致するAP, Mask/Action | CMD=30h・LEN=01h・詳細18h。Lock状態は返らず、認証条件別の確認を別記録 |

### Block処理とEncode（一覧順21–23）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 21 | [`UHF_BlockWrite`](commands/cards/55_1a_uhf_block_write.md) | `55h` | `1Ah` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, 対象1枚, AP, RF側方式, bank・Word範囲・値 | CMD=30h・LEN=01h・詳細1Ah。RF側は1 Wordずつ、NACKでも部分書込みあり |
| 22 | [`UHF_BlockErase`](commands/cards/55_1b_uhf_block_erase.md) | `55h` | `1Bh` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, 対象1枚, AP, タグ対応・消去後の値, Word範囲 | CMD=30h・LEN=01h・詳細1Bh。結果データは返らず、消去後の値はタグ仕様 |
| 23 | [`UHF_BlockWrite2`](commands/cards/55_1d_uhf_block_write2.md) | `55h` | `1Dh` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, 対象1枚, AP, タグ対応数, 範囲・値, timeout | CMD=30h・LEN=01h・詳細1Dh。NACKはコード1/2と3/4を区別。処理数は返らない |

### Block処理とEncode（一覧順24–24）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 24 | [`UHF_Encode`](commands/cards/55_1e_uhf_encode.md) | `55h` | `1Eh` | `-` | `tag-memory-or-high-impact` | `ACK_THEN_TAG_VERIFY` | ROM/機種, ANT, Tag, AP, 長さ, Lock, キャリア | LEN=01h・詳細1Eh。コード3とAP保持はカード参照 |

### Select・Inventory条件の設定（一覧順25–27）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 25 | [`UHF_SetSelectParam`](commands/cards/55_30_uhf_set_select_param.md) | `55h` | `30h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 要求種類と全設定 | CMD=30h・LEN=01h・詳細30h、種類は返らない。同種類で40h読戻し。両RAM独立、FLASHは両RAMへ反映 |
| 26 | [`UHF_SetInventoryParam`](commands/cards/55_31_uhf_set_inventory_param.md) | `55h` | `31h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 27 | [`UHF_SetExpandSelectParam`](commands/cards/55_32_uhf_set_expand_select_param.md) | `55h` | `32h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 要求種類・n・全条件 | CMD=30h・LEN=01h・詳細32h。種類・数・値は返らず42hで読戻す。両RAM独立、FLASHは両RAMへ反映 |

### アンテナ・RF・EPC関連設定（一覧順28–30）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 28 | [`アンテナ切替設定の書き込み`](commands/cards/55_33_00_write_antenna_switching.md) | `55h` | `33h` | `00h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 29 | [`出力設定の書き込み`](commands/cards/55_33_01_write_output_power.md) | `55h` | `33h` | `01h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, パラメータ種類, 4つの要求値, RAM/FLASH対象 | LEN=0Bh・詳細33h・サブ01h・種類と返却値を照合。FLASHは両RAMにも反映 |
| 30 | [`周波数設定の書き込み`](commands/cards/55_33_02_write_frequency.md) | `55h` | `33h` | `02h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 種類, 開始番号, 使用マスク, RAM/FLASH対象 | LEN=0Ch・詳細33h・サブ02h・種類を照合。DATA[4]予約。開始番号5・11・17・23～37chを要求値と照合 |

### アンテナ・RF・EPC関連設定（一覧順31–33）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 31 | [`Accessパスワードの書き込み`](commands/cards/55_33_03_write_access_password.md) | `55h` | `33h` | `03h` | `settings-change` | `ACK_ONLY_NO_READBACK` | ROM/機種, 設定するAP, 終了時のゼロ化 | CMD=30h・LEN=03h・詳細33h・サブ03h・予約。値は読戻せず、タグ認証成功も示さない |
| 32 | [`RFタグ通信関連パラメータの書き込み`](commands/cards/55_33_04_write_rf_tag_comm_params.md) | `55h` | `33h` | `04h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 種類 | LEN=03h・33h/04h・種類。値は読戻す |
| 33 | [`EPC(UII)関連パラメータの書き込み`](commands/cards/55_33_05_write_epc_uii_params.md) | `55h` | `33h` | `05h` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |

### 外部アンテナ・RSSI・個別出力設定（一覧順34–37）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 34 | [`外部アンテナ自動切替設定の書き込み`](commands/cards/55_37_write_external_antenna_auto_switch.md) | `55h` | `37h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 読戻し | ACK後、必要に応じ対応読出しでRAM/FLASH反映確認 |
| 35 | [`使用アンテナ番号の書き込み`](commands/cards/55_38_write_active_antenna.md) | `55h` | `38h` | `-` | `settings-change` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, 種類, 復元値 | LEN=04h・詳細38hを照合。48hは書込み成功にしない |
| 36 | [`RSSIフィルタ設定の書き込み`](commands/cards/55_39_write_rssi_filter.md) | `55h` | `39h` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM, 範囲 | LEN=05h・39h。FLASHを読戻す |
| 37 | [`アンテナ個別送信出力設定の書き込み`](commands/cards/55_3a_write_antenna_output_power.md) | `55h` | `3Ah` | `-` | `settings-change` | `ACK_THEN_READBACK` | ROM/機種, 有効フラグ, 開始番号, 数, 全出力値 | LEN=05h・詳細3Ah・フラグ/開始/数を要求と照合。出力値は返らず4Ahで読戻す。FLASH保存 |

### Select・Inventory条件の読取り（一覧順38–40）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 38 | [`UHF_GetSelectParam`](commands/cards/55_40_uhf_get_select_param.md) | `55h` | `40h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, 要求種類 | 詳細40h・種類一致・LEN=9+ceil(bit数/8)。bit数0～128、開始位置はMSB順のbitアドレス |
| 39 | [`UHF_GetInventoryParam`](commands/cards/55_41_uhf_get_inventory_param.md) | `55h` | `41h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 40 | [`UHF_GetExpandSelectParam`](commands/cards/55_42_uhf_get_expand_select_param.md) | `55h` | `42h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, 要求種類・n | 詳細42h・種類一致・LEN=2+23×要求n。nはACKにない。0 bit枠も23 byteとして全n枠を解析 |

### アンテナ・RF・EPC関連設定の読取り（一覧順41–44）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 41 | [`アンテナ切替設定の読み取り`](commands/cards/55_43_00_read_antenna_switching.md) | `55h` | `43h` | `00h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 42 | [`出力設定の読み取り`](commands/cards/55_43_01_read_output_power.md) | `55h` | `43h` | `01h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, パラメータ種類 | LEN=0Bh・詳細43h・サブ01h・種類を照合。値はLSBファーストの設定値 |
| 43 | [`周波数設定の読み取り`](commands/cards/55_43_02_read_frequency.md) | `55h` | `43h` | `02h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, パラメータ種類 | LEN=0Ch・詳細43h・サブ02h・種類を照合。DATA[4]は最後の出力チャンネル |
| 44 | [`RFタグ通信関連パラメータの読み取り`](commands/cards/55_43_04_read_rf_tag_comm_params.md) | `55h` | `43h` | `04h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, 種類 | LEN=06h・43h/04h・種類を照合 |

### アンテナ・RF・EPC関連設定の読取り（一覧順45–45）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 45 | [`EPC(UII)関連パラメータの読み取り`](commands/cards/55_43_05_read_epc_uii_params.md) | `55h` | `43h` | `05h` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |

### 診断・Handleと個別設定の読取り（一覧順46–49）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 46 | [`UHF_CheckAntenna`](commands/cards/55_44_uhf_check_antenna.md) | `55h` | `44h` | `-` | `rf-read` | `ACK_SIMPLE_OR_PAYLOAD` | 番号・RF | LEN=03h・44h、番号・接続情報 |
| 47 | [`UHF_GetHandle`](commands/cards/55_46_uhf_get_handle.md) | `55h` | `46h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM・Handle経緯 | LEN=03h・46h、Handle2 byte |
| 48 | [`外部アンテナ自動切替設定の読み取り`](commands/cards/55_47_read_external_antenna_auto_switch.md) | `55h` | `47h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種 | ACK/NACK/timeout/invalid frameを共通処理 |
| 49 | [`使用アンテナ番号の読み取り`](commands/cards/55_48_read_active_antenna.md) | `55h` | `48h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, パラメータ種類 | LEN=04h。00hは現在選択値、01h/02hは保存設定 |

### 診断・Handleと個別設定の読取り（一覧順50–51）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 50 | [`RSSIフィルタ設定の読み取り`](commands/cards/55_49_read_rssi_filter.md) | `55h` | `49h` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM, 範囲 | LEN=5+12n・49h・No.を照合 |
| 51 | [`アンテナ個別送信出力設定の読み取り`](commands/cards/55_4a_read_antenna_output_power.md) | `55h` | `4Ah` | `-` | `read-only` | `ACK_SIMPLE_OR_PAYLOAD` | ROM/機種, 開始番号, 数 | 詳細4Ah・LEN=5+n、n=1～250、開始/数を要求と照合。無効でもn個の整数dBm値が返る |

### 機器識別と透過通信（一覧順52–54）

| No. | カード | コマンド | 詳細 | サブ | 操作分類 | レスポンス分類 | 事前スナップショット | 受信ループ方針 |
|---:|---|---|---|---|---|---|---|---|
| 52 | [`チップバージョンの読み取り`](commands/cards/55_90_chip_version_read.md) | `55h` | `90h` | `-` | `rom-identification` | `ACK_SIMPLE_OR_PAYLOAD` | 取得種別 | 90h・種別とLEN=0Bh/0Chを照合 |
| 53 | [`UHF_ThroughCmd`](commands/cards/55_ff_uhf_through_cmd.md) | `55h` | `FFh` | `-` | `tag-memory-or-high-impact` | `ACK_SIMPLE_OR_PAYLOAD` | 動作bit・タグ仕様 | FFh・可変bit列。詳細はカード |
| 54 | [`ROMバージョンの読み取り`](commands/cards/rom_version_read.md) | `4Fh` | `90h` | `-` | `rom-identification` | `ACK_SIMPLE_OR_PAYLOAD` | 要求 | LEN=0Ah・90h。ASCIIの版・シリーズ |

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
