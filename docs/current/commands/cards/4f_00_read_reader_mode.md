---
title: "リーダライタ動作モードの読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.1"
command_group: "reader_setting"
command_name: "リーダライタ動作モードの読み取り"
command_byte: "4Fh"
detail_command: "00h"
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
  - "reader-mode"
  - "startup-snapshot"
  - "pass-with-notes"
  - "read-reader-mode"
---

# リーダライタ動作モードの読み取り

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **リーダライタ動作モードの読み取り** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.1`
- コマンド分類: リーダライタ設定
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `4Fh` / 詳細コマンド: `00h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**現在のリーダライタ動作モードとブザー設定を読み取ること** です。

この読み取り結果は、起動時スナップショットや、`4Eh 00h 10h` の「リーダライタ動作モードの書き込み」後の読戻し確認に使います。ACKデータ部には詳細コマンド、動作モード、ブザーbit、予約byteが含まれるため、byte位置で正確にパースしてください。

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
3. ACKの `LEN=09h` と `DATA[0]=00h` を確認してから読戻し値を読む。
4. `DATA[1]` の動作モードを `00h` / `65h` / `66h` として分類する。
5. `DATA[3]` のbit4だけをブザー設定として扱い、予約bitは独自解釈しない。
6. 書き込みコマンド後の確認では、RAM/FLASHどちらを読戻したいのかを送信コンテキストで管理する。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.4.1` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.1    リーダライタ動作モードの読み取り
  リーダライタの動作モードを読み取るコマンドです。

  ［コマンド］
 ラベル名 バイト数                                             内容
  STX            1       02h
 アドレス            1       00h（「5.2 通信フォーマットの詳細」参照）
 コマンド            1       4Fh
 データ長            1       01h
 データ部            1       00h（詳細コマンド）
  ETX            1       03h
  SUM            1       SUM 値（ 「5.3 SUM の計算方法」参照）
   CR            1       0Dh

  ［ACK レスポンス］
 ラベル名 バイト数                                             内容
  STX            1       02h
 アドレス            1       00h（ 「5.2 通信フォーマットの詳細」参照）
 コマンド            1       30h（ACK）
 データ長            1       09h
                 1       00h（詳細コマンド）
                         リーダライタ動作モード
                           00h      ：コマンドモード
                 1
                           65h      ：UHF 連続インベントリモード
                           66h      ：UHF 連続インベントリリードモード
                 1       将来拡張のための予約（通常は 00h）
 データ部                    ビット        割り当て
                         bit0-3     将来拡張のための予約（通常は 0）
                                    ブザー
                 1
                         bit4       0      ：鳴らさない
                                    1      ：鳴らす［初期値］
                         bit5-7     将来拡張のための予約（通常は   0）
                 5       将来拡張のための予約（通常は 00h）
   ETX           1       03h
   SUM           1       SUM 値（  「5.3 SUM の計算方法」参照）
    CR           1       0Dh

    ［NACK レスポンス］
     「7.6 NACK レスポンスとエラーコード」参照。

    ［コマンド／レスポンス例］
     • コマンド
        02 00 4F 01 00 03 55 0D
        • レスポンス
           02 00 30 09 00 00 00 10 00 00 00 00 00 03 4E 0D
            →「リーダライタの動作モード」＝[00h: コマンドモード]、
             「ブザー」
                 ：[鳴らす]の場合
```

## 7. コマンド形式・PDFフィールド定義の読み方

この節は、PDF 7.4.1 のコマンド表・ACK表・例を、生成AIが実装に使える粒度へ分解したものです。このコマンドは読み取り専用ですが、ACKデータ部に現在の動作モードとブザー設定が返ります。

### 7.1 送信コマンドフレーム

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス。共通通信フォーマットに従う |
| 2 | `CMD` | 1 | `4Fh` | リーダライタ設定読み取り系コマンド |
| 3 | `LEN` | 1 | `01h` | DATA部は1byte |
| 4 | `DATA[0]` | 1 | `00h` | 詳細コマンド: リーダライタ動作モードの読み取り |
| 5 | `ETX` | 1 | `03h` | フレーム終端 |
| 6 | `SUM` | 1 | `55h` | PDF掲載例のSUM。`02+00+4F+01+00+03 = 55h` |
| 7 | `CR` | 1 | `0Dh` | 改行終端 |

### 7.2 ACKレスポンス形式

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス |
| 2 | `CMD` | 1 | `30h` | ACK |
| 3 | `LEN` | 1 | `09h` | DATA部は9byte |
| 4 | `DATA[0]` | 1 | `00h` | 詳細コマンド |
| 5 | `DATA[1]` | 1 | `00h` / `65h` / `66h` | リーダライタ動作モード |
| 6 | `DATA[2]` | 1 | 通常 `00h` | 将来拡張予約。独自解釈しない |
| 7 | `DATA[3]` | 1 | bit4のみ意味あり | ブザー設定 |
| 8 | `DATA[4]` | 1 | 通常 `00h` | 将来拡張予約 |
| 9 | `DATA[5]` | 1 | 通常 `00h` | 将来拡張予約 |
| 10 | `DATA[6]` | 1 | 通常 `00h` | 将来拡張予約 |
| 11 | `DATA[7]` | 1 | 通常 `00h` | 将来拡張予約 |
| 12 | `DATA[8]` | 1 | 通常 `00h` | 将来拡張予約 |
| 13 | `ETX` | 1 | `03h` | フレーム終端 |
| 14 | `SUM` | 1 | 可変 | `STX`から`ETX`までのSUM下位1byte |
| 15 | `CR` | 1 | `0Dh` | 改行終端 |

### 7.3 リーダライタ動作モード

| `DATA[1]` | モード | 意味 | 実装上の注意 |
|---|---|---|---|
| `00h` | コマンドモード | 上位機器からのコマンド待受を基本とする | 通常の安全な操作状態として扱いやすい |
| `65h` | UHF連続インベントリモード | UHF連続インベントリ動作 | 非同期タグ応答など設定依存の受信を考慮する |
| `66h` | UHF連続インベントリリードモード | UHF連続インベントリリード動作 | TID付加やEPC/UII応答設定、ANT ID出力設定の影響を併せて見る |

### 7.4 ブザー設定byte

| bit | 意味 | 値 |
|---:|---|---|
| bit0-3 | 将来拡張予約 | 通常 `0` |
| bit4 | ブザー | `0=鳴らさない`, `1=鳴らす`（初期値） |
| bit5-7 | 将来拡張予約 | 通常 `0` |

PDF掲載例の `DATA[3]=10h` は、bit4だけが1で、ブザー「鳴らす」を意味します。予約bitは意味定義がないため、独自解釈しないでください。

### 7.5 コマンド／レスポンス例

| 種別 | Hex | 説明 |
|---|---|---|
| 送信例 | `02 00 4F 01 00 03 55 0D` | リーダライタ動作モードを読み取る |
| ACK例 | `02 00 30 09 00 00 00 10 00 00 00 00 00 03 4E 0D` | `DATA[1]=00h` コマンドモード、`DATA[3]=10h` ブザー鳴らす |

## 8. レスポンス処理

レスポンス処理では、以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- フレーム不正
- ACKデータ長不一致
- 予約byteの非0値
- 自動読み取り系モード中の非同期応答

NACKは共通NACK形式とPDF該当節を併せて確認してください。予約バイトは、PDFで意味が定義されていない限り、独自解釈しないでください。

### 8.1 受信分類ルール

| 条件 | 分類 | 実装アクション |
|---|---|---|
| フレーム長不一致、`STX/ETX/CR/SUM`不正 | `INVALID_FRAME` | 破棄し、必要なら再同期する |
| 受信期限内に1フレームも来ない | `TIMEOUT` | timeoutとして処理し、NACKとは分ける |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む |
| `CMD=30h` かつ `LEN=09h` かつ `DATA[0]=00h` | `ACK` | PDF 7.4.1 の成功ACKとしてDATAを読む |
| `CMD=30h` だが `LEN!=09h` | `UNEXPECTED_ACK_LENGTH` | このコマンドのACKとして固定解釈しない |
| `DATA[2]` または `DATA[4..8]` が非0 | `RESERVED_NONZERO` | 予約領域として記録し、独自解釈しない |
| `CMD=6Ch` などのタグ応答 | `RF_TAG_DATA_OR_ASYNC_EVENT` | 自動読み取り系モード中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `4Fh` / 詳細 `00h` / サブ `なし`。

### 8.2 ACK/レスポンス例

| 項目 | 内容 |
|---|---|
| 代表TX Hex | `02 00 4F 01 00 03 55 0D` |
| 代表ACK Hex | `02 00 30 09 00 00 00 10 00 00 00 00 00 03 4E 0D` |
| ACKデータ長 | `LEN=09h` |
| ACKデータ部 | `DATA[0]=00h`, `DATA[1]=動作モード`, `DATA[3].bit4=ブザー` |

### 8.3 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 00 44 00 00 00 00 00 00 00 00 03 84 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコード |

NACK時は、エラーコード1だけでなく、PDF定義の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.4 AI実装用レスポンス定義

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

#### ACK/データ部offset

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail_command` | `00h`。リーダライタ動作モード読み取りACK |
| 1 | `reader_mode` | `00h`, `65h`, `66h` のいずれか |
| 2 | `reserved_0` | 通常 `00h`。独自解釈しない |
| 3 | `buzzer_bits` | bit4のみブザー設定。bit0-3/5-7は予約 |
| 4..8 | `reserved_1_5` | 通常 `00h`。独自解釈しない |

#### NACK分類

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象詳細コマンド `00h` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR等の主エラー |
| 2 | `error_code_2` | PDF定義がある場合のみ参照 |
| 3 | `error_code_3` | PDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
send_read_reader_mode()
frame = read_next_frame(timeout)
if frame is None:
    return TIMEOUT
parsed = parse_common_frame(frame)
if parsed.invalid:
    return INVALID_FRAME
if parsed.cmd == 0x31:
    return parse_nack(parsed)
if parsed.cmd == 0x30 and parsed.len == 9 and parsed.data[0] == 0x00:
    return {
        "reader_mode": parsed.data[1],
        "buzzer_enabled": bool(parsed.data[3] & 0x10),
        "reserved_nonzero": any_reserved_nonzero(parsed.data)
    }
return UNKNOWN_RESPONSE_REQUIRES_PDF_CHECK
```

#### 推奨パーサ出力

```json
{
  "frame_type": "ACK | NACK | TIMEOUT | INVALID_FRAME | UNEXPECTED_ACK_LENGTH | RESERVED_NONZERO | RF_TAG_DATA_OR_ASYNC_EVENT",
  "command": "リーダライタ動作モードの読み取り",
  "command_bytes": "4F 00",
  "tx_hex": "02 00 4F 01 00 03 55 0D",
  "ack_hex_example": "02 00 30 09 00 00 00 10 00 00 00 00 00 03 4E 0D",
  "reader_mode": "COMMAND(00h) | UHF_INVENTORY(65h) | UHF_INVENTORY_READ(66h) | unknown",
  "buzzer_enabled": true,
  "settings_snapshot_used": true,
  "is_success": false,
  "error": null,
  "raw_hex_policy": "PDF掲載例は可。実機ログ由来のEPC/UII/TID/パスワードはマスク"
}
```

#### 設定スナップショット必須項目

実行前後に、ROM/機種、現在のリーダライタ動作モード、ブザー設定、アンテナID出力、TID付加、EPC/UII応答設定、読取完了応答、アンテナ切替完了応答、キャリア検知応答、物理アンテナ容量、接続OKアンテナ、現在ANTを確認してください。

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
