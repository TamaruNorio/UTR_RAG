---
title: "V100 Final Usage Guide"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs:
  - "00_OVERVIEW.md"
  - "09_COMMAND_MASTER_V117.md"
  - "10_RESPONSE_AND_NACK_MASTER.md"
  - "11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "14_AI_IMPLEMENTATION_GUARDRAILS.md"
tags:
  - "utr-s201"
  - "v100"
  - "guide"
  - "final-documentation"
---

# V100 Final Usage Guide

## 1. 目的

この文書は、UTR_RAGを使ってAIとペアプログラミングする開発者向けの最終版利用ガイドです。

対象者は、Git / GitHubの基本操作を理解し、ChatGPT、Codex、GitHub Copilotなどを使って実装・レビューを進められる人です。実装言語は限定しません。

## 2. このリポジトリで行うこと

UTR_RAGでは、UTR-S201シリーズの制御プログラムを作るために必要な情報を、AIが参照しやすい単位で整理しています。

主に以下を扱います。

- コマンド一覧
- 個別コマンドカード
- ACK / NACK / timeoutの考え方
- ROMバージョンによる機種判定
- RAM / FLASH影響
- RF送信、アンテナ、タグメモリ操作の安全条件
- 実機確認の段階管理
- AI実装時のガードレール

## 3. 使い方の基本手順

### 3.1 調査する

1. `docs/current/09_COMMAND_MASTER_V117.md` で対象コマンドを探します。
2. `docs/current/commands/cards/` の個別カードを開きます。
3. コマンドバイト、詳細コマンド、サブコマンド、必要条件を確認します。
4. `docs/current/10_RESPONSE_AND_NACK_MASTER.md` で応答処理を確認します。
5. `docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md` で対象機種とROM条件を確認します。

### 3.2 AIへ依頼する

AIへ依頼するときは、以下を明示します。

- 対象機種
- 接続方式
- 対象コマンド
- 実装言語
- dry-runか、実機送信を含むか
- 書き込み、FLASH、周波数、出力、アンテナ、タグメモリ操作を含むか
- 参照するコマンドカード

依頼文の例です。

```text
UTR-S201シリーズ向けに、PythonでROMバージョン読み取り処理を実装してください。
まず docs/current/commands/cards/4f_90_read_rom_version.md を参照してください。
ACK、NACK、timeoutを分けて処理してください。
実機への書き込み、FLASH操作、周波数変更、出力変更、タグメモリ操作は実装しないでください。
```

### 3.3 実装する

AIが生成したコードは、そのまま実機へ送信しないでください。最初に以下を確認します。

- 送信フレームを勝手に完成させていないか。
- SUM計算済みの送信用コマンドを無断で追加していないか。
- 読み取り系と書き込み系が分離されているか。
- timeout処理があるか。
- NACKを共通フォーマットで解析しているか。
- ログに必要情報が残るか。
- 危険操作が明示許可なしに実行されないか。

## 4. 高影響操作の扱い

以下は、明示許可なしに実行しません。

- FLASH write / init
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- InventoryParam / SelectParam / ExpandSelectParam変更
- タグメモリ書き込み
- Lock
- Kill
- Encode
- ThroughCmd

これらは、仕様上存在していても、実行には別途確認が必要です。

## 5. 実機確認前のチェック

実機送信前に以下を満たしてください。

| 確認項目 | 内容 |
|---|---|
| 対象機種 | ROMバージョン読み取りで機種を確認する |
| 接続条件 | COMポート、LAN接続先、timeoutを明示する |
| 対象コマンド | 読み取りか、高影響操作かを分ける |
| パラメータ | 未確定値を残さない |
| 停止条件 | NACK、timeout、無応答、LBT、アンテナエラー時の停止を決める |
| 復旧手順 | 設定変更やタグ操作時は復旧方法を決める |
| ログ | 送信目的、パラメータ、ACK/NACK、結果を残す |

## 6. V100の位置づけ

V100は、過去の作業履歴ではなく、現在の利用方法を説明する最終版です。

このリポジトリを使う人は、まずこの文書とREADMEを読み、必要なコマンドカードを参照してから、AIへ実装またはレビューを依頼してください。

社外公開、顧客提供、海外利用、Stage 3+実機送信は、引き続き別途承認が必要です。
