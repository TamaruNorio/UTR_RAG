---
title: "V100 Final Usage Guide"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs:
  - "09_COMMAND_MASTER_V117.md"
  - "10_RESPONSE_AND_NACK_MASTER.md"
  - "11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "20_VERIFICATION_RESULT_STATUS.md"
tags:
  - "utr-s201"
  - "guide"
  - "v100"
---

# V100 Final Usage Guide

## 1. この文書の目的

この文書は、UTR_RAGをAIペアプログラミングで使うための入口です。

対象読者は、AIを使ったペアプログラミング経験があり、Git / GitHub の基本操作を理解している開発者です。実装言語は限定しません。Python、C#、C++、JavaScript、その他の言語でも利用できます。

## 2. UTR_RAGでできること

- UTR-S201 シリーズのコマンド仕様を調べる。
- コマンド別に、目的、パラメータ、応答、NACK、注意点を確認する。
- ROMバージョンとシリーズ名から、対象機種を整理する。
- AIに実装、移植、レビュー、テスト観点整理を依頼するための前提資料にする。
- 実機送信前に、対象、パラメータ、影響、復旧方法、停止条件を確認する。

## 3. 公式PDFの扱い

公式PDFが一次情報です。このリポジトリは公式PDFの代替ではありません。

PDF原本は、社内の正式な配布場所または管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

## 4. 最初に読む順番

1. `README.md`
2. `llms.txt`
3. `docs/current/AI_CONTEXT_INDEX.md`
4. `docs/current/09_COMMAND_MASTER_V117.md`
5. `docs/current/commands/cards/`
6. `docs/current/10_RESPONSE_AND_NACK_MASTER.md`
7. `docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
8. `docs/current/20_VERIFICATION_RESULT_STATUS.md`

対象範囲が広い場合は、上記をまとめてAIに読ませても構いません。対象コマンドが決まっている場合は、該当するコマンドカードと関連文書を中心に読ませます。

## 5. AIに依頼するときの指定項目

AIに作業を依頼するときは、最低限以下を指定します。

- 目的
- 対象機種
- 接続方式
- 対象コマンド
- 実装言語
- 実行環境
- 実機送信の有無
- 変更してよい範囲
- 変更してはいけない範囲
- 確認方法

## 6. 実装前の分類

実装前に、対象処理を以下に分類します。

| 分類 | 例 | 扱い |
|---|---|---|
| 読み取りのみ | ROM読み取り、設定値読み取り | 机上確認後、条件が揃えば実機確認候補 |
| RF読み取り | Inventory、Read | タグ、アンテナ、ログ、停止条件を確認して実施候補 |
| 設定変更 | 周波数、出力、アンテナ、InventoryParam | 必要に応じて実施対象。対象、値、影響、復旧方法、停止条件を明確にする |
| 永続設定 | FLASH write / init | 永続影響があるため、対象、値、復旧計画、社内手順を明確にする |
| タグメモリ操作 | Write、Lock、Kill、Encode | 対象タグ、メモリ領域、パスワード、復旧可否、停止条件を明確にする |

## 7. GitHubにアップロードしない情報

以下はGitHubにアップロードしないでください。

| 種類 | 扱い |
|---|---|
| PDF原本 | 社内の正式な管理場所から別途準備する |
| runtime logs | ローカル確認用に留める |
| 実CSVログ | 必要に応じてマスク・要約する |
| 顧客情報 | 顧客名、現場名、個別条件を公開しない |
| 実IPアドレス | `192.168.xxx.xxx` のようにマスクする |
| raw EPC / UII / TID | 必ずマスクする |
| 認証情報 | APIキー、パスワード、トークンを記載しない |
| 完成Hex | そのまま実機送信できる形で安易に記載しない |
| SUM計算済み送信用コマンド例 | 実機誤送信を避けるため、安易に記載しない |

## 8. 実機操作の考え方

プロトコル仕様書に存在するコマンドを、高影響という理由だけで禁止扱いにはしません。

プロトコル仕様書に記載され、対象機種、ROMバージョン、地域条件、現場条件を満たすコマンドは、実装・実機送信の対象にできます。

周波数変更、送信出力変更、アンテナ設定変更、InventoryParam / SelectParam / ExpandSelectParam 変更なども、必要に応じて実施対象になります。

ただし、AIが独断で次のことをしないようにします。

- 作業指示にない高影響操作を追加する。
- 設定値や周波数、出力値を勝手に決める。
- 対象機種、ROM、地域条件を確認せずに送信する。
- NACK、timeout、LBT、アンテナエラー発生後に継続判断する。

実機送信時には、対象、パラメータ、影響、復旧方法、停止条件、ログ方針を作業指示として明確にします。
