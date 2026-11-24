---
title: "UHF_Read"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.3"
command_group: "rf_tag_communication"
command_name: "UHF_Read"
command_byte: "55h"
detail_command: "15h"
subcommand: null
operation_profile: "rf-read"
operation_level: "RF read"
rf_emission: true
write_operation: false
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
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
  - "../../PARAMETER_CONFIRMATION_GUIDE.md"
  - "../../AI_IMPLEMENTATION_GUARDRAILS.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../TID_MEMORY_AND_UNITS.md"
  - "../../ANTENNA_NUMBERING_SCHEMES.md"
  - "55_33_03_write_access_password.md"
  - "55_30_uhf_set_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_16_uhf_write.md"
tags:
  - "utr-s201"
  - "command-card"
  - "rf-tag-communication"
  - "rf-read"
  - "rf-emission"
  - "requires-antenna"
  - "requires-tag"
  - "specification-reference"
  - "uhf-read"
---

# UHF_Read（タグメモリ読み取り）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_Read** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.3`
- コマンド分類: rf_tag_communication
- 確認区分: `rf-read`
- 操作レベル: RF read
- コマンドバイト: `55h` / 詳細コマンド: `15h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

1枚のRFタグから、指定MemBank・Wordアドレスの1～32 Wordを読み取ります。

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
| タグメモリ操作 | あり（読取り） |
| ROM確認 | あり |
| アンテナ条件確認 | あり |
| タグ条件確認 | あり |
| Accessパスワード確認 | あり（非ゼロ設定・ロック条件。§8.3参照） |
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

以下は、公式PDF `7.5.3` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.5.3   UHF_Read
  MemBank と Word アドレスを指定し、RF タグのデータを読み取るコマンドです。
  読み取り範囲は Word 単位で指定し、一度に 1～32[Word]までの読み取りが可能です。

  本コマンドを実行すると、ISO18000-63 規格で規定された、[Select], [Query], [Access], [Read]など
  のコマンドを、リーダライタが自動的に順次実行します。
    ※リーダライタと RF タグ間で実行されるコマンドの詳細は、
                                 「3.10 RF タグ通信コマンド実行時の
     リーダライタの内部処理」をご参照ください。
    ※読み書き対象の RF タグが 1 枚となるように、あらかじめ[Select]コマンドのマスク条件や
     [Query]コマンドのパラメータを設定した状態で本コマンドを実行してください。
     複数の RF タグが応答を返す状態でコマンドを実行すると、意図しない RF タグに対して
     コマンドが実行されたり、コマンドの実行に失敗したりする可能性があります。
    ※アンテナの交信範囲にある複数枚の RF タグの指定 MemBank のデータを同時に読み取りする
     場合には、[UHF_InventoryRead]コマンドの使用も併せてご検討ください。
    ※リーダライタの Access パスワードに[0000 0000]以外が設定されている場合には、読み取りする
     MemBank によらず、必ず[Access]コマンドが発行されます。


 ［コマンド］
 ラベル名 バイト数                               内容
  STX   1          02h
 アドレス   1          00h（ 「5.2 通信フォーマットの詳細」参照）
 コマンド   1          55h
 データ長   1          07h
              1    15h（詳細コマンド）
                   パラメータ 1
                            MemBank ※左側が上位 bit
                            00     ：Reserved
                   bit0
              1             01     ：EPC(UII)
                   bit1
                            10     ：TID
 データ部
                            11     ：User
                   bit2-7   将来拡張のための予約（通常は     0）
                   読み取り開始 Word アドレス
              4
                     RF タグのメモリ上の読み取り開始位置（Word 単位）
                   読み取り Word 数
              1
                     読み出す Word 数（1～32）
   ETX        1    03h
   SUM        1    SUM 値（「5.3 SUM の計算方法」参照）
    CR        1    0Dh


＜注意事項＞
  ・[RF送信信号の制御]コマンドを「キャリアON」または「キャリアOFF→ON」の設定で実行
   し、リーダライタが「キャリアONの維持状態」で動作している場合においても、本コマンド実
   行前に[UHF_SetSelectParam]コマンドを実行して、対象となるRFタグが1枚となるようにマス
   ク指定してください。
     ※RFタグの読み取りに失敗してNACK応答となった場合、リーダライタは維持しているRFタ
      グのハンドル情報を破棄します。
      上位機器からリトライ処理を実行すると、リーダライタは[Query]コマンドを再度実行し、
      RFタグのハンドル情報を再度取得します。
      その際に、複数枚のRFタグが読み取りできる環境・設定にある場合、前回と異なるRFタグ
      のハンドルを取得する可能性があるため、必ず、一意にRFタグが読み取りできるようなマ
      スク条件を指定する必要があります。
  ・読み取るRFタグの指定MemBankがPassword Readロックされている場合、RFタグのAccessパ
   スワードと同じAccessパスワードがリーダライタに設定された状態で本コマンドを実行する必
   要があります。リーダライタにAccessパスワードを設定する場合、[Accessパスワードの書き込
   み]コマンドを使用します。
  ・リーダライタに[0000 0000]h以外のAccessパスワードが設定されている場合、本コマンド実行
   時に[Access]コマンドを発行します。RFタグのAccessパスワードと一致しない場合、[Accessパ
   スワードエラー]となり、NACK応答が返ります。


＜コマンドパラメータ＞
 ● MemBank
    読み取るメモリ領域を指定します。
    詳細は、  「4.2 RF タグのメモリ構造」の項を参照ください。

  ● 読み取り開始 Word アドレス
     指定した MemBank 上の読み取り開始位置（Word アドレス）を指定します。
      (例) Word アドレス[03]h を指定する場合は、[00 00 00 03]h を指定します。
      (例) Word アドレス[10D]h を指定する場合は、[00 00 01 0D]h を指定します。

  ● 読み取り Word 数
     読み取るメモリのサイズを Word 長（2 [byte]単位）で指定します。


［ACK レスポンス］
 ラベル名 バイト数                                          内容
 STX          1      02h
アドレス          1      00h（ 「5.2 通信フォーマットの詳細」参照）
コマンド          1      30h（ACK）
データ長          1      n+2
              1      15h（詳細コマンド）
              1      データ長 (n バイト）
                     読み取りデータ（※2-64 バイト）
データ部                 1 [byte]目     (MSB）
              n      2 [byte]目
                      |
                     n [byte]目     (LSB）
 ETX          1      03h
 SUM          1      SUM 値（   「5.3 SUM の計算方法」参照）
  CR          1      0Dh

  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
   (例) [UHF_Read]コマンドを使用して以下の RF タグデータを読み取る場合
           データ種類                         数値／パラメータ        コマンド列
           MemBank                       01: EPC(UII)    01
           読み取り開始 Word アドレス              02              00 00 00 02
           読み取り Word 数                   1               01

       •   コマンド
            02 00 55 07 15 01 00 00 00 02 01 03 7A 0D

       •   レスポンス
            02 00 30 04 15 02 <READ_DATA_BYTES> 03 B2 0D
       ※EPC(UII)領域の Word アドレス[02]h から 1[Word]の読み取りに成功し、
        [<READ_DATA_BYTES>]h を受信した場合
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答の照合ポイント

ここからはPDF §7.5.3 p.271–273の補足整理です。DATAは0起点で、共通フレームのoffset 4から始まります。§6の原典転記は保持しています。

### 8.1 要求はWord単位

CMD=55h、LEN=07h、総14 byteです。

| DATA位置 | 長さ | 内容 |
|---|---:|---|
| 0 | 1 | 詳細15h |
| 1 | 1 | bit1..0がMemBank: 00=Reserved、01=EPC/UII、10=TID、11=User。bit2..7は予約、通常0 |
| 2..5 | 4 | 開始Wordアドレス、MSB先行 |
| 6 | 1 | 読取りWord数m、1～32 |

1 Word=16 bit=2 byteです。Selectのbitアドレスや応答のbyte数と区別します。32 Wordはコマンドの上限であり、各タグ・各bankに32 Word存在する保証ではありません。0を「全領域」の指定として使いません。TIDの範囲や個体識別性は[単位・TIDガイド](../../TID_MEMORY_AND_UNITS.md)とタグ仕様で確認します。

### 8.2 ACKの二つの長さ

成功ACKはCMD=30hです。読取りデータのbyte数をnとすると、LEN=n+2、総フレーム長=n+9です。

| DATA位置 | 長さ | 内容 |
|---|---:|---|
| 0 | 1 | 詳細15h |
| 1 | 1 | 読取りデータのbyte数n（Word数ではない） |
| 2..n+1 | n | 読取りデータ、2～64 byte、MSB先行 |

1. 共通フレームのLEN＋7、STX・ETX・CR・SUMを検査する。
2. CMD=30h、LENが4～66、DATA[0]=15hであることを確認してから可変領域を読む。
3. nが2～64の偶数、LEN=n+2、さらにn=2×要求Word数mであることを確認する。
4. MemBank・開始位置はACKに返らないため要求と対応づける。1 Wordなら総11 byte、32 Wordなら総73 byteとなる。

p.273の掲載例はEPC領域Word 02hから1 Wordを読み、DATA[1]=02hに続くE2 80を得ています。E2 80だけでEPC全体やタグの一意性を確認したことにはなりません。別途のEPC・TID・RSSI・枚数フィールドを付加して解析しません。

ADRは§5.2 p.99の規則に従います。RFタグの読取りデータを返す応答ではアンテナID出力有効時に読取りアンテナ番号となり、それ以外はリーダライタIDです。[アンテナ番号ガイド](../../ANTENNA_NUMBERING_SCHEMES.md)を参照してください。これはDATAの位置や長さが変わる設定ではありません。自動読み取り用の完了通知設定を、このACKの省略条件へ転用しません。

### 8.3 対象タグとAccessパスワード

PDF §3.10.3 p.64、§7.5.3–4 p.271–275に従い、SelectとQueryの条件で対象を1枚に絞ります。Read／Write内部のQueryは設定Q値によらずQ=0です。Q=0は対象の一意性を保証せず、複数タグが応答すると別タグへの実行や失敗があり得ます。

リーダライタに非ゼロのAccessパスワードが設定されていれば、MemBankに関係なくAccessを発行します。不一致ならNACKとなり、未ロック領域でも誤ったパスワード設定を無視できません。ゼロ設定ではAccessを発行しませんが、ロックを解除・迂回する意味ではありません。対象タグのAccess対応と、読取り／書込みそれぞれのロック条件を確認します。

[Accessパスワード設定](55_33_03_write_access_password.md)はリーダライタのRAM設定であり、タグのパスワードを書き換えません。再起動・電源再投入でゼロへ戻り、設定値は読戻せません（§7.4.23 p.226–227）。本カードの`requires_access_password: true`はこの依存条件の確認を表し、常に非ゼロの秘密値が必要という意味ではありません。不要になった設定は同節に従ってゼロへ戻す運用を決めます。秘密値は公開ログに残しません。

### 8.4 NACKと再試行

共通NACKはCMD=31h、LEN=0Ah、総17 byteです。DATA[0]で要求の詳細コマンドとの対応、DATA[1]でエラーコード1を確認し、コード1=0Ahの場合だけDATA[2]のエラーコード2を解釈します。DATA[3]以降のEncode／BlockWrite2用追加コードを本コマンドへ転用しません。予約byteもSUMの計算対象です。

PDF §7.6 p.317ではコード1=04hは「RFタグ無応答」です。コード1=0Ahの場合、コード2の[04h: メモリロック]、[81h: ハンドル取得失敗]、[82h: Accessパスワードエラー]を参照します。コード1とコード2の04hを混同しません。

p.64・65の欄名は、2026-09-09の保守者訂正により「エラーコード2」で確定しました。p.64の名称は「ハンドル取得失敗」とし、81hはQuery実行時にRFタグのハンドル情報を取得できなかったことを表します。コードと名称は半角スペースで区切ります。訂正本文は[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)のOPEN-013（解決済み）を参照してください。

NACK・timeoutをInventoryの「タグ0枚の正常完了」へ置き換えません。指定領域が存在するか、アクセス可能か、選別条件に一致するかを分けて確認します。未規定の範囲外条件へエラー値や自動再試行回数を割り当てません。

### 8.5 Readに固有の運用条件

キャリア維持中のReadでNACKとなると、取得済みRFハンドルを破棄する条件がp.272にあります。再試行時に以前と同じタグのハンドルが残っていると仮定せず、対象を1枚に絞る条件を維持します。

複数タグの読取りには[InventoryRead](55_14_uhf_inventory_read.md)を検討できますが、同コマンドはAccessを発行しません。Password Read Lockされた領域を読むReadの代替にはできません（p.227）。読取り成功、対象タグの同定、全領域の取得完了は別々に記録します。

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

- [SOURCE_REVIEW_STATUS](../../SOURCE_REVIEW_STATUS.md)
- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)
- [TID_MEMORY_AND_UNITS](../../TID_MEMORY_AND_UNITS.md)
- [ANTENNA_NUMBERING_SCHEMES](../../ANTENNA_NUMBERING_SCHEMES.md)
- [55_33_03_write_access_password](55_33_03_write_access_password.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [55_16_uhf_write](55_16_uhf_write.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
- `../../RF_SAFETY_AND_CARRIER_RULES.md`
- `../../PARAMETER_CONFIRMATION_GUIDE.md`
- `../../AI_IMPLEMENTATION_GUARDRAILS.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
