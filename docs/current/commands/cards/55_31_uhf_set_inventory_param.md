---
title: "UHF_SetInventoryParam"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.18"
command_group: "reader_setting"
command_name: "UHF_SetInventoryParam"
command_byte: "55h"
detail_command: "31h"
subcommand: null
operation_profile: "settings-change"
operation_level: "write/configuration"
rf_emission: false
write_operation: true
flash_operation: true
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
requires_tag: false
requires_access_password: false
requires_parameters: true
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../RESPONSE_MODE_APPLICABILITY.md"
  - "55_41_uhf_get_inventory_param.md"
  - "55_31_uhf_set_inventory_param_raw.md"
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "write-operation"
  - "specification-reference"
  - "uhf-set-inventory-param"
---

# UHF_SetInventoryParam（Inventory条件設定）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_SetInventoryParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.18`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `31h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

このコマンドの目的は、**UHF_SetInventoryParam** です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 書き込み操作 | あり |
| FLASH操作 | `02h`指定時にあり。RAM指定時はなし |
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
3. 読み取り専用か、設定変更か、タグメモリ操作かを分類する。
4. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。
5. 周波数、送信出力、アンテナ設定、FLASH、タグメモリに影響する場合は、事前承認を取る。

## 6. PDF仕様フィールド定義

### 6.1 適用範囲と原典への導線

Inventory設定のコマンドモード用RAMと自動読み取りモード用RAMは独立しています。パラメータ4のMemBank・TID付加、読み取り開始Wordアドレス、読み取りWord数は連続インベントリリードモード用です。単発InventoryReadではコマンド内の指定を使います（§7.4.18 p.202、§7.5.2 p.266）。

FLASHへの書込みは両RAMにも反映されます。保存先と復元条件は[RAM・FLASH影響整理](../../RAM_FLASH_IMPACT_MATRIX.md)を参照してください。

### 6.2 原典転記

照合対象: §7.4.18 p.196–203。今回の照合範囲は設定の適用先・ACK形式・参照節で、カード全体の試験完了を意味しません。

PDF原文の全文転記は [原文転記](55_31_uhf_set_inventory_param_raw.md) を参照してください。
このカードには、実装判断に必要な要点とAI向け構造化情報のみを残します。

### 6.3 保守者による用語訂正: p.200下部

2026-09-09に保守者が、＜Sel値が「ALL」の場合の注意点＞の※注記を訂正しました。

| 箇所 | 誤 | 正 |
|---|---|---|
| 「Selectコマンドで遷移させた…」のフラグ名 | Inventoryフラグ | Inventoriedフラグ |

訂正後の注記は次のとおりです。

> ※Selectコマンドで遷移させたInventoriedフラグ以外のフラグを参照して読み取りをおこなった場合、Selectコマンドは意味を持たなくなります。

フラグ名の表記を統一する訂正です。SelectのTargetとInventory側のSessionを対応させる説明の意味は変わりません。コマンド名UHF_SetInventoryParamや「InventoryのTarget」という項目名を、一括してInventoriedへ置き換えません。

[原文転記](55_31_uhf_set_inventory_param_raw.md)は当時の記載を保持し、本注記と併せて参照します。p.193例3の3点の訂正とともに、[OPEN-012](../../SOURCE_REVIEW_STATUS.md)へ記録しています。

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

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

ACK、後続レスポンス、可変長データの解釈は、対象コマンドのPDF定義と機種・ROM・設定に基づきます。[応答マスタ](../../RESPONSE_AND_NACK_MASTER.md)と[モード別適用範囲](../../RESPONSE_MODE_APPLICABILITY.md)を確認し、TID付加や自動読み取り用の通知設定を、すべてのコマンドACKへ一般化しないでください。

### 8.1 ACK/レスポンス例（設定変更成功時）

| 項目 | 内容 |
|---|---|
| ACK構造 | `02 ADR 30 01 31 03 SUM 0D` |
| `CMD` | `30h`（ACK） |
| `LEN` | `01h` |
| `DATA[0]` | `31h`（詳細コマンド: UHF_SetInventoryParam） |
| PDF掲載レスポンス例 | `02 00 30 01 31 03 67 0D` |
| 注意 | 成功ACKには書き込んだInventory条件値は返りません。反映確認は `55h 41h`（UHF_GetInventoryParam）で読戻してください。 |

設定変更後は対応する読取りコマンドで、影響する保存先を読戻します。一時変更の復元対象と順序は[RAM・FLASH影響整理](../../RAM_FLASH_IMPACT_MATRIX.md)を確認します。FLASH値は動作中のRAMにも反映され、再起動後の保持確認とは別です。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 31 44 00 00 00 00 00 00 00 00 03 B5 0D` |
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
| 受信期限内に対象要求の応答を確認できない | `TIMEOUT` | timeoutとして処理し、NACKとは分ける |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む |
| `CMD=30h`、`LEN=01h`、`DATA[0]=31h` | `ACK` | 対象要求の応答として扱う。値の反映確認は別管理する |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |

対象識別子: コマンド `55h` / 詳細 `31h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` は `LEN=01h` の固定長ACKです。書き込んだInventory条件値はACKには含まれません。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `31h`: UHF_SetInventoryParam成功ACK |

`LEN` が `01h` 以外、または `DATA[0]` が `31h` 以外の場合は、このコマンドの通常成功ACKとして扱わず、別レスポンスまたは異常フレームとして分類してください。

ACKの成功と、読戻し一致・保持・復元の確認は別に記録します。本ACKは種類や設定値を返さないため、送信した要求と対応づけて管理します。

非同期通知は通知自身の長さ・識別子・モード条件で別に分類します。本コマンドの成功や終了の代わりにはしません。本ACKに`DATA[1]`は存在しません。`DATA[0]=31h`は詳細識別子で、NACKの`CMD=31h`とは別です。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 31h` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR、LBT_ERROR、ANTENNA_ERROR、UHF_IC_ERRORなどの主エラー |
| 2 | `error_code_2` | `error_code_1=0Ah` のUHF ICエラー時に参照 |
| 3 | `error_code_3` | UHF_Encode / UHF_BlockWrite2 等でPDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 判定手順（文書上の仕様）

1. フレーム長、区切り、SUMを検査してからDATAへアクセスする。
2. NACKは`CMD=31h`で分類し、対象要求との対応を確認する。通知や別要求の応答を成功として扱わない。
3. 上の受信分類ルールにあるLEN・詳細識別子を照合する。
4. ACK受信と、影響する保存先の読戻し確認を分けて記録する。
5. 対象応答が期限までに得られなければ未完了とする。途中の非同期通知だけで待機を成功終了しない。

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

#### この要求で保持する情報

対象機種・ROM、接続先、要求識別子、パラメータ種類、受信期限を保持します。書込み時は要求値、影響する保存先の変更前値、復元条件も記録します。本設定ACKは固定長で、タグのTID付加やアンテナ通知設定によって長さを変えません。並行して非同期通知を解釈する場合の設定は、通知側の処理で別途管理します。

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

- [RAM_FLASH_IMPACT_MATRIX.md](../../RAM_FLASH_IMPACT_MATRIX.md)
- [RESPONSE_MODE_APPLICABILITY.md](../../RESPONSE_MODE_APPLICABILITY.md)
- [55_41_uhf_get_inventory_param.md](55_41_uhf_get_inventory_param.md)
- [55_31_uhf_set_inventory_param_raw.md](55_31_uhf_set_inventory_param_raw.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
