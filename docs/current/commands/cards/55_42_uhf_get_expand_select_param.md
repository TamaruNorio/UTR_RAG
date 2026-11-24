---
title: "UHF_GetExpandSelectParam"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.4"
command_group: "reader_setting"
command_name: "UHF_GetExpandSelectParam"
command_byte: "55h"
detail_command: "42h"
subcommand: null
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
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "55_32_uhf_set_expand_select_param.md"
  - "55_30_uhf_set_select_param.md"
  - "55_40_uhf_get_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_41_uhf_get_inventory_param.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "read-only"
  - "specification-reference"
  - "uhf-get-expand-select-param"
---

# UHF_GetExpandSelectParam（拡張Select条件読み取り）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_GetExpandSelectParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.4`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `55h` / 詳細コマンド: `42h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

このコマンドの目的は、**UHF_GetExpandSelectParam** です。

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
| パラメータ確認 | あり（種類・取得数n） |
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

以下は、公式PDF `7.4.4` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

<a id="expand-response-correction"></a>

保守者訂正（2026-09-09）: p.162のSelect2のマスクbit数は **[60]h（96 bit）** が正しい表記です。以下の原典転記には訂正前の表記を保持しています。

```text
7.4.4   UHF_GetExpandSelectParam
  2回目以降のSelectコマンド用のパラメータ値の取得をおこなうコマンドです。

［コマンド］
 ラベル名 バイト数                               内   容
  STX          1    02h
 アドレス          1    00h（「5.2 通信フォーマットの詳細」参照）
 コマンド          1    55h
 データ長          1    03h
               1    42h（詳細コマンド）
                    パラメータ種類 ※1
                      00h  ：コマンドモード用パラメータ
 データ部          1
                      01h  ：自動読み取りモード用パラメータ
                      02h  ：FLASH データ
               1    n：取得するマスクデータ数(1～7)
   ETX         1    03h
   SUM         1    SUM 値（「5.3 SUM の計算方法」参照）
    CR         1    0Dh
  ※1：パラメータ種類の詳細は「3.12.1 パラメータ種類」をご参照ください。


 ［ACK レスポンス］
ラベル名    バイト数                                       内   容
 STX           1        02h
アドレス           1        00h（「5.2 通信フォーマットの詳細」参照）
コマンド           1        30h（ACK）
データ長           1         23*n +2
               1         42h（詳細コマンド）
                         パラメータ種類
                           00h      ：コマンドモード用パラメータ
               1
                           01h      ：自動読み取りモード用パラメータ
                           02h      ：FLASH データ
                         [コマンド]で指定した [取得するマスクデータ数] 回繰り返します
                         パラメータ 1 ［初期値：85h］
                                 MemBank ※左側が上位 bit
                                 00        ：RFU
                         bit0
                                 01        ：EPC(UII) ［初期値］
                         bit1
                                 10        ：TID
                                 11        ：User
                                 Action 値 ［初期値：001(1)］
                         bit2-4
                                   詳細はパラメータ説明参照
                   1             Select の Target 値 ※左側が上位 bit
                                 000       ：Inventoried(S0)
                                 001       ：Inventoried(S1)
データ部                             010       ：Inventoried(S2)
                         bit5-7  011       ：Inventoried(S3)
         23                      100       ：SL ［初期値］
          ×                      101       ：Reserved
         (n)                     110       ：Reserved
                                 111       ：Reserved
                         パラメータ 2 ［初期値: 00h］
                         bit0-1  将来拡張のための予約（通常は 0）
                                 Truncate 値（0 固定）
                   1
                         bit2    0         ：Disable ［初期値］
                                 1         ：Enable （未サポート）
                         bit3-7  将来拡張のための予約（通常は 0）
                         マスク開始ビットアドレス ［初期値：[00 00 00 00]h］
                   4
                         ※MSB ファースト、ビット単位で指定
                         マスク bit 数 ［初期値: 00h］
                   1
                         ※最大 128[bit] ([80]h) まで
                         マスクデータ ※16[byte]固定
                   16
                        ［初期値：[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]h］
 ETX           1        03h
 SUM           1        SUM 値（「5.3 SUM の計算方法」参照）
  CR           1        0Dh
※取得した値の説明は、「7.4.14 UHF_SetExpandSelectParam」をご参照ください。


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
       • コマンド
          02 00 55 03 42 01 07 03 A7 0D
                            n
                01h: 自動読み取りモード用パラメータ
                07h: 取得するマスクデータ数 n=7
       • レスポンス
         02 00 30 A3 42 01
         85 00 00 00 00 20 60 E2 00 68 0A 00 00 40 02 3C 25 49 18 00 00 00 00
         85 00 00 00 00 20 60 E2 00 68 0A 00 00 40 02 3C 24 D1 17 00 00 00 00
         85 00 00 00 00 20 60 E2 00 68 0A 00 00 40 02 3C 24 E5 17 00 00 00 00
         85 00 00 00 00 20 60 E2 00 68 0A 00 00 40 02 3C 25 51 18 00 00 00 00
         85 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
         85 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
         85 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
         03 46 0D

```

### 拡張Select読取りの原典例：Select2・3

<a id="expand-response-1"></a>

p.162、種類01h・取得数7の同じ例。各枠のマスクは0 bitでも16 byte固定。列はP1/P2・開始bit位置・bit数・マスク。[表2](#expand-response-2) / [表3](#expand-response-3) / [表4](#expand-response-4)。Select2の[60]]hは[確定訂正](#expand-response-correction)を併読。

```text
  •      レスポンスの内容
                 パラメータ 1         マスク開始                   マスク                  マスクデータ
                 パラメータ 2        ビットアドレス                  bit 数               (16 [byte]固定)
                                                                       E2 00 68 0A 00 00 40 02
      Select2       85 00        00 00 00 20         [60]]h→ 96[bit]
                                                                       3C 25 49 18 00 00 00 00
                                                                       E2 00 68 0A 00 00 40 02
      Select3       85 00        00 00 00 20         [60]h→ 96[bit]
                                                                       3C 24 D1 17 00 00 00 00
```

### 拡張Select読取りの原典例：Select4・5

<a id="expand-response-2"></a>

p.162、種類01h・取得数7の同じ例。各枠のマスクは0 bitでも16 byte固定。列はP1/P2・開始bit位置・bit数・マスク。[表1](#expand-response-1) / [表3](#expand-response-3) / [表4](#expand-response-4)。

```text
                                                                       E2 00 68 0A 00 00 40 02
      Select4       85 00        00 00 00 20         [60]h→ 96[bit]
                                                                       3C 24 E5 17 00 00 00 00
                                                                       E2 00 68 0A 00 00 40 02
      Select5       85 00        00 00 00 20         [60]h→ 96[bit]
                                                                       3C 25 51 18 00 00 00 00
```

### 拡張Select読取りの原典例：Select6～8

<a id="expand-response-3"></a>

p.162、種類01h・取得数7の同じ例。各枠のマスクは0 bitでも16 byte固定。列はP1/P2・開始bit位置・bit数・マスク。[表1](#expand-response-1) / [表2](#expand-response-2) / [表4](#expand-response-4)。

```text
                                                                       00 00 00 00 00 00 00 00
      Select6       85 00        00 00 00 00         [00]h→ 0[bit]
                                                                       00 00 00 00 00 00 00 00
                                                                       00 00 00 00 00 00 00 00
      Select7       85 00        00 00 00 00         [00]h→ 0[bit]
                                                                       00 00 00 00 00 00 00 00
                                                                       00 00 00 00 00 00 00 00
      Select8       85 00        00 00 00 00         [00]h→ 0[bit]
                                                                       00 00 00 00 00 00 00 00
```

### 拡張Select読取りの原典例：共通パラメータと0 bit

<a id="expand-response-4"></a>

p.162、種類01h・取得数7の同じ例。各枠のマスクは0 bitでも16 byte固定。列はP1/P2・開始bit位置・bit数・マスク。[表1](#expand-response-1) / [表2](#expand-response-2) / [表3](#expand-response-3)。

```text
※パラメータ 1 : [85]h … Target 値：[SL]、Action 値：[001]、MemBank：EPC(UII)
※パラメータ 2 : [00]h … Truncate 値: [Disable]
※マスク bit 数：[60]h → 96 [bit] … マスクデータの先頭 96[bit] (=12[byte])がマスク対象
※マスク bit 数：[00]h → 0 [bit] … Select コマンドの対象外
                      → Select6, Select7, Select8 は Select コマンドの対象外
```

### 拡張Select読取り原典：選別条件の説明

```text


  Action 値:001 は、OR(論理和)の動作をするため、以下の条件の「いずれか」に一致する
  RF タグが選択されます。
       ・Select1： UHF_SetSelectParam で設定したマスク条件の RF タグ
       ・Select2： EPC(UII)が E2 00 68 0A 00 00 40 02 3C 25 49 18 に一致する RF タグ
       ・Select3： EPC(UII)が E2 00 68 0A 00 00 40 02 3C 24 D1 17 に一致する RF タグ
       ・Select4： EPC(UII)が E2 00 68 0A 00 00 40 02 3C 24 E5 17 に一致する RF タグ
       ・Select5： EPC(UII)が E2 00 68 0A 00 00 40 02 3C 25 51 18 に一致する RF タグ
```

### 6.1 通常Selectとの違い

根拠は§7.4.4 p.160–162、§7.4.19 p.204–211です。通常SelectをSelect1、拡張の7枠をSelect2～Select8と呼びます。要求のnは先頭から扱う拡張枠数（1～7）で、Select1を含めた回数や有効条件の個数ではありません。任意の開始枠を指定するフィールドはありません。

| 項目 | 通常Select | 拡張Select |
|---|---|---|
| 設定先 | Select1 | Select2～Select8 |
| マスク領域 | ceil(bit数/8) byte、0なら省略 | 各枠16 byte固定、0 bitでも省略しない |
| パラメータ1初期値 | 81h（Action=000） | 85h（Action=001） |
| マスクbit数0 | Select使用ONなら空マスクで送信 | その枠とそれ以降のSelectを送信しない |

設定の読戻しはタグのフラグ状態や実際の選別結果の観測ではありません。RFタグへ送る条件は、[通常Select](55_30_uhf_set_select_param.md)と[Inventory設定](55_31_uhf_set_inventory_param.md)のSelect使用・Session・Sel・Inventory Targetも併せて確認します。

### 6.2 23 byteの条件ブロック

先頭位置をBとすると、1枠は次の23 byteです。開始アドレスはbit単位で、Word単位ではありません。

| ブロック内位置 | 内容 |
|---|---|
| B+0 | パラメータ1：bit0–1=MemBank、bit2–4=Action、bit5–7=Select Target |
| B+1 | パラメータ2：bit2=Truncate（0のみ対応）、他は予約（通常0） |
| B+2～B+5 | マスク開始bitアドレス、4 byte・MSBファースト |
| B+6 | マスクbit数b、0～128 |
| B+7～B+22 | マスクデータ、16 byte固定 |

MemBankは01=EPC/UII、10=TID、11=User、00は使用不可のRFUです。Targetは000～011=S0～S3、100=SL、101～111は予約です。Actionは000～111で、初期値は001です。85hはMemBank=EPC/UII・Action=001・Target=SLを表します。Truncate Enableは反映されず、ACKだけで有効化成功としません（p.206）。

#### 端数bitと残りbyteの0埋め

書込みでは、先頭から8 bitずつ区切り、端数となる最後のbyteだけ下位側へ詰め、上位bitを0埋めします。その後、16 byteに足りない分を末尾へ00で埋めます（p.207）。通常Selectの可変長データをそのまま連結しません。

例えばp.211の4 bitのマスク値0011は、先頭byteを03とし、後ろに00を15 byte置きます。マスクbit数は4のままで、領域の長さに合わせて128へ変更しません。読取りでは16 byte全部を受信し、マスク対象は指定されたb bitとして解釈します。対象外のbyteで次のブロック位置をずらさず、SUMには全byteを含めます。

### 6.3 マスク0は後続も停止する

p.207では、拡張枠のマスクbit数が0なら、その枠も後続の枠もSelectを送りません。後ろに非ゼロ条件があっても飛び越して実行しません。次の表はSelect使用が有効な場合です。

| Select1～8のマスクbit数（p.207） | 実行範囲 |
|---|---|
| 0, 96, 16, 0, 32, 0, 0, 0 | Select1～3 |
| 0, 0, 0, 0, 0, 0, 0, 0 | Select1のみ |
| 32, 0, 16, 96, 96, 96, 16, 0 | Select1のみ |
| 96, 16, 16, 32, 96, 96, 0, 0 | Select1～6 |

拡張条件を使わない場合はSelect2のbit数0が停止条件になります。n=0は指定範囲外であり、全消去コマンドとして使いません。無効枠も23 byteのデータ構造は残ります。読取りACKは要求したn枠すべてを解析し、最初の0 bitで受信解析を打ち切りません。

### 6.4 保存先と未指定枠

両RAMは独立です。00hはコマンド用RAMのみ、01hは自動用RAMのみ、02hはFLASHと両RAMへ反映します（§3.12 p.71–74）。変更前後の種類と条件順を記録し、[RAM/FLASHガイド](../../RAM_FLASH_IMPACT_MATRIX.md)に従って復元します。

少ないnで書いたときに、送らなかった後続枠が保持・消去・初期化のどれになるかは、本照合範囲の原典から確定していません。「n=1ならSelect3以降は消える」とは断定しません。必要な後続設定も含めて変更前後を読戻し、設定が残っていることと、0 bitで実行されないことを分けて記録します。

### 6.5 原典の参照補足

PDF p.161末尾の参照「7.4.14 UHF_SetExpandSelectParam」は、Ver.1.17では**7.4.19（p.204–211）**です。原典転記を保持し、こちらへ案内します。p.162のSelect2のbit数は、2026-09-09の保守者訂正により、誤「[60]]h」→正「[60]h」で確定しました。単純な表記の誤記であり、値は60h=96 bitのままです。掲載Hex・長さ・SUMは変わりません。

p.162のAction=001によるORの説明は、[書込みカードの論理表](55_32_uhf_set_expand_select_param.md)で初回Action・同一Target・実行順を確認します。拡張の初期値85hだけで、任意の通常SelectとのOR動作を保証しません。

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. レスポンス処理

### 8.1 読取り要求とACKの位置

要求はCMD=55h・LEN=03h、DATA[0]=42h、DATA[1]=種類00h／01h／02h、DATA[2]=取得数n（1～7）です。ACKはCMD=30h・LEN=2+23×n、DATA[0]=42h、DATA[1]=種類で、**取得数nは返りません**（p.160–161）。DATA[2]は最初のブロックのパラメータ1です。

0起点のj番目のブロック先頭はB=2+23×j、Select(j+2)に対応します。ブロック内の位置は§6.2を参照してください。

| n | 読取りACKのLEN | ACK総長 |
|---:|---|---:|
| 1 | 19h（25） | 32 byte |
| 7 | A3h（163） | 170 byte |

### 8.2 判定手順

1. 共通フレームの総長・STX／ETX／CR／SUMを検査し、CMD=30hでLEN≥25を確認してからDATAを参照します。
2. DATA[0]=42h、DATA[1]=要求した種類、LEN=2+23×要求nを確認します。単に(LEN−2)が23で割り切れるだけでは、別の取得数の応答を排除できません。
3. 要求nは1～7です。0枠・8枠を許容する独自仕様へ広げず、読み取る数をACKのDATA[2]から取得しません。
4. n枠すべてを23 byteずつ解析し、各bit数0～128を確認します。0 bitの枠も16 byteのマスクデータが存在し、後続枠があれば続けて解析します。
5. 設定として取得できた枠と、実行対象の枠を区別します。最初の拡張0 bit以降に非ゼロ設定が返っても、実行されるとは判断しません。

要求の種類・nと対象機種・ROMを保持します。タグ選別を評価する場合に必要な通常Select・Inventory設定は、このACKに含まれません。

### 8.3 NACK・非同期応答

NACKはCMD=31h・LEN=0Ah・総17 byteの[共通形式](../../RESPONSE_AND_NACK_MASTER.md)です。DATA[0]を要求の詳細と対応づけ、DATA[1]を主エラー、DATA[2]を主エラー0Ahの場合の追加エラーとして読みます。Encode／BlockWrite2固有の追加コードをこの設定コマンドへ転用しません。予約領域は独自解釈せず、非ゼロでもSUMに含めます。

RFタグデータや切替通知を設定要求の成功ACKへ取り込まず、ホストの待機期限切れを機器NACKと区別します。設定ACKの解析に、TID付加やアンテナID出力設定を一律必須にはしません。

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

- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)
- [55_32_uhf_set_expand_select_param](55_32_uhf_set_expand_select_param.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_40_uhf_get_select_param](55_40_uhf_get_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [55_41_uhf_get_inventory_param](55_41_uhf_get_inventory_param.md)

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。