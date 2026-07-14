# UTR_RAG ドキュメント

このディレクトリには、UTR-S201シリーズ向けAI補助ドキュメントを格納します。公式PDFの内容を置き換えるものではなく、実装、調査、レビュー、段階的な実機確認を支援するためのno-PDFドキュメント群です。

## 1. 最新状態

最新の統合成果物は v022 Final RC no-PDF package です。

- ZIP: `artifacts/utr_s201_ai_v022/utr_s201_ai_v022_final_rc_no_pdf.zip`
- Final RC review: `docs/current/43_FINAL_RC_REVIEW.md`
- Release decision notes: `docs/current/44_RELEASE_DECISION_NOTES.md`
- SHA256: `2A7E97DE4A19B634EC49953B5E6815C307C90D0E420AA381E3AF5752C9166984`

## 2. 主要ドキュメント

最初に読むべき文書は以下です。

- `docs/current/AI_CONTEXT_INDEX.md`
- `docs/current/00_OVERVIEW.md`
- `docs/current/09_COMMAND_MASTER_V117.md`
- `docs/current/10_RESPONSE_AND_NACK_MASTER.md`
- `docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
- `docs/current/16_TRACEABILITY_INDEX_V117.md`
- `docs/current/20_VERIFICATION_RESULT_STATUS.md`
- `docs/current/commands/cards/`

## 3. 段階別の到達点

| Stage / Version | 内容 | 状態 |
|---|---|---|
| v009 | Ver.1.17 traceability completed | クリーンRAG基準 |
| v010 | 実機確認フレームワーク | no-PDF package |
| v011 | Stage 0/1 read-only verification kit | dry-run既定 |
| v012 | Stage 0 read-only result | masked summary |
| v013 | ROM read frame adapter | ROM 2.052 / USM02確認 |
| v014 | Stage 0 remaining read-only result | 3コマンド確認 |
| v015 | Stage 1 read-only configuration result | PASS / BLOCKED等を記録 |
| v016 | Stage 2 RF read preflight | 実行前提・停止条件を整理 |
| v017 | Stage 2 RF read minimal result | ZIPなし、最小実行結果 |
| v018 | Stage 2 RF read operations result | Inventory応答解析 |
| v019 | Stage 2 read completion | safe-tidでRead系完了 |
| v020 | Stage 3+ high-impact readiness | 実行ゲート整理、実機送信なし |
| v021 | Stage 3+ first batch planning | 初回実行候補計画、実機送信なし |
| v022 | Final RC no-PDF package | pre-release完了 |

## 4. v022の内容

v022には以下を含めます。

- PDF Ver.1.17に基づくコマンドマスタ
- 54件のコマンドカード
- ACK / NACK / timeout関連整理
- ROM / device identification flow
- Stage 0 / Stage 1 / Stage 2 の実機確認結果
- Stage 3+ high-impact readiness
- Stage 3+ first batch planning
- AI context / frontmatter metadata

## 5. 含めないもの

- PDFファイル
- runtime logs
- 生CSVログ
- 顧客情報
- 実IPアドレス
- raw EPC / UII / TID
- 旧ZIP

## 6. 安全方針

- 実機確認済みでない内容を、実機確認済みとは書きません。
- protocol support と execution permission を分けます。
- 高影響コマンドを、影響が大きいという理由だけで禁止扱いしません。
- Stage 3+の実機実行には、明示許可、パラメータ確定、復旧計画、停止条件が必要です。
