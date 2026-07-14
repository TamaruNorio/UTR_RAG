---
title: "トレーサビリティ索引 Ver.1.17"
doc_type: "index"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs: []
tags:
  - "utr-s201"
  - "traceability"
  - "v100"
---

# トレーサビリティ索引 Ver.1.17

## 1. 目的

この文書は、UTR-S201シリーズ通信プロトコル説明書 Ver.1.17 と、リポジトリ内のドキュメント・コマンドカードの対応関係を確認するための索引です。

## 2. 確認する対応関係

- PDF 6.1 コマンド一覧
- PDF 6.2 リーダライタ別コマンド対応表
- PDF 7章 各コマンド形式
- PDF 7.6 共通NACK
- RAM / FLASH影響
- RF / キャリア / アンテナ条件
- 実機確認ステージ

## 3. 使い方

1. `COMMAND_MASTER_V117.md` で対象コマンドを確認する。
2. `docs/current/commands/cards/` の対象コマンドカードを開く。
3. コマンドカード内の参照ドキュメントを確認する。
4. 公式PDFの該当章で一次情報を確認する。
5. 実機送信が必要な場合は、対象、値、影響、復旧方法、停止条件、ログ方針を明確にする。

## 4. 注意

この索引は、公式PDFの代替ではありません。

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

runtime logs、実CSVログ、顧客情報、実IPアドレス、タグIDなどの生情報はGitHubにアップロードしないでください。必要な場合はマスク・要約してください。