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
  - "../../TID_MEMORY_AND_UNITS.md"
  - "55_40_uhf_get_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_41_uhf_get_inventory_param.md"
  - "55_32_uhf_set_expand_select_param.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "write-operation"
  - "specification-reference"
  - "uhf-set-select-param"
---

# UHF_SetSelectParam（Select条件設定）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_SetSelectParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.17`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `30h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

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


```

### Select原典：EPC選別の条件

<a id="select-epc-condition"></a>

p.191。条件と[タグ別の状態表](#select-epc-states)を併読してください。

```text
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
```

### Select原典：EPC選別の状態表

<a id="select-epc-states"></a>

p.191。[条件](#select-epc-condition)：EPC先頭AB12、Target=S0、Action=000。表はEPC・実行前・一致判定・実行後の順です。

```text
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
```

### Select原典：MemBank以降

```text



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


```

### 通常SelectのAction表：定義と列名

<a id="select-action-header"></a>

[000～011](#select-action-low) / [100～111](#select-action-high)を併読。

```text
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
```

### 通常SelectのAction表：000～011

<a id="select-action-low"></a>

p.192。列順はAction、一致時のInventoried・SL、不一致時のInventoried・SL。指定Targetのみ変化します。[定義](#select-action-header) / [100～111](#select-action-high)。

```text
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
```

### 通常SelectのAction表：100～111

<a id="select-action-high"></a>

p.192。列順はAction、一致時のInventoried・SL、不一致時のInventoried・SL。指定Targetのみ変化します。[定義](#select-action-header) / [000～011](#select-action-low)。

```text
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
```

### Select原典の例1：条件

<a id="select-example1-1"></a>

p.193例1：Target=SL、Action=000。[部分2](#select-example1-2) / [部分3](#select-example1-3)を併読。

```text
(例 1) 「Target 値」=[SL]、「Action 値」=[000(0)]の場合
 ※Action 値=000(0)の SL フラグの遷移 → [一致]：SL=[Set]、[不一致]：SL=[Reset]
    ・「Target 値」=[SL]なので、「SL フラグ」のみが遷移します。
        ・マスク条件に[一致]の RF タグは、SL=[Set]となります。
        ・マスク条件に[不一致]の RF タグは、SL=[Reset]となります。
    ・「Inventoried フラグ」は遷移しません。
```

### Select原典の例1：タグ1・2

<a id="select-example1-2"></a>

p.193例1：Target=SL、Action=000。[部分1](#select-example1-1) / [部分3](#select-example1-3)を併読。列順はタグ・一致判定・実行前・実行後。

```text
                マスク条件への           Select コマンド               Select コマンド
               [一致]／[不一致]             実行前                       実行後
                              S0=[A], S1=[A], S2=[A],   S0=[A], S1=[A], S2=[A],
    RF タグ 1        一致
                              S3=[A], SL=[Reset]        S3=[A], SL=[Set]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 2        一致
                              S3=[A], SL=[Set]          S3=[A], SL=[Set]
```

### Select原典の例1：タグ3・4

<a id="select-example1-3"></a>

p.193例1：Target=SL、Action=000。[部分1](#select-example1-1) / [部分2](#select-example1-2)を併読。列順はタグ・一致判定・実行前・実行後。

```text
                              S0=[A], S1=[B], S2=[A],   S0=[A], S1=[B], S2=[A],
    RF タグ 3        不一致
                              S3=[B], SL=[Reset]        S3=[B], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 4        不一致
                              S3=[B], SL=[Set]          S3=[B], SL=[Reset]
```

### Select原典の例2：条件

<a id="select-example2-1"></a>

p.193例2：Target=SL、Action=001。[部分2](#select-example2-2) / [部分3](#select-example2-3)を併読。

```text
(例 2) 「Target 値」=[SL]、「Action 値」=[001(1)]の場合
 ※Action 値=001(1)の SL フラグの遷移 → [一致]：SL=[Set]、[不一致]：SL=[なにもしない]
    ・「Target 値」=[SL]なので、「SL フラグ」のみが遷移します。
    ・「Inventoried フラグ」は遷移しません。
```

### Select原典の例2：タグ1・2

<a id="select-example2-2"></a>

p.193例2：Target=SL、Action=001。[部分1](#select-example2-1) / [部分3](#select-example2-3)を併読。列順はタグ・一致判定・実行前・実行後。

```text
                マスク条件への           Select コマンド               Select コマンド
               [一致]／[不一致]             実行前                       実行後
                              S0=[A], S1=[A], S2=[A],   S0=[A], S1=[A], S2=[A],
    RF タグ 1        一致
                              S3=[A], SL=[Reset]        S3=[A], SL=[Set]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 2        一致
                              S3=[A], SL=[Set]          S3=[A], SL=[Set]
```

### Select原典の例2：タグ3・4

<a id="select-example2-3"></a>

p.193例2：Target=SL、Action=001。[部分1](#select-example2-1) / [部分2](#select-example2-2)を併読。列順はタグ・一致判定・実行前・実行後。

```text
                              S0=[A], S1=[B], S2=[A],   S0=[A], S1=[B], S2=[A],
    RF タグ 3        不一致
                              S3=[B], SL=[Reset]        S3=[B], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 4        不一致
                              S3=[B], SL=[Set]          S3=[B], SL=[Set]
```

### Select原典の例3：条件

<a id="select-example3-1"></a>

p.193例3：Target=S2、Action=100。[部分2](#select-example3-2) / [部分3](#select-example3-3)を併読。原典の誤記は[確定訂正](#select-example3-correction)を参照。

```text
(例 3) 「Target 値」=[S2]、「Action 値」=[100(4)]の場合
 ※Action 値=001(1)の Inventory フラグ(S2)の遷移 → [一致]：S2=[B]、不一致：S2=[A]
  ・「Target 値」=[S2]なので、「Inventoried(S2)フラグ」のみが遷移します。
  ・「SL フラグ」や S2 以外の「Inventoried フラグ」は遷移しません。
```

### Select原典の例3：タグ1・2

<a id="select-example3-2"></a>

p.193例3：Target=S2、Action=100。[部分1](#select-example3-1) / [部分3](#select-example3-3)を併読。列順はタグ・一致判定・実行前・実行後。原典の誤記は[確定訂正](#select-example3-correction)を参照。

```text
                マスク条件への           Select コマンド               Select コマンド
               [一致]／[不一致]             実行前                       実行後
                              S0=[A], S1=[A], S2=[A],   S0=[A], S1=[A], S2=[B],
    RF タグ 1        一致
                              S3=[A], SL=[Reset]        S3=[A], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[B],
    RF タグ 2        一致
                              S3=[A], SL=[Set]          S3=[A], SL=[Set]
```

### Select原典の例3：タグ3・4

<a id="select-example3-3"></a>

p.193例3：Target=S2、Action=100。[部分1](#select-example3-1) / [部分2](#select-example3-2)を併読。列順はタグ・一致判定・実行前・実行後。原典の誤記は[確定訂正](#select-example3-correction)を参照。

```text
                              S0=[A], S1=[B], S2=[A],   S0=[A], S1=[B], S2=[A],
    RF タグ 3        不一致
                              S3=[B], SL=[Reset]        S3=[B], SL=[Reset]
                              S0=[A], S1=[A], S2=[B],   S0=[A], S1=[A], S2=[A],
    RF タグ 4        不一致
                              S3=[B], SL=[Set]          S3=[B], SL=[Set]
```

### Select原典：例3の後続説明

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

### 6.1 パラメータのbit位置とAction

根拠は§7.4.17 p.190–194、読取り表は§7.4.2 p.154です。表の2進数は左側が上位bitです。

| パラメータ1の位置 | 項目 | 値 |
|---|---|---|
| bit0–1 | MemBank | 00=RFU（使用不可）、01=EPC/UII、10=TID、11=User |
| bit2–4 | Action | 000～111（下表）、初期値000 |
| bit5–7 | Select Target | 000=S0、001=S1、010=S2、011=S3、100=SL、101～111=予約 |

初期値81hはMemBank=EPC/UII、Action=000、Target=SLです。RFU=00はタグReadのReservedバンク指定とは異なり、Kill／Accessパスワードをマスク条件に使えません（p.192）。

| パラメータ2の位置 | 項目 | 値 |
|---|---|---|
| bit0–1 | 予約 | 通常0 |
| bit2 | Truncate | 0=Disableのみ対応、1=Enableは未対応 |
| bit3–7 | 予約 | 通常0 |

旧補助表の「bit1=Truncate」は誤りで、**Truncateはbit2**です。Enableを指定しても設定や実動作に反映されないというp.194の説明に従い、Enableへの設定成功をACKだけで判断しません。特定のNACKが返るとは推測しません。

#### Action: Inventoriedフラグ（指定したS0～S3の1つ）が対象

| Action（2進／10進） | 一致 | 不一致 |
|---|---|---|
| 000 / 0 | Aへ設定 | Bへ設定 |
| 001 / 1 | Aへ設定 | 変更なし |
| 010 / 2 | 変更なし | Bへ設定 |
| 011 / 3 | A/Bを反転 | 変更なし |
| 100 / 4 | Bへ設定 | Aへ設定 |
| 101 / 5 | Bへ設定 | 変更なし |
| 110 / 6 | 変更なし | Aへ設定 |
| 111 / 7 | 変更なし | A/Bを反転 |

#### Action: SLフラグが対象

| Action（2進／10進） | 一致 | 不一致 |
|---|---|---|
| 000 / 0 | Set | Reset |
| 001 / 1 | Set | 変更なし |
| 010 / 2 | 変更なし | Reset |
| 011 / 3 | 反転 | 変更なし |
| 100 / 4 | Reset | Set |
| 101 / 5 | Reset | 変更なし |
| 110 / 6 | 変更なし | Set |
| 111 / 7 | 変更なし | 反転 |

2表はp.192の状態遷移表を整理したものです。反転を「一致なら常に選択」と置き換えず、変更前の状態も考慮します。

### 6.2 マスクの単位と端数byte

根拠は§7.4.17 p.191・194です。開始位置は4 byte・MSBファーストの**bitアドレス**です。EPC本体の先頭は20h（32 bit、Wordアドレス02h相当）で、00hからのCRC・PCとは区別します。

マスク長bは0～128 bit、マスクデータのbyte数nはceil(b/8)、0～16です。b=0ではn=0としてデータを省略します。128 bitを128 byteにしません。

| bit数b | byte数n | 読取りACK／書込み要求のLEN=9+n |
|---:|---:|---:|
| 0 | 0 | 09h |
| 5 | 1 | 0Ah |
| 8 | 1 | 0Ah |
| 9 | 2 | 0Bh |
| 28 | 4 | 0Dh |
| 128 | 16 | 19h |

マスクは先頭から8 bitずつ区切ります。最後が8 bit未満なら、その最後のbyteだけは**下位側に詰め、上位を0埋め**します。開始アドレスのMSBファーストと、端数の詰め方を混同しません。これはUTRのホスト通信フィールドの規則です。

| PDF p.194の条件 | 正しいマスクデータ | 誤った例 |
|---|---|---|
| TID先頭28 bitがE2 80 11 7 | E2 80 11 07 | E2 80 11 70 |
| PC内のEPC Length 5 bitが00110 | 06 | 30（上位へ詰めた値） |

上の値は公式PDFの公開例です。既存転記に残る`<TID_PREFIX_BYTES>`では正誤の違いが見えないため、本表で補います。TIDの先頭一致だけでタグ個体の一意性を保証しません。[TIDと単位](../../TID_MEMORY_AND_UNITS.md)を併せて確認します。

### 6.3 設定変更・Select送信・タグの応答を分ける

SetSelectParamはリーダライタへの設定で、その実行だけではRFタグへSelectを送りません（p.190）。マスクbit数0でも、[Inventory設定](55_31_uhf_set_inventory_param.md)でSelect使用が有効なら、空のマスクを持つSelectを送ります。長さ0をSelect使用OFFとして扱いません。

SelectのTargetは変更するフラグ（S0～S3またはSL）、Actionは一致／不一致時の変更方法です。InventoryのTarget（A/B）とは別の設定です。対象を絞るには、Select後のQueryで使うSession・Sel・Inventory Targetも確認します（§3.10.1 p.62、§7.4.18 p.196–201）。

- Sel=ALLでも、指定SessionのInventoriedフラグとInventory Targetの一致が必要です。「ALLだから全タグ応答」とは解釈しません。
- Sel=SLではSL=Set、Sel=^SLではSL=Resetに加え、上記Session・Inventory Targetの一致も必要です。
- Selectが触らないフラグはそのままです。例えばSLだけを設定しても、S0～S3を一緒に初期化したことにはなりません。

追加条件がある場合は[拡張Select](55_32_uhf_set_expand_select_param.md)も確認します。通常条件に加えて最大7条件ですが、拡張枠でマスクbit数0に達すると、その枠も後続枠も送信されません（p.207）。通常Selectの0 bitとは意味が異なります。拡張側のマスク領域は常に16 byteで、通常側の可変長形式を流用しません。条件の順序・Action・Targetを確認して最終的なフラグ状態を判断します。

### 6.4 RAMとFLASH

00hはコマンド用RAM、01hは自動用RAM、02hはFLASHです。Select設定の両RAMは独立で、一方への書込みは他方へ反映しません。02hへの書込みはFLASHと両RAMへ反映します（§3.12 p.71–74）。[RAM/FLASHガイド](../../RAM_FLASH_IMPACT_MATRIX.md)に従い、変更前後を種類ごとに記録します。

Selectの設定値と、RFタグに保持されるフラグの状態は別です。設定の読戻し一致は、タグが指定どおり選別された実機試験の代わりにはなりません。

### 6.5 保守者による訂正: p.193 例3

<a id="select-example3-correction"></a>

2026-09-09に保守者が次の3点を訂正しました。[OPEN-012](../../SOURCE_REVIEW_STATUS.md)は解決済みです。原典転記を保持し、本注記と併せて参照します。

| 例3の※注記の箇所 | 誤 | 正 |
|---|---|---|
| Action値 | 001(1) | 100(4) |
| フラグ名 | Inventory フラグ(S2) | Inventoried(S2)フラグ |
| 不一致の表記 | 不一致 | [不一致] |

訂正後の例3の本文は以下のとおりです。

> (例3) 「Target値」=[S2]、「Action値」=[100(4)]の場合
>
> ※Action値=100(4)のInventoried(S2)フラグの遷移 → [一致]: S2=[B]、[不一致]: S2=[A]
>
> ・「Target値」=[S2]なので、「Inventoried(S2)フラグ」のみが遷移します。
>
> ・「SLフラグ」やS2以外の「Inventoriedフラグ」は遷移しません。

例3の見出し・状態遷移表と、p.192のAction=100(4)の表に整合する訂正です。p.200下部の「Inventoryフラグ → Inventoriedフラグ」も、[Inventory設定カード](55_31_uhf_set_inventory_param.md)に訂正注記を記載しています。

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. レスポンス処理

### 8.1 要求のDATA位置

CMD=55h、LEN=9+n、総フレーム長は16+n byteです。nはマスクbit数から求めたbyte数です。

| DATA位置 | 意味 |
|---|---|
| 0 | 詳細30h |
| 1 | パラメータ種類00h／01h／02h |
| 2 | パラメータ1（MemBank・Action・Select Target） |
| 3 | パラメータ2（Truncate・予約） |
| 4～7 | マスク開始bitアドレス、MSBファースト |
| 8 | マスクbit数b、0～128 |
| 9以降 | マスクデータn=ceil(b/8) byte、b=0なら省略 |

### 8.2 固定長ACKと読戻し

書込みACKはCMD=30h・LEN=01h・DATA[0]=30h、総8 byteです（p.195）。ここでCMDの30hはACK、DATA[0]の30hはSetSelectParamの詳細識別子です。パラメータ種類や設定値は返りません。

1. 共通フレームの長さ・固定値・SUMを検査し、上の3条件で書込みACKを識別します。DATA[1]は存在しないため参照しません。
2. 要求側でパラメータ種類と送った全設定を保持し、[GetSelectParam](55_40_uhf_get_select_param.md)で同じ種類を読戻します。ACKだけで種類やマスクの反映一致を記録しません。
3. MemBank・Action・Select Target・Truncate・開始bitアドレス・bit数・マスクを照合します。予約は意味を付けず、未対応Truncateを反映済みとしません。
4. FLASHを変更した場合は両RAMへの影響も確認します。ACK受信、読戻し一致、再起動後保持、タグ選別の実機結果を別々に記録します。

### 8.3 NACK・非同期応答・要求との対応

NACKはCMD=31h・LEN=0Ah・総17 byteの[共通形式](../../RESPONSE_AND_NACK_MASTER.md)です。DATA[0]の詳細を要求と対応づけ、DATA[1]を主エラー、DATA[2]を主エラー0Ahの場合の追加エラーとして読みます。Encode／BlockWrite2固有の追加コードをSelect設定へ転用しません。予約byteは意味を付けず、非ゼロでもSUMには含めます。

RFタグデータや切替通知を、この設定要求の成功ACKへ取り込みません。タイムアウトはホスト側の待機結果で、機器のNACKとは別です。設定ACKの解析に、TID付加やタグ応答のアンテナID出力設定を一律必須にはしません。

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
- [TID_MEMORY_AND_UNITS](../../TID_MEMORY_AND_UNITS.md)
- [55_40_uhf_get_select_param](55_40_uhf_get_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [55_41_uhf_get_inventory_param](55_41_uhf_get_inventory_param.md)
- [55_32_uhf_set_expand_select_param](55_32_uhf_set_expand_select_param.md)

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
