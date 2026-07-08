# R9-10 Artifact and ZIP Inventory

## 1. 結論

判定:

`R9-10_ARTIFACT_AND_ZIP_INVENTORY_READY_WITH_HOLD_NOTES`

v004、v005、v006のZIP成果物と用途を整理した。現在の外部レビュー候補はv006であり、v004/v005は履歴保持用または内部確認用として扱う。

## 2. 整理対象

- `artifacts/utr_s201_ai_v004/`
- `artifacts/utr_s201_ai_v005/`
- `artifacts/utr_s201_ai_v006/`
- 各ZIP、README、MANIFEST

## 3. ZIP一覧

| No | Version | ZIP path | SHA256 | Release tag | Status | Intended audience | Use / Do not use | Notes |
|---:|---|---|---|---|---|---|---|---|
| 1 | v004 | `artifacts/utr_s201_ai_v004/utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip` | `2103B818045608383FD94F0047B471D4B2E3A3610BC8E46EAA644DF29F738521` | R7-5A相当 | pre-RC候補 / 履歴保持 | 内部関係者 | 現在の外部レビュー候補として案内しない | no-PDF |
| 2 | v005 | `artifacts/utr_s201_ai_v005/utr_s201_ai_v005_full_command_internal_release_no_pdf.zip` | `20F87EE55FC3B555EABE38BB3492CFEB303754E7539DAD8D0BC46BEBD7B29712` | v005 internal pre-release相当 | 内部確認 / 履歴保持 | 内部関係者 | 現在の外部レビュー候補として案内しない | full-command internal release |
| 3 | v006 | `artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip` | `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA` | `utr-s201-ai-v006-r9-7-external-review-candidate.1` | External Review Candidate | 社内確認後の外部レビュー先 | 現在の外部レビュー候補として使う | 正式社外公開版ではない |

## 4. 現在の最新版

現在の外部レビュー候補は v006。

- ZIP: `artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip`
- SHA256: `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA`
- Release: `utr-s201-ai-v006-r9-7-external-review-candidate.1`

## 5. v004 / v005 の扱い

- v004は履歴保持用
- v005は内部確認・履歴保持用
- v004/v005は削除しない
- v004/v005は現在の外部レビュー候補として案内しない
- 必要な場合のみ過去成果物として参照する

## 6. v006 の扱い

- 現在の外部レビュー候補
- no-PDF package
- GitHub pre-release添付済み
- SHA256固定
- 正式社外公開版ではない
- 正式RCではない
- 顧客提供版ではない
- PDF正本の代替ではない
- 海外販売・海外運用向けではない

## 7. HOLD事項

- 正式社外公開は社内承認待ち
- PDF原本との全件再照合
- traceability不足補完
- ライセンス/IP最終確定
- UHF_Read standalone
- 全38コマンド個別実機送信確認
- Level 4以上操作
- Level 5操作
- 海外利用・海外販売
