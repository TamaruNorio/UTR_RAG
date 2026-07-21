---
title: "汎用ポート値の書き込み"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.27"
command_group: "reader_setting"
command_name: "汎用ポート値の書き込み"
command_byte: "4Eh"
detail_command: "9Fh"
subcommand: null
operation_profile: "settings-change"
operation_level: "write/configuration"
rf_emission: false
write_operation: true
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
  - "write-operation"
  - "pass-with-notes"
---

# 汎用ポート値の書き込み

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **汎用ポート値の書き込み** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.27`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `4Eh` / 詳細コマンド: `9Fh` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、リーダライタの汎用ポート1〜8のうち、指定したビットに対応するポート値だけをLow/Highへ書き換えることです。

このカードには、PDF 7.4.27に記載されたコマンドフィールド、ポート指示ビット、ポート設定値ビット、ACK条件、実動作条件を記載します。公式PDFが一次情報ですが、AIが実装・レビュー時にPDFの表を読み落とさないよう、必要な値を省略せず構造化します。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 書き込み操作 | あり |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | なし |
| タグ条件確認 | なし |
| Accessパスワード確認 | なし |
| パラメータ確認 | あり |
| 明示許可 | 必要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 書き込み対象ポートの「汎用ポートの入出力設定」が出力に設定されているか確認する。
4. 書き込むポートだけ、ポートの指示ビットを`1`にする。
5. ポートの設定値は、ポートの指示ビットが`1`のポートだけ反映されることを確認する。
6. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.4.27` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.27 汎用ポート値の書き込み
 リーダライタの「汎用ポート」の設定値を書き換えるコマンドです。
 なお、本コマンドで汎用ポート値の書き込みをおこなうためには、対象となる汎用ポートの「汎用ポ
 ートの入出力設定」が「出力」に設定されている必要があります。

 ［コマンド］
ラベル名 バイト数                          内容
 STX   1         02h
アドレス   1         00h（  「5.2 通信フォーマットの詳細」参照）
コマンド   1         4Eh
データ長   1         03h
       1         9Fh（詳細コマンド）
                 ポートの指示 (0:書き込まない / 1:書き込む)
                      [1:書き込む]が指定されたビットに割り当てられた
                      汎用ポートの値が変更されます。
                 ビット         割り当て
                 bit0        汎用ポート 1 の値
                 bit1        汎用ポート 2 の値
            1
                 bit2        汎用ポート 3 の値
                 bit3        汎用ポート 4 の値
                 bit4        汎用ポート 5 の値
                 bit5        汎用ポート 6 の値
                 bit6        汎用ポート 7 の値
                 bit7        汎用ポート 8 の値
データ部
                 ポートの設定値 (0: Low / 1: High)
                      変更後の各汎用ポートの値を指定します。
                      ポートの指示で[0:書き込まない]を指定した汎用ポートは、
                      [0]と[1]のどちらを指定しても書き込みをおこないません。
                 ビット         割り当て
                 bit0        汎用ポート 1 の値
            1    bit1        汎用ポート 2 の値
                 bit2        汎用ポート 3 の値
                 bit3        汎用ポート 4 の値
                 bit4        汎用ポート 5 の値
                 bit5        汎用ポート 6 の値
                 bit6        汎用ポート 7 の値
                 bit7        汎用ポート 8 の値
 ETX        1    03h
 SUM        1    SUM 値（   「5.3 SUM の計算方法」参照）
  CR        1    0Dh


  ［ACK レスポンス］
ラベル名 バイト数                          内容
 STX     1   02h
アドレス     1   00h（「5.2 通信フォーマットの詳細」参照）
コマンド     1   30h（ACK）
データ長     1   01h
データ部     1   9Fh（詳細コマンド）
 ETX     1   03h
 SUM     1   SUM 値（ 「5.3 SUM の計算方法」参照）
  CR     1   0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


(例) 汎用ポート 1 と 3 の値を変更し、汎用ポート 1=[0: Low]、汎用ポート 3=[1: High]
    とする場合
                            汎用ポート 8


                                       汎用ポート 7


                                                     汎用ポート 6


                                                               汎用ポート 5


                                                                         汎用ポート 4


                                                                                   汎用ポート 3


                                                                                                 汎用ポート 2


                                                                                                           汎用ポート 1
                              の値


                                         の値


                                                       の値


                                                                 の値


                                                                           の値


                                                                                     の値


                                                                                                   の値


                                                                                                             の値
         汎用ポート


      割り当てビット                   bit7    bit6          bit5      bit4      bit3      bit2          bit1      bit0
  ポートの         2 進数表示            0       0             0         0         0         1             0         1
   指示         16 進数表示                            0                                           5
  ポートの         2 進数表示           0※       0※            0※        0※        0※        1            0※         0
  設定値         16 進数表示                            0                                           4

※「ポートの指示」でビットが[1]になっていない汎用ポートは、 「ポートの設定値」に
 [0]と[1]のどちらを入れても反映されないため結果は変わりません。
上記設定とする場合、「ポートの指示」に[05]h、「ポートの設定値」に[04]h を指定します。


  ［コマンド／レスポンス例］
  • コマンド
    02 00 4E 03 9F 05 04 03 FE 0D

  •   レスポンス
      02 00 30 01 9F 03 D5 0D
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF 7.4.27のフィールド定義に従って実装してください。

### 7.1 コマンドフレーム

| offset | ラベル名 | バイト数 | 値 | 内容 |
|---:|---|---:|---|---|
| 0 | STX | 1 | `02h` | フレーム開始 |
| 1 | アドレス | 1 | `00h` | 通常はリーダライタID。詳細はPDF 5.2参照 |
| 2 | コマンド | 1 | `4Eh` | リーダライタ制御系コマンド |
| 3 | データ長 | 1 | `03h` | データ部は3byte |
| 4 | データ部[0] | 1 | `9Fh` | 詳細コマンド。汎用ポート値の書き込み |
| 5 | データ部[1] | 1 | bit field | ポートの指示。`0`=書き込まない、`1`=書き込む |
| 6 | データ部[2] | 1 | bit field | ポートの設定値。`0`=Low、`1`=High |
| 7 | ETX | 1 | `03h` | フレーム終了 |
| 8 | SUM | 1 | `SUM` | SUM値。PDF 5.3参照 |
| 9 | CR | 1 | `0Dh` | 終端 |

### 7.2 データ部[1]: ポートの指示

| bit | 対象 | 値`0` | 値`1` |
|---:|---|---|---|
| bit0 | 汎用ポート1 | 書き込まない | 書き込む |
| bit1 | 汎用ポート2 | 書き込まない | 書き込む |
| bit2 | 汎用ポート3 | 書き込まない | 書き込む |
| bit3 | 汎用ポート4 | 書き込まない | 書き込む |
| bit4 | 汎用ポート5 | 書き込まない | 書き込む |
| bit5 | 汎用ポート6 | 書き込まない | 書き込む |
| bit6 | 汎用ポート7 | 書き込まない | 書き込む |
| bit7 | 汎用ポート8 | 書き込まない | 書き込む |

### 7.3 データ部[2]: ポートの設定値

| bit | 対象 | 値`0` | 値`1` | 注意 |
|---:|---|---|---|---|
| bit0 | 汎用ポート1 | Low | High | データ部[1] bit0が`1`の場合のみ反映 |
| bit1 | 汎用ポート2 | Low | High | データ部[1] bit1が`1`の場合のみ反映 |
| bit2 | 汎用ポート3 | Low | High | データ部[1] bit2が`1`の場合のみ反映 |
| bit3 | 汎用ポート4 | Low | High | データ部[1] bit3が`1`の場合のみ反映 |
| bit4 | 汎用ポート5 | Low | High | データ部[1] bit4が`1`の場合のみ反映 |
| bit5 | 汎用ポート6 | Low | High | データ部[1] bit5が`1`の場合のみ反映 |
| bit6 | 汎用ポート7 | Low | High | データ部[1] bit6が`1`の場合のみ反映 |
| bit7 | 汎用ポート8 | Low | High | データ部[1] bit7が`1`の場合のみ反映 |

### 7.4 実動作条件

本コマンドで汎用ポート値を書き込むには、対象ポートの入出力設定が「出力」に設定されている必要があります。

ポートの指示で`0`を指定したポートは、ポートの設定値に`0`または`1`のどちらを指定しても書き込みを行いません。実装では、対象外ビットの設定値を結果判定に使わないでください。

### 7.5 PDF掲載コマンド／レスポンス例

| 種別 | Hex |
|---|---|
| TX | `02 00 4E 03 9F 05 04 03 FE 0D` |
| RX | `02 00 30 01 9F 03 D5 0D` |

この例では、ポートの指示`05h`により汎用ポート1と3だけを書き込み対象にし、ポートの設定値`04h`により汎用ポート1をLow、汎用ポート3をHighへ変更します。

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

| 項目 | 内容 |
|---|---|
| TX | `02 00 4E 03 9F 05 04 03 FE 0D` |
| RX | `02 00 30 01 9F 03 D5 0D` |
| ACK CMD | `30h` |
| ACK LEN | `01h` |
| ACK DATA[0] | `9Fh`。詳細コマンド |

ACKは通信上の正常受理を示します。実際にポート値が意図どおり変わったかは、対応する読み取りコマンドで確認してください。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 9F 44 00 00 00 00 00 00 00 00 03 23 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.3 設定依存の注意

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
| `CMD=30h` かつ `LEN=01h` かつ `DATA[0]=9Fh` | `ACK` | 対象コマンド `4Eh 9Fh` の成功ACK |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |
| `CMD=30h` だが書込値の反映を確認していない | `ACK_PENDING_VERIFY` | 必要に応じて対応する読出コマンドで読戻し確認する |

対象識別子: コマンド `4Eh` / 詳細 `9Fh` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は `9Fh` です。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail_command` | `9Fh`。汎用ポート値の書き込みに対するACK |

このACKには変更後ポート値の詳細データは含まれません。状態確認が必要な場合は `4Fh 9Fh` で読戻してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `4Eh 9Fh` |
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

このコマンドでは、上記に加えて、対象汎用ポートの機能、入出力設定、送信DATA[1]のポート指示、送信DATA[2]のポート設定値をパーサへ渡してください。
## 9. 実機確認

実機確認区分: `settings-change`

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
