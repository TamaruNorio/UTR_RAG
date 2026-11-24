---
title: "UHF_ThroughCmd"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.11"
command_group: "rf_tag_communication"
command_name: "UHF_ThroughCmd"
command_byte: "55h"
detail_command: "FFh"
subcommand: null
operation_profile: "tag-memory-or-high-impact"
operation_level: "tag command dependent"
rf_emission: true
write_operation: true
flash_operation: false
tag_memory_operation: true
requires_rom_check: true
requires_antenna: true
requires_tag: true
requires_access_password: true
requires_parameters: true
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "4e_9e_rf_carrier_control.md"
  - "55_10_uhf_inventory.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_30_uhf_set_select_param.md"
  - "4e_00_10_write_reader_mode.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "55_46_uhf_get_handle.md"
  - "55_ff_uhf_through_cmd_raw.md"
  - "55_33_03_write_access_password.md"
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
tags:
  - "utr-s201"
  - "command-card"
  - "rf-tag-communication"
  - "rf-emission"
  - "tag-memory"
  - "requires-antenna"
  - "requires-tag"
  - "specification-reference"
  - "uhf-through-cmd"
---

# UHF_ThroughCmd（高度なタグ直接コマンド）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_ThroughCmd** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.11`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: 送信するタグコマンドに依存
- コマンドバイト: `55h` / 詳細コマンド: `FFh` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

ホストが組み立てたタグコマンドのbit列をRFタグへ送り、受信bit列をホストへ返します（p.306）。タグのデータシートまたはISO/IEC 18000-63に従う生成・解析が必要です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

p.110の機種別対応表では、UTR-S201・UTR-SHR201・UTR-SUN02-4CHはROM 2.040以前が非対応、2.050以降／2.100以降が対応です。UTR-SUN02-8CH・UTR-SUN02V-8CHは「全バージョン」列が対応です。複数列に該当する場合は最も右の列を使用し、4CHを8CHの列へ含めません。未掲載ROMの空白範囲は推測で埋めません。

両コマンドともp.19–20の連続モード65h／66h中の受付例外ではありません。[モード書込み](4e_00_10_write_reader_mode.md)で00hへ戻す条件を確認します。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | あり |
| 書き込み操作 | 送信内容による。BlockWrite等も実行可能 |
| FLASH操作 | なし |
| タグメモリ操作 | あり |
| ROM確認 | あり |
| アンテナ条件確認 | あり |
| タグ条件確認 | あり |
| Accessパスワード確認 | 送信するタグコマンドの認証条件を確認 |
| パラメータ確認 | あり |
| 明示許可 | 必要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

メタデータwrite_operation=true・requires_access_password=trueは、透過先の書込み・認証条件を確認するための保守的分類です。すべての要求が書込み、または常に非ゼロパスワード必須という意味ではありません。bit0–2のリード／ライト指定だけで送信内容の影響を判定しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 読み取り専用か、設定変更か、タグメモリ操作かを分類する。
4. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。
5. 周波数、送信出力、アンテナ設定、FLASH、タグメモリに影響する場合は、事前承認を取る。

## 6. PDF仕様フィールド定義

原典転記は[raw資料](55_ff_uhf_through_cmd_raw.md)を参照してください。既存のマスクを含めて保持しています。p.308–309のSUM参照「5.4」は、実際の§5.3 p.100へ読み替えて参照します。
このカードには、実装判断に必要な要点とAI向け構造化情報のみを残します。

## 7. 要求の構造（p.307–308）

CMD=55hです。以下はDATA内の0起点offsetで、kは種別7なら2、それ以外は0です。nはホストが渡すタグコマンドのbyte数です。

| DATA offset | 内容 |
|---:|---|
| 0 | FFh |
| 1 | 動作パラメータ |
| 2–3 | 受信bit長。上位byte先 |
| 4–5（種別7のみ） | 受信待ち時間、1～20ms、上位byte先 |
| 4+k～5+k | 送信bit長。掲載例は上位byte先 |
| 6+k以降 | タグへの送信データn byte |

フィールドから求めるLENは6+k+n、総フレーム長はLEN+7です。p.308のnは1～247で、種別7以外なら249まで空くという計算だけで上限を拡張しません。送信bit長の0指定や上限の細条件は未確認です。

### 7.1 動作パラメータのbit割当

| bit | 0／1または列挙値の意味 |
|---|---|
| 0–2 | 0=送信のみ、1=リード系、2=ライト系、7=受信待ち時間指定。他は予約 |
| 3 | 0=受信ゲインアップ無効、1=有効（ライト系で推奨） |
| 4 | 0=Handle自動付加、1=付加しない |
| 5 | 0=受信CRCをホスト応答へ付加、1=付加しない |
| 6 | 0=リーダで受信CRCをチェック、1=チェックしない |
| 7 | 0=送信CRCを付加しない、1=付加する |

Handle・受信CRCのbitは0で有効です。bit5、6、7を同じCRC有効フラグへまとめません。UART/TCPフレームのSUMとタグ無線側のCRCも別です。

### 7.2 bit長と自動付加

受信bit長はHeaderからCRCまでの全長1～2008 bitで、送信のみの場合は0000hです。送信bit長には自動付加するHandle16 bit・CRC16 bitを含めません。ホストが送る有効bitを上位側から詰め、端数は最終byteの上位側に置きます。

Handle自動付加時はリーダの保持値をデータの後へ付加します。送信CRCを付ける場合はその後でCRCを計算・付加し、Handle自動付加も有効ならCRC計算にHandleを含めます。両方自動ならRF上の順序は「指定bit列→Handle→CRC」です。ホスト側のbyte埋めと有効bit数を混同しません。

### 7.3 タイムアウト

種別1はFLASH 93（5Dh）のReadタイムアウト、種別2は91（5Bh）のWriteタイムアウトを使います。種別7だけ要求内に1～20msの2 byteを挿入します。他種別で00 00を予約として残すと、後続offsetがずれます。

これらはタグ応答待ちの指定であり、USB/COM・LAN/TCP全体のホスト受信期限ではありません。RF制御の休止・キャリアセンスと通信遅延を分けます。本要求にFLASH書換え指定はありません。

## 8. ACKのbit列・タグ処理・復旧

### 8.1 受信データを含むACK（p.309）

| ACK DATA offset | 内容 |
|---:|---|
| 0 | FFh |
| 1 | 要求の動作パラメータのエコー |
| 2–3 | 受信bit長。掲載例は上位byte先 |
| 4以降 | 受信データ1～251 byte、有効bitは上位詰め |

受信データを含む表のフィールド合計はLEN=4+n（5～255）、総長LEN+7です。LEN=01h・FFhだけの固定成功ACKとして扱いません。bit5=0の掲載例ではn=ceil(受信bit長/8)で、余った下位bitは解析対象外です。下位bitがすべて0とは一般化しません。

先頭Headerが1 bitである応答では、そのbitを先に解釈して後続フィールドを解析します。単に全応答を1 bitシフトして成功とせず、コマンド固有の成功・エラー形式をタグ仕様で確認します。リーダACKとタグ処理の成功を同一視しません。

### 8.2 掲載例で確認できる長さ

| 例 | 送信bit／byte数 | 受信bit／byte数 | TX LEN／ACK LEN |
|---|---|---|---|
| Read、p.310–311 | 26／4 | 49／7 | 0Ah／0Bh |
| BlockWrite、p.312–313 | 42／6 | 33／5 | 0Ch／09h |
| M730 Margin Read、p.314–315 | 130／17 | 33／5 | 17h／09h |

いずれもHandleと送信CRCが自動付加、受信CRCを含む例です。Readの49 bitはHeader1+データ16+Handle16+CRC16です。33 bit応答はHeader1+Handle16+CRC16で、受信byteの先頭からWordとして読めません。Margin Readの例は通常Readのような96 bitのメモリ内容を返す例ではなく、他のチップへ一般化しません。

rawのマスク済み列と掲載SUMを組み合わせて送信しません。原典掲載例の長さ・SUM照合と、カスタムタグ仕様・実機での動作確認は別です。

### 8.3 必須の準備と認証

p.306はタグがOpen／Securedの場合に使用可能とし、キャリアON後、Q自動UP/DOWNなし・開始／最小／最大Q=0のInventoryを必須としています。複数タグから1枚を扱う場合はSelect実行の設定も必要です。[GetHandle](55_46_uhf_get_handle.md)はHandleを手動で含める場合などに取得し、自動付加なら省略できます。前段のInventoryまで省略できるという意味ではありません。

透過コマンドがSelect・Query・Accessを自動で一通り実行すると仮定しません。p.226の[Access設定](55_33_03_write_access_password.md)による自動Access発行対象にはThroughCmdは列挙されていません。非ゼロ値をリーダに設定しただけでSecuredや認証成功を保証せず、透過先コマンドの状態・認証・書込み条件を確認します。

### 8.4 NACK・停止・再試行

CMD=31hは[共通NACK](../../RESPONSE_AND_NACK_MASTER.md)へ渡し、タグ応答のHeaderやエラーbit列と別に扱います。Inventory用のTID付加・アンテナID・完了通知をThroughCmdのACKへ流用しません。

処理終了後は直ちに[キャリアOFF](4e_9e_rf_carrier_control.md)が推奨です（p.306）。出力開始から最大4秒、OFFやタグ読み書きNACK等によるHandle破棄を考慮し、自動付加をHandle再取得とみなしません。NACK・timeout後はタグ処理の未実行やRF OFFを断定せず、書込みを含む要求をそのまま再送しません。新しい対象選択・Handle取得・結果確認を含む復旧条件が必要です。

### 8.5 保留している応答条件

[OPEN-027](../../SOURCE_REVIEW_STATUS.md): p.308は種別0で受信bit長0を要求しますが、p.309は受信bit長1～2008、受信データ1～251とし、送信のみの場合のACK構造・応答有無を明示しません。同表のLEN欄1～255とフィールド合計5～255の違いも含め、空ACKや正常無応答を推測で確定しません。

[OPEN-028](../../SOURCE_REVIEW_STATUS.md): bit5=1で受信CRCをホストへ返さない場合、返却bit長がCRC分を含むか減るか、短くなるpayloadとの対応が不明です。要求bit長はp.308のHeader～CRCの定義を保持し、返却bit長から無条件に16を引く規則を追加しません。

送信bit長の許容範囲・未取得Handle時の応答・受信CRC不一致やタグエラーの全経路、全機種ROM・カスタムチップの挙動は未確認です。これらの不明点を一般的なNACK値や正常0件へ置き換えません。

## 9. 実機確認

実機確認区分: `tag-memory-or-high-impact`

実機確認では、以下をログに残してください。

- 実行日時
- 操作者
- 対象機種
- ROMバージョン
- 接続方式
- 対象コマンド
- パラメータ
- 送信目的
- ACK/NACK/timeout
- エラーコード
- 復旧判断
- 結果状態

runtime logs、実CSVログ、顧客情報、実IPアドレス、raw EPC / UII / TID は GitHub にアップロードしないでください。必要な場合はマスク・要約して記録してください。

## 10. AIに実装・移植を依頼するときの注意

AIへ依頼するときは、次の前提を明示してください。

- 対象機種とROMバージョン
- 接続方式
- 実装言語
- このコマンドカード
- 関連ドキュメント
- 実機送信の有無
- 許可する操作範囲
- 禁止する操作範囲
- テスト方法
- 完了条件

実装言語は限定しません。Python、C#、C++、JavaScriptなど、対象環境に合わせて選択してください。

## 11. 参照ドキュメント

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

- `4e_9e_rf_carrier_control.md`
- `55_10_uhf_inventory.md`
- `55_31_uhf_set_inventory_param.md`
- `55_30_uhf_set_select_param.md`
- `4e_00_10_write_reader_mode.md`
- `../../SOURCE_REVIEW_STATUS.md`
- `55_46_uhf_get_handle.md`
- `55_ff_uhf_through_cmd_raw.md`
- `55_33_03_write_access_password.md`
- `../../RF_SAFETY_AND_CARRIER_RULES.md`
- `../../RAM_FLASH_IMPACT_MATRIX.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
