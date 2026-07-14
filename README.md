# UTR_RAG

UTR_RAG は、UTR-S201シリーズ通信プロトコル説明書 Ver.1.17 を前提に、AIが参照しやすいRAG用ドキュメント、コマンドカード、段階的な実機確認記録、no-PDF成果物を管理するリポジトリです。

本リポジトリは、公式PDFの代替ではありません。実装・調査・レビューを支援するためのAI補助パッケージです。

## 1. 最新成果物

最新の成果物は v022 Final RC no-PDF package です。

- Release tag: `utr-s201-ai-v022-final-rc.1`
- ZIP: `artifacts/utr_s201_ai_v022/utr_s201_ai_v022_final_rc_no_pdf.zip`
- SHA256: `2A7E97DE4A19B634EC49953B5E6815C307C90D0E420AA381E3AF5752C9166984`
- Final RC review: `docs/current/43_FINAL_RC_REVIEW.md`
- Release decision notes: `docs/current/44_RELEASE_DECISION_NOTES.md`

v022 は、v019 Stage 2 read completion、v020 Stage 3+ high-impact readiness、v021 Stage 3+ first batch planning、AI context / frontmatter metadata、54件のコマンドカードを統合したFinal RCです。

## 2. 位置づけ

このリポジトリの成果物は次の位置づけです。

- 日本国内仕様を前提とします。
- 主な利用者は日本語話者です。
- PDF原本は含めません。
- 正式な社外公開版ではありません。
- 顧客提供版ではありません。
- 量産・本番運用版ではありません。
- 公式PDFの代替ではありません。
- 全54コマンドを個別に実機送信済みとは主張しません。

## 3. 主な参照先

- `llms.txt`
- `docs/README.md`
- `docs/OPERATIONS.md`
- `docs/current/AI_CONTEXT_INDEX.md`
- `docs/current/00_OVERVIEW.md`
- `docs/current/09_COMMAND_MASTER_V117.md`
- `docs/current/16_TRACEABILITY_INDEX_V117.md`
- `docs/current/20_VERIFICATION_RESULT_STATUS.md`
- `docs/current/commands/cards/`
- `artifacts/README.md`

## 4. 現在の到達点

| Version | 内容 | 状態 |
|---|---|---|
| v009 | Ver.1.17 traceability completed no-PDF package | 履歴上のクリーンRAG基準 |
| v019 | Stage 2 read completion no-PDF package | pre-release完了 |
| v020 | Stage 3+ high-impact readiness | merge済み、実機送信なし |
| v021 | Stage 3+ first batch planning | merge済み、実機送信なし |
| v022 | Final RC no-PDF package | pre-release完了 |

## 5. v019 Stage 2 read completion

v019 では、明示的な `safe-tid` 読み取り専用プロファイルを使い、ROM read、UHF_CheckAntenna、UHF_GetHandle、UHF_Inventory、UHF_InventoryRead、UHF_Read を notes付きで完了しました。

v019では、書き込み系、FLASH、周波数変更、出力変更、アンテナ設定変更、InventoryParam / SelectParam / ExpandSelectParam変更、タグメモリ書き込み、Lock、Kill、Encode、ThroughCmdは実行していません。

## 6. v020 Stage 3+ high-impact readiness

v020 では、Stage 3以降の高影響コマンドを整理しました。プロトコル上の対応可否と、実行許可を分離しています。

Stage 3+ の実機実行には、明示許可、パラメータ確定、影響確認、復旧計画、runtime logging、停止条件が必要です。v020では実機送信、ZIP作成、GitHub Release作成は行っていません。

## 7. v021 Stage 3+ first batch planning

v021 では、Stage 3+ の最初の実行候補バッチを選定するための計画文書を追加しました。

- Stage 3+ first execution batch plan
- Stage 3+ parameter sheet
- Stage 3+ operator approval template

v021では実機送信、ZIP作成、GitHub Release作成は行っていません。

## 8. v022 Final RC package

v022 は、現時点のno-PDF UTR-S201 AI assistant packageをFinal RCとして統合したものです。

含むもの:

- Stage 2 read completion
- Stage 3+ readiness
- Stage 3+ first batch planning
- AI context / frontmatter metadata
- 54 command cards
- current verification and HOLD notes

含まないもの:

- PDFファイル
- runtime logs
- 実CSVログ
- 顧客情報
- 実IPアドレス
- raw EPC / UII / TID

## 9. AI context / frontmatter 方針

本リポジトリでは、階層構造、index文書、標準Markdownリンク、frontmatter metadataを併用します。

- `llms.txt` はAI向けの最初の地図です。
- `docs/current/AI_CONTEXT_INDEX.md` は詳細なAIナビゲーションです。
- `docs/current/FRONTMATTER_SCHEMA.md` はfrontmatterのキー定義です。
- `docs/current/TAG_TAXONOMY.md` はタグ語彙です。
- `docs/current/commands/cards/` 配下のコマンドカードはfrontmatter metadataを持ちます。
- 標準Markdownリンクを優先します。
- 新規のObsidian形式wikilinkは追加しません。

## 10. 安全方針

- プロトコル仕様書に定義されたコマンドを、高影響という理由だけで禁止扱いしません。
- 高影響コマンドは、条件、パラメータ、影響、復旧方法、明示許可を整理して扱います。
- 実機送信ログ、顧客情報、raw EPC / UII / TID、実IPアドレスはGitに含めません。
- 完成HexやSUM計算済みの送信用コマンド例は、安易にドキュメントへ追加しません。
