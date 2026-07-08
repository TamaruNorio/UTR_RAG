# Artifacts

## 1. 目的

このディレクトリは、UTR-S201 AI補助RAGの成果物ZIP、MANIFEST、成果物READMEを保管する。

## 2. 現在の成果物一覧

| Version | Path | Package name | SHA256 | Release / Status | Purpose | Current use | Notes |
|---|---|---|---|---|---|---|---|
| v004 | `artifacts/utr_s201_ai_v004/utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip` | `utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip` | `2103B818045608383FD94F0047B471D4B2E3A3610BC8E46EAA644DF29F738521` | R7-5A / pre-RC候補 | no-PDF成果物の初期整理 | 履歴保持用 | 現在の外部レビュー候補ではない |
| v005 | `artifacts/utr_s201_ai_v005/utr_s201_ai_v005_full_command_internal_release_no_pdf.zip` | `utr_s201_ai_v005_full_command_internal_release_no_pdf.zip` | `20F87EE55FC3B555EABE38BB3492CFEB303754E7539DAD8D0BC46BEBD7B29712` | internal pre-release / internal release candidate | full-command internal release | 内部確認・履歴保持用 | 現在の外部レビュー候補ではない |
| v006 | `artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip` | `utr_s201_ai_v006_external_review_candidate_no_pdf.zip` | `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA` | `utr-s201-ai-v006-r9-7-external-review-candidate.1` | External Review Candidate | Release済み成果物 | v006 ZIP、Release、tag、assetは変更しない |
| v007 | `artifacts/utr_s201_ai_v007/utr_s201_ai_v007_final_minimal_no_pdf.zip` | `utr_s201_ai_v007_final_minimal_no_pdf.zip` | `3DE8BEAD99BFE25DC30F1EFF85ADB354B3F4AB3322E6F37E75D268F62037BD62` | final minimal package | v006から不要な作業履歴文書を除外した整理版 | 現在の最終整理版 | 正式社外公開版、正式RC、顧客提供版、PDF正本の代替ではない |

## 3. v007の位置づけ

- final minimal package
- no-PDF
- v006から不要な作業履歴文書を除外した整理版
- 日本国内向け
- 日本語利用者向け
- 日本の電波法準拠機器向け
- 正式社外公開版ではない
- 正式RCではない
- 顧客提供版ではない
- PDF正本の代替ではない
- 海外販売・海外運用向けではない

## 4. 重要ルール

- Release済みZIPは削除しない
- Release済みZIPは上書きしない
- Release済みZIPは再作成しない
- ZIPを作り直す場合は新しいversionを作成する
- 既存ZIPを別ZIPに二重梱包しない
- PDFをZIPに含めない
- 完成Hex、SUM計算済みコマンド、実機送信用コードを含めない
- 顧客情報、タグ固有ID、実IPアドレスを含めない
