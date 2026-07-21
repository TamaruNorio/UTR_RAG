---
title: "FLASH設定値の読み取り(1バイトアクセス)"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.13"
command_group: "reader_setting"
command_name: "FLASH設定値の読み取り(1バイトアクセス)"
command_byte: "4Fh"
detail_command: "B4h"
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

# FLASH設定値の読み取り(1バイトアクセス)

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **FLASH設定値の読み取り(1バイトアクセス)** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.13`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: read-only
- コマンドバイト: `4Fh` / 詳細コマンド: `B4h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、FLASH設定値を指定アドレスから1byte単位で読み取ることです。

このカードには、PDF 7.4.13に記載されたコマンドフィールド、読み取りアドレス、ACKデータ部のFLASH設定値、レスポンス例を記載します。公式PDFが一次情報ですが、AIが実装・レビュー時にPDFの表を読み落とさないよう、必要な値を省略せず構造化します。

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
| パラメータ確認 | あり |
| 明示許可 | 不要または通常不要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 読み取り対象FLASHアドレスをPDF 9.1 FLASHアドレス一覧で確認する。
4. ACKデータ部の `DATA[1]` を、指定アドレスのFLASH設定値として扱う。
5. 読み取った値の意味は、アドレスごとの定義に従って解釈する。
6. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.4.13` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.13 FLASH 設定値の読み取り(1 バイトアクセス)
 FLASH設定値をアドレス単位（1 バイト単位）で読み取るコマンドです。
 FLASHアドレスの一覧は、
              「9.1 FLASHアドレス一覧」をご参照ください。

 ［コマンド］
ラベル名 バイト数                                       内容
 STX         1     02h
アドレス         1     00h（「5.2 通信フォーマットの詳細」参照）
コマンド         1     4Fh
データ長         1     02h
             1     B4h（詳細コマンド）
データ部
             1     読み取りアドレス
 ETX         1     03h
 SUM         1     SUM 値（「5.3 SUM の計算方法」参照）
  CR         1     0Dh


 ［ACK レスポンス］
ラベル名 バイト数                                       内容
 STX         1     02h
アドレス         1     00h（「5.2 通信フォーマットの詳細」参照）
 ACK         1     30h（ACK）
データ長         1     02h
             1     B4h（詳細コマンド）
データ部
             1     FLASH 設定値
 ETX         1     03h
 SUM         1     SUM 値（「5.3 SUM の計算方法」参照）
  CR         1     0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
    FLASH のアドレス 94([5B]h)に格納されている、
                                 「Write コマンドタイムアウト時間(msec)」を
    読み取った結果、[14]h (=20) が返ってきた場合
    • コマンド
      02 00 4F 02 B4 5B 03 65 0D
                      ↑ アドレス 94 (=[5B]h)
    • レスポンス
      02 00 30 02 B4 14 03 FF 0D
                      ↑ FLASH 設定値 [14]h (=20)
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF 7.4.13のフィールド定義に従って実装してください。

### 7.1 コマンドフレーム

| offset | ラベル名 | バイト数 | 値 | 内容 |
|---:|---|---:|---|---|
| 0 | STX | 1 | `02h` | フレーム開始 |
| 1 | アドレス | 1 | `00h` | 通常はリーダライタID。詳細はPDF 5.2参照 |
| 2 | コマンド | 1 | `4Fh` | リーダライタ設定・状態読み取り系コマンド |
| 3 | データ長 | 1 | `02h` | データ部は2byte |
| 4 | データ部[0] | 1 | `B4h` | 詳細コマンド。FLASH設定値の読み取り |
| 5 | データ部[1] | 1 | address | 読み取りアドレス。PDF 9.1参照 |
| 6 | ETX | 1 | `03h` | フレーム終了 |
| 7 | SUM | 1 | `SUM` | SUM値。PDF 5.3参照 |
| 8 | CR | 1 | `0Dh` | 終端 |

### 7.2 ACKフレーム

| offset | ラベル名 | バイト数 | 値 | 内容 |
|---:|---|---:|---|---|
| 0 | STX | 1 | `02h` | フレーム開始 |
| 1 | アドレス | 1 | `00h` | 通常はリーダライタID |
| 2 | コマンド | 1 | `30h` | ACK |
| 3 | データ長 | 1 | `02h` | ACKデータ部は2byte |
| 4 | DATA[0] | 1 | `B4h` | 詳細コマンド |
| 5 | DATA[1] | 1 | value | FLASH設定値 |
| 6 | ETX | 1 | `03h` | フレーム終了 |
| 7 | SUM | 1 | `SUM` | SUM値 |
| 8 | CR | 1 | `0Dh` | 終端 |

### 7.3 データ部[1]: 読み取りアドレス

読み取り対象のFLASHアドレスを1byteのHex値で指定します。アドレスの意味はPDF 9.1 FLASHアドレス一覧を一次情報として確認してください。

### 7.4 ACK DATA[1]: FLASH設定値

ACKの `DATA[1]` が、指定したFLASHアドレスに格納されている1byte設定値です。値の意味、単位、bit割り当てはアドレスごとに異なります。

### 7.5 PDF掲載コマンド／レスポンス例

| 種別 | Hex | 意味 |
|---|---|---|
| TX | `02 00 4F 02 B4 5B 03 65 0D` | FLASHアドレス`5Bh`を読み取り |
| RX | `02 00 30 02 B4 14 03 FF 0D` | FLASH設定値`14h`を返す |

この例では、FLASHアドレス`5Bh`に格納されているWriteコマンドタイムアウト時間を読み取り、`14h`、つまり20msecが返っています。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理、アドレス別デコードを分けて設計してください。

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
| TX | `02 00 4F 02 B4 5B 03 65 0D` |
| RX | `02 00 30 02 B4 14 03 FF 0D` |
| ACK CMD | `30h` |
| ACK LEN | `02h` |
| ACK DATA[0] | `B4h`。詳細コマンド |
| ACK DATA[1] | FLASH設定値。この例では`14h` |

読み取り系は、ACKデータ部に読戻し値が入ります。実装では、`LEN=02h` と `DATA[0]=B4h` を確認してから、`DATA[1]` を指定アドレスのFLASH設定値としてパースしてください。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A B4 44 00 00 00 00 00 00 00 00 03 38 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.3 設定依存の注意

- FLASH変更は再起動後保持され、RAM設定を上書きする場合があります。
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
| `CMD=30h` かつ `LEN=02h` かつ `DATA[0]=B4h` | `ACK` | 対象コマンド `4Fh B4h` の読み取り成功ACK |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `4Fh` / 詳細 `B4h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は `B4h` です。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail_command` | `B4h`。FLASH設定値の読み取りに対するACK |
| 1 | `flash_value` | 指定アドレスのFLASH設定値 |

`flash_value` の意味は読み取りアドレスに依存します。PDF 9.1 FLASHアドレス一覧でデコードしてください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `4Fh B4h` |
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

このコマンドでは、上記に加えて、読み取りFLASHアドレスとACK DATA[1]のFLASH設定値をパーサへ渡してください。
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
