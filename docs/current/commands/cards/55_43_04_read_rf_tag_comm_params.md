---
title: "RFタグ通信関連パラメータの読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.8"
command_group: "reader_setting"
command_name: "RFタグ通信関連パラメータの読み取り"
command_byte: "55h"
detail_command: "43h"
subcommand: "04h"
operation_profile: "read-only"
operation_level: "read-only"
rf_emission: false
write_operation: false
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
requires_tag: false
requires_access_password: false
requires_parameters: true
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "55_33_04_write_rf_tag_comm_params.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../RESPONSE_MODE_APPLICABILITY.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "55_33_02_write_frequency.md"
  - "55_43_02_read_frequency.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_30_uhf_set_select_param.md"
  - "55_39_write_rssi_filter.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "read-only"
  - "specification-reference"
  - "read-rf-tag-comm-params"
---

# RFタグ通信関連パラメータの読み取り

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **RFタグ通信関連パラメータの読み取り** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.8`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `55h` / 詳細コマンド: `43h` / サブコマンド: `04h`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

このコマンドの目的は、**RFタグ通信関連パラメータの読み取り** です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 書き込み操作 | なし |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | なし |
| タグ条件確認 | なし |
| Accessパスワード確認 | なし |
| パラメータ確認 | あり（読取り種類） |
| 明示許可 | 不要または通常不要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 読み取り専用か、設定変更か、タグメモリ操作かを分類する。
4. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。
5. 周波数、送信出力、アンテナ設定、FLASH、タグメモリに影響する場合は、事前承認を取る。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.4.8` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.8   RF タグ通信関連パラメータの読み取り
  RF タグの通信関連パラメータを読み取るコマンドです。

  ［コマンド］
 ラベル名 バイト数                          内   容
  STX        1    02h
 アドレス        1    00h（「5.2 通信フォーマットの詳細」参照）
 コマンド        1    55h
 データ長        1    03h
             1    43h（詳細コマンド）
             1    04h（詳細サブコマンド）
                  パラメータ種類 ※1
 データ部
                    00h  ：コマンドモード用パラメータ
             1
                    01h  ：自動読み取りモード用パラメータ
                    02h  ：FLASH データ
   ETX       1    03h
   SUM       1    SUM 値（「5.3 SUM の計算方法」参照）
    CR       1    0Dh
  ※1：パラメータ種類の詳細は「3.12.1 パラメータ種類」をご参照ください。


 ［ACK レスポンス］
ラベル名 バイト数                                       内   容
 STX         1      02h
アドレス         1      00h（「5.2 通信フォーマットの詳細」参照）
コマンド         1      30h（ACK）
データ長         1      06h
             1      43h（詳細コマンド）
             1      04h（詳細サブコマンド）
                    パラメータ種類
                      00h      ：コマンドモード用パラメータ
             1
                      01h      ：自動読み取りモード用パラメータ
                      02h      ：FLASH データ
                    パラメータ 1 ［初期値：18h］
                    ビット     内容
                    bit0    将来拡張のための予約（通常は 0）
                            RSSI フィルタ
                    bit1    0         ：使用しない ［初期値］
                            1         ：使用する
データ部                        周波数のスキャンモード ※左側が上位 bit
             1              00        ：指定周波数固定
                    bit2-3  01        ：周波数ホッピング
                            10        ：キャリアセンス優先 ［初期値］
                            11        ：将来拡張のための予約
                            Inventory の Target A/B 自動切替
                    bit4    0         ：無効
                            1         ：有効 ［初期値］
                    bit5-7  将来拡張のための予約（通常は 0）
                    RSSI 値 ［初期値：[BF]h(-65)］
             1
                      ※RSSI の閾値（符号付き 8 ビット整数）
                    bit0-3 インベントリ処理のリトライ回数［初期値：0］
             1
                    bit4-7 リードライト処理のリトライ回数［初期値：0］
 ETX         1      03h
 SUM         1      SUM 値（「5.3 SUM の計算方法」参照）
  CR         1      0Dh
※取得した値の説明は、「7.4.22 RF タグ通信関連パラメータの書き込み」をご参照ください。


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
   • コマンド
      02 00 55 03 43 04 00 03 A4 0D
    • レスポンス
       02 00 30 06 43 04 00 18 BF 00 03 59 0D
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答と解釈の補足

### 8.1 種類を指定して読む固定長ACK

根拠: §7.4.8 p.171–172。要求はCMD=55h・LEN=03h、DATAは43h、04h、PARAM_KINDの3 byte、総10 byteです。PARAM_KINDは00h=コマンド用RAM、01h=自動用RAM、02h=FLASHで、読取りにも指定が必要です。

| 読取りACKの位置 | 内容 |
|---|---|
| CMD／LEN | 30h／06h。総13 byte |
| DATA[0]／[1] | 43h／04h |
| DATA[2] | PARAM_KIND。要求した種類と照合 |
| DATA[3] | PARAM1 |
| DATA[4] | RSSI閾値 |
| DATA[5] | RETRY |

共通フレームの長さ・STX／ETX／CR／SUMを検証後、CMD・LEN・詳細・サブ・種類を揃えて要求へ対応づけます。詳細43hだけで別の設定ACKを成功扱いにしません。このACKのADRはリーダライタIDであり、タグ応答のアンテナ番号ではありません。TIDや通知設定でACK長を増やしません。

p.172末尾の「7.4.22 RFタグ通信関連パラメータの書き込み」は参照番号の不一致です。実際の説明は[§7.4.24 p.228–232](55_33_04_write_rf_tag_comm_params.md)です。第6節の原典転記は保持し、[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)へ記録しています。

### 8.2 パラメータ3 byteの意味

根拠: §7.4.8 p.172、§7.4.24 p.228–232。読取りACKと書込み要求では、DATA[3..5]の配置が同じです。

| フィールド | 位置・意味 | 初期値 |
|---|---|---|
| PARAM1 bit0、bit5–7 | 予約。通常0。未定義の機能を割り当てない | 0 |
| PARAM1 bit1 | 共通RSSIフィルタ: 0=使用しない、1=使用する | 0 |
| PARAM1 bit3:bit2 | 左が上位bit。00=指定周波数固定、01=周波数ホッピング、10=キャリアセンス優先、11=予約 | 10b |
| PARAM1 bit4 | Inventory Target A/B自動切替: 0=無効、1=有効。機能は自動読み取り用 | 1 |
| RSSI | 符号付き8 bit閾値、-128～127 | BFh（-65） |
| RETRY bit0–3 | インベントリ処理のリトライ回数、0～15 | 0 |
| RETRY bit4–7 | リードライト処理のリトライ回数、0～15 | 0 |

PARAM1の初期値18hは、フィルタOFF・スキャン10b・Target切替ONです。RETRY=12hはInventoryが2、Read/Writeが1で、逆ではありません。RSSIの符号変換は、受信byteが128未満ならその値、128以上なら256を引きます。BFhを191として比較しません。

### 8.3 保存先と機能の適用を分ける

§3.12 p.71–74では、この設定は両RAMへ相互反映します。00h／01hのどちらを書いてもコマンド用・自動用RAMが同じ設定となり、FLASHは変更しません。02hはFLASHと両RAMへ直ちに反映します。起動・リスタート時もFLASHから両RAMへコピーされます。

同じ値が保存されることは、全機能が両モードで有効なことを意味しません。Target A/B自動切替は自動読み取りモード限定（§3.8 p.58）。コマンドモードではbit4を有効にしていても、Inventoryの設定Targetを使います。[RAM影響](../../RAM_FLASH_IMPACT_MATRIX.md)と[モード別適用範囲](../../RESPONSE_MODE_APPLICABILITY.md)も確認します。

### 8.4 共通RSSIフィルタの対象と境界

§7.4.24 p.229の対象は、コマンドモードのUHF_Inventory／UHF_InventoryReadと、UHF連続インベントリ／UHF連続インベントリリードです。有効時、タグRSSIが閾値より小さい場合に上位機器へのタグ読取りレスポンスを抑制します。閾値-65なら-66は抑制、-65と-64はこの段階を通過します。

RFタグとの交信自体を禁止する機能や、Select・Accessによる対象保護ではありません。受信データがないだけで物理的なタグ0枚と判定せず、Write等の全ACKへ適用しません。p.229のRSSIのおおよその観測範囲-70～-20は、設定可能範囲や距離保証ではありません。マルチパスや使用周波数でも変わります。

### 8.5 個別RSSIフィルタとの関係

§7.4.30 p.249–250では、共通設定と[個別RSSIフィルタ](55_39_write_rssi_filter.md)は独立で、共通を先に判定します。共通で抑制されたデータを個別条件で復活させません。共通を通過しても、有効な個別条件の判定が続くため、必ず上位へ返るとは限りません。

個別設定の対象はInventoryRead／連続インベントリリードで、Inventory／連続インベントリとは異なります。個別のNo.1～10・比較条件・不一致データの扱い・FLASH保存は別カードで確認し、この3 byteへ詰め込みません。個別の構造・判定順は別カードの部分照合へ進みました。閾値表現と等号の不一致は[OPEN-019／020](../../SOURCE_REVIEW_STATUS.md)で確認中です。

### 8.6 読取り結果の限界と異常系

このACKは保存設定を返します。RSSI欄は現在読んだタグのRSSI測定値ではなく閾値、RETRY欄は実際に発生したリトライ回数ではなく設定値です。スキャン・Target・リトライの動作条件は[書込みカード](55_33_04_write_rf_tag_comm_params.md)の8.6～8.8も確認してください。

CMD=31hは[共通NACK](../../RESPONSE_AND_NACK_MASTER.md)として扱い、設定値を解析しません。Encode等の追加コードをこの設定応答に転用しません。ホストの受信期限切れ、壊れたフレーム、別要求のACK、非同期タグ通知をそれぞれ分け、予約値へ独自の機能名を与えません。

変更準備では種類ごとの値を記録し、読取り結果をそのまま自動書込みしません。全機種・ROMの適用条件と各NACK発生条件の網羅照合、実機確認は未実施です。

## 9. 実機確認

実機確認区分: `read-only`

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

- `55_33_04_write_rf_tag_comm_params.md`
- `../../RAM_FLASH_IMPACT_MATRIX.md`
- `../../RESPONSE_MODE_APPLICABILITY.md`
- `../../SOURCE_REVIEW_STATUS.md`
- `55_33_02_write_frequency.md`
- `55_43_02_read_frequency.md`
- `55_31_uhf_set_inventory_param.md`
- `55_30_uhf_set_select_param.md`
- `55_39_write_rssi_filter.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
