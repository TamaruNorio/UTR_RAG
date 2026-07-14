---
title: "V100概要"
doc_type: "index"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs:
  - "45_V100_FINAL_USAGE_GUIDE.md"
  - "09_COMMAND_MASTER_V117.md"
  - "10_RESPONSE_AND_NACK_MASTER.md"
  - "11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
tags:
  - "utr-s201"
  - "guide"
  - "v100"
---

# V100概要

この文書は、UTR_RAG の現在版である **V100 Final documentation package** の入口です。

## 1. 目的

UTR_RAGは、UTR-S201 シリーズの通信プロトコルをAIと一緒に扱いやすくするためのドキュメントセットです。

主な目的は以下です。

- コマンド仕様を探しやすくする。
- AIへ実装・レビューを依頼しやすくする。
- 実機送信前の確認事項を明確にする。
- 読み取り系、設定変更系、タグメモリ操作系を分けて扱う。
- 任意のプログラミング言語への移植を支援する。

## 2. 対象者

- AIを使ったペアプログラミング経験がある人
- Git / GitHub の基本操作を理解している人
- UTR-S201 シリーズの制御ソフトを作る人
- Python、C#、C++、JavaScriptなど任意の言語で実装したい人

## 3. 公式PDFとの関係

公式PDFが一次情報です。UTR_RAGは公式PDFの代替ではありません。

PDF原本は、社内の正式な配布場所または管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

このリポジトリは、公式PDFを参照しながら、AI補助で実装・確認・レビューを進めるための補助資料です。

## 4. 基本的な使い方

1. `AI_CONTEXT_INDEX.md` を読む。
2. `45_V100_FINAL_USAGE_GUIDE.md` で全体の使い方を確認する。
3. `09_COMMAND_MASTER_V117.md` で対象コマンドを探す。
4. `commands/cards/` の該当カードを読む。
5. `10_RESPONSE_AND_NACK_MASTER.md` で応答処理を確認する。
6. `11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md` でROMと機種差分を確認する。
7. 実機送信が必要な場合は、実行ゲート、復旧計画、停止条件を確認する。

## 5. 安全方針

高影響コマンドは、明示許可、パラメータ確定、影響確認、復旧方法、停止条件が揃うまで実機送信しません。

## 6. GitHubにアップロードしない情報

PDF原本、runtime logs、実CSVログ、顧客情報、実IPアドレス、raw EPC / UII / TID、完成Hex、SUM計算済み送信用コマンド例はGitHubにアップロードしないでください。
