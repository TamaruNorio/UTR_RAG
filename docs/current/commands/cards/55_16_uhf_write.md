---
title: "UHF_Write"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.4"
command_group: "rf_tag_communication"
command_name: "UHF_Write"
command_byte: "55h"
detail_command: "16h"
subcommand: null
operation_profile: "tag-memory-or-high-impact"
operation_level: "write/configuration"
rf_emission: true
write_operation: true
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
  - "../../SOURCE_REVIEW_STATUS.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../TID_MEMORY_AND_UNITS.md"
  - "../../ANTENNA_NUMBERING_SCHEMES.md"
  - "55_33_03_write_access_password.md"
  - "55_30_uhf_set_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_15_uhf_read.md"
tags:
  - "utr-s201"
  - "command-card"
  - "rf-tag-communication"
  - "rf-emission"
  - "write-operation"
  - "tag-memory"
  - "requires-antenna"
  - "requires-tag"
  - "specification-reference"
  - "uhf-write"
---

# UHF_Write（タグメモリ書き込み）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_Write** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.4`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `16h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

1枚のRFタグの、指定MemBank・Wordアドレスへ1 Wordを書き込みます。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | あり |
| 書き込み操作 | あり |
| FLASH操作 | なし |
| タグメモリ操作 | あり |
| ROM確認 | あり |
| アンテナ条件確認 | あり |
| タグ条件確認 | あり |
| Accessパスワード確認 | あり（非ゼロ設定・ロック条件。§8.3参照） |
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

以下は、公式PDF `7.5.4` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.5.4   UHF_Write
  MemBankとWordアドレスを指定し、RFタグにWord単位でデータを書き込むコマンドです。
  一度に1[Word]のみの書き込みが可能です。
        ※複数Wordの書き込みをおこなう場合は、[UHF_BlockWrite]コマンドを併せてご検討くださ
         い。
        ※複数MemBankへの書き込みをおこなう場合や、続けてLock処理をおこなう場合は、
         [UHF_Encode]コマンドを併せてご検討ください。

  本コマンドを実行すると、ISO18000-63 規格で規定された、[Select], [Query], [Access], [Write]など
  のコマンドを、リーダライタが自動的に順次実行します。
    ※リーダライタと RF タグ間で実行されるコマンドの詳細は、
                                 「3.10 RF タグ通信コマンド実行時の
     リーダライタの内部処理」をご参照ください。
    ※読み書き対象の RF タグが 1 枚となるように、あらかじめ[Select]コマンドのマスク条件や
     [Query]コマンドのパラメータを設定した状態で本コマンドを実行してください。
     複数の RF タグが応答を返す状態でコマンドを実行すると、意図しない RF タグに対して
     コマンドが実行されたり、コマンドの実行に失敗したりする可能性があります。
    ※リーダライタの Access パスワードに[0000 0000]h 以外が設定されている場合には、書き込みす
     る MemBank によらず、必ず、[Access]コマンドが発行されます。


 ［コマンド］
 ラベル名 バイト数                                内容
  STX   1           02h
 アドレス   1           00h（ 「5.2 通信フォーマットの詳細」参照）
 コマンド   1           55h
 データ長   1           08h
              1     16h（詳細コマンド）
                    パラメータ 1
                             MemBank ※左側が上位 bit
                             00     ：Reserved
                    bit0
              1              01     ：EPC(UII)
                    bit1
                             10     ：TID
 データ部                        11     ：User
                    bit2-7   将来拡張のための予約（通常は 0）
                    書き込み開始 Word アドレス
              4
                      RF タグのメモリ上の書き込み開始位置（Word 単位）
                    書き込みデータ
              2       1 バイト目：上位バイト（MSB）
                     2 バイト目：下位バイト（LSB）
   ETX        1     03h
   SUM        1     SUM 値（「5.3 SUM の計算方法」参照）
    CR        1     0Dh


＜注意事項＞
 ・書き込み対象のRFタグの指定MemBankがWriteロックされている場合、RFタグのAccessパス
  ワードと同じAccessパスワードがリーダライタに設定された状態で本コマンドを実行する必要
  があります。リーダライタにAccessパスワードを設定する場合、[Accessパスワードの書き込み]
  コマンドを使用します。
  ・リーダライタに[0000 0000]h以外のAccessパスワードが設定されている場合、本コマンド実行
   時に[Access]コマンドを発行します。RFタグのAccessパスワードと一致しない場合、[Accessパ
   スワードエラー]となり、NACK応答が返ります。


＜コマンドパラメータ＞
 ● MemBank
    書き込むメモリ領域を指定します。
    詳細は、  「4.2 RF タグのメモリ構造」の項を参照ください。

  ● 書き込み開始Wordアドレス
     書き込みを開始する RF タグ上のメモリの Word アドレスを指定します。

  ● 書き込みデータ
     書き込むデータを指定します。


［ACKレスポンス］
ラベル名 バイト数                                           内容
 STX          1      02h
アドレス          1      00h（「5.2 通信フォーマットの詳細」参照）
コマンド          1      30h（ACK）
データ長          1      01h
データ部          1      16h（詳細コマンド）
 ETX          1      03h
 SUM          1      SUM 値（「5.3 SUM の計算方法」参照）
  CR          1      0Dh

［NACK レスポンス］
 「7.6 NACK レスポンスとエラーコード」参照。


［コマンド／レスポンス例］
    (例) [UHF_Write]コマンドを使用して以下のパラメータを書き込む場合
         データ種類                        数値／パラメータ           コマンド列
         MemBank                      01: EPC(UII)       01
         書き込みアドレス                     01h                00 00 00 01
         書き込みデータ                      30 00              30 00
       ● コマンド
          02 00 55 08 16 01 00 00 00 01 30 00 03 AA 0D
       ● レスポンス
          02 00 30 01 16 03 4C 0D
       ※EPC(UII)領域の Word アドレス 01h への[30 00]h の書き込みに成功した場合
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答の照合ポイント

ここからはPDF §7.5.4 p.274–275の補足整理です。DATAは0起点で、共通フレームのoffset 4から始まります。§6の原典転記は保持しています。

### 8.1 1回の要求は1 Word

CMD=55h、LEN=08h、総15 byteです。Word数を指定するフィールドはありません。

| DATA位置 | 長さ | 内容 |
|---|---:|---|
| 0 | 1 | 詳細16h |
| 1 | 1 | bit1..0がMemBank: 00=Reserved、01=EPC/UII、10=TID、11=User。bit2..7は予約、通常0 |
| 2..5 | 4 | 開始Wordアドレス、MSB先行 |
| 6 | 1 | 書込み1 Wordの上位byte |
| 7 | 1 | 書込み1 Wordの下位byte |

1 Word=16 bit=2 byteです。MemBankの選択肢にあることは、対象タグのその領域が書換え可能である保証ではありません。容量・書込み可否・ロック条件はタグ仕様と照合します。複数Wordには[BlockWrite](55_1a_uhf_block_write.md)、複数bankや続くLock処理には[Encode](55_1e_uhf_encode.md)が別コマンドとして案内されています。Writeのデータ部を単純に延長しません。

### 8.2 成功ACKは8 byte固定

成功ACKはCMD=30h、LEN=01h、DATA[0]=16h、総8 byteです。MemBank、Wordアドレス、書込みデータ、枚数は返りません。

1. 共通フレームの長さ・STX・ETX・CR・SUMを検査する。
2. CMD=30h、LEN=01h、DATA[0]=16hをすべて確認する。DATA[1]以降を参照しない。
3. 送信要求と対応づけてWrite成功応答を記録する。読戻し確認済みという状態は別に記録する。

ADRは§5.2 p.99のリーダライタIDです。このACKはタグの読取りデータを含まないため、アンテナID出力による読取りアンテナ番号への置換を一般化しません。TID付加や自動読み取りの完了通知設定を理由に、この固定ACKの構造・有無を変えません。

p.275の例はEPC領域のWord 01hに30 00を書き込んでいます。ここはPC領域であり、EPC本体の開始位置はWord 02hです（§4.2 p.84–87）。30 00はEPC Lengthが6 WordとなるPC値の例で、EPC本体の12 byteを書き込む例ではありません。Stored CRCのWord 00hには書き込めません（p.85）。掲載例を目的の異なるタグへそのまま送らないでください。

### 8.3 対象タグとAccessパスワード

PDF §3.10.3 p.64、§7.5.3–4 p.271–275に従い、SelectとQueryの条件で対象を1枚に絞ります。Read／Write内部のQueryは設定Q値によらずQ=0です。Q=0は対象の一意性を保証せず、複数タグが応答すると別タグへの実行や失敗があり得ます。

リーダライタに非ゼロのAccessパスワードが設定されていれば、MemBankに関係なくAccessを発行します。不一致ならNACKとなり、未ロック領域でも誤ったパスワード設定を無視できません。ゼロ設定ではAccessを発行しませんが、ロックを解除・迂回する意味ではありません。対象タグのAccess対応と、読取り／書込みそれぞれのロック条件を確認します。

[Accessパスワード設定](55_33_03_write_access_password.md)はリーダライタのRAM設定であり、タグのパスワードを書き換えません。再起動・電源再投入でゼロへ戻り、設定値は読戻せません（§7.4.23 p.226–227）。本カードの`requires_access_password: true`はこの依存条件の確認を表し、常に非ゼロの秘密値が必要という意味ではありません。不要になった設定は同節に従ってゼロへ戻す運用を決めます。秘密値は公開ログに残しません。

### 8.4 NACKと再試行

共通NACKはCMD=31h、LEN=0Ah、総17 byteです。DATA[0]で要求の詳細コマンドとの対応、DATA[1]でエラーコード1を確認し、コード1=0Ahの場合だけDATA[2]のエラーコード2を解釈します。DATA[3]以降のEncode／BlockWrite2用追加コードを本コマンドへ転用しません。予約byteもSUMの計算対象です。

PDF §7.6 p.317ではコード1=04hは「RFタグ無応答」です。コード1=0Ahの場合、コード2の[04h: メモリロック]、[81h: ハンドル取得失敗]、[82h: Accessパスワードエラー]を参照します。コード1とコード2の04hを混同しません。

p.64・65の欄名は、2026-09-09の保守者訂正により「エラーコード2」で確定しました。p.64の名称は「ハンドル取得失敗」とし、81hはQuery実行時にRFタグのハンドル情報を取得できなかったことを表します。コードと名称は半角スペースで区切ります。訂正本文は[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)のOPEN-013（解決済み）を参照してください。

NACK・timeoutをInventoryの「タグ0枚の正常完了」へ置き換えません。指定領域が存在するか、アクセス可能か、選別条件に一致するかを分けて確認します。未規定の範囲外条件へエラー値や自動再試行回数を割り当てません。

### 8.5 書込み後の確認と復旧

以下は応答が値を返さない仕様から導く実装・運用上の注意です。ACKの受信と、期待値の読戻し一致を区別します。読取り可能な領域であれば[Read](55_15_uhf_read.md)で同じbank・Word位置を確認しますが、Read側のロックやAccess条件も満たす必要があります。

変更箇所がSelectマスクに含まれる場合、書込み後に元の条件ではタグを選べなくなる可能性があります。対象を一意に確認できる変更後の条件を事前に決め、読戻せないからといって無条件に選別範囲を広げません。

NACKやtimeoutだけで「元の値から一切変わっていない」と保証せず、結果不明として対象と状態を確認します。自動再書込み・パスワード変更・Lockを連鎖実行しません。1 Wordずつの要求であることから、複数回の書込み全体の一括成功や巻戻しを保証しません。

## 9. 実機確認

実機確認区分: `tag-memory-or-high-impact`

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
- [55_15_uhf_read](55_15_uhf_read.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
