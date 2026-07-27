---
title: "汎用ポート値の読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.11"
command_group: "reader_setting"
command_name: "汎用ポート値の読み取り"
command_byte: "4Fh"
detail_command: "9Fh"
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
  - "read-general-port"
---

# 汎用ポート値の読み取り

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **汎用ポート値の読み取り** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.11`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `4Fh` / 詳細コマンド: `9Fh` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、リーダライタの汎用ポートについて、現在値、機能、入出力設定、初期値を読み取ることです。

このカードには、PDF 7.4.11に記載されたコマンドフィールド、ACKデータ部5byteの意味、bit割り当て、初期値、レスポンス例を記載します。公式PDFが一次情報ですが、AIが実装・レビュー時にPDFの表を読み落とさないよう、必要な値を省略せず構造化します。

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

以下は、公式PDF `7.4.11` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.11   汎用ポート値の読み取り
  リーダライタの「汎用ポート」の「現在値」
                     ・「機能」
                         ・「入出力設定」
                                ・「初期値」を読み取るコマンド
  です。
   ［コマンド］
 ラベル名 バイト数                          内容
  STX    1        02h
 アドレス    1        00h（「5.2 通信フォーマットの詳細」参照）
 コマンド    1        4Fh
 データ長    1        01h
 データ部    1        9Fh（詳細コマンド）
  ETX    1        03h
  SUM    1        SUM 値（ 「5.3 SUM の計算方法」参照）
   CR    1        0Dh

  ［ACK レスポンス］
 ラベル名 バイト数                          内容
  STX    1   02h
 アドレス    1   00h（ 「5.2 通信フォーマットの詳細」参照）
 コマンド    1   30h（ACK）
 データ長    1   05h
         1   9Fh（詳細コマンド）
             汎用ポートの現在値 (0: Low / 1: High) ［初期値：B8h］
             ビット        割り当て
             bit0       汎用ポート 1 の現在値            ［初期値：0］
             bit1       汎用ポート 2 の現在値            ［初期値：0］
             bit2       汎用ポート 3 の現在値            ［初期値：0］
         1
             bit3       汎用ポート 4 の現在値            ［初期値：1］
             bit4       汎用ポート 5 の現在値            ［初期値：1］
             bit5       汎用ポート 6 の現在値            ［初期値：1］
             bit6       汎用ポート 7 の現在値            ［初期値：0］
             bit7       汎用ポート 8 の現在値            ［初期値：1］
             汎用ポートの機能 ［初期値：00h］
             ビット        割り当て
 データ部                   汎用ポート 1 の機能
             bit0       0  ：LED 制御信号出力ポート       ［初期値］
                        1  ：汎用ポート
                        汎用ポート 2 の機能
             bit1       0  ：トリガー制御信号入力ポート       ［初期値］
                        1  ：汎用ポート
         1
                        汎用ポート 3 の機能
             bit2       0  ：エラー制御信号出力ポート        ［初期値］
                        1  ：汎用ポート
             bit3-5     将来拡張のための予約（通常は 0）
                        汎用ポート 7 の機能
             bit6       0  ：ブザー制御信号出力ポート        ［初期値］
                        1  ：汎用ポート
             bit7       将来拡張のための予約（通常は 0）
    （次ページへ続く）


  （前ページからの続き）
ラベル名      バイト数                              内容
                    汎用ポートの入出力設定 (0: 入力 / 1: 出力) ［初期値：00h］
                         ※汎用ポート 1,2,3,7 は、「汎用ポートの機能」の値が
                          [汎用ポート]に設定されている場合のみ有効
                    ビット        割り当て
                    bit0       汎用ポート 1 の入出力設定           ［初期値：0］
                    bit1       汎用ポート   2 の入出力設定         ［初期値：0］
             1
                    bit2       汎用ポート 3 の入出力設定           ［初期値：0］
                    bit3       汎用ポート 4 の入出力設定           ［初期値：0］
                    bit4       汎用ポート 5 の入出力設定           ［初期値：0］
                    bit5       汎用ポート 6 の入出力設定           ［初期値：0］
                    bit6       汎用ポート 7 の入出力設定           ［初期値：0］
                    bit7       汎用ポート 8 の入出力設定           ［初期値：0］
                    汎用ポートの初期値 (0: Low / 1: High) ［初期値：[FF]h］
                    ビット        割り当て
                    bit0       汎用ポート 1 の初期値             ［初期値：1］
                    bit1       汎用ポート 2 の初期値             ［初期値：1］
                    bit2       汎用ポート 3 の初期値             ［初期値：1］
             1
                    bit3       汎用ポート 4 の初期値             ［初期値：1］
                    bit4       汎用ポート 5 の初期値             ［初期値：1］
                    bit5       汎用ポート 6 の初期値             ［初期値：1］
                    bit6       汎用ポート 7 の初期値             ［初期値：1］
                    bit7       汎用ポート 8 の初期値             ［初期値：1］
 ETX         1      03h
 SUM         1      SUM 値（  「5.3 SUM の計算方法」参照）
  CR         1      0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
    • コマンド
       02 00 4F 01 9F 03 F4 0D
    • レスポンス
       02 00 30 05 9F BA 00 00 FF 03 92 0D

  ＜読み取った汎用ポートの現在値が[BA]h の場合＞
    [BA]h= [1011 1010]b で、最上位 bit が[汎用ポート 8]、最下位 bit が[汎用ポート 1]の
    現在値の順です。上記の場合、汎用ポートの現在値は、汎用ポート 1,3,7= [0: Low]、
    汎用ポート 2,4,5,6,8= [1:High]であることを表しています。
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF 7.4.11のフィールド定義に従って実装してください。

### 7.1 コマンドフレーム

| offset | ラベル名 | バイト数 | 値 | 内容 |
|---:|---|---:|---|---|
| 0 | STX | 1 | `02h` | フレーム開始 |
| 1 | アドレス | 1 | `00h` | 通常はリーダライタID。詳細はPDF 5.2参照 |
| 2 | コマンド | 1 | `4Fh` | リーダライタ設定・状態読み取り系コマンド |
| 3 | データ長 | 1 | `01h` | データ部は1byte |
| 4 | データ部[0] | 1 | `9Fh` | 詳細コマンド。汎用ポート値の読み取り |
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
| 4 | DATA[0] | 1 | `9Fh` | 詳細コマンド |
| 5 | DATA[1] | 1 | bit field | 汎用ポートの現在値 |
| 6 | DATA[2] | 1 | bit field | 汎用ポートの機能 |
| 7 | DATA[3] | 1 | bit field | 汎用ポートの入出力設定 |
| 8 | DATA[4] | 1 | bit field | 汎用ポートの初期値 |
| 9 | ETX | 1 | `03h` | フレーム終了 |
| 10 | SUM | 1 | `SUM` | SUM値 |
| 11 | CR | 1 | `0Dh` | 終端 |

### 7.3 DATA[1]: 汎用ポートの現在値

| bit | 対象 | 値`0` | 値`1` | PDF初期値 |
|---:|---|---|---|---|
| bit0 | 汎用ポート1 | Low | High | `0` |
| bit1 | 汎用ポート2 | Low | High | `0` |
| bit2 | 汎用ポート3 | Low | High | `0` |
| bit3 | 汎用ポート4 | Low | High | `1` |
| bit4 | 汎用ポート5 | Low | High | `1` |
| bit5 | 汎用ポート6 | Low | High | `1` |
| bit6 | 汎用ポート7 | Low | High | `0` |
| bit7 | 汎用ポート8 | Low | High | `1` |

### 7.4 DATA[2]: 汎用ポートの機能

| bit | 対象 | 値`0` | 値`1` |
|---:|---|---|---|
| bit0 | 汎用ポート1 | LED制御信号出力ポート | 汎用ポート |
| bit1 | 汎用ポート2 | トリガー制御信号入力ポート | 汎用ポート |
| bit2 | 汎用ポート3 | エラー制御信号出力ポート | 汎用ポート |
| bit3-5 | 予約 | 通常`0` | PDFで意味定義なし |
| bit6 | 汎用ポート7 | ブザー制御信号出力ポート | 汎用ポート |
| bit7 | 予約 | 通常`0` | PDFで意味定義なし |

### 7.5 DATA[3]: 汎用ポートの入出力設定

| bit | 対象 | 値`0` | 値`1` | 注意 |
|---:|---|---|---|---|
| bit0 | 汎用ポート1 | 入力 | 出力 | 機能が汎用ポートの場合のみ有効 |
| bit1 | 汎用ポート2 | 入力 | 出力 | 機能が汎用ポートの場合のみ有効 |
| bit2 | 汎用ポート3 | 入力 | 出力 | 機能が汎用ポートの場合のみ有効 |
| bit3 | 汎用ポート4 | 入力 | 出力 |  |
| bit4 | 汎用ポート5 | 入力 | 出力 |  |
| bit5 | 汎用ポート6 | 入力 | 出力 |  |
| bit6 | 汎用ポート7 | 入力 | 出力 | 機能が汎用ポートの場合のみ有効 |
| bit7 | 汎用ポート8 | 入力 | 出力 |  |

### 7.6 DATA[4]: 汎用ポートの初期値

| bit | 対象 | 値`0` | 値`1` | PDF初期値 |
|---:|---|---|---|---|
| bit0 | 汎用ポート1 | Low | High | `1` |
| bit1 | 汎用ポート2 | Low | High | `1` |
| bit2 | 汎用ポート3 | Low | High | `1` |
| bit3 | 汎用ポート4 | Low | High | `1` |
| bit4 | 汎用ポート5 | Low | High | `1` |
| bit5 | 汎用ポート6 | Low | High | `1` |
| bit6 | 汎用ポート7 | Low | High | `1` |
| bit7 | 汎用ポート8 | Low | High | `1` |

### 7.7 PDF掲載コマンド／レスポンス例

| 種別 | Hex |
|---|---|
| TX | `02 00 4F 01 9F 03 F4 0D` |
| RX | `02 00 30 05 9F BA 00 00 FF 03 92 0D` |

例の現在値`BAh`は`1011 1010b`です。bit0が汎用ポート1、bit7が汎用ポート8なので、汎用ポート1,3,7はLow、汎用ポート2,4,5,6,8はHighです。

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
| TX | `02 00 4F 01 9F 03 F4 0D` |
| RX | `02 00 30 05 9F BA 00 00 FF 03 92 0D` |
| ACK CMD | `30h` |
| ACK LEN | `05h` |
| ACK DATA[0] | `9Fh`。詳細コマンド |
| ACK DATA[1] | 汎用ポートの現在値 |
| ACK DATA[2] | 汎用ポートの機能 |
| ACK DATA[3] | 汎用ポートの入出力設定 |
| ACK DATA[4] | 汎用ポートの初期値 |

読み取り系は、ACKデータ部に読戻し値が入ります。実装では、`LEN=05h` と `DATA[0]=9Fh` を確認してから、`DATA[1]`〜`DATA[4]` をPDF 7.4.11のフィールド定義でパースしてください。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 9F 44 00 00 00 00 00 00 00 00 03 23 0D` |
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
| `CMD=30h` かつ `LEN=05h` かつ `DATA[0]=9Fh` | `ACK` | 対象コマンド `4Fh 9Fh` の読み取り成功ACK |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `4Fh` / 詳細 `9Fh` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は `9Fh` です。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail_command` | `9Fh`。汎用ポート値の読み取りに対するACK |
| 1 | `current_value` | 汎用ポート1〜8の現在値。bit0=ポート1、bit7=ポート8 |
| 2 | `function` | 汎用ポート1/2/3/7の機能と予約bit |
| 3 | `direction` | 入出力設定。`0`=入力、`1`=出力 |
| 4 | `initial_value` | 初期値。`0`=Low、`1`=High |

予約bitはPDFで意味が定義されていない限り独自解釈しないでください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `4Fh 9Fh` |
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

このコマンドでは、上記に加えて、ACK DATA[1]〜DATA[4]をbit0=ポート1、bit7=ポート8として展開してください。
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
