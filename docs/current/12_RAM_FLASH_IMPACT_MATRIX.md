---
title: "RAM・FLASH影響整理"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs: []
tags:
  - "utr-s201"
  - "guide"
  - "ram-flash"
---

# RAM・FLASH影響整理

## 1. 目的

この文書は、設定変更がRAMだけに影響するのか、FLASHなどの永続設定に影響するのかを確認するための整理資料です。

公式PDFが一次情報です。実装前に、対象コマンドの該当節と機種・ROM条件を確認してください。

## 2. 影響分類

| 分類 | 代表例 | 確認すること |
|---|---|---|
| 読み取りのみ | 設定値読み取り、ROM読み取り | 通常は設定変更なし。対象機種とレスポンス形式を確認する。 |
| RAM上の一時設定 | 動作中だけ有効な設定 | 再起動時に失われるか確認する。 |
| FLASH保存を伴う設定 | FLASH設定値書き込み、FLASH初期化 | 変更前の値、変更後の値、復旧方法を記録する。 |
| RF関連設定 | 周波数、送信出力、アンテナ設定 | 地域条件、接続アンテナ、現場条件を確認する。 |
| タグメモリ操作 | Write、Lock、Kill、Encode | 対象タグ、メモリ領域、Accessパスワード、復旧可否を確認する。 |

## 3. 実装時の扱い

プロトコル仕様書にある設定変更は、条件が揃えば実施対象です。

ただし、AIが独断でRAM/FLASHの保存先、設定値、復旧方法を決めないようにします。実機送信する場合は、変更前後の値と復旧手順をログに残します。

## 4. GitHubに残さないもの

- runtime logs
- 実CSVログ
- 顧客情報
- 実IPアドレス
- raw EPC / UII / TID
- 認証情報
- 完成Hex
- SUM計算済み送信用コマンド例