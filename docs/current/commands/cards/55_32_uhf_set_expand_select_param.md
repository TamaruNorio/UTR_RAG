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
flash_operation: true
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
  - "55_42_uhf_get_expand_select_param.md"
  - "55_30_uhf_set_select_param.md"
  - "55_40_uhf_get_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_41_uhf_get_inventory_param.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "write-operation"
  - "specification-reference"
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
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

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
| FLASH操作 | あり（種類02hの場合） |
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


```

### 拡張SelectのAction表：定義と後続条件

<a id="expand-action-def"></a>

[000～011](#expand-action-low) / [100～111](#expand-action-high)へ続きます。通常Selectと異なり、拡張の初期値は001です。

```text
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
```

### 拡張SelectのAction表：000～011

<a id="expand-action-low"></a>

p.206。列順はAction、一致時のInventoried・SL、不一致時のInventoried・SL。指定Targetのみ変化。[適用条件](#expand-action-def)を併読。[100～111](#expand-action-high)。

```text
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
```

### 拡張SelectのAction表：100～111

<a id="expand-action-high"></a>

p.206。列順はAction、一致時のInventoried・SL、不一致時のInventoried・SL。指定Targetのみ変化。[適用条件](#expand-action-def)を併読。[000～011](#expand-action-low)。

```text
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
```

### 拡張Select原典：Target以降

```text



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

```

### 拡張Select原典のOR例：条件と処理のつながり

<a id="expand-or-1"></a>

p.208例1。両方Target=SL、1回目Action=000、2回目Action=001。[部分2](#expand-or-2) / [部分3](#expand-or-3)を併読。

```text
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
```

### 拡張Select原典のOR例：実行前SL=Set

<a id="expand-or-2"></a>

p.208例1。両方Target=SL、1回目Action=000、2回目Action=001。[部分1](#expand-or-1) / [部分3](#expand-or-3)を併読。列順は実行前、条件1、Select1後、条件2、Select2後。条件1または条件2に一致するとSL=Setになります。

```text
       コマンド      マスク条件 1 への         Select1   マスク条件 2 への         Select2
       実行前       [一致]／[不一致]         実行後       [一致]／[不一致]         実行後
                                                  一致               Set
                       一致             Set
                                                 不一致               Set
         Set
                                                  一致               Set
                      不一致            Reset
                                                 不一致              Reset
```

### 拡張Select原典のOR例：実行前SL=Resetと結論

<a id="expand-or-3"></a>

p.208例1。両方Target=SL、1回目Action=000、2回目Action=001。[部分1](#expand-or-1) / [部分2](#expand-or-2)を併読。列順は実行前、条件1、Select1後、条件2、Select2後。条件1または条件2に一致するとSL=Setになります。

```text
                                                  一致               Set
                       一致             Set
                                                 不一致               Set
        Reset
                                                  一致               Set
                      不一致            Reset
                                                 不一致              Reset
   以上の動作をおこなうと、[マスク条件 1]または[マスク条件 2]に一致する RF タグが
   [SL=Set]となるため、結果として論理演算の[OR]の動作をおこないます。
```

### 拡張Select原典：例2以降

```text


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

### 6.5 Actionと条件の順序

Actionの8通りのフラグ遷移は、p.206と[通常SelectのAction表](55_30_uhf_set_select_param.md)で一致します。変更するのは指定したTargetのみです。SelectのTarget（S0～S3／SL）と、InventoryのTarget（A/B）を混同しません。

p.206・208では、最初と同じTargetを使う後続SelectにAction=000または100を指定しないよう説明しています。これらは一致・不一致の両方で対象フラグを設定し、それ以前の結果を上書きするためです。**Targetが異なる場合はp.206の例外**があります。全Targetで禁止される値や、必ずNACKとなる値とは解釈しません。

#### 最初がAction=000の場合

以下は、Select1・2がともに実行され、両方のTargetがSLの場合です。P・Qを各マスクへの一致とし、SL=Setとなる条件を示します（p.208–209）。

| Select2のAction | SL=Setとなる条件 |
|---|---|
| 001 | P OR Q |
| 010 | P AND Q |
| 011 | P XOR Q |
| 101 | P AND NOT Q |
| 110 | P OR NOT Q |
| 111 | NOT (P XOR Q) |

#### 最初がAction=100の場合

同じ前提で、Select1が100の場合の表です（p.210）。

| Select2のAction | SL=Setとなる条件 |
|---|---|
| 001 | NOT P OR Q |
| 010 | NOT P AND Q |
| 011 | NOT (P XOR Q) |
| 101 | NOT (P OR Q) |
| 110 | NOT (P AND Q) |
| 111 | P XOR Q |

p.210の001の式「P NAND NOT Q」は「NOT P OR Q」と等価です。誤記として扱いません。Action=001をいつでも「通常条件とのOR」と決めつけず、最初のAction・Target・実行順を確認します。例えば順にOR、ANDを適用すると結果は(P OR Q) AND Rであり、条件順の変更は結果を変え得ます。

これらはフラグの状態遷移の整理です。最終的にQueryへ応答するには、Inventory側のSession・Sel・Targetの条件も満たす必要があります。

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. レスポンス処理

### 8.1 書込み要求と固定長ACK

要求はCMD=55h・LEN=3+23×nです。DATA[0]=32h、DATA[1]=種類、DATA[2]=n（1～7）で、DATA[3]からn個の23 byteブロックを並べます。0起点のj番目のブロックはB=3+23×j、Select(j+2)の条件です。

| n | 要求LEN | 要求総長 | 書込みACK総長 |
|---:|---|---:|---:|
| 1 | 1Ah（26） | 33 byte | 8 byte |
| 7 | A4h（164） | 171 byte | 8 byte |

ACKはCMD=30h・LEN=01h・DATA[0]=32h、総8 byte固定です（p.211）。種類、n、条件ブロックは返りません。DATA[1]を参照して種類や件数を読むことはできません。

### 8.2 判定と読戻し

1. 共通フレームの総長・固定値・SUMを検査し、CMD=30h・LEN=01h・詳細32hで成功ACKを識別します。
2. 要求側で種類・n・全条件を順序も含めて保持し、[GetExpandSelectParam](55_42_uhf_get_expand_select_param.md)で同じ種類を読戻します。
3. 各枠のMemBank・Action・Target・Truncate・開始bitアドレス・bit数・マスク対象データを照合します。16 byteの領域を受け取り、マスク対象部分と対象外部分を分けます。予約へ意味を付けません。
4. 後続枠まで影響を確認する場合は7枠を取得します。未指定枠の扱いを推測せず、最初の0 bitによる実行範囲も確認します。
5. ACK受信、読戻し一致、FLASHの再起動後保持、タグ選別の実機試験を別の結果として記録します。

### 8.3 NACK・非同期応答

NACKはCMD=31h・LEN=0Ah・総17 byteの[共通形式](../../RESPONSE_AND_NACK_MASTER.md)です。DATA[0]を要求の詳細と対応づけ、DATA[1]を主エラー、DATA[2]を主エラー0Ahの場合の追加エラーとして読みます。Encode／BlockWrite2固有の追加コードをこの設定コマンドへ転用しません。予約領域は独自解釈せず、非ゼロでもSUMに含めます。

RFタグデータや切替通知を設定要求の成功ACKへ取り込まず、ホストの待機期限切れを機器NACKと区別します。設定ACKの解析に、TID付加やアンテナID出力設定を一律必須にはしません。

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

- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)
- [55_42_uhf_get_expand_select_param](55_42_uhf_get_expand_select_param.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_40_uhf_get_select_param](55_40_uhf_get_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [55_41_uhf_get_inventory_param](55_41_uhf_get_inventory_param.md)

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
