---
title: "UHF_SetExpandSelectParam"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.19"
command_group: "reader_setting"
command_name: "UHF_SetExpandSelectParam"
command_byte: "55h"
detail_command: "32h"
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
  - "uhf-set-expand-select-param"
---

# UHF_SetExpandSelectParam（拡張Select条件設定）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_SetExpandSelectParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.19`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `32h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_SetExpandSelectParam** です。

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

以下は、公式PDF `7.4.19` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.19 UHF_SetExpandSelectParam
 2回目以降のSelectコマンド用のパラメータ値の設定をおこなうコマンドです。
 [UHF_SetSelectParam]コマンドにて指定したマスクに加えて、別のエリアのマスク対象を指定する
 ために使用します。必要なエリアの数だけ最大7ヶ所追加することが可能です。

  ［コマンド］
 ラベル名  バイト数                                 内容
  STX           1        02h
 アドレス           1        00h（「5.2 通信フォーマットの詳細」参照）
 コマンド           1        55h
 データ長           1        23*n+3
                1        32h（詳細コマンド）
                         パラメータ種類 ※1
                           00h   ：コマンドモード用パラメータ
                1
                           01h   ：自動読み取りモード用パラメータ
                           02h   ：FLASH データ
                1        設定するマスクデータ数 n（1～7）
                         [設定するマスクデータ数] 回繰り返します
                         パラメータ 1 ［初期値: 85h］
                                  MemBank ※左側が上位 bit
                                  00      ：RFU
                         bit0
                                  01      ：EPC(UII) ［初期値］
                         bit1
                                  10      ：TID
                                  11      ：User
                                  Action 値 ［初期値：001］
                         bit2-4
                                    詳細はパラメータ説明参照
                    1             Target 値
                                  000     ：Inventoried(S0)
 データ部
                                  001     ：Inventoried(S1)
                                  010     ：Inventoried(S2)
          23             bit5-7   011     ：Inventoried(S3)
           ×                      100     ：SL ［初期値］
          (n)                     101     ：Reserved
                                  110     ：Reserved
                                  111     ：Reserved
                         パラメータ 2 ［初期値: 00h］
                         bit0-1   将来拡張のための予約（通常は 0）
                                  Truncate 値（0 固定）
                    1
                         bit2     0       ：Disable［初期値］
                                  1       ：Enable（未サポート）
                         bit3-7   将来拡張のための予約（通常は 0）
                         マスク開始ビットアドレス ［初期値: 00 00 00 00］
                    4
                         ※MSB ファースト、ビット単位で指定
                    1    マスク bit 数     ※最大 128[bit]まで
                    16   マスクデータ （16 [byte]固定）
   （次ページへ続く）


  （前ページからの続き）

 ETX         1       03h
 SUM         1       SUM 値（「5.3 SUM の計算方法」参照）
  CR         1       0Dh
※1：パラメータ種類の詳細は「3.12.1 パラメータ種類」をご参照ください。


● 設定するマスクデータ数（1～7）
   2 回目以降の Select コマンドを送信する数を指定します。


● MemBank
   [Select]コマンドの対象のメモリ領域を指定します。   （FLASH 初期値：EPC(UII)）
   詳細は、    「4.2 RF タグのメモリ構造」の項を参照ください。
  ・RFU
    ISO18000-63 規格上の予約領域です。現在使用することはできません
    ※RF タグのメモリ領域の[00h: Reserved]とは異なります。
  ・EPC(UII)
    ビットアドレス[00]h から CRC (16[bit]) + PC (16[bit])
    ビットアドレス[20]h から EPC(UII)
  ・TID
     ビットアドレス[00]h から RF タグのユニークな ID 領域（一般的には 64[bit]または 96[bit]）
  ・USER
    ビットアドレス[00]h からユーザメモリ


● Action 値
    「マスク条件」で指定した内容に「一致」／「不一致」の RF タグに対し、「Target 値」で指定
    したフラグの状態をそれぞれどのように変化させるかを指定するパラメータです。（FLASH 初
    期値：001）
    ※「Target 値」で指定したフラグのみ変化します。
    ・2回目以降の[Select]コマンドの「Action値」の設定により、「マスク条件」は論理演算
     (AND, ORなど)されます。
    ・1回目の[Select]コマンドの「Target値」と異なる場合を除き、2回目以降の[Select]コマンド
     の「Action値」は、000(0)、100(4)以外を指定してください。詳細は後述の(例2)をご参照く
     ださい。
                           Matching                     Non-Matching
    Action
                     （マスク条件が一致）                    （マスク条件が不一致）
※左側が MSB
                  Inventoried        SL フラグ      Inventoried        SL フラグ
( )内は 10 進数
                  フラグが対象              が対象        フラグが対象              が対象
    000        Inventoried フラグ      SL フラグを   Inventoried フラグ      SL フラグを
    (0)          を[A]にセット             セット       を[B]にセット             リセット
    001        Inventoried フラグ      SL フラグを
                                                      なにもしない
    (1)          を[A]にセット             セット
    010                                       Inventoried フラグ   SL フラグを
                       なにもしない
    (2)                                         を[B]にセット         リセット
               Inventoried フラグ
    011             を反転          SL フラグを
                                                      なにもしない
    (3)          ※[A]なら[B]へ         反転
                 ※[B]なら[A]へ
    100        Inventoried フラグ   SL フラグを      Inventoried フラグ   SL フラグを
    (4)          を[B]にセット         リセット          を[A]にセット          セット
    101        Inventoried フラグ   SL フラグを
                                                      なにもしない
    (5)          を[B]にセット         リセット
    110                                       Inventoried フラグ   SL フラグを
                       なにもしない
    (6)                                         を[A]にセット          セット
                                              Inventoried フラグ
    111                                            を反転          SL フラグを
                       なにもしない
    (7)                                         ※[A]なら[B]へ         反転
                                                ※[B]なら[A]へ


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
   も反映されません。


● マスク開始 bit アドレス（FLASH 初期値：[00 00 00 00]h）
   「MemBank」で指定したメモリ領域の、「マスク条件」を設定する開始 bit アドレスを指定しま
   す。
   ※ Word アドレスではなく、bit アドレスで指定します。
   ※ 0 [Word]目の最上位 bit が bit アドレス[00]h、最下位 bit が bit アドレス[0F]h です。


● マスク bit 数
   マスク開始 bit アドレスから開始して、マスクする bit 長を指定します。
   上限 128[bit]まで指定することができます。（FLASH 初期値：0）
                                                   「マスク bit 数」
     ※[UHF_SetExpandSelectParam]コマンドで指定するマスク条件においては、
     が 0 の場合は、そのマスク条件の Select コマンドは送信されません。また、その場合、それ以
     降の番号のマスク条件が設定されている場合においても、Select コマンドは送信されません。

                                  マスク bit 数                                Select コマンドは
          Sel-1   Sel-2   Sel-3   Sel-4   Sel-5    Sel-6   Sel-7   Sel-8   何回実行されるか？

   例1       0      96      16       0      32        0       0       0     Select3 まで実行

   例2       0       0       0       0       0        0       0       0     Select1 のみ実行

   例3      32       0      16      96      96       96      16       0     Select1 のみ実行

   例4      96      16      16      32      96       96       0       0     Select6 まで実行


● マスクデータ （16 [byte]固定）
 （FLASH 初期値：[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]h）
    ・マスクデータを「byte 単位」で指定します。上限 16[byte]まで指定することができます。
     ※マスク bit 数が 8 の倍数にならない場合は、上位 bit から byte 単位で区切り、
      端数となる byte 内では下位 bit にデータを詰めて、上位 bit は 0 埋めします。
      詳細は、「7.4.17 UHF_SetSelectParam」の「マスクデータ」をご参照ください。
    ・マスクデータ長が 16 [byte]未満となる場合は、下位バイトに「00」を詰めて、16[byte]となる
     ように指定します。
        (例) EPC(UII) : 「E2 00 68 0A 00 00 40 02 3C 25 49 18」(12[byte])でマスクする場合
          「マスクデータ」 = [E2 00 68 0A 00 00 40 02 3C 25 49 18 00 00 00 00 ] h


 ● Select コマンドを 2 回以上使用した場合の RF タグのフラグ状態遷移
   ・[UHF_SetSelectParam]コマンドで指定する 1 回目の Select コマンドのマスク条件と、
    [UHF_SetExpandSelectParam]コマンドで指定する 2 回目以降の Select コマンドのマスク条件
    の組み合わせにより、RF タグのフラグの状態遷移は異なります。
   ※以下の説明では、
           「Target 値」=[SL]の場合の例を示しています。

(例 1) 1 回目の Select の Action 値 000 (0)、2 回目の Select の Action 値 001 (1)を指定した場合
 ※Action 値の説明 （必要部分を抜粋）
                                  SL フラグが対象
    Action 値    Matching（マスク条件が一致）    Non-Matching（マスク条件が不一致）
     000 (0)             SL=[Set]                SL=[Reset]
     001 (1)             SL=[Set]                なにもしない
 ・1 回目の Select の Action 値は 000(0)なので、マスク条件 1 に[一致]する RF タグは[SL=Set]とな
  り、[不一致]の RF タグは[SL = Reset]となります。
 ・2 回目の Select の Action 値は 001(1)なので、マスク条件 2 に[一致]する RF タグは[SL=Set]とな
  りますので、1 回目の Select の結果によらず[SL=Set]になります。
  マスク条件 2 に[不一致]の RF タグは、Action が[なにもしない]なので、1 回目の Select の結果が
  そのまま反映されます。
       コマンド      マスク条件 1 への         Select1   マスク条件 2 への         Select2
       実行前       [一致]／[不一致]         実行後       [一致]／[不一致]         実行後
                                                  一致               Set
                       一致             Set
                                                 不一致               Set
         Set
                                                  一致               Set
                      不一致            Reset
                                                 不一致              Reset
                                                  一致               Set
                       一致             Set
                                                 不一致               Set
        Reset
                                                  一致               Set
                      不一致            Reset
                                                 不一致              Reset
   以上の動作をおこなうと、[マスク条件 1]または[マスク条件 2]に一致する RF タグが
   [SL=Set]となるため、結果として論理演算の[OR]の動作をおこないます。

(例 2) 2 回目の Select の Action 値に、000(0)または 100 (4)を指定した場合
 ※Action 値の説明 （必要部分を抜粋）
                                   SL フラグが対象
    Action 値    Matching（マスク条件が一致）     Non-Matching（マスク条件が不一致）
     000 (0)             SL=[Set]                 SL=[Reset]
     100 (4)            SL=[Reset]                 SL=[Set]

 ・2 回目の Select の Action 値に 000(0)または 100(4)を指定すると、1 回目の Select の Action の結
  果によらず、2 回目の Select のマスク条件への[一致]／[不一致]の結果のみでフラグの状態遷移が
  決まります。
  よって、UHF_SetExpandSelectParam で 2 回目以降の Select コマンドを実行する場合には、
  Action 値は 000(0)と 100(4)は使用しないように設定します。

 ・次ページ以降に、1 回目の Select コマンドの Action 値が 000(0)の場合および 100(4)の場合におけ
  る、2 回目の Select コマンド毎の RF タグのフラグ状態遷移をまとめます。
   ※上記理由により、2 回目の Select の Action 値が 000(0)または 100(4)の場合を除外していま
    す。


● 1 回目の Select の Action 値が 000 (0)の場合
  ・1 回目の Select のマスク条件への[一致]／[不一致]を P とします。
  ・2 回目の Select のマスク条件への[一致]／[不一致]を Q とします。

  ① 2 回目の Select の Action 値が 001 (1)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致      SL = Set     SL = Set    論理式 ： P ∨ Q
      (P)    不一致      SL = Set    SL = Reset   論理演算：OR (論理和)

  ② 2 回目の Select の Action 値が 010 (2)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致
              一致      SL = Set    SL = Reset   論理式 ： P ∧ Q
      条件 1
      (P)    不一致     SL = Reset   SL = Reset   論理演算：AND (論理積)

  ③ 2 回目の Select の Action 値が 011 (3)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致
              一致     SL = Reset    SL = Set    論理式 ： P (XOR) Q
      条件 1
      (P)    不一致      SL = Set    SL = Reset   論理演算：XOR (排他的論理和)

  ④ 2 回目の Select の Action 値が 101 (5)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致     SL = Reset    SL = Set    論理式 ： P ∧ ￢Q
      (P)    不一致     SL = Reset   SL = Reset   論理演算 ： 該当なし

  ⑤ 2 回目の Select の Action 値が 110 (6)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致      SL = Set     SL = Set    論理式 ： P ∨ ￢Q
      (P)    不一致     SL = Reset    SL = Set    論理演算 ： 該当なし

  ⑥ 2 回目の Select の Action 値が 111 (7)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致      SL = Set    SL = Reset   論理式 ： ￢ ( P (XOR) Q )
      (P)    不一致     SL = Reset    SL = Set    論理演算 ： 該当なし


● 1 回目の Select の Action 値が 100 (4)の場合
  ・1 回目の Select のマスク条件への[一致]／[不一致]を P とします。
  ・2 回目の Select のマスク条件への[一致]／[不一致]を Q とします。

  ① 2 回目の Select の Action 値が 001 (1)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致      SL = Set    SL = Reset   論理式 ： P (NAND) ￢Q
      (P)    不一致      SL = Set     SL = Set    論理演算 ： 該当なし

  ② 2 回目の Select の Action 値が 010 (2)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致
              一致     SL = Reset   SL = Reset   論理式 ： ￢P ∧ Q
      条件 1
      (P)    不一致      SL = Set    SL = Reset   論理演算 ： 該当なし

  ③ 2 回目の Select の Action 値が 011 (3)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致
              一致      SL = Set    SL = Reset   論理式 ： ￢ ( P (XOR) Q )
      条件 1
      (P)    不一致     SL = Reset    SL = Set    論理演算 ： 該当なし

  ④ 2 回目の Select の Action 値が 101 (5)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致     SL = Reset   SL = Reset   論理式 ： P (NOR) Q
      (P)    不一致     SL = Reset    SL = Set    論理演算：NOR (否定論理和)

  ⑤ 2 回目の Select の Action 値が 110 (6)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致     SL = Reset    SL = Set    論理式 ： P (NAND) Q
      (P)    不一致      SL = Set     SL = Set    論理演算：NAND (否定論理積)

  ⑥ 2 回目の Select の Action 値が 111 (7)の場合
                           条件 2 ( Q )
       マスク条件
                         一致         不一致

      条件 1    一致     SL = Reset    SL = Set    論理式 ： P (XOR) Q
      (P)    不一致      SL = Set    SL = Reset   論理演算：XOR (排他的論理和)


 ［ACK レスポンス］
ラベル名 バイト数                                             内容
 STX           1      02h
アドレス           1      00h（「5.2 通信フォーマットの詳細」参照）
コマンド           1      30h（ACK）
データ長           1      01h
データ部           1      32h（詳細コマンド）
 ETX           1      03h
 SUM           1      SUM 値（「5.3 SUM の計算方法」参照）
  CR           1      0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
  以下のパラメータを書き込む場合
               データ種類                      数値／パラメータ                      コマンド列
                                       自動読み取りモード用
      書き込み対象                                                     01
                                       パラメータ
      設定するマスクデータ数 n                    1                         01
                 MemBank               11：User
                                                                 (01000111)b
      パラメータ 1    Action 値              001 (1)
                                                                  → 47
                 Target 値              010：Inventoried(S2)
      パラメータ 2    Truncate 値            0：Disable                 00
      マスク開始 bit アドレス                   4                         00 00 00 04
      マスク bit 数                        4                         04
                                                                 03 00 00 00 00 00 00 00
      マスクデータ                           3
                                                                 00 00 00 00 00 00 00 00
      ・User 領域の 4[bit]目から 4[bit]をマスクして Inventoried フラグ(S2)に対して
       Action 001 (1)を実行します。
      ・UHF_SetSelectParam で指定した 1 回目の Select の Action 値により、
       読み取りできる RF タグは異なります。

  •    コマンド
       02 00 55 1A 32 01 01 47 00 00 00 00 04 04 03 00 00 00 00 00 00 00 00 00 00 00
       00 00 00 00 03 FA 0D
  •    レスポンス
       02 00 30 01 32 03 68 0D
```

### 6.1 拡張Select条件設定ビット表

#### パラメータ1［初期値: 85h］（設定するマスクデータ数n回繰り返す構造の内側）

| bit | 項目 | 値 | 意味 |
|---:|---|---:|---|
| bit0-1 | MemBank | 00 | RFU |
| bit0-1 | MemBank | 01 | EPC(UII)［初期値］ |
| bit0-1 | MemBank | 10 | TID |
| bit0-1 | MemBank | 11 | User |
| bit2-4 | Action値 | 001 | 詳細はパラメータ説明参照 |
| bit5-7 | Target値 | 000 | Inventoried(S0) |
| bit5-7 | Target値 | 001 | Inventoried(S1) |
| bit5-7 | Target値 | 010 | Inventoried(S2) |
| bit5-7 | Target値 | 011 | Inventoried(S3) |
| bit5-7 | Target値 | 100 | SL［初期値］ |
| bit5-7 | Target値 | 101 | Reserved |
| bit5-7 | Target値 | 110 | Reserved |
| bit5-7 | Target値 | 111 | Reserved |

#### パラメータ2［初期値: 00h］

| bit | 項目 | 値 | 意味 |
|---:|---|---:|---|
| bit0-1 | 将来拡張のための予約 | 0 | 通常は0 |
| bit2 | Truncate値 | 0 | Disable［初期値］ |
| bit2 | Truncate値 | 1 | Enable（未サポート） |
| bit3-7 | 将来拡張のための予約 | 0 | 通常は0 |

注: 55_30との違いは、こちらは繰り返し構造（1～7ヶ所）を持つ点。パラメータ1の初期値も85hと81hで異なる。

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
| ACK構造 | `02 ADR 30 01 32 03 SUM 0D` |
| `CMD` | `30h`（ACK） |
| `LEN` | `01h` |
| `DATA[0]` | `32h`（詳細コマンド: UHF_SetExpandSelectParam） |
| PDF掲載レスポンス例 | `02 00 30 01 32 03 68 0D` |
| 注意 | 成功ACKには書き込んだ拡張Select条件値は返りません。反映確認は `55h 42h`（UHF_GetExpandSelectParam）で読戻してください。 |

設定変更後は、対応する読み取りコマンドで読戻し確認し、RAM変更の場合は終了時に開始値へ復元してください。FLASH変更の場合は再起動後の保持も確認対象です。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 32 44 00 00 00 00 00 00 00 00 03 B6 0D` |
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
| `CMD=30h` かつ `DATA[0]` が `32h` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h 32h` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |
| `CMD=30h` だが書込値の反映を確認していない | `ACK_PENDING_VERIFY` | 必要に応じて対応する読出コマンドで読戻し確認する |

対象識別子: コマンド `55h` / 詳細 `32h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` は `LEN=01h` の固定長ACKです。書き込んだ拡張Select条件値はACKには含まれません。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `32h`: UHF_SetExpandSelectParam成功ACK |

`LEN` が `01h` 以外、または `DATA[0]` が `32h` 以外の場合は、このコマンドの通常成功ACKとして扱わず、別レスポンスまたは異常フレームとして分類してください。

設定書き込み系は、ACK受信後に必要なら対応する読出コマンドで読戻しし、RAM/FLASHの反映範囲と復元要否を別管理してください。

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 32h` |
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
