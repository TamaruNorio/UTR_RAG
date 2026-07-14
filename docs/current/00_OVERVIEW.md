---
title: "概要"
doc_type: "index"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:
  - "43_FINAL_RC_REVIEW.md"
  - "44_RELEASE_DECISION_NOTES.md"
tags:
  - "utr-s201"
  - "guide"
---

# 概要

この文書は、`docs/current/` 配下の現在版ドキュメントの入口です。

## 1. 最新状態

最新成果物は v022 Final RC no-PDF package です。

- ZIP: `artifacts/utr_s201_ai_v022/utr_s201_ai_v022_final_rc_no_pdf.zip`
- SHA256: `2A7E97DE4A19B634EC49953B5E6815C307C90D0E420AA381E3AF5752C9166984`
- Final RC review: `43_FINAL_RC_REVIEW.md`
- Release decision notes: `44_RELEASE_DECISION_NOTES.md`

## 2. 対象範囲

対象は、UTR-S201シリーズ通信プロトコル説明書 Ver.1.17 に基づくAI補助用ドキュメントです。

整理対象:

- 54件のコマンドカード
- コマンド一覧とコマンドフォーマット
- ACK / NACK / timeout
- ROMによる機種判定
- device / ROM support
- RAM / FLASH影響
- RF safety / carrier rules
- Stage 0 / Stage 1 / Stage 2 の実機確認結果
- Stage 3+の高影響コマンドに対する実行ゲートと復旧計画
- AI context / frontmatter metadata

## 3. 位置づけ

このドキュメント群は、公式PDFの代替ではありません。

また、以下ではありません。

- 正式な社外公開版
- 顧客提供版
- 本番運用版
- 海外利用または海外販売の承認資料
- 全54コマンドの個別実機送信完了記録

## 4. version別整理

| Version | 内容 | 状態 |
|---|---|---|
| v009 | traceability completed no-PDF package | 履歴上のクリーンRAG基準 |
| v019 | Stage 2 read completion | pre-release完了 |
| v020 | Stage 3+ high-impact readiness | 実機送信なし、計画整理 |
| v021 | Stage 3+ first batch planning | 実機送信なし、初回候補計画 |
| v022 | Final RC no-PDF package | pre-release完了 |

## 5. 実機確認の現状

Stage 2 read completion では、`safe-tid` 読み取り専用プロファイルにより、UHF_InventoryRead と UHF_Read を notes付きで確認しました。

Stage 3+では、Write、Kill、Lock、BlockWrite、Encode、ThroughCmd、FLASH、周波数、出力、アンテナ設定などの高影響コマンドを整理済みです。ただし、v020〜v022ではこれらの実機送信は行っていません。

## 6. 安全方針

- protocol support と execution permission を分けます。
- 高影響コマンドは、条件、パラメータ、影響、復旧方法、明示許可を揃えてから扱います。
- runtime logs、実CSVログ、顧客情報、raw EPC / UII / TID、実IPアドレスはGitに含めません。
- 完成HexやSUM計算済み送信用コマンド例は安易に追加しません。
