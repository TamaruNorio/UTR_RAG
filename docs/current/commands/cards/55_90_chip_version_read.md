---
title: "チップバージョンの読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.3.9"
command_group: "reader_control"
command_name: "チップバージョンの読み取り"
command_byte: "55h"
detail_command: "90h"
subcommand: null
operation_profile: "rom-identification"
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
  - "reader-control"
  - "read-only"
  - "pass-with-notes"
---

# チップバージョンの読み取り

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **チップバージョンの読み取り** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.9`
- コマンド分類: リーダライタ制御
- 確認区分: `rom-identification`
- 操作レベル: 読み取り専用
- コマンドバイト: `55h` / 詳細コマンド: `90h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**チップバージョンの読み取り** です。

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

以下は、公式PDF `7.3.9` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.3.9   チップバージョンの読み取り
  リーダライタの内蔵チップバージョン（ファームウェアバージョン／シリアル番号）を読み取るコマ
  ンドです。
  シリアル番号は、リーダライタの製造番号(8 桁)を含む情報が返ります。

  ［コマンド］
 ラベル名 バイト数                                             内容
  STX   1               02h
 アドレス   1               00h（「5.2 通信フォーマットの詳細」参照）
 コマンド   1               55h
 データ長   1               02h
        1               90h（詳細コマンド）
                        内蔵チップバージョン
 データ部
                1         00h     ：ファームウェアバージョン取得
                          01h     ：シリアル番号取得
   ETX          1       03h
   SUM          1       SUM 値（ 「5.3 SUM の計算方法」参照）
    CR          1       0Dh


   ［ACK レスポンス：ファームウェアバージョン取得時］
 ラベル名 バイト数                          内容
  STX     1   02h
 アドレス     1   00h（「5.2 通信フォーマットの詳細」参照）
 コマンド     1   30h（ACK）
 データ長     1   0Bh
          1   90h（詳細コマンド）
          1   00h（ファームウェアバージョン取得）
 データ部     1   メジャーバージョン番号
          3   マイナーバージョン番号
          5   チップ名（例：‘UR201’）
  ETX     1   03h
  SUM     1   SUM 値（ 「5.3 SUM の計算方法」参照）
   CR     1   0Dh


    ［NACK レスポンス］
    「7.6 NACK レスポンスとエラーコード」参照。


    ［コマンド／レスポンス例］
    • コマンド
      02 00 55 02 90 00 03 EC 0D
    •    レスポンス
         02 00 30 0B 90 00 31 31 30 30 55 52 32 30 31 03 CC 0D
                           ファームウェアバージョン

          受信データ列                      31    31    30   30    55   52   32   30   31
          ファームウェアバージョン                1     1     0    0     U    R    2    0    1


  ［ACK レスポンス：シリアル番号取得時］
ラベル名 バイト数                          内容
 STX     1   02h
アドレス     1   00h（「5.2 通信フォーマットの詳細」参照）
コマンド     1   30h（ACK）
データ長     1   0Ch
         1   90h（詳細コマンド）
データ部     1   01h（シリアル番号取得）
         10  シリアル番号
 ETX     1   03h
 SUM     1   SUM 値（ 「5.3 SUM の計算方法」参照）
  CR     1   0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］

    • コマンド
       02 00 55 02 90 01 03 ED 0D
    • レスポンス
       02 00 30 0C 90 01 54 4B 30 30 30 30 32 35 31 34 03 21 0D
                                  シリアル番号

       受信データ列           54   4B     30   30    30   30   32       35   31   34
       シリアル番号           T    K      0    0     0    0    2        5    1    4
      ※上記例では、シリアル番号は「TK00002514」となります。
```

## 7. コマンド形式の扱い

このコマンドは、リーダライタ内蔵チップのファームウェアバージョンまたはシリアル番号を読み取る読み取り専用コマンドです。`DATA[1]` の指定値により、ACKの `LEN` と後続フィールドが変わります。

### 7.1 送信フレーム

| フィールド | byte数 | 値 | 意味 |
|---|---:|---|---|
| `STX` | 1 | `02h` | フレーム開始 |
| `ADR` | 1 | `00h` | 通常アドレス |
| `CMD` | 1 | `55h` | UHF系コマンド |
| `LEN` | 1 | `02h` | DATA部2byte |
| `DATA[0]` | 1 | `90h` | チップバージョンの読み取り |
| `DATA[1]` | 1 | `00h` / `01h` | `00h`=ファームウェアバージョン取得、`01h`=シリアル番号取得 |
| `ETX` | 1 | `03h` | フレーム終了 |
| `SUM` | 1 | 計算値 | `STX`から`ETX`までのSUM下位1byte |
| `CR` | 1 | `0Dh` | 終端 |

PDF掲載TX例:

| 取得対象 | TX例 |
|---|---|
| ファームウェアバージョン | `02 00 55 02 90 00 03 EC 0D` |
| シリアル番号 | `02 00 55 02 90 01 03 ED 0D` |

実装では `DATA[1]` の要求種別とACK内の `DATA[1]` が一致することを確認してください。要求と異なる応答種別は `UNEXPECTED_RESPONSE` として扱います。

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

#### ファームウェアバージョン取得時

| 項目 | 内容 |
|---|---|
| RX例 | `02 00 30 0B 90 00 31 31 30 30 55 52 32 30 31 03 CC 0D` |
| ACK判定 | `CMD=30h` / `LEN=0Bh` / `DATA[0]=90h` / `DATA[1]=00h` |

| DATA offset | byte数 | 内容 | 例 | 実装上の扱い |
|---:|---:|---|---|---|
| `DATA[0]` | 1 | `90h` | `90h` | 応答識別子 |
| `DATA[1]` | 1 | `00h` | `00h` | ファームウェアバージョン取得 |
| `DATA[2]` | 1 | メジャーバージョン番号 | `31h`=`1` | ASCIIとして読む |
| `DATA[3..5]` | 3 | マイナーバージョン番号 | `31 30 30`=`100` | ASCIIとして読む |
| `DATA[6..10]` | 5 | チップ名 | `55 52 32 30 31`=`UR201` | ASCIIとして読む |

#### シリアル番号取得時

| 項目 | 内容 |
|---|---|
| RX例 | `02 00 30 0C 90 01 54 4B 30 30 30 30 32 35 31 34 03 21 0D` |
| ACK判定 | `CMD=30h` / `LEN=0Ch` / `DATA[0]=90h` / `DATA[1]=01h` |
| SUM注意 | PDF掲載例のSUMは `21h`。ただし本書5.3方式で `STX` から `ETX` までを再計算すると `FDh` になるため、実装時は実機応答ログで要確認 |

| DATA offset | byte数 | 内容 | 例 | 実装上の扱い |
|---:|---:|---|---|---|
| `DATA[0]` | 1 | `90h` | `90h` | 応答識別子 |
| `DATA[1]` | 1 | `01h` | `01h` | シリアル番号取得 |
| `DATA[2..11]` | 10 | シリアル番号 | `54 4B 30 30 30 30 32 35 31 34`=`TK00002514` | ASCIIとして読む |

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 90 44 00 00 00 00 00 00 00 00 03 14 0D` |
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
| `CMD=30h` かつ `DATA[0]` が `90h` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h 90h` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `55h` / 詳細 `90h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は、原則として `90h` またはPDF該当節の応答識別子として扱います。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail/status` | 対象コマンドの詳細識別子または状態識別子 |
| 1.. | `payload` | PDF該当節の順序で読む。予約byteは独自解釈しない |

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 90h` |
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

実機確認区分: `rom-identification`

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
