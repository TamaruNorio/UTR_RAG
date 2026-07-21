---
title: "リーダライタ動作モードの書き込み"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.16"
command_group: "reader_setting"
command_name: "リーダライタ動作モードの書き込み"
command_byte: "4Eh"
detail_command: "00h"
subcommand: "10h"
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
  - "reader-mode"
  - "ram-flash-target"
  - "pass-with-notes"
---

# リーダライタ動作モードの書き込み

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **リーダライタ動作モードの書き込み** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.16`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `4Eh` / 詳細コマンド: `00h` / サブコマンド: `10h`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**リーダライタの動作モードをRAMまたはFLASHへ書き込むこと** です。

コマンドモード、UHF連続インベントリモード、UHF連続インベントリリードモードを切り替える設定変更コマンドです。FLASHへ書き込む場合は、リーダライタが自動的にFLASHデータを再読み込みし、RAMデータがFLASHデータで上書きされる点に注意してください。

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
3. 書き込み対象が `00h=RAM` か `10h=FLASH` かを確認する。
4. 設定する動作モードが `00h=コマンドモード`、`65h=UHF連続インベントリモード`、`66h=UHF連続インベントリリードモード` のどれかを確認する。
5. ブザーbitは `bit4` のみを意味として扱い、予約bitは通常0にする。
6. FLASHへ書く場合は、実行前にRAM/FLASH設定スナップショットを取得し、ACK後のRAM上書き影響を確認する。
7. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件、復元手順を決める。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.4.16` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.16 リーダライタ動作モードの書き込み
 リーダライタの動作モードを書き込むコマンドです。

 ［コマンド］
ラベル名 バイト数                                内容
 STX   1         02h
アドレス   1         00h（ 「5.2 通信フォーマットの詳細」参照）
コマンド   1         4Eh
データ長   1         07h
                 書き込み対象
            1      00h        ：RAM への書き込み
                   10h        ：FLASH への書き込み
                 リーダライタ動作モード
                   00h        ：コマンドモード
            1
                   65h        ：UHF 連続インベントリモード
                   66h        ：UHF 連続インベントリリードモード
データ部        1    将来拡張のための予約（通常は 00h）
                 ビット          割り当て
                 bit0-3       将来拡張のための予約（通常は 0）
                              ブザー
            1
                 bit4         0：鳴らさない
                              1：鳴らす［初期値］
                 bit5-7       将来拡張のための予約（通常は 0）
            3    将来拡張のための予約（通常は 00h）
 ETX        1    03h
 SUM        1    SUM 値（  「5.3 SUM の計算方法」参照）
  CR        1    0Dh
 ＜注意事項＞
 ・FLASH への書き込みを実行した場合、リーダライタは自動的に FLASH データの再読み込みをお
  こないます。
  リーダライタの RAM に保存されたデータは FLASH データで上書きされます。


  ［ACK レスポンス］
ラベル名 バイト数                          内容
 STX     1   02h
アドレス     1   00h（「5.2 通信フォーマットの詳細」参照）
コマンド     1   30h（ACK）
データ長     1   00h（固定値）
 ETX     1   03h
 SUM     1   SUM 値（ 「5.3 SUM の計算方法」参照）
  CR     1   0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］

      (例) 以下のパラメータを書き込む場合
      データ種類                        数値／パラメータ            コマンド列
      書き込み対象                       RAM への書き込み          00
      リーダライタ動作モード                  UHF 連続インベントリモード     65
      ブザー                          鳴らす                 10

  •    コマンド
       02 00 4E 07 00 65 00 10 00 00 00 03 CF 0D

  •    レスポンス
       02 00 30 00 03 35 0D
```

## 7. コマンド形式・PDFフィールド定義の読み方

この節は、PDF 7.4.16 のコマンド表・ACK表・注意事項を、生成AIが実装に使える粒度へ分解したものです。特に、成功ACKは `LEN=00h` でDATA部を持たない点に注意してください。

### 7.1 送信コマンドフレーム

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス。共通通信フォーマットに従う |
| 2 | `CMD` | 1 | `4Eh` | リーダライタ設定書き込み系コマンド |
| 3 | `LEN` | 1 | `07h` | DATA部は7byte |
| 4 | `DATA[0]` | 1 | `00h` / `10h` | 書き込み対象。`00h=RAM`, `10h=FLASH` |
| 5 | `DATA[1]` | 1 | `00h` / `65h` / `66h` | リーダライタ動作モード |
| 6 | `DATA[2]` | 1 | 通常 `00h` | 将来拡張予約。独自解釈しない |
| 7 | `DATA[3]` | 1 | bit4のみ意味あり | ブザー設定。bit4=`0`鳴らさない、bit4=`1`鳴らす |
| 8 | `DATA[4]` | 1 | 通常 `00h` | 将来拡張予約 |
| 9 | `DATA[5]` | 1 | 通常 `00h` | 将来拡張予約 |
| 10 | `DATA[6]` | 1 | 通常 `00h` | 将来拡張予約 |
| 11 | `ETX` | 1 | `03h` | フレーム終端 |
| 12 | `SUM` | 1 | 可変 | `STX`から`ETX`までのSUM下位1byte |
| 13 | `CR` | 1 | `0Dh` | 改行終端 |

### 7.2 書き込み対象

| `DATA[0]` | 対象 | 影響 | 実装上の注意 |
|---|---|---|---|
| `00h` | RAMへの書き込み | 現在動作中のRAM設定を変更 | 電源再起動やリスタート後はFLASH値に戻る可能性がある |
| `10h` | FLASHへの書き込み | 不揮発設定を変更 | PDF注意事項により、リーダライタは自動的にFLASHデータを再読み込みし、RAMデータがFLASHデータで上書きされる |

### 7.3 リーダライタ動作モード

| `DATA[1]` | モード | 意味 | 応答・運用上の注意 |
|---|---|---|---|
| `00h` | コマンドモード | 上位機器からのコマンド待受を基本とする | 実装・検証時の安全な復帰先として扱いやすい |
| `65h` | UHF連続インベントリモード | UHF連続インベントリ動作 | 設定状態によりRFタグ応答や非同期応答を受ける可能性がある |
| `66h` | UHF連続インベントリリードモード | UHF連続インベントリリード動作 | TID付加、EPC/UII応答設定、アンテナID出力等の設定依存を確認する |

### 7.4 ブザー設定byte

| bit | 意味 | 値 |
|---:|---|---|
| bit0-3 | 将来拡張予約 | 通常 `0` |
| bit4 | ブザー | `0=鳴らさない`, `1=鳴らす`（初期値） |
| bit5-7 | 将来拡張予約 | 通常 `0` |

PDF掲載例の `10h` は、bit4だけが1で、ブザーを「鳴らす」設定です。予約bitは意味定義がないため、独自解釈しないでください。

### 7.5 ACKレスポンス形式

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス |
| 2 | `CMD` | 1 | `30h` | ACK |
| 3 | `LEN` | 1 | `00h` | DATA部なし |
| 4 | `ETX` | 1 | `03h` | フレーム終端 |
| 5 | `SUM` | 1 | `35h` | PDF掲載例のSUM。`02+00+30+00+03 = 35h` |
| 6 | `CR` | 1 | `0Dh` | 改行終端 |

このACKには詳細コマンド `00h` やサブコマンド `10h` は含まれません。実装では、送信中コマンドのコンテキストと受信順序で、どの書き込みに対するACKかを対応づけてください。

### 7.6 コマンド／レスポンス例

| 種別 | Hex | 説明 |
|---|---|---|
| 送信例 | `02 00 4E 07 00 65 00 10 00 00 00 03 CF 0D` | RAMへ、UHF連続インベントリモード、ブザー鳴らすを書き込み |
| ACK例 | `02 00 30 00 03 35 0D` | `CMD=30h`, `LEN=00h` の成功ACK |

### 7.7 FLASH書き込み時の設定反映

FLASHへ書き込む場合、リーダライタは自動的にFLASHデータを再読み込みし、RAMに保存されたデータはFLASHデータで上書きされます。

| 場面 | 影響 | 実装アクション |
|---|---|---|
| `DATA[0]=00h` RAM書き込み | RAM設定のみ変更 | 読戻しでRAM反映を確認。必要なら復帰値を書き戻す |
| `DATA[0]=10h` FLASH書き込み | FLASH変更後、RAMがFLASH値で上書き | 実行前にRAM/FLASHスナップショットを取得し、ACK後に設定再取得する |
| 自動読み取り系モードへ変更 | 非同期タグ応答が発生し得る | ACK後の受信ループでRFタグデータ等を通常ACKと混同しない |
| コマンドモードへ復帰 | 通常のコマンド待受へ戻る | 実機検証の終了時はコマンドモードへ戻す方針を明確にする |

## 8. レスポンス処理

レスポンス処理では、以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- フレーム不正
- ACK後の読戻し未確認
- FLASH書き込み後のRAM上書き
- 自動読み取り系モード変更後の非同期応答

NACKは共通NACK形式とPDF該当節を併せて確認してください。予約バイトは、PDFで意味が定義されていない限り、独自解釈しないでください。

### 8.1 受信分類ルール

| 条件 | 分類 | 実装アクション |
|---|---|---|
| フレーム長不一致、`STX/ETX/CR/SUM`不正 | `INVALID_FRAME` | ACK成功とは扱わない |
| 受信期限内に1フレームも来ない | `TIMEOUT` | timeoutとして処理し、設定反映を断定しない |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む |
| `CMD=30h` かつ `LEN=00h` | `ACK` | リーダライタ動作モード書き込みの成功ACK候補。送信中コンテキストで対応づける |
| `CMD=30h` だが `LEN!=00h` | `UNEXPECTED_ACK_SHAPE` | このコマンドのPDF ACKではない可能性として扱う |
| ACK後に読戻し未実施 | `ACK_PENDING_VERIFY` | 対応する読出コマンドでRAM/FLASH反映を確認する |
| `CMD=6Ch` などのタグ応答 | `RF_TAG_DATA_OR_ASYNC_EVENT` | 自動読み取り系モード変更後の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `4Eh` / 詳細 `00h` / サブ `10h`。

### 8.2 ACK/レスポンス例

| 項目 | 内容 |
|---|---|
| 代表TX Hex | `02 00 4E 07 00 65 00 10 00 00 00 03 CF 0D` |
| 代表ACK Hex | `02 00 30 00 03 35 0D` |
| ACKデータ部 | なし。`LEN=00h` |
| ACK照合 | DATAがないため、送信中コマンドコンテキストで照合する |

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
| 4..`4+LEN-1` | `DATA` | ACKでは空、NACKではエラー情報 |
| `4+LEN` | `ETX` | 常に `03h`。異なる場合は `INVALID_FRAME` |
| `5+LEN` | `SUM` | `STX`から`ETX`までのSUM下位1byte |
| `6+LEN` | `CR` | 常に `0Dh` |

#### ACK/データ部offset

成功ACK `CMD=30h` は `LEN=00h` です。DATA offsetは存在しません。

| 項目 | 解釈 |
|---|---|
| `CMD=30h` | ACK |
| `LEN=00h` | DATA部なし |
| `DATA[0]` | 存在しない。`DATA[0]=00h` と誤判定しない |

#### NACK分類

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象詳細コマンド `00h`。サブコマンド `10h` は送信コンテキスト側で保持する |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR等の主エラー |
| 2 | `error_code_2` | PDF定義がある場合のみ参照 |
| 3 | `error_code_3` | PDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
snapshot = read_startup_snapshot_if_needed()
send_write_reader_mode(target, mode, buzzer_bit4)
frame = read_next_frame(timeout)
if frame is None:
    return TIMEOUT
parsed = parse_common_frame(frame)
if parsed.invalid:
    return INVALID_FRAME
if parsed.cmd == 0x31:
    return parse_nack(parsed, sent_context={"detail": "00h", "sub": "10h"})
if parsed.cmd == 0x30 and parsed.len == 0:
    verify_by_read_reader_mode(target)
    if target == 0x10:
        refresh_ram_flash_snapshot()
    return ACK_PENDING_OR_VERIFIED
return UNKNOWN_RESPONSE_REQUIRES_PDF_CHECK
```

#### 推奨パーサ出力

```json
{
  "frame_type": "ACK | NACK | TIMEOUT | INVALID_FRAME | ACK_PENDING_VERIFY | RF_TAG_DATA_OR_ASYNC_EVENT",
  "command": "リーダライタ動作モードの書き込み",
  "command_bytes": "4E 00 10",
  "write_target": "RAM(00h) | FLASH(10h)",
  "reader_mode": "COMMAND(00h) | UHF_INVENTORY(65h) | UHF_INVENTORY_READ(66h)",
  "ack_hex": "02 00 30 00 03 35 0D",
  "ack_data_length": 0,
  "flash_write_reloads_ram": true,
  "settings_snapshot_used": true,
  "is_success": false,
  "error": null,
  "raw_hex_policy": "PDF掲載例は可。実機ログ由来のEPC/UII/TID/パスワードはマスク"
}
```

#### 設定スナップショット必須項目

実行前後に、ROM/機種、現在のリーダライタ動作モード、RAM/FLASH対象、アンテナID出力、TID付加、EPC/UII応答設定、読取完了応答、アンテナ切替完了応答、キャリア検知応答、物理アンテナ容量、接続OKアンテナ、現在ANT、復元要否を確認してください。

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
