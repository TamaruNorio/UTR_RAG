---
title: "UHF_GetSelectParam"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.2"
command_group: "reader_setting"
command_name: "UHF_GetSelectParam"
command_byte: "55h"
detail_command: "40h"
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
  - "../../TID_MEMORY_AND_UNITS.md"
  - "55_30_uhf_set_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_41_uhf_get_inventory_param.md"
  - "55_32_uhf_set_expand_select_param.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "read-only"
  - "specification-reference"
  - "uhf-get-select-param"
---

# UHF_GetSelectParam（Select条件読み取り）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_GetSelectParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.2`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `55h` / 詳細コマンド: `40h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

このコマンドの目的は、**UHF_GetSelectParam** です。

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
| パラメータ確認 | あり（種類00h／01h／02h） |
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

以下は、公式PDF `7.4.2` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.2   UHF_GetSelectParam
  Selectコマンド用のパラメータ値の取得をおこなうコマンドです。

  ［コマンド］
 ラベル名 バイト数                            内   容
  STX          1    02h
 アドレス          1    00h（「5.2 通信フォーマットの詳細」参照）
 コマンド          1    55h
 データ長          1    02h
               1    40h（詳細コマンド）
                    パラメータ種類 ※1
 データ部                 00h  ：コマンドモード用パラメータ
               1
                      01h  ：自動読み取りモード用パラメータ
                      02h  ：FLASH データ
   ETX         1    03h
   SUM         1    SUM 値（「5.3 SUM の計算方法」参照）
    CR         1    0Dh
  ※1：パラメータ種類の詳細は「3.12.1 パラメータ種類」をご参照ください。


 ［ACK レスポンス］
ラベル名 バイト数                            内   容
 STX        1    02h
アドレス        1    00h（「5.2 通信フォーマットの詳細」参照）
コマンド        1    30h（ACK）
データ長        1    9+n
            1    40h（詳細コマンド）
                 パラメータ種類
                   00h   ：コマンドモード用パラメータ
            1
                   01h   ：自動読み取りモード用パラメータ
                   02h   ：FLASH データ
                 パラメータ 1 （初期値：81h）
                       MemBank ※左側が上位 bit
                         00        ：RFU
                 bit0-1  01        ：EPC(UII)［初期値］
                         10        ：TID
                         11        ：User
                         Action 値 ［初期値：000］
                 bit2-4
                           ※左側が上位 bit、詳細はパラメータ説明参照
            1            Select の Target 値 ※左側が上位 bit
                         000       ：Inventoried(S0)
                         001       ：Inventoried(S1)
                         010       ：Inventoried(S2)
データ部             bit5-7  011       ：Inventoried(S3)
                         100       ：SL［初期値］
                         101       ：Reserved
                         110       ：Reserved
                         111       ：Reserved
                 パラメータ 2 （初期値：00h）
                 bit0-1  将来拡張のための予約（通常は 0）
                         Truncate 値（0 固定）
            1
                 bit2    0         ：Disable［初期値］
                         1         ：Enable（未サポート）
                 bit3-7  将来拡張のための予約（通常は             0）
                 マスク開始ビットアドレス ［初期値：[00 00 00 00]h］
            4
                   ※MSB ファースト
                 マスク bit 数 ［初期値：00h］
            1
                   ※最大 128[bit]まで (=[80]h)
                 マスクデータ
           (n)     ※「マスク bit 数」で指定した長さのマスクデータ
                   ※「マスク bit 数」=0 の場合は省略(n=0)
 ETX        1    03h
 SUM        1    SUM 値（「5.3 SUM の計算方法」参照）
  CR        1    0Dh
※取得した値の説明は、「7.4.12 UHF_SetSelectParam」をご参照ください。


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
    • コマンド
       02 00 55 02 40 00 03 9C 0D
    • レスポンス
       02 00 30 09 40 00 81 00 00 00 00 00 00 03 FF 0D

      バイト位置           レスポンス                              パラメータ
       3 [byte]目          [30]h        ・ACK 応答
       4 [byte]目          [09]h        ・データ長 = 9
       5 [byte]目          [40]h        ・詳細コマンド…[UHF_GetSelectParam]
       6 [byte]目          [00]h        ・パラメータ種類=[コマンドモード用パラメータ]
                                       ・Select の Target 値=[SL]
        7 [byte]目             [81]h    ・Action 値=[000(0)]
                                       ・MemBank = EPC(UII)
        8 [byte]目              [00]h   ・Truncate 値=[0: Disable]
     9-12 [byte]目     [00 00 00 00]h   ←マスク開始ビットアドレス
       13 [byte]目              [00]h   ・マスク bit 数 = 0
```

### 6.1 読取り値の意味と参照先

要求はCMD=55h・LEN=02h、DATA[0]=40h、DATA[1]=パラメータ種類00h／01h／02hです（p.153）。読み取る種類を先に決めます。

ACKのパラメータ1はbit0–1=MemBank、bit2–4=Action、bit5–7=Select Targetです。パラメータ2のTruncateは**bit2**で、bit0–1とbit3–7は予約です。初期値はパラメータ1=81h、パラメータ2=00hです。MemBank=00は使用不可のRFU、Target=101～111は予約、TruncateはDisableのみ対応します。

Actionの8通りと各フラグの状態変化は[SetSelectParamの補足](55_30_uhf_set_select_param.md)を確認します。読取り結果はリーダライタの保存設定で、タグが現在持っているS0～S3・SLの観測値ではありません。

PDF p.154末尾の参照「7.4.12 UHF_SetSelectParam」は節番号が一致しません。Ver.1.17の該当節は**7.4.17（p.190–195）**です。上の転記は保持し、本補足で正しい参照先へ案内します。

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

### 8.1 可変長ACKの位置

根拠はp.154–155です。CMD=30h、LEN=9+n、総フレーム長は16+n byteです。nはマスクデータのbyte数で、bit数ではありません。

| DATA位置 | 意味 |
|---|---|
| 0 | 詳細40h |
| 1 | パラメータ種類00h／01h／02h |
| 2 | パラメータ1（MemBank・Action・Select Target） |
| 3 | パラメータ2（Truncate・予約） |
| 4～7 | マスク開始bitアドレス、MSBファースト |
| 8 | マスクbit数b、0～128 |
| 9以降 | マスクデータn=ceil(b/8) byte。b=0なら省略 |

### 8.2 判定手順

1. 共通フレームの総長・STX／ETX／CR／SUMを検査します。CMD=30h・LEN≥9を確認してからDATA位置を参照します。
2. DATA[0]=40hと、DATA[1]が要求した種類に一致することを確認します。
3. b=DATA[8]が0～128で、n=ceil(b/8)、LEN=9+nであることを検査します。LENだけからnを決めてbit数との矛盾を見逃しません。
4. b=0ならLEN=09h・総16 byte、b=128ならLEN=19h・総32 byteです。固定16 byteのマスク領域を常に読む実装にはしません。
5. 4 byteの開始位置をMSBファーストで解釈し、端数byteの上位0埋めと各フィールドの対応を確認します。予約値や不整合値を切詰め・初期値置換して成功にしません。

要求の種類と対象機種・ROMを保持します。選別結果を検討する場合は、Inventory設定のSelect使用・Session・Sel・Inventory Target、拡張Select条件も別に確認します。読取りACKだけでそれらを取得したことにはなりません。

### 8.3 NACK・非同期応答・要求との対応

NACKはCMD=31h・LEN=0Ah・総17 byteの[共通形式](../../RESPONSE_AND_NACK_MASTER.md)です。DATA[0]の詳細を要求と対応づけ、DATA[1]を主エラー、DATA[2]を主エラー0Ahの場合の追加エラーとして読みます。Encode／BlockWrite2固有の追加コードをSelect設定へ転用しません。予約byteは意味を付けず、非ゼロでもSUMには含めます。

RFタグデータや切替通知を、この設定要求の成功ACKへ取り込みません。タイムアウトはホスト側の待機結果で、機器のNACKとは別です。設定ACKの解析に、TID付加やタグ応答のアンテナID出力設定を一律必須にはしません。

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
- [TID_MEMORY_AND_UNITS](../../TID_MEMORY_AND_UNITS.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [55_41_uhf_get_inventory_param](55_41_uhf_get_inventory_param.md)
- [55_32_uhf_set_expand_select_param](55_32_uhf_set_expand_select_param.md)

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。