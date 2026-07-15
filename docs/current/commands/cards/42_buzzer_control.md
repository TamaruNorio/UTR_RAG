---
title: "ブザーの制御"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.3.2"
command_group: "reader_control"
command_name: "ブザーの制御"
command_byte: "42h"
detail_command: null
subcommand: null
operation_profile: "needs-metadata-confirmation"
operation_level: "reader-control"
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
  - "reader-control"
  - "requires-parameters"
  - "pass-with-notes"
---

# ブザーの制御

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **ブザーの制御** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.2`
- コマンド分類: リーダライタ制御
- 確認区分: `needs-metadata-confirmation`
- 操作レベル: reader-control
- コマンドバイト: `42h` / 詳細コマンド: `null` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、リーダライタのブザーを指定した鳴動パターンで鳴らすことです。

このカードには、PDF 7.3.2に記載されたコマンドフィールド、指定可能なブザー音、ACK条件、実動作条件を記載します。公式PDFが一次情報ですが、AIが実装・レビュー時にPDFの表を読み落とさないよう、必要な値を省略せず構造化します。

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
3. 汎用ポート7の機能が、ブザー制御信号出力ポートに設定されているか確認する。
4. 応答要求を `00h` にするか `01h` にするか決める。
5. ブザー音を `00h` から `08h` の定義済み値から選ぶ。
6. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。

## 6. コマンド形式の扱い

コマンド形式は、共通フレームとPDF 7.3.2のフィールド定義に従って実装してください。

### 6.1 コマンドフレーム

| offset | ラベル名 | バイト数 | 値 | 内容 |
|---:|---|---:|---|---|
| 0 | STX | 1 | `02h` | フレーム開始 |
| 1 | アドレス | 1 | `00h` | 通常はリーダライタID。詳細はPDF 5.2参照 |
| 2 | コマンド | 1 | `42h` | ブザーの制御 |
| 3 | データ長 | 1 | `02h` | データ部は2byte |
| 4 | データ部[0] | 1 | `00h` または `01h` | リーダライタへの応答要求 |
| 5 | データ部[1] | 1 | `00h` から `08h` | ブザー音 |
| 6 | ETX | 1 | `03h` | フレーム終了 |
| 7 | SUM | 1 | `SUM` | SUM値。PDF 5.3参照 |
| 8 | CR | 1 | `0Dh` | 終端 |

### 6.2 データ部[0]: リーダライタへの応答要求

| 値 | 意味 | レスポンス処理 |
|---|---|---|
| `00h` | 応答を要求しない | 正常時、リーダライタはレスポンスを返しません。ただしSUM値エラーなどが発生した場合はNACK応答が返されます。 |
| `01h` | 応答を要求する | 正常時、ACKレスポンスを返します。 |

### 6.3 データ部[1]: ブザー音

| 値 | ブザー音 | 備考 |
|---|---|---|
| `00h` | ピー | PDF掲載例で使用 |
| `01h` | ピッピッピ |  |
| `02h` | ピッピー |  |
| `03h` | ピッピッピー |  |
| `04h` | ピーー |  |
| `05h` | ピーピーピーピー |  |
| `06h` | ピーーー |  |
| `07h` | ピッピッピッピッピッ |  |
| `08h` | ピッピッピッピッ |  |

### 6.4 実動作条件

本コマンドでブザーを制御するには、リーダライタの汎用ポート7の機能が「ブザー制御信号出力ポート」に設定されている必要があります。

汎用ポート7の機能が「汎用ポート」に設定されている場合、ブザーの制御はできません。この場合、通信上のACKだけでブザー鳴動成功と断定せず、設定状態と実機動作を分けて扱ってください。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 7. レスポンス処理

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

### 7.1 ACK/レスポンス例（PDF掲載例）

| 種別 | Hex |
|---|---|
| TX | `02 00 42 02 01 00 03 4A 0D` |
| RX | `02 00 30 00 03 35 0D` |

ACKはデータ長00hです。応答要求00hの場合は正常時レスポンスを返しません。

実動作として、汎用ポート7の機能が「ブザー制御信号出力ポート」に設定されている場合、リーダライタ本体またはインターフェース基板のブザーから、指定したブザー音が鳴動します。

### 7.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 42 44 00 00 00 00 00 00 00 00 03 C6 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。


### 7.4 AI実装用レスポンス定義

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
| `DATA[0]`送信値が`00h`、かつ正常時にレスポンスなし | `NO_RESPONSE` | 応答要求なしの正常系。timeoutとは分けて扱う |
| `CMD=30h` かつ `LEN=00h` | `ACK` | 応答要求`01h`時の成功ACK |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `42h` / 詳細 `なし` / サブ `なし`。


#### ACK/データ部offset
応答要求 `01h` の成功ACKは `CMD=30h`、`LEN=00h` です。ACKのDATA部はありません。

| offset | フィールド | 値 | 解釈 |
|---:|---|---|---|
| 0 | STX | `02h` | フレーム開始 |
| 1 | ADR | `00h` | 通常はリーダライタID |
| 2 | CMD | `30h` | ACK |
| 3 | LEN | `00h` | DATAなし |
| 4 | ETX | `03h` | フレーム終了 |
| 5 | SUM | `SUM` | SUM値 |
| 6 | CR | `0Dh` | 終端 |

応答要求 `00h` の正常系はレスポンスなしです。ただし、SUM値エラーなどの異常時はNACKが返る可能性があります。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `42h` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR、LBT_ERROR、ANTENNA_ERROR、UHF_IC_ERRORなどの主エラー |
| 2 | `error_code_2` | `error_code_1=0Ah` のUHF ICエラー時に参照 |
| 3 | `error_code_3` | UHF_Encode / UHF_BlockWrite2 等でPDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
if request.response_required == 0x00:
    frame = read_next_frame(short_error_window)
    if frame is None:
        return NO_RESPONSE_SUCCESS
    parsed = parse_common_frame(frame)
    if parsed.cmd == 0x31:
        return parse_nack(parsed)
    return parse_unexpected_response(parsed)

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

このコマンドでは、上記に加えて、汎用ポート7の機能、送信DATA[0]の応答要求、送信DATA[1]のブザー音をパーサへ渡してください。応答要求`00h`の場合、正常無応答をtimeout失敗として扱わないでください。
## 8. 実機確認

実機確認区分: `needs-metadata-confirmation`

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

## 9. AIに実装・移植を依頼するときの注意

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

## 10. 参照ドキュメント

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
