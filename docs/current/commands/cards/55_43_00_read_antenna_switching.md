---
title: "アンテナ切替設定の読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.5"
command_group: "reader_setting"
command_name: "アンテナ切替設定の読み取り"
command_byte: "55h"
detail_command: "43h"
subcommand: "00h"
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
  - "55_33_00_write_antenna_switching.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../ANTENNA_NUMBERING_SCHEMES.md"
  - "../../RESPONSE_MODE_APPLICABILITY.md"
  - "55_33_05_write_epc_uii_params.md"
  - "55_43_05_read_epc_uii_params.md"
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "read-only"
  - "specification-reference"
  - "read-antenna-switching"
---

# アンテナ切替設定の読み取り

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **アンテナ切替設定の読み取り** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.5`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `55h` / 詳細コマンド: `43h` / サブコマンド: `00h`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

このコマンドの目的は、**アンテナ切替設定の読み取り** です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

PDF §6.2.2 p.109では読取り（55h/43h/00h）は8CH機も対応ですが、書込み（55h/33h/00h）は8CH機では非対応です。読めることから同形式で書けると判断しないでください。8CH機の制御は[使用アンテナ番号](55_38_write_active_antenna.md)と[外部アンテナ自動切替設定](55_37_write_external_antenna_auto_switch.md)の機種条件を別途確認します。

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
| パラメータ確認 | 読取り対象の種類00h/01h/02h |
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

### 適用範囲の補足（原典転記と区別）

根拠: 公式PDF Ver.1.17 §7.4.5 p.163–165、§7.4.20 p.212–216。

- 自動切替は自動読み取りモードで有効です。コマンドモードでは自動切替しません。切替方式00bは使用対象の最小番号を使用し、01bは小さい順に切り替えます。10bと11bは予約で、通知節の「複数アンテナを一つとして扱う」という説明から割り当てを推測しません。
- 書込み対象のAnt0～Ant3は使用有無のbit maskです。全て不使用、またはコマンド用RAMへ複数を使用指定するとNACKです。機種に存在しないポートが設定されない場合もあるため、要求値と読戻し値を区別します。
- RAMは種類ごとに独立します。FLASHに複数指定すると、自動読み取り用RAMには同じ選択、コマンド用RAMには最小番号の1本だけが反映されます。[RAM・FLASH影響整理](../../RAM_FLASH_IMPACT_MATRIX.md)を参照してください。
- アンテナID出力bitはタグ応答のADRに関係します。設定ACKや切替終了通知のADRを、タグ応答と同じアンテナ番号として扱わないでください。[番号体系](../../ANTENNA_NUMBERING_SCHEMES.md)と[通知の適用範囲](../../RESPONSE_MODE_APPLICABILITY.md)で区別します。

原典p.164の参照「7.4.15 アンテナ切替設定の書き込み」は、Ver.1.17では **§7.4.20** です。転記本文は保持し、[書込みカード](55_33_00_write_antenna_switching.md)へ案内します。この補足はメーカー発行の正誤表ではありません。

以下は、公式PDF `7.4.5` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.5   アンテナ切替設定の読み取り
  アンテナ切替時のパラメータを読み取るコマンドです。

  ［コマンド］
 ラベル名 バイト数                           内   容
  STX       1     02h
 アドレス       1     00h（「5.2 通信フォーマットの詳細」参照）
 コマンド       1     55h
 データ長       1     03h
            1     43h（詳細コマンド）
            1     00h（詳細サブコマンド）
                  パラメータ種類 ※1
 データ部
                    00h  ：コマンドモード用パラメータ
            1
                    01h  ：自動読み取りモード用パラメータ
                    02h  ：FLASH データ
   ETX      1     03h
   SUM      1     SUM 値（「5.3 SUM の計算方法」参照）
    CR      1     0Dh
  ※1：パラメータ種類の詳細は「3.12.1 パラメータ種類」をご参照ください。


 ［ACK レスポンス］
ラベル名 バイト数                                内   容
 STX        1    02h
アドレス        1    00h（「5.2 通信フォーマットの詳細」参照）
コマンド        1    30h（ACK）
データ長        1    08h
            1    43h（詳細コマンド）
            1    00h（詳細サブコマンド）
                 パラメータ種類
                   00h  ：コマンドモード用パラメータ
            1
                   01h  ：自動読み取りモード用パラメータ
                  02h       ：FLASH データ
                 ビット       内容  ［初期値：80h］
                           アンテナ切替方式 ※左側が上位 bit
                           00    ：制御しない ［初期値］
                 bit0
                           01    ：制御する
                 bit1
                           10    ：将来拡張のための予約
            1              11    ：将来拡張のための予約
                 bit2-6    将来拡張のための予約（通常は 0）
                           アンテナ ID の出力
                 bit7      0     ：無効
データ部                       1     ：有効 ［初期値］
                 ビット       アンテナ切替設定 ［初期値：01h］
                        Ant0
                 bit0   0    ：使用しない
                        1    ：使用する  ［初期値］
                        Ant1
                 bit1   0    ：使用しない ［初期値］
                        1    ：使用する
            1
                        Ant2
                 bit2   0    ：使用しない ［初期値］
                        1    ：使用する
                        Ant3
                 bit3   0    ：使用しない ［初期値］
                        1    ：使用する
                 bit4-7 将来拡張のための予約（通常は 0）
            3    将来拡張のための予約（通常は 00h）
 ETX        1    03h
 SUM        1    SUM 値（「5.3 SUM の計算方法」参照）
  CR        1    0Dh
※取得した値の説明は、「7.4.15 アンテナ切替設定の書き込み」をご参照ください。


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
    • コマンド
       02 00 55 03 43 00 00 03 A0 0D
    • レスポンス
       02 00 30 08 43 00 00 80 01 00 00 00 03 01 0D

       バイト位置           レスポンス                          パラメータ
         3 [byte]目      [30]h          ・ACK 応答
         4 [byte]目      [08]h          ・データ長 = 8
         5 [byte]目      [43]h          ・詳細コマンド=[43]h, 詳細サブコマンド=[00]h
         6 [byte]目      [00]h           [アンテナ切替設定の読み取り]コマンド
         7 [byte]目      [00]h          ・パラメータ種類=[コマンドモード用パラメータ]
                                       ・アンテナ切替方式=[制御しない]
          8 [byte]目       [80]h
                                       ・アンテナ ID 出力=[有効]
                                       ・Ant0=[使用する] , Ant1=[使用しない]
          9 [byte]目       [01]h
                                        Ant2=[使用しない], Ant3=[使用しない]
    10～12 [byte]目      [00 00 00]h     ・将来拡張のための予約
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. レスポンス処理

レスポンス処理では、以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- 複数レスポンス
- 完了レスポンス
- LBTエラー
- アンテナ関連エラー
- UHF ICエラー

NACKは共通NACK形式とPDF該当節を併せて確認してください。予約バイトは、PDFで意味が定義されていない限り、独自解釈しないでください。

ACK、後続レスポンス、可変長データの解釈は、対象コマンドのPDF定義と機種・ROM・設定に基づきます。[応答マスタ](../../RESPONSE_AND_NACK_MASTER.md)と[モード別適用範囲](../../RESPONSE_MODE_APPLICABILITY.md)を確認し、TID付加や自動読み取り用の通知設定を、すべてのコマンドACKへ一般化しないでください。

### 8.1 ACK/レスポンス例（読み取り成功時）

| 項目 | 内容 |
|---|---|
| ACK構造 | `02 ADR 30 08 43 00 PARAM_KIND SWITCH_MODE ANT_ENABLE RESERVED[3] 03 SUM 0D` |
| `LEN` | `08h` 固定 |
| `DATA[0]` | `43h`: 詳細コマンド |
| `DATA[1]` | `00h`: 詳細サブコマンド、アンテナ切替設定の読み取り |
| `DATA[2]` | パラメータ種類。`00h`=コマンドモード、`01h`=自動読み取りモード、`02h`=FLASHデータ |
| `DATA[3]` | アンテナ切替方式、アンテナID出力、予約bit |
| `DATA[4]` | Ant0〜Ant3の使用有無bit |
| `DATA[5..7]` | 予約領域。通常 `00 00 00` |

実装では `CMD=30h`、`LEN=08h`、`DATA[0]=43h`、`DATA[1]=00h` と要求したパラメータ種類の一致を確認します。切替終了通知や別設定のACKと混同しません。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 43 44 00 00 00 00 00 00 00 00 03 C7 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。


### 8.4 AI実装用レスポンス定義

この節は、生成AIや実装者がACK/レスポンス処理を固定文言ではなく、byte位置と設定依存で実装するための機械可読寄りの整理です。公式PDFの該当節を一次情報とし、この表は実装時のチェックリストとして使ってください。

#### 共通フレームoffset

| offset | フィールド | 実装上の意味 |
|---:|---|---|
| 0 | `STX` | 常に `02h`。異なる場合は `INVALID_FRAME` |
| 1 | `ADR` | 通常はリーダライタID。RFタグ応答でアンテナID出力ONの場合は読み取りANT番号 |
| 2 | `CMD` | `30h`=ACK、`31h`=NACK、`6Ch`=RFタグデータ、その他はPDF該当節で分類 |
| 3 | `LEN` | `DATA`部のbyte数。総フレーム長は `LEN + 7` |
| 4..`4+LEN-1` | `DATA` | ACK/NACK/タグ応答ごとの可変領域 |
| `4+LEN` | `ETX` | 常に `03h`。異なる場合は `INVALID_FRAME` |
| `5+LEN` | `SUM` | `STX`から`ETX`までのSUM下位1byte |
| `6+LEN` | `CR` | 常に `0Dh` |

#### 受信分類ルール

| 条件 | 分類 | 実装アクション |
|---|---|---|
| フレーム長不一致、`STX/ETX/CR/SUM`不正 | `INVALID_FRAME` | 破棄し、必要なら再同期する |
| 受信期限内に対象要求の応答を確認できない | `TIMEOUT` | timeoutとして処理し、NACKとは分ける |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む |
| `CMD=30h`、`LEN=08h`、`DATA[0]=43h`、`DATA[1]=00h`、`DATA[2]`が要求した種類と一致 | `ACK` | 対象の設定要求への応答。切替終了通知とは別 |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `55h` / 詳細 `43h` / サブ `00h`。


#### ACK/データ部offset

`CMD=30h`、`LEN=08h`、`DATA[0]=43h`、`DATA[1]=00h`、`DATA[2]`が要求した種類と一致することを確認します。DATAは8byte固定で、通知設定やアンテナID出力設定によって長さを変えません。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `43h` |
| 1 | `sub` | `00h` |
| 2 | `parameter_kind` | 要求した00h/01h/02h。状態コードではない |
| 3 | `parameter_1` | bit0–1切替方式、bit2–6予約、bit7アンテナID出力 |
| 4 | `antenna_mask` | bit0–3がAnt0～Ant3の使用有無、bit4–7予約 |
| 5..7 | `reserved` | 通常00h。独自の意味を与えない |

読んだ種類と値を対応づけて保存します。読取り結果をそのまま別の種類へ書き戻したり、8CH機への書込みに転用したりしないでください。

切替終了通知は連続モード用のLEN=02h、DATA=[10h,01h]または[14h,01h]です。本設定のACKや継続受信全体の終了とは区別します。[通知の識別条件](../../RESPONSE_MODE_APPLICABILITY.md)を参照してください。

#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 43h 00h` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR、LBT_ERROR、ANTENNA_ERROR、UHF_IC_ERRORなどの主エラー |
| 2 | `error_code_2` | `error_code_1=0Ah` のUHF ICエラー時に参照 |
| 3 | `error_code_3` | UHF_Encode / UHF_BlockWrite2 等でPDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 判定手順（文書上の仕様）

1. フレーム長、区切り、SUMを確認してからDATAにアクセスする。
2. CMDでNACKとACKを分類し、対象要求との対応を確認する。
3. 設定ACKは上記LEN・詳細・サブ・要求した種類を全て照合する。
4. 切替終了通知やタグ応答は別イベントとして扱い、設定要求への成功応答に代用しない。
5. 対象応答が期限までに得られなければ未完了とする。読取りだけを契機に自動で設定を書き戻さない。

#### 推奨パーサ出力

```json
{
  "frame_type": "ACK | NACK | RF_TAG_DATA | COMPLETION | ANT_SWITCH_COMPLETE | CARRIER_DETECTED | NO_RESPONSE | TIMEOUT | INVALID_FRAME",
  "command": "対象コマンド名",
  "address_role": "reader_id | antenna_id | unknown",
  "detail": "PDFで定義された詳細コマンドまたは応答種別",
  "data_length": 0,
  "settings_snapshot_used": true,
  "is_success": false,
  "error": null,
  "raw_hex_policy": "PDF掲載例は可。実機ログ由来のEPC/UII/TID/パスワードはマスク"
}
```

#### この要求で保持する情報

機種・ROM、接続先、要求識別子、パラメータ種類、受信期限を保持します。この設定を読む前に同じ設定の取得を必須とする循環した依存関係を作らないでください。固定長の設定ACKを読むためにTID付加や全通知設定を要求しません。並行する自動読み取りの通知条件は、通知側で別に管理します。

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

- [55_33_00_write_antenna_switching.md](55_33_00_write_antenna_switching.md)
- [RAM_FLASH_IMPACT_MATRIX.md](../../RAM_FLASH_IMPACT_MATRIX.md)
- [ANTENNA_NUMBERING_SCHEMES.md](../../ANTENNA_NUMBERING_SCHEMES.md)
- [RESPONSE_MODE_APPLICABILITY.md](../../RESPONSE_MODE_APPLICABILITY.md)
- [55_33_05_write_epc_uii_params.md](55_33_05_write_epc_uii_params.md)
- [55_43_05_read_epc_uii_params.md](55_43_05_read_epc_uii_params.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。