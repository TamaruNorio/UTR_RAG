---
title: "UHF_GetHandle"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.3.12"
command_group: "reader_control"
command_name: "UHF_GetHandle"
command_byte: "55h"
detail_command: "46h"
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
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
  - "../../PARAMETER_CONFIRMATION_GUIDE.md"
  - "../../AI_IMPLEMENTATION_GUARDRAILS.md"
  - "4e_9e_rf_carrier_control.md"
  - "55_10_uhf_inventory.md"
  - "55_31_uhf_set_inventory_param.md"
  - "55_30_uhf_set_select_param.md"
  - "4e_00_10_write_reader_mode.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "55_ff_uhf_through_cmd.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-control"
  - "read-only"
  - "specification-reference"
  - "uhf-get-handle"
---

# UHF_GetHandle（ハンドル取得）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_GetHandle** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.12`
- コマンド分類: リーダライタ制御
- 確認区分: `read-only`
- 操作レベル: 読み取り専用
- コマンドバイト: `55h` / 詳細コマンド: `46h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

リーダライタ内部に保持している、RFタグから最後に取得した16 bitのHandleを読みます（p.150）。新しいHandleの取得やタグ側との一致確認を、この要求単独で実行するという意味ではありません。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

p.108の機種別対応表では、UTR-S201・UTR-SHR201・UTR-SUN02-4CHはROM 2.040以前が非対応、2.050以降／2.100以降が対応です。UTR-SUN02-8CH・UTR-SUN02V-8CHは「全バージョン」列が対応です。複数列に該当する場合は最も右の列を使用し、4CHを8CHの列へ含めません。未掲載ROMの空白範囲は推測で埋めません。

両コマンドともp.19–20の連続モード65h／66h中の受付例外ではありません。[モード書込み](4e_00_10_write_reader_mode.md)で00hへ戻す条件を確認します。

p.150冒頭の「ROM 2.050以降」という注意と、上記の機種別対応表を併せて参照してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | 本要求は内部保持値の読取り。前後のRF処理は別 |
| 書き込み操作 | なし |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | 本要求単独は不要。Handle使用フローでは必要 |
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

以下は、公式PDF `7.3.12` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.3.12 UHF_GetHandle
 リーダライタ内部に保持している、
                「RFタグから最後に取得したHandleデータ」を取得する
 コマンドです。
 ※リーダライタのROMバージョンがVer.2.050以降の場合に有効なコマンドです。
 Open状態、Secured状態のRFタグに対してコマンドを送信する際に、RFタグから取得したHandle
 データをコマンドパラメータにセットする必要があります。
 [UHF_ThroughCmd]を使用してカスタムコマンドを実行する場合など、必要に応じてリーダライタ
 からHandleデータを取得してください。

  [コマンド]
 ラベル名   バイト数                            内容
  STX         1        02h
 アドレス         1        00h（「5.2 通信フォーマットの詳細」参照）
 コマンド         1        55h
 データ長         1        01h
 データ部         1        46h（詳細コマンド）
  ETX         1        03h
  SUM         1        SUM 値（ 「5.4 SUM の計算方法」参照）
   CR         1        0Dh

 RFタグが保持しているHandleデータは、RFタグがOpen状態またはSecured状態から抜けるとクリ
 アまたは再生成されてしまいますので、正しいフローで制御しないと、「リーダライタ内部で保持し
 ているHandleデータ」と「RFタグが生成したHandleデータ」が異なる可能性があります。
 Handleデータを取得してコマンド制御に使用する場合は、以下の手順で処理をおこなう必要があり
 ますのでご注意ください。
   1．RF送信信号の制御コマンドを実行し、キャリア出力をONする。
   2．Inventoryコマンドを以下のパラメータで実行し、RFタグをOpen状態とする。
    ・Q値の自動UP/DOWN機能=使用しない
    ・Q値の開始値=0
    ・Q値の最小値=0
    ・Q値の最大値=0
    ※複数のRFタグから1枚を指定して処理をおこなう場合は、事前にSelectコマンドを実行する設
      定も必要です。
   3．UHF_GetHandleコマンドを実行してHandleデータを取得する。（必要に応じて）
   4．UHF_ThroughCmdを使用してRFタグのカスタムコマンドを実行する。
    （必要に応じてHandleデータをパラメータに含める）
   5．RF送信信号の制御コマンドを実行し、キャリア出力をOFFする。      （推奨処理）
      ※不要な電波を出し続けると電波干渉の要因となりますので、処理終了後は直ちにキャリア
        出力OFFすることを推奨します。
   ※Handleデータは、UHF_ThroughCmdのパラメータ設定により、RFタグへの送信データに自動
    的に付与させることも可能です。
    詳細は「7.5.11 UHF_ThroughCmd」をご参照ください。


 [ACK レスポンス]
ラベル名    バイト数                                 内容
 STX      1          02h
アドレス      1          00h（「5.2 通信フォーマットの詳細」参照）
コマンド      1          30h（ACK）
データ長      1          03h
          1          46h
データ部                 RF タグから受信した Handle 値
          2
                       ※MSB ファーストでセットされます
 ETX          1      03h
 SUM          1      SUM 値（ 「5.4 SUM の計算方法」参照）
  CR          1      0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
    • コマンド
       02 00 55 01 46 03 A1 0D
    • レスポンス
       02 00 30 03 46 52 90 03 60 0D
        ※取得した RF タグの Handle 値がリーダライタに維持されている状態で
         [UHF_GetHandle]コマンドを実行し、Handle 値 = [52 90]h が返ってきた場合
```

原典参照の補足（2026-09-08）: 上記の「5.4 SUM の計算方法」は、Ver.1.17では「5.3 SUM の計算方法」（p.100）を参照してください。§5.4はレスポンスの説明です。PDF転記は保持し、本注記を分けています。この時点ではSUM参照だけの照合でした。2026-09-14にp.150–151の主要条件を追加照合しました。全条件の実機確認ではありません。

## 7. 要求と固定ACK

DATA offsetは0起点です。要求はCMD=55h・LEN=01h・DATA[0]=46h、総8 byte。追加パラメータはありません（p.150）。ACKはCMD=30h・LEN=03h、総10 byteです（p.151）。

| ACK DATA offset | 内容 |
|---:|---|
| 0 | 46h |
| 1 | Handle上位byte |
| 2 | Handle下位byte |

HandleはMSB firstです。p.151の52 90は5290hで、9052hではありません。共通フレームの長さ・SUMと要求の対応を検査し、LEN=01hの空ACKへ読み替えません。掲載Hexは原典の説明例であり、実機への送信許可ではありません。

## 8. Handleの有効性と応答処理

### 8.1 保持値とタグ状態

ACKが返っても、返却Handleと現在のタグHandleの一致を保証する応答ではありません。タグがOpen／Securedから抜けるとHandleがクリア・再生成され得ます（p.150）。HandleをEPC/TIDのような恒久IDとして保存・再利用しません。

GetHandleにRAM/FLASH選択、アンテナ指定、タグ探索パラメータはありません。メタデータread-only・rf_emission=falseは内部保持値を読む本要求の分類であり、実行中キャリアがOFFであることを保証しません。下記の準備・利用にはRF送信とタグが必要です。

### 8.2 原典の使用フロー

1. [RF制御](4e_9e_rf_carrier_control.md)でキャリアON。
2. [Inventory](55_10_uhf_inventory.md)をQ自動UP/DOWNなし、開始・最小・最大Qすべて0で実行し、タグをOpenへ移す。複数タグから1枚を扱う場合は事前に[Select](55_30_uhf_set_select_param.md)実行の設定も行う。
3. 必要ならGetHandleで保持値を取得する。
4. [ThroughCmd](55_ff_uhf_through_cmd.md)でカスタムコマンドを実行する。Handle自動付加なら手順3は不要だが、1・2は必要。
5. 終了後は直ちにキャリアOFFにすることが原典の推奨。

RF維持は出力開始から最大4秒です。OFF・4秒経過・新Handle取得・タグ読み書きNACK等の後に旧Handleを使い続けません。NACKによるHandle破棄とRF OFFは別です（p.129–135）。ThroughCmdの自動付加も古いHandleを有効に戻す機能ではありません。

### 8.3 応答の区別と未確認範囲

このACKへInventoryのタグ別応答、読取完了、TID付加、アンテナID出力、キャリア検知通知の設定を適用しません。共通受信側で別の通知を受けてもGetHandleの完了と混同しません。

CMD=31hは[共通NACK](../../RESPONSE_AND_NACK_MASTER.md)で解析し、timeout・不正フレームと分けます。Handle未取得・破棄済み時の返却値や固有NACK、0000hを無効とする判定、全ROMの保持期間はp.150–151だけでは確定しません。未確認状態で値から有効性を推測しません。

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
- `../../RF_SAFETY_AND_CARRIER_RULES.md`
- `../../PARAMETER_CONFIRMATION_GUIDE.md`
- `../../AI_IMPLEMENTATION_GUARDRAILS.md`

- `4e_9e_rf_carrier_control.md`
- `55_10_uhf_inventory.md`
- `55_31_uhf_set_inventory_param.md`
- `55_30_uhf_set_select_param.md`
- `4e_00_10_write_reader_mode.md`
- `../../SOURCE_REVIEW_STATUS.md`
- `55_ff_uhf_through_cmd.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
