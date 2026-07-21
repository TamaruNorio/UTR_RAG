---
title: "UHF_GetInventoryParam"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.3"
command_group: "reader_setting"
command_name: "UHF_GetInventoryParam"
command_byte: "55h"
detail_command: "41h"
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
requires_parameters: false
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
  - "read-only"
  - "pass-with-notes"
---

# UHF_GetInventoryParam（Inventory条件読み取り）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_GetInventoryParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.3`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `55h` / 詳細コマンド: `41h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_GetInventoryParam** です。

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
| パラメータ確認 | なし |
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

以下は、公式PDF `7.4.3` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.3   UHF_GetInventoryParam
  RFタグ読み取り時のインベントリ処理に使用するパラメータの取得をおこなうコマンドです。

  ［コマンド］
 ラベル名 バイト数                            内   容
  STX          1    02h
 アドレス          1    00h（「5.2 通信フォーマットの詳細」参照）
 コマンド          1    55h
 データ長          1    02h
               1    41h（詳細コマンド）
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
ラベル名 バイト数                             内   容
 STX        1    02h
アドレス        1    00h（「5.2 通信フォーマットの詳細」参照）
コマンド        1    30h（ACK）
データ長        1    0Bh
            1    41h（詳細コマンド）
                 パラメータ種類
                   00h     ：コマンドモード用パラメータ
            1
                   01h     ：自動読み取りモード用パラメータ
                   02h     ：FLASH データ
                 パラメータ 1 （初期値：1Fh）
                        Select コマンドの使用
                 bit0   0         ：使用しない
                        1         ：使用する［初期値］
                        Q 値の自動 UP/DOWN 機能
データ部             bit1   0         ：使用しない
                        1         ：使用する［初期値］
                        アンチコリジョン機能
            1
                 bit2   0         ：使用しない
                        1         ：使用する［初期値］
                        Q 値の開始値
                 bit3-6 0～15 ［初期値：3(0011b)］
                        ※bit3 を LSB とする 4[bit]の数値
                        Inventory の Target
                 bit7   0         ：A［初期値］
                        1         ：B
  （次ページへ続く）


  （前ページからの続き）

ラベル名     バイト数                           内   容
                 パラメータ 2 （初期値：DCh）
                        Session 値 ※左側が上位 bit
                        00       ：S0［初期値］
                 bit0-1 01       ：S1
                        10       ：S2
                        11       ：S3
                        Sel 値 ※左側が上位 bit
                        00       ：ALL
                 bit2-3 01       ：ALL
                        10       ：^SL
                        11       ：SL［初期値］
            1
                        TRext 値
                 bit4   0        ：No pilot tone （未サポート）
                        1        ：Use pilot tone ［初期値］
                        M 値 ※左側が上位 bit
                        00       ：M1(FM0) （未サポート）
                 bit5-6 01       ：M2 （未サポート）
                        10       ：M4 ［初期値］
                        11       ：M8 （未サポート）
データ部                    DR 値
                 bit7   0        ：8 （未サポート）
                        1        ：64/3 ［初期値］
                 パラメータ 3 （初期値：81h）
                        Q 値の最小値
                 bit0-3 0～15 ［初期値：1 (0001b)］
            1             ※bit0 を LSB とする 4[bit]の数値
                        Q 値の最大値
                 bit4-7 0～15 ［初期値：8 (1000b)］
                          ※bit4 を LSB とする 4[bit]の数値
                 パラメータ 4 （初期値：02h）
                        MemBank ※左側が上位 bit
                        00       ：Reserved
                 bit0-1 01       ：EPC(UII)
                        10       ：TID ［初期値］
            1
                        11       ：User
                        TID 付加
                 bit2   0        ：付加しない ［初期値］
                        1        ：付加する
                 bit3-7 将来拡張のための予約（通常は 0）
  （次ページへ続く）


  （前ページからの続き）

ラベル名      バイト数                                    内   容
                     読み取り開始 Word アドレス （初期値：[00 00 00 00]h）
             4        RF タグのメモリ上の読み取り開始位置（Word 単位）
データ部                  ※MSB ファーストで指定
                     読み取り Word 数 （初期値：02h）
             1
                      読み取りする Word 数（1～32）
 ETX         1       03h
 SUM         1       SUM 値（「5.3 SUM の計算方法」参照）
  CR         1       0Dh
※取得した値の説明は、「7.4.13 UHF_SetInventoryParam」をご参照ください。


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
    • コマンド
       02 00 55 02 41 00 03 9D 0D
    • レスポンス
       02 00 30 0B 41 00 1F DC 81 02 00 00 00 00 02 03 01 0D

       バイト位置           レスポンス                            パラメータ
         3 [byte]目          [30]h       ・ACK 応答
         4 [byte]目         [0B]h        ・データ長 = 11
         5 [byte]目          [41]h       ・詳細コマンド…[UHF_GetInventoryParam]
         6 [byte]目          [00]h       ・パラメータ種類=[コマンドモード用パラメータ]
                                        パラメータ 1
                                         ・Select コマンドの使用=[使用する]
                                         ・Q 値の自動 UP/DOWN 機能=[使用する]
         7 [byte]目             [1F]h
                                         ・アンチコリジョン機能=[使用する]
                                         ・Q 値の開始値=[3]
                                         ・Inventory の Target=[A]
                                        パラメータ 2
                                         ・Session 値=[S0]、Sel 値=[SL]
         8 [byte]目             [DC]h
                                         ・TRext 値=[Use pilot tone]
                                         ・M 値=[M4]、DR 値=[64/3]
                                        パラメータ 3
         9 [byte]目             [81]h
                                         ・Q 値の最小値=[1]、Q 値の最大値=[8]
                                        パラメータ 4
        10 [byte]目             [02]h
                                         ・MemBank=[TID]、TID 付加=[付加しない]
     11-14 [byte]目     [00 00 00 00]h   ←読み取り開始 Word アドレス
        15 [byte]目              [02]h   ・読み取り Word 数 = 2
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

### 8.1 ACK/レスポンス例（読み取り成功時）

| 項目 | 内容 |
|---|---|
| ACK構造 | `02 ADR 30 0B 41 PARAM_KIND PARAM1 PARAM2 PARAM3 PARAM4 READ_START[4] READ_WORDS 03 SUM 0D` |
| `LEN` | `0Bh` 固定 |
| `DATA[0]` | `41h`: 詳細コマンド `UHF_GetInventoryParam` |
| `DATA[1]` | パラメータ種類。`00h`=コマンドモード、`01h`=自動読み取りモード、`02h`=FLASHデータ |
| `DATA[2]` | パラメータ1。Select使用、Q自動UP/DOWN、アンチコリジョン、Q開始値、Inventory Target |
| `DATA[3]` | パラメータ2。Session、Sel、TRext、M、DR |
| `DATA[4]` | パラメータ3。Q最小値、Q最大値 |
| `DATA[5]` | パラメータ4。MemBank、TID付加、予約bit |
| `DATA[6..9]` | 読み取り開始Wordアドレス。MSBファースト |
| `DATA[10]` | 読み取りWord数。PDF上の設定範囲は1〜32 |

実装では `LEN=0Bh`、`DATA[0]=41h` を満たす場合だけ成功ACKとして扱ってください。`DATA[5].bit2` のTID付加はInventory応答長にも影響するため、起動時スナップショットに保存してください。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 41 44 00 00 00 00 00 00 00 00 03 C5 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。


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
| `CMD=30h` かつ `DATA[0]` が `41h` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h 41h` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `55h` / 詳細 `41h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は、原則として `41h` またはPDF該当節の応答識別子として扱います。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail/status` | 対象コマンドの詳細識別子または状態識別子 |
| 1.. | `payload` | PDF該当節の順序で読む。予約byteは独自解釈しない |

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 41h` |
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

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。