---
title: "UHF_InventoryRead"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.2"
command_group: "rf_tag_communication"
command_name: "UHF_InventoryRead"
command_byte: "55h"
detail_command: "14h"
subcommand: null
operation_profile: "rf-read"
operation_level: "RF read"
rf_emission: true
write_operation: false
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: true
requires_tag: true
requires_access_password: false
requires_parameters: true
verification_status: "REAL_DEVICE_VERIFIED_WITH_NOTES"
result_status: "REAL_DEVICE_PASS_WITH_NOTES"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
  - "../../PARAMETER_CONFIRMATION_GUIDE.md"
  - "../../AI_IMPLEMENTATION_GUARDRAILS.md"
tags:
  - "utr-s201"
  - "command-card"
  - "rf-tag-communication"
  - "rf-read"
  - "rf-emission"
  - "requires-antenna"
  - "requires-tag"
  - "pass-with-notes"
  - "uhf-inventory-read"
---

# UHF_InventoryRead（タグ一覧読み取り＋メモリ読み取り）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_InventoryRead** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.2`
- コマンド分類: rf_tag_communication
- 確認区分: `rf-read`
- 操作レベル: RF read
- コマンドバイト: `55h` / 詳細コマンド: `14h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_InventoryRead** です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | あり |
| 書き込み操作 | なし |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | あり |
| タグ条件確認 | あり |
| Accessパスワード確認 | なし |
| パラメータ確認 | あり |
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

以下は、公式PDF `7.5.2` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.5.2   UHF_InventoryRead
  インベントリ処理をおこない RF タグの Stored PC および EPC(UII)、および指定 MemBank のデー
  タの読み取りをおこなうコマンドです。TID の読み取り結果も付加することができます。

  本コマンドを実行すると、インベントリ処理をおこない、RF タグの Stored PC および EPC(UII)を
  読み取ります。続いて、Read コマンドで指定 MemBank のデータと TID の読み取りをおこないま
  す。
  インベントリ処理では、ISO18000-63 規格に規定された[Select]コマンド、[Query]コマンド、
  [QueryRep]コマンド等を順に実行します。
        ・[Select]コマンドで使用する MemBank、Target 値、Action 値、マスク条件の指定は、
         「7.4.17 UHF_SetSelectParam」、Select コマンドの発行の有無の指定は、
         「7.4.18 UHF_SetInventoryParam」をご参照ください。
        ・[Query]コマンドで使用する Q 値、Session 値、Sel 値の指定の詳細は、
         「7.4.18 UHF_SetInventoryParam」をご参照ください。


［コマンド］
 ラベル名 バイト数                              内容
  STX   1            02h
 アドレス   1            00h（ 「5.2 通信フォーマットの詳細」参照）
 コマンド   1            55h
 データ長   1            07h
               1     14h（詳細コマンド）
                     パラメータ 1
                              MemBank ※左側が上位 bit
                              00     ：Reserved
                     bit0
                              01     ：EPC(UII)
                     bit1
                              10     ：TID
               1
                              11     ：User
 データ部                         TID 付加
                     bit2     0      ：付加しない
                              1      ：付加する
                     bit3-7   将来拡張のための予約（通常は 0）
                     読み取り開始 Word アドレス ※MSB ファーストで指定
               4
                       RF タグのメモリ上の読み取り開始位置（Word 単位）
                     読み取り Word 数
               1
                       読み取る Word 数（1～32）
   ETX         1     03h
   SUM         1     SUM 値（「5.3 SUM の計算方法」参照）
    CR         1     0Dh


  ＜注意事項＞
  ・本コマンドで読み取るメモリ領域は、[UHF_SetInventoryParam]コマンドで「00h:コマンドモ
   ード用パラメータ」に設定した「読み取り設定」によらず、本コマンド内のパラメータで指定さ
   れた領域となります。
  ・読み取り対象の RF タグに、指定した MemBank が存在しない場合や、指定した読み取りアドレ
   スが存在しない場合には、RF タグのデータを読み取りすることができないため、RF タグ読み取
   りのレスポンスが返りません。

● MemBank
   読み取るメモリ領域を指定します。
   詳細は、  「4.2RF タグのメモリ構造」の項を参照ください。
    ※Reserved 領域読み取り時の注意点
       [UHF_InventoryRead]コマンド実行時には、リーダライタに Access パスワードが設定さ
       れていても、Access コマンド発行しないで RF タグへのアクセスをおこないます。
       そのため、指定 MemBank に Reserved 領域を指定した場合、RF タグ側の Reserved 領域
       が Read ロックされていると、データを読み取ることができないため、RF タグ読み取りの
       レスポンスが返りません。

● TID 付加
    指定したメモリ領域に加えて、TID を読み取りして付加するかどうかを指定します。
    ※TID を付加することで、例えば EPC(UII)と指定 MemBank の値が全て同一の RF タグを複数
      読み取った場合も、TID は異なりますので、RF タグを区別することができます。
    ・TID は、4[Word] (=96[bit])または 6[Word] (=128[bit])に対応しています。
    ・6[Word]を超える TID を持つ RF タグを読み取った場合、全ての TID 領域を読み取ることは
     できず、TID の上位 6[Word]のみを読み取ったレスポンスが返ります。
     RF タグが持つ TID 領域の詳細は、使用する RF タグのデータシートをご確認ください。
    ・6[Word]を超える TID 領域の読み取りをする場合には、[UHF_SetInventoryParam]コマンド
     で MemBank に TID 領域を指定して読み取りをおこなってください。

● 読み取り開始アドレス
   MemBank で指定したメモリ領域の読み取り開始位置（Word アドレス）を指定します。
   ※MSB ファーストで指定
   (例) Word アドレス[03]h を指定する場合は、[00 00 00 03]h を指定します。
   (例) Word アドレス[10D]h を指定する場合は、[00 00 01 0D]h を指定します。

● 読み取り Word 数
   読み取るメモリのサイズを Word 長（2 [byte]単位）で指定します。
   1～32 [Word]まで指定可能です。


［ACK レスポンス］
 RF タグを読み取った場合のレスポンスは、①のレスポンスが RF タグの枚数分返り、続いて②の
 レスポンスが 1 回返ります。
 RF タグを読み取らなかった場合、②のレスポンスのみが 1 回返ります。

 ①RF タグを読み取った場合の RF タグデータのレスポンス
ラベル名 バイト数                    内容
 STX        1    02h
アドレス        1    00h（ 「5.2 通信フォーマットの詳細」参照）
コマンド        1    6Ch
データ長        1    7+n1+n2+n3
            1    0Ah（詳細コマンド）
                 RSSI 値
                    RSSI 値(dBm)を 10 倍した値がセットされます
            2       （符号付き 16 ビット整数）
                 1 [byte]目     ：上位バイト(MSB)
                 2 [byte]目     ：下位バイト(LSB)
                 ANGLE 値
            1       RF タグからの受信信号の位相(0～180 度) を 16/45 倍した値が
                    セットされます（符号なし 8 ビット整数）
                 n1（4-64）
            1
                 ※n1：PC+EPC のバイト数（Word 単位）
                 PC+EPC
                 1 [byte]目     ：PC の上位バイト(MSB)
                 2 [byte]目     ：PC の下位バイト(LSB)
           n1
データ部             3 [byte]目     ：EPC(UII)の最上位バイト(MSB)
                 |
                 n1 [byte]目    ：EPC(UII)の最下位バイト(LSB)
                 n2（1-64）
            1
                 ※n2：読み取りデータのバイト数
                 読み取りデータ
                 1 [byte]目     ：読み取りデータの最上位バイト(MSB)
           n2
                 |
                 n2 [byte]目    ：読み取りデータの最下位バイト(LSB)
                 n3（0-32）
            1
                 ※n3：TID のバイト数（バイト単位）
                 TID
                 1 [byte]目     ：TID の最上位バイト(MSB)
           n3
                 |
                 n3 [byte]目    ：TID の最下位バイト(LSB)
 ETX        1    03h
 SUM        1    SUM 値（   「5.3 SUM の計算方法」参照）
  CR        1    0Dh
＜注意事項＞
 ・指定した MemBank や TID が読めなかった場合は、EPC(UII)が読めてもレスポンスは返りませ
  ん。指定した MemBank および読み取りアドレスが RF タグに存在するか、RF タグの通信環境
  が良好かをご確認ください。


● RSSI 値
  RF タグからの受信信号強度(dBm)を 10 倍し、
                            「符号付き 16 ビット整数」に変換した値が
  セットされます。
  ・RSSI 値の算出方法
   レスポンスの 6~7 [byte]目を「符号付き 16 ビット整数」として読み取り、
   10 進数に変換してから 10 で割ります。
     (例) レスポンスの 6~7[byte]目が[FF 12]h の場合
         [FF 12]h → -238 → RSSI 値: -23.8
     ※16 進数(符号付き 16 ビット整数)から 10 進数(負の整数)への変換手順については、
      「10.1.2 符号付き 16 進数整数と 10 進数の変換」をご参照ください。

● ANGLE 値
   RF タグからの受信信号の位相(Phase 値)を 16/45 倍 (45 分の 16 倍)し、
   符号なし 8 ビットに変換した値がセットされます。
   ANGLE 値は、00h(0 度)から 40h(180 度)の範囲の値が返ります。
    ・ANGLE 値の算出方法
     レスポンスの 8[byte]目を符号なし 8 ビットとして読み取り、
     10 進数に変換してから 45/16 倍 (16 分の 45 倍)します。
       (例) レスポンスの 8[byte]目が[30]h の場合
            [30]h → 48 → ANGLE 値= 48×45/16 = 135 度

  ②読み取り完了レスポンス
ラベル名 バイト数                          内容
 STX    1  02h
アドレス    1  00h（ 「5.2 通信フォーマットの詳細」参照）
コマンド    1  30h
データ長    1  05h
        1  14h（詳細コマンド）
        1  00h（固定値）
           RF タグの読み取り枚数
データ部
        2  1 [byte]目     ：読み取り枚数の下位バイト(LSB)
           2 [byte]目     ：読み取り枚数の上位バイト(MSB)
        1  読み取り時のキャリアのチャンネル番号 (ch.5/11/17/23-37)
 ETX    1  03h
 SUM    1  SUM 値（   「5.3 SUM の計算方法」参照）
  CR    1  0Dh


● RF タグの読み取り枚数
    読み取った RF タグの枚数が 16 進数の 2[byte]で返ります。
     (例) RF タグを 2 枚読み取った場合、[02 00]h が返ります。
     (例) RF タグを 18 枚読み取った場合、[12 00]h が返ります。

● 読み取り時のキャリアのチャンネル番号
   読み取りをおこなったキャリアの周波数（チャンネル番号）が 16 進数で返ります。
    (例)26ch (921.0MHz)で読み取りをおこなった場合、[1A]h が返ります。
  UHF 帯の RFID においては、周囲環境での反射や、近接チャンネルでの他の機器の使用の影響に
  より、特定の周波数チャンネルのみ読み取り精度が悪くなったりする場合がありますので、読み取
  り時の電波環境の確認にご使用ください。


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ＜注意事項＞
   ・キャリア出力開始から 4 秒が経過すると、電波法の規定により、Inventory 処理の途中であっ
    ても、リーダライタは自動的にキャリア OFF となります。
    Q 値を大きく設定した場合や、アンテナの読み取り範囲にある RF タグの枚数が多い場合
    で、4 秒以内に Inventory 処理が終了せずにキャリア OFF となった場合には、まだ読み取り
    をおこなっていない RF タグデータの読み取りレスポンスは返さません。また、読み取り完了
    レスポンス中の読み取り枚数には、それまでに読み取った RF タグの枚数が返されます。


［コマンド＆レスポンス例］
 ● コマンド
   [TX] 02 00 55 07 14 07 00 00 00 00 02 03 7E 0D
     → 指定 MemBank…User 領域の Word アドレス[00]h から 2[Word]、TID 付加する
  ● レスポンス
    [RX] 02 00 6C 25 0A FE FF 2F 0E 34 00 <EPC_BYTES>
         04 <READ_DATA_BYTES> 0C <TID_BYTES> 03 D9 0D
    [RX] 02 00 30 05 14 00 01 00 1A 03 69 0D

    ・上記の解析結果
         データ種類               受信コマンド列                   数値／パラメータ
     RSSI 値      FE FF                               RSSI 値： -25.7
     ANGLE 値     2F                                  ANGLE 値：132 度
     PC          34 00                               同左
     EPC         <EPC_BYTES>                         同左
     指定 MemBank
                 <READ_DATA_BYTES>                  同左
     データ
     TID         <TID_BYTES>                         同左
     読み取りアンテナ(※) 00                                  Ant.0 で読み取り
     読み取り枚数      01 00                               読み取り枚数：1 枚
     チャンネル番号     1A                                  26ch.で読み取り
     ※ 読み取りアンテナのアンテナ番号を表示するためには、[アンテナ切替設定の書き込み]コマ
        ンドで、リーダライタのコマンドモード用パラメータに「アンテナ ID の出力：有効」が設
        定されている必要があります。

      ・RSSI 値の算出方法
       レスポンスの 6~7 [byte]目[FE FF]h を符号付き 16 ビットとして扱い、10 進数に変換して
       から 10 で割ります。
       (例) [FE FF]h → -257 → RSSI 値: -25.7

      ・ANGLE 値の算出方法
       レスポンスの 8[byte]目の[2F]h を符号なし 8 ビットとして読み取り、10 進数に変換してか
       ら 45/16 倍 (16 分の 45 倍)します。
       (例) [2F]h → 47 → ANGLE 値= 47×45/16 = 132.1875 度
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

このカードでは、以下を意図的に記載しません。

- 実機へそのまま送信できる完成Hex
- SUM計算済みの送信用コマンド例
- 安全ガードを省略した実装コード

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

ACK、後続レスポンス、可変長データの解釈は、コマンド番号だけで固定せず、`../../RESPONSE_AND_NACK_MASTER.md` の起動時スナップショットに基づいてください。ROM・機種、アンテナID出力、TID付加、読取完了応答、アンテナ切替完了応答、キャリア検知応答、RAM/FLASH設定の状態により、ACKのタイミングや応答データ長が変わります。

### 8.1 ACK/レスポンス例（PDF掲載例）

| 種別 | Hex |
|---|---|
| TX | `02 00 55 07 14 07 00 00 00 00 02 03 7E 0D` |
| RX | `02 00 6C 25 0A FE FF 2F 0E 34 00 <EPC_BYTES> 04 <READ_DATA_BYTES> 0C <TID_BYTES> 03 D9 0D`<br>`02 00 30 05 14 00 01 00 1A 03 69 0D` |

1行目はRFタグデータ、2行目は読み取り完了ACKです。アンテナID出力ONの場合、アドレス位置に読み取りANT番号が入ります。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 14 44 00 00 00 00 00 00 00 00 03 98 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.3 設定依存の注意

- アンテナID出力ON/OFFにより、レスポンスのアドレス位置がリーダライタIDまたは読み取りANT番号に変わります。
- 読取完了応答、アンテナ切替完了応答、キャリア検知応答のON/OFFで、後続ACKの有無が変わります。
- TID付加、EPC/UII応答設定、読み取りWord数により、可変長データの長さが変わります。


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
| 受信期限内に1フレームも来ない | `TIMEOUT` | timeoutとして処理し、NACKとは分ける |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む |
| `CMD=6Ch` かつ `DATA[0]=0Ah` | `RF_TAG_DATA` | RFタグデータとして可変長解析する |
| `CMD=30h` かつ `DATA[0]=14h` かつ `DATA[1]=00h` | `COMPLETION` | 読取完了応答ON時の完了ACKとして扱う |
| `CMD=30h` かつ `DATA[0]=10h` かつ `DATA[1]=01h` | `ANT_SWITCH_COMPLETE` | アンテナ切替完了応答ON時のみ必須候補にする |
| `CMD=30h` かつ `DATA[0]=10h` かつ `DATA[1]=02h` | `CARRIER_DETECTED` | キャリア検知応答ON時のみイベントとして扱う。0件は失敗ではない |
| `CMD=30h` だが上記に一致しない | `ACK` | PDF該当節のACKとして詳細確認する |

受信ループは「タグ応答が複数回来る」「最後に完了ACKが来る場合がある」「設定により完了ACK自体が来ない」を前提にしてください。

対象識別子: コマンド `55h` / 詳細 `14h` / サブ `なし`。


#### ACK/データ部offset
RFタグデータ `CMD=6Ch` / `DATA[0]=0Ah`:

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `0Ah`: UHF_InventoryReadタグ応答 |
| 1..2 | `RSSI` | signed 16bit。必要に応じてPDFの倍率で変換 |
| 3 | `ANGLE` | 位相角。PDF定義に従って変換 |
| 4 | `n_pc_epc` | PC+EPC長 |
| 5.. | `PC+EPC` | `n_pc_epc` byte |
| 可変 | `read_data_length/read_data` | 読み取り対象メモリの戻り値。要求Word数に依存 |
| 可変 | `tid_length/tid` | TID付加ON時のみ出現。OFF時は長さ0または領域なしとして扱う |

読取完了ACK `CMD=30h` / `DATA[0]=14h` / `DATA[1]=00h`:

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `14h` |
| 1 | `status` | `00h`: 読取完了 |
| 2 | `count_lsb` | 読取タグ数LSB |
| 3 | `count_msb` | 読取タグ数MSB |
| 4 | `channel` | 使用CH |

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 14h` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR、LBT_ERROR、ANTENNA_ERROR、UHF_IC_ERRORなどの主エラー |
| 2 | `error_code_2` | `error_code_1=0Ah` のUHF ICエラー時に参照 |
| 3 | `error_code_3` | UHF_Encode / UHF_BlockWrite2 等でPDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
deadline = now + command_timeout
while now < deadline:
    frame = read_next_frame()
    if frame is None:
        continue
    parsed = parse_common_frame(frame)
    if parsed.invalid:
        emit(INVALID_FRAME)
        continue
    if parsed.cmd == 0x31:
        return parse_nack(parsed)
    if parsed.cmd == 0x6C:
        emit(parse_rf_tag_data(parsed, settings_snapshot))
        continue
    if parsed.cmd == 0x30 and is_completion_ack(parsed):
        emit(parse_completion_ack(parsed))
        return SUCCESS
    if parsed.cmd == 0x30 and is_optional_async_ack(parsed, settings_snapshot):
        emit(parse_optional_async_ack(parsed))
        continue
return TIMEOUT_OR_PARTIAL_SUCCESS_BY_SETTINGS
```

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

#### 設定スナップショット必須項目

実行前に、ROM/機種、物理アンテナ容量、接続OKアンテナ、現在ANT、アンテナID出力、TID付加、EPC/UII応答設定、読取完了応答、アンテナ切替完了応答、キャリア検知応答、RAM/FLASH対象を取得し、この結果をパーサへ渡してください。
## 9. 実機確認

実機確認区分: `rf-read`

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
- `../../RF_SAFETY_AND_CARRIER_RULES.md`
- `../../PARAMETER_CONFIRMATION_GUIDE.md`
- `../../AI_IMPLEMENTATION_GUARDRAILS.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
