---
title: "UHF_BlockErase"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.8"
command_group: "rf_tag_communication"
command_name: "UHF_BlockErase"
command_byte: "55h"
detail_command: "1Bh"
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
  - "55_1a_uhf_block_write.md"
  - "55_1e_uhf_encode.md"
  - "55_15_uhf_read.md"
  - "55_33_03_write_access_password.md"
  - "55_30_uhf_set_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
tags:
  - "utr-s201"
  - "command-card"
  - "rf-tag-communication"
  - "rf-emission"
  - "write-operation"
  - "tag-memory"
  - "requires-antenna"
  - "requires-tag"
  - "access-password"
  - "specification-reference"
  - "uhf-block-erase"
---

# UHF_BlockErase（ブロック消去）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_BlockErase** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.8`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `1Bh` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

1枚のタグの指定bank・開始Word位置・Word数で連続領域を消去します。消去後の値はタグ仕様で確認します。

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
| Accessパスワード確認 | あり |
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

以下は、公式PDF `7.5.8` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

原典照合注記: p.287の送信例のSUMは掲載E9hに対して計算値81hとなり、OPEN-016で確認待ちです。以下の転記は原典どおりに保持しています。

```text
7.5.8   UHF_BlockErase
  RFタグの連続する複数Wordのデータを消去するコマンドです。
  MemBankと、消去するアドレスおよびWord数を指定して実行します。
  消去後の値の詳細は、RFタグのデータシートをご参照ください。

  本コマンドを実行すると、ISO18000-63 規格で規定された、[Select], [Query], [Access],
  [BlockErase]などのコマンドを、リーダライタが自動的に順次実行します。
    ※リーダライタと RF タグ間で実行されるコマンドの詳細は、
                                 「3.10 RF タグ通信コマンド実行時の
     リーダライタの内部処理」をご参照ください。
    ※読み書き対象の RF タグが 1 枚となるように、あらかじめ[Select]コマンドのマスク条件や
     [Query]コマンドのパラメータを設定した状態で本コマンドを実行してください。
     複数の RF タグが応答を返す状態でコマンドを実行すると、意図しない RF タグに対して
     コマンドが実行されたり、コマンドの実行に失敗したりする可能性があります。
    ※リーダライタの Access パスワードに[0000 0000]h 以外が設定されている場合には、書き込みす
     る MemBank によらず、必ず、[Access]コマンドが発行されます。

  ※リーダライタからRFタグに対して、[BlockErase]コマンドを発行します。
   [BlockErase]コマンドは、ISO18000-63ではRFタグのオプションコマンドのため、一部のRFタグ
   のみ対応しています。詳細は「4.2.7 RFタグオプションコマンド対応表」または使用するRFタグ
   Chipのデータシートを参照ください。
    ・[BlockErase]コマンドに対応していないRFタグの内容を消去する場合には、
     [UHF_BlockWrite]コマンドや[UHF_Encode]コマンドで代用してください。

  ［コマンド］
 ラベル名 バイト数                               内容
  STX    1          02h
 アドレス    1          00h（「5.2 通信フォーマットの詳細」参照）
 コマンド    1          55h
 データ長    1          08h
               1    1Bh（詳細コマンド）
                    パラメータ 1
                           MemBank ※左側が上位 bit
                           00     ：Reserved
                    bit0
               1           01     ：EPC(UII)
                    bit1
                           10     ：TID
 データ部                      11     ：User
                    bit2-7 将来拡張のための予約（通常は 0）
                    消去開始 Word アドレス
               4
                    RF タグのメモリ上の消去開始位置（Word 単位）
                    消去 Word 数
               2    1 バイト目：上位バイト（MSB）
                    2 バイト目：下位バイト（LSB）
   ETX         1    03h
   SUM         1    SUM 値（「5.3 SUM の計算方法」参照）
    CR         1    0Dh


＜コマンドパラメータ＞
  ● MemBank
     消去するメモリ領域を指定します。
     詳細は、 「4.2RF タグのメモリ構造」の項を参照ください。
  ● 消去開始Wordアドレス
     消去するメモリの開始 Word アドレスを指定します。
  ● 消去 Word 数
     消去するメモリのサイズを Word 長（2 [byte]単位）で指定します。


［ACK レスポンス］
ラベル名 バイト数                                             内容
 STX         1      02h
アドレス         1      00h（「5.2 通信フォーマットの詳細」参照）
 ACK         1      30h
データ長         1      01h
データ部         1      1Bh（詳細コマンド）
 ETX         1      03h
 SUM         1      SUM 値（「5.3 SUM の計算方法」参照）
  CR         1      0Dh


［NACK レスポンス］
 「7.6 NACK レスポンスとエラーコード」参照。


［コマンド／レスポンス例］

    (例) User 領域の Word アドレス[00]h から 1[Word]を消去する場合
        データ種類                             数値／パラメータ           コマンド列
        MemBank                           11: USER           03
        消去開始 Word アドレス                    0                  00 00 00 00
        消去 Word 数                         1                  00 01
    • コマンド
       02 00 55 08 1B 03 00 00 00 00 00 01 03 E9 0D
    • レスポンス
       02 00 30 01 1B 03 51 0D
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答の照合ポイント

PDF §7.5.8 p.286–287の補足です。DATAは0起点で共通フレームoffset 4から始まります。

### 8.1 消去要求にはデータを付けない

CMD=55h、LEN=08h、総15 byteです。

| DATA位置 | 長さ | 内容 |
|---|---:|---|
| 0 | 1 | 詳細1Bh |
| 1 | 1 | bit1..0: 00=Reserved、01=EPC/UII、10=TID、11=User。bit2..7は予約、通常0 |
| 2..5 | 4 | 消去開始Wordアドレス |
| 6..7 | 2 | 消去Word数、上位byte・下位byteの順 |

Word数は2 byteで指定しますが、当該節には有効な最大Word数や0の意味が明記されていません。65535 Wordまで実行できる、0で全消去できる、と推測しません。4 byteアドレスのbyte順は当該欄に明記がなく、掲載例も0なので、非ゼロ指定の追加根拠は残項目です。

#### p.287の掲載SUMは確認待ち

掲載送信例のSUMはE9hですが、§5.3 p.100に従ってSTXからETXまで加算すると81hです。応答例のSUM51hは計算と一致します。送信例のE9h→81hへの訂正は[OPEN-016](../../SOURCE_REVIEW_STATUS.md)で保守者確認待ちです。例に合わせてSUMアルゴリズムを変更したり、E9hを正しい計算値とする例外を追加したりしません。訂正前の原典転記と、計算結果を区別します。

### 8.2 消去後はゼロ固定ではない

p.286は消去後の値をタグのデータシートで確認するよう指定しています。00h埋め・FFh埋めのどちらも全タグ共通の期待値にしません。BlockEraseはオプションコマンドで、一部タグのみが対応します。

未対応タグにはBlockWriteやEncodeでの代用が案内されていますが、これは別の書込み操作です。消去と同じ結果になる値・範囲をタグ仕様と利用目的で決め、失敗時に自動で別コマンドへ切り替えません。タグの復旧可否や既存データの扱いも別途確認します。

### 8.3 成功ACKは8 byte固定

成功ACKはCMD=30h、LEN=01h、DATA[0]=1Bh、総8 byteです。共通フレームの長さ・STX・ETX・CR・SUMを検査し、CMD・LEN・詳細を要求と対応づけます。bank・開始位置・処理Word数・結果データは返りません。

ADRはリーダライタIDです。タグの読取りデータを含まないこのACKへ、アンテナID出力による番号置換を一般化しません。TID付加や自動読み取り用の通知設定でACKの構造・有無を変えません。

### 8.4 対象・Access・変更後の確認

対象はSelect／Query条件で1枚に絞ります。内部Queryは設定Q値によらずQ=0ですが、一意性の保証ではありません（p.64）。リーダライタに非ゼロのAccessパスワードが設定されていればAccessを発行します（p.226）。[Access設定](55_33_03_write_access_password.md)はRAM設定で、タグのパスワード書換えとは別です。対象領域の容量・ロック・タグ固有の対応も確認します。

以下は運用上の注意です。ACK受信と期待値の読戻し一致を区別します。読取り可能な範囲は[Read](55_15_uhf_read.md)で確認できますが、同コマンドの上限は32 Wordなので、長い領域は範囲を分ける計画が必要です。変更箇所がSelectマスクに含まれる場合は変更後の対象同定も決め、失敗時に選別範囲を無条件に広げません。NACK・timeoutだけで未変更や自動的な巻戻しを保証せず、確認なしの再送をしません。

### 8.5 NACKの解釈

共通NACKはCMD=31h、LEN=0Ah、総17 byteです。DATA[0]=1Bhで要求と対応づけ、DATA[1]をコード1として読み、コード1=0Ahの場合のみDATA[2]のコード2を参照します。DATA[3]以降をBlockWrite2／Encode固有の追加コードとして解釈しません。予約byteもSUMには含めます。

[共通NACKマスタ](../../RESPONSE_AND_NACK_MASTER.md)を参照してください。コード2の[04h: メモリロック]を、コード1の04h（RFタグ無応答）と混同しません。NACKを正常なタグ0枚として扱いません。

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

- [55_1a_uhf_block_write](55_1a_uhf_block_write.md)
- [55_1e_uhf_encode](55_1e_uhf_encode.md)
- [55_15_uhf_read](55_15_uhf_read.md)
- [55_33_03_write_access_password](55_33_03_write_access_password.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [SOURCE_REVIEW_STATUS](../../SOURCE_REVIEW_STATUS.md)
- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
