---
title: "RFタグ通信関連パラメータの読み取り"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.8"
command_group: "reader_setting"
command_name: "RFタグ通信関連パラメータの読み取り"
command_byte: "55h"
detail_command: "43h"
subcommand: "04h"
operation_stage: "Stage 1"
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
  - "../../09_COMMAND_MASTER_V117.md"
  - "../../16_TRACEABILITY_INDEX_V117.md"
  - "../../10_RESPONSE_AND_NACK_MASTER.md"
  - "../../11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "stage1"
  - "read-only"
  - "pass-with-notes"
---

# RFタグ通信関連パラメータの読み取り

## 1. コマンドの位置づけ

このコマンドは、リーダライタに設定されているRFタグ通信関連パラメータを読み取るためのコマンドです。

- PDF章番号: 7.4.8
- コマンド分類: リーダライタ設定
- コマンドバイト: `55h`
- 詳細コマンド: `43h`
- サブコマンド: `04h`
- 操作種別: 読み取り専用
- 実機確認段階: Stage 1
- 現在の確認結果: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

RFタグ通信に関係するリーダライタ側の現在設定を確認します。

設定を書き換えるコマンドではありません。読み取り専用のため、通常はFLASH、周波数、送信出力、アンテナ設定、タグメモリを変更しません。

## 3. 使用可否

判定: `SUPPORTED`

理由: UTR-S201シリーズ通信プロトコル説明書 Ver.1.17 の 7.4.8 に定義されているためです。

ただし、実装前にはROMバージョン読み取りにより対象機種とROM条件を確認してください。

## 4. 安全分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 設定変更 | なし |
| FLASH変更 | なし |
| タグメモリ変更 | なし |
| 外部I/O変更 | なし |
| 明示許可 | 通常不要。ただし実機送信時は対象機と接続条件を確認する |

## 5. 対象機種とROM確認

実装時は、最初にROMバージョンを読み取ってください。

確認する内容は以下です。

- ROMバージョン番号
- シリーズ名
- 対象機種
- 4CH / 8CHなどの機種差分
- PDFの対応表で対象コマンドが利用可能か

ROMから判断できることはAIや実装側で自動判定し、ROMから判断できない現場条件だけを利用者へ確認します。

## 6. 必要パラメータ

このカード上では、完成済みの送信用Hexは記載しません。

実装時に確認する条件は以下です。

- 対象機種
- ROMバージョン
- 接続方式
- 接続先アドレスまたはポート
- timeout値
- ログ出力先

## 7. 送信フォーマットの考え方

第5章の共通フレーム形式を使用します。

このカードでは以下を明示します。

- コマンドバイト: `55h`
- 詳細コマンド: `43h`
- サブコマンド: `04h`

このカードでは、完成Hex、SUM計算済み送信用コマンド、実機送信可能な完成コードは記載しません。

## 8. ACK応答

ACKを受信した場合は、PDF 7.4.8 の応答形式に従ってデータ部を解析します。

実装では以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- 受信途中の不完全フレーム

## 9. NACK応答

NACKは共通NACK形式を使って解析します。

確認すべき代表例は以下です。

- SUMエラー
- フォーマットエラー
- 受信エラー
- timeout
- RFタグ無応答
- UHF ICエラー
- LBTエラー
- アンテナエラー

予約バイトは、PDFで意味が定義されていない限り判定に使いません。

## 10. 実装時の注意

AIへ実装を依頼する場合は、以下を守ってください。

- 最初にROMバージョン読み取りを行う。
- 機種とROMを判定してから本コマンドを実行する。
- ACK、NACK、timeout、無応答を区別する。
- ログに送信目的、接続条件、ACK/NACK、結果、所要時間を残す。
- 読み取り専用コマンドとして扱い、書き込み処理を混在させない。

## 11. 現在のRAG判定

判定: `SUPPORTED`

現在の実機確認結果: `REAL_DEVICE_PASS_WITH_NOTES`

補足: v015のStage 1読み取り確認でACKが返ることを確認済みです。RFタグ通信そのものは実行していません。

## 12. 関連ドキュメント

- `docs/current/09_COMMAND_MASTER_V117.md`
- `docs/current/10_RESPONSE_AND_NACK_MASTER.md`
- `docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
- `docs/current/16_TRACEABILITY_INDEX_V117.md`
- `docs/current/17_REAL_DEVICE_VERIFICATION_FRAMEWORK.md`
- `docs/current/20_VERIFICATION_RESULT_STATUS.md`
