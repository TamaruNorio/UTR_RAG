---
title: "FLASH設定の初期化"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.3.11"
command_group: "reader_control"
command_name: "FLASH設定の初期化"
command_byte: "4Eh"
detail_command: "6Fh"
subcommand: null
operation_profile: "needs-metadata-confirmation"
operation_level: "reader-control"
rf_emission: false
write_operation: false
flash_operation: true
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
  - "flash-operation"
  - "requires-backup"
  - "pass-with-notes"
  - "flash-initialize"
---

# FLASH設定の初期化

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **FLASH設定の初期化** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.11`
- コマンド分類: リーダライタ制御
- 確認区分: `needs-metadata-confirmation`
- 操作レベル: リーダライタ制御
- コマンドバイト: `4Eh` / 詳細コマンド: `6Fh` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**リーダライタのFLASH設定を出荷時設定に戻すこと** です。

本コマンドはタグメモリを書き換えませんが、リーダライタ本体のFLASH設定を変更します。実行後は、リスタートコマンドまたは電源再起動を行い、FLASH初期化後の設定がRAMへ反映される前提で復帰確認してください。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 書き込み操作 | なし |
| FLASH操作 | あり |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | なし |
| タグ条件確認 | なし |
| Accessパスワード確認 | なし |
| パラメータ確認 | なし |
| 明示許可 | 必要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 実行前にFLASH設定を読み取り、復元に必要な値をバックアップする。
4. 本コマンドはFLASH設定を出荷時設定へ戻すため、明示許可なしに送信しない。
5. ACK受信後に、リスタートコマンドまたは電源再起動を実行する手順を決める。
6. 復帰後、FLASH設定・RAM設定・アンテナ設定・送信出力・周波数などが期待どおりか確認する。
7. 必要に応じてバックアップ値を再書き込みし、再度リスタートまたは電源再起動を行う。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.3.11` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.3.11 FLASH 設定の初期化
 リーダライタの FLASH 設定を出荷時設定に戻すコマンドです。
 コマンド実行後はリスタートコマンド、あるいはリーダライタの電源再起動を実行してください。
  ※FLASH の汎用ポートまたは拡張ポートの設定を変更した場合は、リスタートが必要です。

   ［コマンド］
 ラベル名 バイト数                             内容
  STX    1          02h
 アドレス    1          00h（「5.2 通信フォーマットの詳細」参照）
 コマンド    1          4Eh
 データ長    1          01h
 データ部    1          6Fh（詳細コマンド）
  ETX    1          03h
  SUM    1          SUM 値（ 「5.3 SUM の計算方法」参照）
   CR    1          0Dh


   ［ACK レスポンス］
 ラベル名 バイト数                          内容
  STX     1   02h
 アドレス     1   00h（「5.2 通信フォーマットの詳細」参照）
 コマンド     1   30h（ACK）
 データ長     1   01h
 データ部     1   6Fh（詳細コマンド）
  ETX     1   03h
  SUM     1   SUM 値（ 「5.3 SUM の計算方法」参照）
   CR     1   0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
   • コマンド
      02 00 4E 01 6F 03 C3 0D
    • レスポンス
       02 00 30 01 6F 03 A5 0D
```

## 7. コマンド形式・PDFフィールド定義の読み方

この節は、PDF 7.3.11 のコマンド表・ACK表・注意事項を、生成AIが実装に使える粒度へ分解したものです。このコマンドはFLASH設定を出荷時設定へ戻すため、送信前バックアップと送信後復帰確認を必須扱いにしてください。

### 7.1 送信コマンドフレーム

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス。共通通信フォーマットに従う |
| 2 | `CMD` | 1 | `4Eh` | リーダライタ制御コマンド |
| 3 | `LEN` | 1 | `01h` | DATA部は1byte |
| 4 | `DATA[0]` | 1 | `6Fh` | 詳細コマンド: FLASH設定の初期化 |
| 5 | `ETX` | 1 | `03h` | フレーム終端 |
| 6 | `SUM` | 1 | `C3h` | PDF掲載例のSUM。`02+00+4E+01+6F+03 = C3h` |
| 7 | `CR` | 1 | `0Dh` | 改行終端 |

### 7.2 ACKレスポンス形式

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス |
| 2 | `CMD` | 1 | `30h` | ACK |
| 3 | `LEN` | 1 | `01h` | DATA部は1byte |
| 4 | `DATA[0]` | 1 | `6Fh` | 応答元の詳細コマンド |
| 5 | `ETX` | 1 | `03h` | フレーム終端 |
| 6 | `SUM` | 1 | `A5h` | PDF掲載例のSUM。`02+00+30+01+6F+03 = A5h` |
| 7 | `CR` | 1 | `0Dh` | 改行終端 |

### 7.3 コマンド／レスポンス例

| 種別 | Hex | 説明 |
|---|---|---|
| 送信例 | `02 00 4E 01 6F 03 C3 0D` | FLASH設定を出荷時設定へ戻す要求 |
| ACK例 | `02 00 30 01 6F 03 A5 0D` | `CMD=30h`、`DATA[0]=6Fh` の成功ACK |

### 7.4 実行後に必要な再起動

PDF 7.3.11では、コマンド実行後にリスタートコマンド、またはリーダライタの電源再起動を実行するよう記載されています。

| 条件 | 必要な処理 | 理由 |
|---|---|---|
| FLASH設定初期化ACKを受信 | リスタートまたは電源再起動 | 初期化したFLASH設定を実運用状態へ反映するため |
| FLASHの汎用ポート設定を変更していた | リスタート必須 | PDF注意事項で明記 |
| FLASHの拡張ポート設定を変更していた | リスタート必須 | PDF注意事項で明記 |
| 再起動後 | 設定読戻し | RAM設定がFLASHの出荷時設定で上書きされた状態を確認する |

### 7.5 バックアップ・復元対象

このカードでは、個別のFLASH設定項目の値定義は各コマンドカードを一次参照します。実行前後の確認対象は、少なくとも以下です。

| 対象 | 実行前 | 実行後 | 復元時の注意 |
|---|---|---|---|
| FLASH設定全体 | `FLASH設定の読み取り` でバックアップ | 出荷時設定へ戻る | 必要値を再書き込み後、再起動または電源再起動 |
| コマンドモード用RAM | 必要ならスナップショット | 再起動後にFLASH値で上書きされる | 初期化後に必要なRAM設定を再設定 |
| 自動読み取りモード用RAM | 必要ならスナップショット | 再起動後にFLASH値で上書きされる | 自動読み取り、TID付加、EPC/UII応答設定等を再確認 |
| アンテナ設定 | 接続ANT、使用ANT、切替方式を確認 | 出荷時設定の影響を受ける可能性 | 実機ANT数と接続状態を再確認 |
| 送信出力・周波数 | 運用値を控える | 出荷時設定へ戻る可能性 | 法規・LBT・現場条件を再確認してから復元 |
| 汎用ポート・拡張ポート | 運用値を控える | 出荷時設定へ戻る | PDF注意事項に従いリスタートが必要 |

### 7.6 実装ステップ

1. ROM/機種を確認する。
2. FLASH設定を読み取り、復元に必要な値を保存する。
3. 必要ならRAM設定、アンテナ状態、送信出力、周波数、ポート設定もスナップショット化する。
4. 操作者の明示許可を確認する。
5. `02 00 4E 01 6F 03 C3 0D` を送信する。
6. ACK `02 00 30 01 6F 03 A5 0D` を確認する。
7. ACK確認後、リスタートコマンドまたは電源再起動を実行する。
8. 復帰後、ROM読み取りなど低影響コマンドで接続を確認する。
9. FLASH/RAM設定を読戻し、出荷時設定化されたことと、復元が必要な項目を確認する。
10. 必要ならバックアップ値を書き戻し、再度リスタートまたは電源再起動を行う。

## 8. レスポンス処理

レスポンス処理では、以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- フレーム不正
- ACK後の再起動未実施
- 再起動後の未復帰
- FLASH設定読戻し不一致
- 復元失敗

NACKは共通NACK形式とPDF該当節を併せて確認してください。予約バイトは、PDFで意味が定義されていない限り、独自解釈しないでください。

### 8.1 受信分類ルール

| 条件 | 分類 | 実装アクション |
|---|---|---|
| フレーム長不一致、`STX/ETX/CR/SUM`不正 | `INVALID_FRAME` | ACK成功とは扱わず、送信済みの場合は状態確認へ進む |
| 受信期限内に1フレームも来ない | `TIMEOUT` | ACK未確認。初期化完了を断定しない |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む。再送前に原因確認 |
| `CMD=30h` かつ `LEN=01h` かつ `DATA[0]=6Fh` | `ACK` | FLASH設定初期化の成功ACK。次にリスタートまたは電源再起動を行う |
| ACK後に再起動していない | `RESTART_REQUIRED` | 初期化後の設定反映確認としては未完了 |
| 再起動後の読戻し不一致 | `VERIFY_FAILED` | バックアップ、復元要否、対象機種差を確認する |

対象識別子: コマンド `4Eh` / 詳細 `6Fh` / サブ `なし`。

### 8.2 ACK/レスポンス例

| 項目 | 内容 |
|---|---|
| 代表TX Hex | `02 00 4E 01 6F 03 C3 0D` |
| 代表ACK Hex | `02 00 30 01 6F 03 A5 0D` |
| ACKデータ部 | `DATA[0]=6Fh` |
| ACK後の必須処理 | リスタートまたは電源再起動 |

### 8.3 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 6F 44 00 00 00 00 00 00 00 00 03 F3 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコード |

NACK時は、エラーコード1だけでなく、PDF定義の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.4 AI実装用レスポンス定義

#### 共通フレームoffset

| offset | フィールド | 実装上の意味 |
|---:|---|---|
| 0 | `STX` | 常に `02h`。異なる場合は `INVALID_FRAME` |
| 1 | `ADR` | 通常はリーダライタID。RFタグ応答でアンテナID出力ONの場合は読み取りANT番号 |
| 2 | `CMD` | `30h`=ACK、`31h`=NACK。その他はPDF該当節で分類 |
| 3 | `LEN` | `DATA`部のbyte数。総フレーム長は `LEN + 7` |
| 4..`4+LEN-1` | `DATA` | ACK/NACKごとの可変領域 |
| `4+LEN` | `ETX` | 常に `03h`。異なる場合は `INVALID_FRAME` |
| `5+LEN` | `SUM` | `STX`から`ETX`までのSUM下位1byte |
| `6+LEN` | `CR` | 常に `0Dh` |

#### ACK/データ部offset

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail_command` | `6Fh`。FLASH設定初期化に対するACK |

#### NACK分類

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象詳細コマンド `6Fh` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR等の主エラー |
| 2 | `error_code_2` | PDF定義がある場合のみ参照 |
| 3 | `error_code_3` | PDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
before_flash = read_flash_settings_backup()
before_ram = read_ram_settings_snapshot_if_needed()
require_operator_approval("FLASH設定を出荷時設定へ初期化します")
send_frame("02 00 4E 01 6F 03 C3 0D")
frame = read_next_frame(timeout)
if frame is None:
    return TIMEOUT_ACK_NOT_CONFIRMED
parsed = parse_common_frame(frame)
if parsed.invalid:
    return INVALID_FRAME_STATE_CHECK_REQUIRED
if parsed.cmd == 0x31:
    return parse_nack(parsed)
if parsed.cmd == 0x30 and parsed.len == 1 and parsed.data[0] == 0x6F:
    restart_or_power_cycle()
    verify_after_restart()
    return FLASH_INITIALIZE_ACKED_RESTART_REQUIRED_OR_DONE
return UNKNOWN_RESPONSE_REQUIRES_PDF_CHECK
```

#### 推奨パーサ出力

```json
{
  "frame_type": "ACK | NACK | TIMEOUT | INVALID_FRAME | RESTART_REQUIRED | VERIFY_FAILED",
  "command": "FLASH設定の初期化",
  "command_bytes": "4E 6F",
  "tx_hex": "02 00 4E 01 6F 03 C3 0D",
  "ack_hex": "02 00 30 01 6F 03 A5 0D",
  "flash_operation": true,
  "backup_required": true,
  "restart_required_after_ack": true,
  "settings_snapshot_used": true,
  "is_success": false,
  "error": null,
  "raw_hex_policy": "PDF掲載例は可。実機ログ由来のEPC/UII/TID/パスワードはマスク"
}
```

#### 設定スナップショット必須項目

実行前後に、ROM/機種、FLASH設定バックアップ、RAM設定、物理アンテナ容量、接続OKアンテナ、現在ANT、アンテナID出力、TID付加、EPC/UII応答設定、読取完了応答、アンテナ切替完了応答、キャリア検知応答、送信出力、周波数、汎用ポート、拡張ポート、復元要否を確認してください。

## 9. 実機確認

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
