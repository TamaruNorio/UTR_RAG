# 用途別の参照ガイド

メーカーSDKを使わずに、公開プロトコルから実装・レビューするための入口です。実機と通信する用途ではUSB/COMまたはLAN/TCPを先に指定します。送受信せず受信済みbytesの共通構造だけを調べる用途はOFFLINEと明記し、接続・機種識別コマンド・設定読戻しを追加しません。構造検査だけでコマンド成功や実機適合を判定しません。OS・実装言語・接続ライブラリの選択は、通信仕様そのものと分けて扱います。

## 1. 最初の確認

AIの作業では [AGENTS.md](../../AGENTS.md) の必読順序に従い、[README](../../README.md)、[公開範囲](../../RELEASE_SCOPE.md)、[利用ガイド](V100_USAGE_GUIDE.md)で目的と条件を確認します。仕様の疑問点は[原典照合・確認待ち一覧](SOURCE_REVIEW_STATUS.md)、試験状態は[確認状態の記録方針](VERIFICATION_POLICY.md)と[実機確認索引](commands/cards/TEST_STATUS_INDEX.md)を確認します。

実装・パーサレビューでは、[コマンドマスタ](COMMAND_MASTER_V117.md)、[NACKマスタ](RESPONSE_AND_NACK_MASTER.md)、[レスポンス分類](RESPONSE_CLASSIFICATION_MATRIX.md)、[機種・ROM条件](DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md)が共通資料です。次の表は追加の入口であり、カードの `related_docs` を省略する許可ではありません。

## 2. 用途から選ぶ

読み取り方式・完了条件・通知設定を扱う場合は、[モード別の適用範囲](RESPONSE_MODE_APPLICABILITY.md)も確認してください。自動読み取りのサイクル通知を、単発コマンドの完了と同一視しないでください。

TIDやWord数を扱う場合は、[TIDメモリと単位](TID_MEMORY_AND_UNITS.md)でGS1の単位定義とUTRの製品機能を分けて確認してください。

### 機種判定と単発読取り

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| 機種判定・対応可否 | [機種・ROM](DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md)、[ROM読取り](commands/cards/rom_version_read.md) | 機種、ROM、コマンド対応。未知機種を既知機種へ決め打ちしない |
| 単発のタグ一覧読取り | [Inventory](commands/cards/55_10_uhf_inventory.md)、[Inventory設定読取り](commands/cards/55_41_uhf_get_inventory_param.md) | 正常0件、NACK、複数タグ、完了、期限、可変長。連続受信と分ける |

### 連続読取りと複数アンテナ

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| 連続読取り・受信ログの評価 | [動作モード読取り](commands/cards/4f_00_read_reader_mode.md)、[動作モード書込み](commands/cards/4e_00_10_write_reader_mode.md)、[Inventory設定](commands/cards/55_31_uhf_set_inventory_param.md)、[既知の失敗](KNOWN_AI_FAILURE_PATTERNS.md) | 連続中の設定読取りは保証外。切替は00h経由、起動はFLASH値。ACK・非同期応答・停止時復元を区別 |
| 複数アンテナ | [番号体系](ANTENNA_NUMBERING_SCHEMES.md)、[接続確認](commands/cards/55_44_uhf_check_antenna.md)、[使用番号読取り](commands/cards/55_48_read_active_antenna.md)、[使用番号書込み](commands/cards/55_38_write_active_antenna.md)、[外部自動切替読取り](commands/cards/55_47_read_external_antenna_auto_switch.md)、[外部自動切替書込み](commands/cards/55_37_write_external_antenna_auto_switch.md) | 各カードの対応機種。4CH等では[アンテナ切替設定](commands/cards/55_33_00_write_antenna_switching.md)も確認し、8CH専用コマンドを送らない |

### 異常応答とタグメモリ

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| 異常応答の解析 | [NACKマスタ](RESPONSE_AND_NACK_MASTER.md)、対象カード、[既知の失敗](KNOWN_AI_FAILURE_PATTERNS.md) | エラーの値と意味、条件付き追加コード、正常結果との区別。PDF 7.6へ戻る |
| タグメモリの読取り・変更 | [Read](commands/cards/55_15_uhf_read.md)、[Write](commands/cards/55_16_uhf_write.md)を入口に[全コマンド一覧](RESPONSE_CLASSIFICATION_MATRIX.md)で実際の対象を選ぶ | Readは1～32 Word、Writeは1 Word。対象1枚・Access条件・要求との対応、PCとEPC本体を区別。Lock/Killは別途確認 |
| パスワード・Lock・Kill | [Access設定](commands/cards/55_33_03_write_access_password.md)、[Lock](commands/cards/55_18_uhf_lock.md)、[Kill](commands/cards/55_17_uhf_kill.md) | リーダライタRAMとタグ内パスワードを区別。Lockの対象・Mask/Action・恒久化、Kill用パスワードと不可逆性、読戻しできない応答 |
| 連続領域の書込み・消去 | [BlockWrite](commands/cards/55_1a_uhf_block_write.md)、[BlockWrite2](commands/cards/55_1d_uhf_block_write2.md)、[BlockErase](commands/cards/55_1b_uhf_block_erase.md) | RF側1 Wordずつ／一括、アドレスと数の幅、部分書込み、タグの消去後の値、NACK追加コード、timeout |

### RSSI・RF通信設定と複数bankへの一括要求

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| データ条件ごとにRSSIで通知を絞る | [個別RSSI読取り](commands/cards/55_49_read_rssi_filter.md)、[書込み](commands/cards/55_39_write_rssi_filter.md)、[共通RSSI](commands/cards/55_33_04_write_rf_tag_comm_params.md) | ROM 2.100以降・FLASHのみ。最初に一致したNo.の閾値で終了、全無効と全不一致、TID内部読取りと出力を区別。原典不一致はOPEN-019／020 |
| 共通RSSI・スキャン・Target切替・リトライを調べる | [RF通信設定読取り](commands/cards/55_43_04_read_rf_tag_comm_params.md)、[書込み](commands/cards/55_33_04_write_rf_tag_comm_params.md)、[モード別適用](RESPONSE_MODE_APPLICABILITY.md)、[RAM影響](RAM_FLASH_IMPACT_MATRIX.md) | 両RAM相互反映、Target切替は自動用、符号付きRSSIと個別フィルタの優先順。2種類のリトライをホスト再送と分ける |
| Encodeで複数領域を書いてLockする | [Encode](commands/cards/55_1e_uhf_encode.md)、[BlockWrite](commands/cards/55_1a_uhf_block_write.md)、[Lock](commands/cards/55_18_uhf_lock.md)、[Access設定](commands/cards/55_33_03_write_access_password.md)、[RAM影響](RAM_FLASH_IMPACT_MATRIX.md) | 4つの長さ欄と総LEN、要求順と内部順、認証・保持・部分失敗、キャリア復帰。例2の不一致とゼロ化前の認証は確認待ち |

### タグを条件で選別する

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| EPC/UII・TID・Userの条件指定 | [Select設定](commands/cards/55_30_uhf_set_select_param.md)、[読取り](commands/cards/55_40_uhf_get_select_param.md)、[Inventory設定読取り](commands/cards/55_41_uhf_get_inventory_param.md) | bitアドレス、端数byteの下位詰め、Select TargetとInventory Targetの違い、Sel／Session、マスク0とSelect使用OFFの違い |
| 複数の選別条件 | 上記に加え[拡張Select設定](commands/cards/55_32_uhf_set_expand_select_param.md)と[読取り](commands/cards/55_42_uhf_get_expand_select_param.md) | 初回・後続のActionとTarget、最初の0 bitで後続停止、固定16 byteマスク、保存先 |

### 汎用・拡張ポートの状態と出力

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| 汎用ポートの状態取得・出力変更 | [汎用ポート読取り](commands/cards/4f_9f_read_general_port.md)、[書込み](commands/cards/4e_9f_write_general_port.md)、[保存と復元](RAM_FLASH_IMPACT_MATRIX.md) | 現在値・機能・方向・起動初期値を分ける。指示マスクと対象出力条件、値なしACK後の読戻し、機種別LED条件 |
| 拡張ポートの状態取得・出力変更 | [拡張ポート読取り](commands/cards/4f_a0_read_extended_port.md)、[書込み](commands/cards/4e_a0_write_extended_port.md) | 8CH専用、機能全bit0固定、方向・初期値の機種差。対象出力だけを指示・読戻し |

### 表示と鳴動

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| ブザー音・LEDの時間制御 | [ブザー制御](commands/cards/42_buzzer_control.md)、[LED&ブザー](commands/cards/4e_57_led_buzzer_control.md)、[汎用ポート読取り](commands/cards/4f_9f_read_general_port.md) | 42hの応答要求、57hの固定ACK、ポート機能・方向、200ms単位と鳴動有無の分岐。ACKと実動作を分ける |

### FLASHの1 byte設定

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| 設定アドレスの読取り・変更 | [読取り](commands/cards/4f_b4_read_flash_settings.md)、[書込み](commands/cards/4e_b4_flash_write.md)、[保存・反映](RAM_FLASH_IMPACT_MATRIX.md) | ADRとメモリアドレス、全byte更新、予約bit、51hのRAM例外とROM条件、リスタート要件。読戻しと実動作を分ける |

### 再起動と出荷時設定への復帰

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| リスタート・FLASH初期化 | [リスタート](commands/cards/4e_9d_restart_reader.md)、[初期化](commands/cards/4e_6f_flash_initialize.md)、[RAM影響](RAM_FLASH_IMPACT_MATRIX.md)、[RF条件](RF_SAFETY_AND_CARRIER_RULES.md) | 9Dh無応答と6Fh固定ACK、待機、保存モード、旧ROMのRF、取得・復元できる範囲。ROM応答と実行証明を分ける |

### 機種・バージョン・製造番号

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| 識別と対応判定 | [ROM読取り](commands/cards/rom_version_read.md)、[チップ読取り](commands/cards/55_90_chip_version_read.md)、[機種・ROMガイド](DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md) | 制御マイコン版とチップ版、ASCII固定配置、種別、10 byteシリアル、機種とROM列の組合せ。SUM不一致は保留 |

### 装置異常とアンテナ接続の診断

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| エラー情報・接続確認 | [エラー情報](commands/cards/4f_80_read_error_info.md)、[CheckAntenna](commands/cards/55_44_uhf_check_antenna.md)、[番号体系](ANTENNA_NUMBERING_SCHEMES.md) | ACK内の異常とNACK、予約byte、機種別端子番号、RF診断と受動取得の違い、診断後状態の未確認範囲 |

### Handleを使ったカスタムタグコマンド

[GetHandle](commands/cards/55_46_uhf_get_handle.md)と[ThroughCmd](commands/cards/55_ff_uhf_through_cmd.md)を入口に、[RF制御](commands/cards/4e_9e_rf_carrier_control.md)、[Inventory](commands/cards/55_10_uhf_inventory.md)、[Select](commands/cards/55_30_uhf_set_select_param.md)と対象タグの仕様を確認します。保持値とタグ状態、bit長・CRC・任意timeout欄を分け、送信のみや受信CRC省略の未確認条件は推測で補いません。

### 設定と依頼内容

| 用途 | 最初に開く資料・カード | 確認すべきこと |
|---|---|---|
| RF・FLASH等の設定 | [RAM/FLASH影響](RAM_FLASH_IMPACT_MATRIX.md)、[RF条件](RF_SAFETY_AND_CARRIER_RULES.md)、対象カード | 変更範囲、地域・機種・ROM条件、停止、復元。値は推測しない |
| GUI等の依頼内容の整理 | [依頼文例](EXAMPLE_IMPLEMENTATION_REQUEST.md)、[既知の失敗](KNOWN_AI_FAILURE_PATTERNS.md) | 要件と実機条件を分ける。過去の制作記録を現在の仕様として流用しない |

## 3. 読み漏れと重複を防ぐ

1. 対象カードと共通資料を選ぶ。
2. 各カードの `related_docs` をすべて開き、必要な原典節を確認する。
3. 同じ作業中に既に全文を確認した同一版のファイルは、参照済み一覧で追跡する。同じファイルへ戻る循環参照のために無限に再読しない。
4. ファイルが更新された場合、内容が省略表示された場合、確認内容が保持できていない場合は再確認する。以前のセッションの記憶で代用しない。
5. 最後に、参照ファイル、PDF節、未確認項目を報告する。

資料が矛盾する場合は、注意書きの強さや多数決で決めない。[原典照合・確認待ち一覧](SOURCE_REVIEW_STATUS.md)へ記録し、原典を照合して保守者へ確認する。

`_raw.md` は元の転記を確認するための資料です。コマンドカードと二重に別コマンドとして数えず、本文の適用条件や訂正を外して使わないでください。

## 4. 他社事例の適用範囲

用途別の入口と注意点の整理は、[整備計画の参考事例](../IMPROVEMENT_PLAN.md)に基づきます。他社SDKのエラー名、番号、アンテナ体系、再接続、FLASH保存の動作をUTR仕様へ転用しないでください。
