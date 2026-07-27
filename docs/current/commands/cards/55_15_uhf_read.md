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
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_Read** です。

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
| TX | `02 00 55 07 15 01 00 00 00 02 01 03 7A 0D` |
| RX | `02 00 30 04 15 02 <READ_DATA_BYTES> 03 B2 0D` |

ACKデータ部は15h、読み取りデータ長、読み取りデータです。例ではEPC領域1Wordの読み取りデータが返っています。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 15 44 00 00 00 00 00 00 00 00 03 99 0D` |
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
| `CMD=30h` かつ `DATA[0]=15h` | `ACK` | UHF_Read成功応答。読み取りデータ長と読み取りデータをDATA内で解析する |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期タグ応答の可能性として分類し、要求応答と混同しない |
| `CMD=30h` かつ `DATA[0]=10h` `DATA[1]=02h` | `CARRIER_DETECTED` | キャリア検知応答ON時の非同期イベント候補 |

対象識別子: コマンド `55h` / 詳細 `15h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` / `DATA[0]=15h`:

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `15h`: UHF_Read |
| 1 | `read_length` | 後続の読み取りデータ長 |
| 2.. | `read_data` | `read_length` byte。実機タグ固有値は公開ログへ載せない |

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 15h` |
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
