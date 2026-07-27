---
title: "拡張ポート値の読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.12"
command_group: "reader_setting"
command_name: "拡張ポート値の読み取り"
command_byte: "4Fh"
detail_command: "A0h"
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
  - "read-extended-port"
---

# 拡張ポート値の読み取り

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **拡張ポート値の読み取り** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.12`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `4Fh` / 詳細コマンド: `A0h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、アンテナポート8CH仕様リーダライタの拡張ポートについて、現在値、機能、入出力設定、初期値を読み取ることです。

このカードには、PDF 7.4.12に記載されたコマンドフィールド、ACKデータ部5byteの意味、bit割り当て、レスポンス例を記載します。公式PDFが一次情報ですが、AIが実装・レビュー時にPDFの表を読み落とさないよう、必要な値を省略せず構造化します。

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
3. 対象機がアンテナポート8CH仕様で、拡張ポートコマンドを利用できるか確認する。
4. ACKデータ部のbit順を、bit0=拡張ポート1、bit7=拡張ポート8として展開する。
5. 予約または固定bitは、PDFで意味が定義されていない限り独自解釈しない。
6. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.4.12` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.12 拡張ポート値の読み取り
 リーダライタの「拡張ポート」の「現在値」
                    ・「機能」
                        ・「入出力設定」
                               ・「初期値」を読み取るコマンド
 です。
  ※アンテナポート8ch仕様のリーダライタの場合に有効なコマンドです。

  ［コマンド］
ラベル名 バイト数                          内容
 STX    1        02h
アドレス    1        00h（「5.2 通信フォーマットの詳細」参照）
コマンド    1        4Fh
データ長    1        01h
データ部    1        A0h（詳細コマンド）
 ETX    1        03h
 SUM    1        SUM 値（ 「5.3 SUM の計算方法」参照）
  CR    1        0Dh


 ［ACK レスポンス］
ラベル名 バイト数                          内容
 STX    1   02h
アドレス    1   00h（ 「5.2 通信フォーマットの詳細」参照）
コマンド    1   30h（ACK）
データ長    1   05h
        1   A0h（詳細コマンド）
            拡張ポートの現在値 (0: Low / 1: High)
            ビット        割り当て
            bit0       拡張ポート 1 の現在値
            bit1       拡張ポート 2 の現在値
            bit2       拡張ポート 3 の現在値
        1
            bit3       拡張ポート 4 の現在値
            bit4       拡張ポート 5 の現在値
            bit5       拡張ポート 6 の現在値
            bit6       拡張ポート 7 の現在値
データ部        bit7       拡張ポート 8 の現在値
            拡張ポートの機能
            ビット        割り当て
            bit0       [0]固定
            bit1       [0]固定
            bit2       [0]固定
        1
            bit3       [0]固定
            bit4       [0]固定
            bit5       [0]固定
            bit6       [0]固定
            bit7       [0]固定
  （次ページへ続く）


  （前ページからの続き）
ラベル名       バイト数                              内容
                      拡張ポートの入出力設定 (0: 入力 / 1: 出力)
                      ※「拡張ポートの機能」の値が「拡張ポート」に設定されて
                           いる場合のみ有効
                      ビット       割り当て
                      bit0      拡張ポート 1 の入出力設定
                      bit1      拡張ポート 2 の入出力設定
              1
                      bit2      拡張ポート 3 の入出力設定
                      bit3      拡張ポート 4 の入出力設定
                      bit4      拡張ポート 5 の入出力設定
                      bit5      拡張ポート 6 の入出力設定
                      bit6      拡張ポート 7 の入出力設定
                      bit7      拡張ポート 8 の入出力設定
                      拡張ポートの初期値 (0: Low / 1: High)
                      ビット       割り当て
                      bit0      拡張ポート 1 の初期値
                      bit1      拡張ポート 2 の初期値
                      bit2      拡張ポート 3 の初期値
              1
                      bit3      拡張ポート 4 の初期値
                      bit4      拡張ポート 5 の初期値
                      bit5      拡張ポート 6 の初期値
                      bit6      拡張ポート 7 の初期値
                      bit7      拡張ポート 8 の初期値
 ETX          1       03h
 SUM          1       SUM 値（ 「5.3 SUM の計算方法」参照）
  CR          1       0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
  • コマンド
    02 00 4F 01 A0 03 F5 0D

  •    レスポンス
       02 00 30 05 A0 7F 00 00 FF 03 58 0D

  ＜読み取った拡張ポートの現在値が[7F]h の場合＞
   [7F]h= [0111 1111]b で、最上位 bit が[拡張ポート 8]、最下位 bit が[拡張ポート 1]の
   現在値の順です。
   上記の場合、拡張ポートの現在値は、拡張ポート 8= [0: Low]、拡張ポート 1,2,3,4,5,6,7= [1:High]
   であることを表しています。
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF 7.4.12のフィールド定義に従って実装してください。

### 7.1 コマンドフレーム

| offset | ラベル名 | バイト数 | 値 | 内容 |
|---:|---|---:|---|---|
| 0 | STX | 1 | `02h` | フレーム開始 |
| 1 | アドレス | 1 | `00h` | 通常はリーダライタID。詳細はPDF 5.2参照 |
| 2 | コマンド | 1 | `4Fh` | リーダライタ設定・状態読み取り系コマンド |
| 3 | データ長 | 1 | `01h` | データ部は1byte |
| 4 | データ部[0] | 1 | `A0h` | 詳細コマンド。拡張ポート値の読み取り |
| 5 | ETX | 1 | `03h` | フレーム終了 |
| 6 | SUM | 1 | `SUM` | SUM値。PDF 5.3参照 |
| 7 | CR | 1 | `0Dh` | 終端 |

### 7.2 ACKフレーム

| offset | ラベル名 | バイト数 | 値 | 内容 |
|---:|---|---:|---|---|
| 0 | STX | 1 | `02h` | フレーム開始 |
| 1 | アドレス | 1 | `00h` | 通常はリーダライタID |
| 2 | コマンド | 1 | `30h` | ACK |
| 3 | データ長 | 1 | `05h` | ACKデータ部は5byte |
| 4 | DATA[0] | 1 | `A0h` | 詳細コマンド |
| 5 | DATA[1] | 1 | bit field | 拡張ポートの現在値 |
| 6 | DATA[2] | 1 | bit field | 拡張ポートの機能 |
| 7 | DATA[3] | 1 | bit field | 拡張ポートの入出力設定 |
| 8 | DATA[4] | 1 | bit field | 拡張ポートの初期値 |
| 9 | ETX | 1 | `03h` | フレーム終了 |
| 10 | SUM | 1 | `SUM` | SUM値 |
| 11 | CR | 1 | `0Dh` | 終端 |

### 7.3 DATA[1]: 拡張ポートの現在値

| bit | 対象 | 値`0` | 値`1` |
|---:|---|---|---|
| bit0 | 拡張ポート1 | Low | High |
| bit1 | 拡張ポート2 | Low | High |
| bit2 | 拡張ポート3 | Low | High |
| bit3 | 拡張ポート4 | Low | High |
| bit4 | 拡張ポート5 | Low | High |
| bit5 | 拡張ポート6 | Low | High |
| bit6 | 拡張ポート7 | Low | High |
| bit7 | 拡張ポート8 | Low | High |

### 7.4 DATA[2]: 拡張ポートの機能

| bit | 対象 | PDF定義 |
|---:|---|---|
| bit0 | 拡張ポート1 | `0`固定 |
| bit1 | 拡張ポート2 | `0`固定 |
| bit2 | 拡張ポート3 | `0`固定 |
| bit3 | 拡張ポート4 | `0`固定 |
| bit4 | 拡張ポート5 | `0`固定 |
| bit5 | 拡張ポート6 | `0`固定 |
| bit6 | 拡張ポート7 | `0`固定 |
| bit7 | 拡張ポート8 | `0`固定 |

### 7.5 DATA[3]: 拡張ポートの入出力設定

| bit | 対象 | 値`0` | 値`1` | 注意 |
|---:|---|---|---|---|
| bit0 | 拡張ポート1 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |
| bit1 | 拡張ポート2 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |
| bit2 | 拡張ポート3 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |
| bit3 | 拡張ポート4 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |
| bit4 | 拡張ポート5 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |
| bit5 | 拡張ポート6 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |
| bit6 | 拡張ポート7 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |
| bit7 | 拡張ポート8 | 入力 | 出力 | 機能が拡張ポートの場合のみ有効 |

### 7.6 DATA[4]: 拡張ポートの初期値

| bit | 対象 | 値`0` | 値`1` |
|---:|---|---|---|
| bit0 | 拡張ポート1 | Low | High |
| bit1 | 拡張ポート2 | Low | High |
| bit2 | 拡張ポート3 | Low | High |
| bit3 | 拡張ポート4 | Low | High |
| bit4 | 拡張ポート5 | Low | High |
| bit5 | 拡張ポート6 | Low | High |
| bit6 | 拡張ポート7 | Low | High |
| bit7 | 拡張ポート8 | Low | High |

### 7.7 PDF掲載コマンド／レスポンス例

| 種別 | Hex |
|---|---|
| TX | `02 00 4F 01 A0 03 F5 0D` |
| RX | `02 00 30 05 A0 7F 00 00 FF 03 58 0D` |

例の現在値`7Fh`は`0111 1111b`です。bit0が拡張ポート1、bit7が拡張ポート8なので、拡張ポート8はLow、拡張ポート1〜7はHighです。

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
| TX | `02 00 4F 01 A0 03 F5 0D` |
| RX | `02 00 30 05 A0 7F 00 00 FF 03 58 0D` |
| ACK CMD | `30h` |
| ACK LEN | `05h` |
| ACK DATA[0] | `A0h`。詳細コマンド |
| ACK DATA[1] | 拡張ポートの現在値 |
| ACK DATA[2] | 拡張ポートの機能 |
| ACK DATA[3] | 拡張ポートの入出力設定 |
| ACK DATA[4] | 拡張ポートの初期値 |

読み取り系は、ACKデータ部に読戻し値が入ります。実装では、`LEN=05h` と `DATA[0]=A0h` を確認してから、`DATA[1]`〜`DATA[4]` をPDF 7.4.12のフィールド定義でパースしてください。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A A0 44 00 00 00 00 00 00 00 00 03 24 0D` |
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
| `CMD=30h` かつ `LEN=05h` かつ `DATA[0]=A0h` | `ACK` | 対象コマンド `4Fh A0h` の読み取り成功ACK |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `4Fh` / 詳細 `A0h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は `A0h` です。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail_command` | `A0h`。拡張ポート値の読み取りに対するACK |
| 1 | `current_value` | 拡張ポート1〜8の現在値。bit0=ポート1、bit7=ポート8 |
| 2 | `function` | 拡張ポートの機能。PDFでは各bit `0`固定 |
| 3 | `direction` | 入出力設定。`0`=入力、`1`=出力 |
| 4 | `initial_value` | 初期値。`0`=Low、`1`=High |

固定bitや予約的な領域は、PDFで意味が定義されていない限り独自解釈しないでください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `4Fh A0h` |
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

このコマンドでは、上記に加えて、対象機がアンテナポート8CH仕様か、ACK DATA[1]〜DATA[4]をbit0=ポート1、bit7=ポート8として展開してください。

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
