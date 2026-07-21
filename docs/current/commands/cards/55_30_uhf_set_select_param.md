---
title: "UHF_SetSelectParam"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.17"
command_group: "reader_setting"
command_name: "UHF_SetSelectParam"
command_byte: "55h"
detail_command: "30h"
subcommand: null
operation_profile: "settings-change"
operation_level: "write/configuration"
rf_emission: false
write_operation: true
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
requires_tag: false
requires_access_password: false
requires_parameters: true
verification_status: "REAL_DEVICE_VERIFIED_WITH_NOTES"
result_status: "REAL_DEVICE_PASS_WITH_NOTES"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "write-operation"
  - "pass-with-notes"
---

# UHF_SetSelectParam（Select条件設定）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_SetSelectParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.17`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `30h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_SetSelectParam** です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 書き込み操作 | あり |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | なし |
| タグ条件確認 | なし |
| Accessパスワード確認 | なし |
| パラメータ確認 | あり |
| 明示許可 | 必要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 読み取り専用か、設定変更か、タグメモリ操作かを分類する。
4. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。
5. 周波数、送信出力、アンテナ設定、FLASH、タグメモリに影響する場合は、事前承認を取る。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.4.17` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.17 UHF_SetSelectParam
 RFタグへのSelectコマンドで送信するパラメータの設定コマンドです。
 このコマンドは、リーダライタへの設定コマンドです。本コマンドを実行しても、リーダライタか
 らのSelectコマンドの送信はおこなわれません。
 Selectコマンドの送信のタイミングについては、「3.10 RFタグ通信コマンド実行時のリーダライタ
 の内部処理」をご参照ください。
 ※[UHF_SetInventoryParam]コマンドで「Selectコマンド：使用する」に設定されている場合は、
  本コマンドで「マスクbit数」=[0]としてもSelectコマンドは発行されます。
  （「マスクbit数」=[0]、「マスクデータ」=[empty]のSelectコマンドが発行されます）

  ［コマンド］
 ラベル名 バイト数                                  内容
  STX        1     02h
 アドレス        1     00h（「5.2 通信フォーマットの詳細」参照）
 コマンド        1     55h
 データ長        1     9+n
             1     30h（詳細コマンド）
                   パラメータ種類 ※1
                     00h   ：コマンドモード用パラメータ
             1
                     01h   ：自動読み取りモード用パラメータ
                     02h   ：FLASH データ
                   パラメータ 1 ［初期値：81h］
                         MemBank ※左側が上位 bit
                            00      ：RFU
                   bit0
                            01      ：EPC(UII) ［初期値］
                   bit1
                            10      ：TID
                            11      ：User
 データ部
                            Action 値 ［初期値：000］
                   bit2-4
                            詳細はパラメータ説明参照
             1              Target 値 ※左側が上位 bit
                            000     ：Inventoried(S0)
                            001     ：Inventoried(S1)
                            010     ：Inventoried(S2)
                   bit5-7   011     ：Inventoried(S3)
                            100     ：SL ［初期値］
                            101     ：Reserved
                            110     ：Reserved
                            111     ：Reserved
   （次ページへ続く）


  （前ページからの続き）

ラベル名     バイト数                               内容
                  パラメータ 2 ［初期値：00h］
                  bit0
                           将来拡張のための予約（通常は 0）
                  bit1
            1            Truncate 値（0 固定）
                  bit2   0        ：Disable［初期値］
                         1        ：Enable（未サポート）
                  bit3-7 将来拡張のための予約（通常は 0）
データ部              マスク開始ビットアドレス ［初期値: 00 00 00 00］h
            4
                  ※MSB ファースト、ビット単位で指定
                  マスク bit 数
            1
                  ※最大 128[bit] (=80[h])まで
                  マスクデータ
           (n)    マスク bit 数で指定した長さのマスクデータ
                  ※「マスク bit 数」=[0]の場合は省略(n=0)
 ETX        1     03h
 SUM        1     SUM 値（「5.3 SUM の計算方法」参照）
  CR        1     0Dh
※1：パラメータ種類の詳細は「3.12.1 パラメータ種類」をご参照ください。


● Select コマンドについて
  リーダライタが「Select コマンドを使用する」の設定となっている場合、RF タグ読み取り時の
  Inventory 処理中に、リーダライタから RF タグに対して[Select]コマンドが実行されます。[Select]
  コマンドにより、指定した条件を満たす RF タグのみを選択(または除外)することができます。
  (例) EPC が[AB 12]h で始まる RF タグのみを選択する場合
    ※EPC は、EPC 領域の Word アドレス[02]h（ビットアドレス[20]h）から始まります
    →EPC 領域のビットアドレス[20]h から 16[bit]が[AB 12]h, Action 値=000(0), Target 値=[S0]を
     指定します。
     ※Action 値=000(0)の状態遷移 … 一致: [A]に遷移、不一致: [B]に遷移
    →EPC が[AB 12]で始まる RF タグは S0=[A]に、[AB 12]で始まらない RF タグは S0=[B]に遷移
     します。
     ※S1 や SL など、Target 値で指定していないフラグは遷移しません
                           Select コマンド     Mask 条件への  Select コマンド
                   EPC
                               実行前        [一致]／[不一致]      実行後
                          S0=[A], S1=[A],            S0=[A], S1=[A],
     RF タグ 1   AB12 0021…                      一致
                          S2=[B], S3=[A]             S2=[B], S3=[A]
                          S0=[A], S1=[A],            S0=[B], S1=[A],
     RF タグ 2   CD35 2200…                     不一致
                          S2=[B], S3=[A]             S2=[B], S3=[A]
                          S0=[B], S1=[B],            S0=[B], S1=[B],
     RF タグ 3   ABCD 1234…                     不一致
                          S2=[A], S3=[B]             S2=[A], S3=[B]


● MemBank
  [Select]コマンドの対象のメモリ領域を指定します。   （FLASH 初期値：EPC(UII)）
  詳細は、    「4.2 RF タグのメモリ構造」の項を参照ください。
  ・RFU
    ISO18000-63 規格上の予約領域です。現在使用することはできません
    ※RF タグのメモリ領域の[00h: Reserved]とは異なります。
      →Kill Password や Access Password を「マスク条件」とすることはできません。


  ・EPC(UII)
    ビットアドレス[00]h から CRC (16[bit]) + PC (16[bit])
    ビットアドレス[20]h から EPC(UII)
  ・TID
     ビットアドレス[00]h から RF タグのユニークな ID 領域（一般的には 64[bit]または 96[bit]）
  ・USER
    ビットアドレス[00]h からユーザメモリ


● Action 値
   「マスク条件」で指定した内容に[一致]／[不一致]の RF タグに対し、「Target 値」で指定した
   フラグの状態をそれぞれどのように変化させるかを指定するパラメータです。
   （FLASH 初期値：000）
   ※「Target 値」で指定したフラグのみ変化します。
                           Matching                      Non-Matching
   Action
                     （マスク条件が一致）                     （マスク条件が不一致）
※左側が MSB
                  Inventoried        SL フラグ       Inventoried        SL フラグ
()内は 10 進数
                  フラグが対象              が対象         フラグが対象              が対象
    000        Inventoried フラグ      SL フラグを    Inventoried フラグ      SL フラグを
    (0)          を[A]にセット             セット        を[B]にセット             リセット
    001        Inventoried フラグ      SL フラグを
                                                       なにもしない
    (1)          を[A]にセット             セット
    010                                        Inventoried フラグ   SL フラグを
                        なにもしない
    (2)                                          を[B]にセット         リセット
               Inventoried フラグ
    011             を反転           SL フラグを
                                                       なにもしない
    (3)          ※[A]なら[B]へ          反転
                 ※[B]なら[A]へ
    100        Inventoried フラグ    SL フラグを      Inventoried フラグ   SL フラグを
    (4)          を[B]にセット          リセット          を[A]にセット          セット
    101        Inventoried フラグ    SL フラグを
                                                       なにもしない
    (5)          を[B]にセット          リセット
    110                                        Inventoried フラグ   SL フラグを
                        なにもしない
    (6)                                          を[A]にセット          セット
                                               Inventoried フラグ
    111                                             を反転          SL フラグを
                        なにもしない
    (7)                                          ※[A]なら[B]へ         反転
                                                 ※[B]なら[A]へ


(例 1) 「Target 値」=[SL]、「Action 値」=[000(0)]の場合
 ※Action 値=000(0)の SL フラグの遷移 → [一致]：SL=[Set]、[不一致]：SL=[Reset]
    ・「Target 値」=[SL]なので、「SL フラグ」のみが遷移します。
        ・マスク条件に[一致]の RF タグは、SL=[Set]となります。
        ・マスク条件に[不一致]の RF タグは、SL=[Reset]となります。
    ・「Inventoried フラグ」は遷移しません。
                マスク条件への           Select コマンド               Select コマンド
               [一致]／[不一致]             実行前                       実行後
                              S0=[A], S1=[A], S2=[A],   S0=[A], S1=[A], S2=[A],
    RF タグ 1        一致
                              S3=[A], SL=[Reset]        S3=[A], SL=[Set]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 2        一致
                              S3=[A], SL=[Set]          S3=[A], SL=[Set]
                              S0=[A], S1=[B], S2=[A],   S0=[A], S1=[B], S2=[A],
    RF タグ 3        不一致
                              S3=[B], SL=[Reset]        S3=[B], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 4        不一致
                              S3=[B], SL=[Set]          S3=[B], SL=[Reset]

(例 2) 「Target 値」=[SL]、「Action 値」=[001(1)]の場合
 ※Action 値=001(1)の SL フラグの遷移 → [一致]：SL=[Set]、[不一致]：SL=[なにもしない]
    ・「Target 値」=[SL]なので、「SL フラグ」のみが遷移します。
    ・「Inventoried フラグ」は遷移しません。
                マスク条件への           Select コマンド               Select コマンド
               [一致]／[不一致]             実行前                       実行後
                              S0=[A], S1=[A], S2=[A],   S0=[A], S1=[A], S2=[A],
    RF タグ 1        一致
                              S3=[A], SL=[Reset]        S3=[A], SL=[Set]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 2        一致
                              S3=[A], SL=[Set]          S3=[A], SL=[Set]
                              S0=[A], S1=[B], S2=[A],   S0=[A], S1=[B], S2=[A],
    RF タグ 3        不一致
                              S3=[B], SL=[Reset]        S3=[B], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 4        不一致
                              S3=[B], SL=[Set]          S3=[B], SL=[Set]

(例 3) 「Target 値」=[S2]、「Action 値」=[100(4)]の場合
 ※Action 値=001(1)の Inventory フラグ(S2)の遷移 → [一致]：S2=[B]、不一致：S2=[A]
  ・「Target 値」=[S2]なので、「Inventoried(S2)フラグ」のみが遷移します。
  ・「SL フラグ」や S2 以外の「Inventoried フラグ」は遷移しません。
                マスク条件への           Select コマンド               Select コマンド
               [一致]／[不一致]             実行前                       実行後
                              S0=[A], S1=[A], S2=[A],   S0=[A], S1=[A], S2=[B],
    RF タグ 1        一致
                              S3=[A], SL=[Reset]        S3=[A], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 2        一致
                              S3=[A], SL=[Set]          S3=[A], SL=[Set]
                              S0=[A], S1=[B], S2=[A],   S0=[A], S1=[B], S2=[A],
    RF タグ 3        不一致
                              S3=[B], SL=[Reset]        S3=[B], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[A],
    RF タグ 4        不一致
                              S3=[B], SL=[Set]          S3=[B], SL=[Set]


● Target 値
    Select コマンドを受けた RF タグが、    「Inventoried フラグ」または「SL フラグ」のどちらを遷
    移させるかを指定します。        （FLASH 初期値：SL）
    また、  「Inventoried フラグ」の場合はさらに、4 つのセッション(S0, S1, S2, S3)のうちどのセッ
    ションが対象かを指定します。
    RF タグは、Select コマンドで指定した「マスク条件」への[一致]／[不一致]に応じて、「Action
    値」で指定した状態遷移をおこないます。

● Truncate 値（FLASH 初期値：Disable）
  ・Select コマンドのコマンドパラメータ中の Truncate の値を設定します。
  ・UTR-S201 シリーズは、「Truncate 値」は[Disable]のみ対応しています。[Enable]を指定して
   も設定や実動作に反映されません。

● マスク開始 bit アドレス（FLASH 初期値：[00 00 00 00]h）
   MemBank で指定したメモリ領域の、マスク条件を設定する開始 bit アドレスを指定します。
   ※ Word アドレスではなく、bit アドレスで指定します。
   ※ 0 [Word]目の最上位 bit が bit アドレス[00]h、最下位 bit が bit アドレス[0F]h です。

● マスク bit 数
   マスク開始 bit アドレスから開始して、マスクする bit 長を指定します。
   上限 128[bit]まで指定することができます。（FLASH 初期値：0）
    「Select コマンド使用」=[使用する]の場合、「マスク bit 数」=[0]を設定した場合でも、
    「マスク bit 数=0」、「マスクデータ」=[empty]の[Select]コマンドが発行されます。

● マスクデータ
   マスクデータを「byte 単位」で指定します。
   上限 16[byte]まで指定することができます。（FLASH 初期値：0）
    ※マスクビット数が 8 の倍数にならない場合は、上位 bit から byte 単位で区切り、
     端数となる byte 内では下位 bit にデータを詰めて、上位 bit は 0 埋めします。
    (例 1) TID 領域の先頭 28[bit]が[E2 80 11 7]の条件でマスクする場合
      ※ [E2 80 11 7]h=[1110 0010 1000 0000 0001 0001 0111]b
     byte 単位で区切った場合、下位[4bit]の[0111]b が端数 byte となります。
     8[bit]に満たない最下位 byte は、上位 4[bit]を 0 埋めし、[0000 0111]b (=07h)とします。
     マスクデータは、[<TID_PREFIX_BYTES>]h となります。（※[<TID_PREFIX_BYTES>]h ではありません）
     ＜コマンド例＞
      [TX] 02 00 55 0D 30 00 82 00 00 00 00 00 1C <TID_PREFIX_BYTES> 03 AF 0D

    (例 2) EPC 領域のビットアドレス[10]h から 5[bit] ([10]h-[14]h: EPC Length)が[00110]b の
         条件でマスクする場合
     指定したマスク bit 数(=5)が 8[bit]に満たないため、上位 3[bit]を 0 埋めして、
     [0000 0110]b (=[06]h)とします。マスクデータは、[06]h となります。
     ＜コマンド例＞
      [TX] 02 00 55 0A 30 00 81 00 00 00 00 10 05 06 03 30 0D
       7 [byte]目 :[81]h … Target=SL(=[100]b), Action 値=0 (=[000]b), MemBank=EPC (=[01]b)
       8 [byte]目 :[00]h … Truncate 値=0 (Disable)
       9-12 [byte]目 : [00 00 00 10]h … マスク開始ビットアドレス
       13 [byte]目 : [05]h … マスク bit 数(=5)
       14 [byte]目 : [06]h … マスクデータ


 ［ACK レスポンス］
ラベル名 バイト数                                             内容
 STX           1      02h
アドレス           1      00h（「5.2 通信フォーマットの詳細」参照）
コマンド           1      30h（ACK）
データ長           1      01h
データ部           1      30h（詳細コマンド）
 ETX           1      03h
 SUM           1      SUM 値（「5.3 SUM の計算方法」参照）
  CR           1      0Dh

  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
      (例 1) 以下のパラメータを書き込む場合
              データ種類              数値／パラメータ                                   コマンド列
       書き込み対象          FLASH データ                                          02
       MemBank         EPC(UII)
       Action 値        000(0)                                             81
       Target 値        SL
       Truncate 値      Disable                                            00
       マスク開始ビットアドレス [20]h                                                 00 00 00 20
       マスク bit 数       96                                                 60
       マスクデータ          E2 00 68 0A 00 00 40 02 3C 25 39 17                同左
  •    コマンド
       02 00 55 15 30 02 81 00 00 00 00 20 60 E2 00 68 0A 00 00 40 02 3C 25 39 17 03 E9 0D
  •    レスポンス
       02 00 30 01 30 03 66 0D

      (例 2) 以下のパラメータを書き込む場合（マスクを使用しない場合）
              データ種類             数値／パラメータ                                    コマンド列
       書き込み対象          コマンドモード用パラメータ                                      00
       MemBank         EPC(UII)
       Action 値        000(0)                                             41
       Target 値        S2
       Truncate 値      Disable                                            00
       マスク開始ビットアドレス [00]h                                                 00 00 00 00
       マスク bit 数       0                                                  00
       マスクデータ          [empty]                                            ―
  •    コマンド
       02 00 55 09 30 00 41 00 00 00 00 00 00 03 D4 0D
  •    レスポンス
       02 00 30 01 30 03 66 0D
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

### 8.1 ACK/レスポンス例（設定変更成功時）

| 項目 | 内容 |
|---|---|
| ACK構造 | `02 ADR 30 01 30 03 SUM 0D` |
| `CMD` | `30h`（ACK） |
| `LEN` | `01h` |
| `DATA[0]` | `30h`（詳細コマンド: UHF_SetSelectParam） |
| PDF掲載レスポンス例 | `02 00 30 01 30 03 66 0D` |
| 注意 | 成功ACKには書き込んだSelect条件値は返りません。反映確認は `55h 40h`（UHF_GetSelectParam）で読戻してください。 |

設定変更後は、対応する読み取りコマンドで読戻し確認し、RAM変更の場合は終了時に開始値へ復元してください。FLASH変更の場合は再起動後の保持も確認対象です。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 30 44 00 00 00 00 00 00 00 00 03 B4 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.3 設定依存の注意

- 設定変更またはタグメモリ変更後は、対応する読み取りコマンドで読戻し確認してください。


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
| `CMD=30h` かつ `DATA[0]` が `30h` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h 30h` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |
| `CMD=30h` だが書込値の反映を確認していない | `ACK_PENDING_VERIFY` | 必要に応じて対応する読出コマンドで読戻し確認する |

対象識別子: コマンド `55h` / 詳細 `30h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` は `LEN=01h` の固定長ACKです。書き込んだSelect条件値はACKには含まれません。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `30h`: UHF_SetSelectParam成功ACK |

`LEN` が `01h` 以外、または `DATA[0]` が `30h` 以外の場合は、このコマンドの通常成功ACKとして扱わず、別レスポンスまたは異常フレームとして分類してください。

設定書き込み系は、ACK受信後に必要なら対応する読出コマンドで読戻しし、RAM/FLASHの反映範囲と復元要否を別管理してください。

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 30h` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR、LBT_ERROR、ANTENNA_ERROR、UHF_IC_ERRORなどの主エラー |
| 2 | `error_code_2` | `error_code_1=0Ah` のUHF ICエラー時に参照 |
| 3 | `error_code_3` | UHF_Encode / UHF_BlockWrite2 等でPDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
frame = read_next_frame(timeout)
if frame is None:
    return TIMEOUT
parsed = parse_common_frame(frame)
if parsed.invalid:
    return INVALID_FRAME
if parsed.cmd == 0x31:
    return parse_nack(parsed)
if parsed.cmd == 0x30:
    return parse_ack_payload(parsed, settings_snapshot)
if parsed.cmd == 0x6C:
    return RF_TAG_DATA_ASYNC_EVENT
return UNKNOWN_RESPONSE_REQUIRES_PDF_CHECK
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

実機確認区分: `settings-change`

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

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
