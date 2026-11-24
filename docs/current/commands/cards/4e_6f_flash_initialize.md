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
operation_profile: "settings-change"
operation_level: "write/configuration"
rf_emission: true
write_operation: true
flash_operation: true
tag_memory_operation: false
requires_rom_check: true
requires_antenna: true
requires_tag: false
requires_access_password: false
requires_parameters: false
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "4e_00_10_write_reader_mode.md"
  - "4e_9d_restart_reader.md"
  - "rom_version_read.md"
  - "4f_b4_read_flash_settings.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-control"
  - "flash-operation"
  - "requires-backup"
  - "specification-reference"
  - "flash-initialize"
---

# FLASH設定の初期化

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **FLASH設定の初期化** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.11`
- コマンド分類: リーダライタ制御
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `4Eh` / 詳細コマンド: `6Fh` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

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
| RF送信 | 再起動時の条件付き影響あり |
| 書き込み操作 | あり |
| FLASH操作 | あり |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | 再起動時の条件を確認 |
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

この節は、PDF 7.3.11 のコマンド表・ACK表・注意事項を、生成AIが実装に使える粒度へ分解したものです。このコマンドはFLASH設定を出荷時設定へ戻すため、送信前にバックアップ可能な範囲と復元の限界を確認し、送信後の反映確認を計画してください。

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

### 7.4 初期化後の再起動

p.149は本コマンド実行後にリスタートまたは電源再起動を求めています。汎用・拡張ポートに関する※注記だけを条件にして、その他の初期化では再起動不要と読み替えません。6FhはFLASH初期化、9Dhは再起動で、別の要求です。ACK受信だけを自動再起動済みと扱いません。

[リスタート](4e_9d_restart_reader.md)にはACK/NACKがなく、次コマンドまで2秒以上空けます（p.148）。この待機時間は6Fhの処理時間やACK期限ではありません。初期化ACK・再起動要求・通信確認・設定反映確認を分けて記録します。p.17の工場出荷時モードは00hですが、実機の初期化後状態は確認を省略しません。

### 7.5 バックアップの範囲と限界

本要求には初期化するアドレス・パラメータ種類・範囲の指定欄がありません。特定ポートだけの初期化やRAMだけの初期化へ転用しません。p.149の「FLASH設定を出荷時設定に戻す」は、全物理番地・校正値・通信モジュール・ネットワーク設定までの初期化リストではなく、それらの包含・除外は未確認です。

バックアップは各設定の対応する読取りで、保存先と取得範囲を明示して行います。[B4h読取り](4f_b4_read_flash_settings.md)は指定アドレスの1 byteアクセスであり、FLASH全体の一括読出しではありません。未掲載・予約領域を総当たりで取得せず、51hのRAM例外も分けます。保存モード等の独立読出し方法が未確認なら、その値を取得済み・完全復元可能としません。

初期値は各設定の機種・ROM条件で確認します。例えばp.343の拡張ポート方向・初期値やp.344の時間設定には機種・ROM差があります。未知の値を0で埋めたり、一機種の初期値を全機種へ流用したりしません。FLASHと両RAM、現在出力は別に記録し、FLASH復元後の再起動でRAMが上書きされる順序も考慮します。

### 7.6 受付条件と影響分類

65h／66hの連続モード中は6Fhも9Dhも受付例外ではなく、動作保証外です（p.19–20）。[モード書込み](4e_00_10_write_reader_mode.md)で00hへ復帰してから扱います。停止前に読めない設定は未取得とし、初期化後の値で元設定を補いません。

FLASHを変更するためwrite_operation=true、flash_operation=true、操作区分settings-changeとします。要求に追加パラメータはありませんが、対象機種・ROM・復元範囲・外部出力・RF条件の確認は必要です。rf_emission・requires_antennaのtrueは後続再起動も含む条件付き影響です。ROM 1.120以前のUTR-S201では、再起動時の断線確認がRFを使います（p.48–49）。6Fh自体をRFタグへの書込み要求とは扱いません。

## 8. 固定ACKと異常時の扱い

### 8.1 ACKと反映確認

要求はCMD=4Eh、LEN=01h、DATA[0]=6Fh、成功ACKはCMD=30h、LEN=01h、DATA[0]=6Fhで、双方総8 byteです（p.149）。フレーム長・SUMと未完了要求への対応を確認します。ACKには初期値、初期化件数、対象範囲、再起動完了フラグは含まれません。

ACK後は許可された手順でリスタートまたは電源再起動し、通信可能なことと設定反映を別々に確認します。ROM読取り成功だけで全設定の初期化・復元やRF条件の確認を済ませません。再設定後も機種・ROM・アンテナ・出力・周波数・停止方法を確認してからRF動作へ進みます。

### 8.2 NACK・timeout・不正フレーム

NACKは[共通マスタ](../../RESPONSE_AND_NACK_MASTER.md)の§7.6に従って解析します。未出典の「代表NACK」を本コマンドの保証値にしません。timeoutや不正フレームはACK未確認であり、初期化未実施の証拠ではありません。NACKについても全設定が元のままという原子性は未確認です。

異常時は自動再送・再起動・追加初期化を行わず、通信状態、取得できる設定、開始前の記録から復旧を判断します。FLASH初期化を接続不良時の一般的な復旧手段にしません。p.71は同一内容を含むFLASH書換え回数を減らすよう求めており、記載の10万回以下は保証値ではありません。

### 8.3 残る確認事項

初期化対象・除外項目の完全な一覧、ACK返却と永続化の厳密な時点、初期化中のRAMへの反映順、電源断・失敗時の反映単位、最長処理時間、通信設定と接続の扱いは未確認です。p.149の再起動要件を保持し、未確認事項を「全設定を一括退避・完全復元可能」という実装前提で埋めません。

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

- `../../RAM_FLASH_IMPACT_MATRIX.md`
- `../../RF_SAFETY_AND_CARRIER_RULES.md`
- `../../SOURCE_REVIEW_STATUS.md`
- `4e_00_10_write_reader_mode.md`
- `4e_9d_restart_reader.md`
- `rom_version_read.md`
- `4f_b4_read_flash_settings.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
