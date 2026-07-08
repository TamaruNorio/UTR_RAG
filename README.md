# UTR_RAG

## 目的

このリポジトリは、タカヤ製 UTR-S201 シリーズに関する、仕様・安全ルール・根拠資料・RAGパッケージ成果物を管理するための保管庫です。

このリポジトリは、実機制御プログラム本体ではありません。

## 現在の収録物

- UTR-S201 AI補助パッケージ v004
- R7-5A front matter notes cleanup
- no-PDF package
- pre-RC候補
- R8-8A 実機コマンド送信確認 PASS_WITH_NOTES
- 正式RCではない
- R8-1 pre-RC 社内共有用チェックリスト
- R8-2 リリース準備文書
- R8-3 実機確認計画
- v005 full-command internal release no-PDF package
- v006 External Review Candidate preparation

## 成果物

現在の成果物は以下です。

```text
artifacts/utr_s201_ai_v004/utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip
```

SHA256:

```text
2103B818045608383FD94F0047B471D4B2E3A3610BC8E46EAA644DF29F738521
```

## チェックリスト

R8-1 pre-RC 社内共有用チェックリスト:

```text
docs/R8-1_PRE_RC_INTERNAL_SHARE_CHECKLIST.md
```

R8-2 / R8-3 リリース準備文書:

```text
docs/release/R8-2_RELEASE_READINESS_PLAN.md
docs/release/R8-2_RELEASE_DECISION_TABLE.md
docs/real_device/R8-3_REAL_DEVICE_TEST_PLAN.md
docs/real_device/results/R8-3_REAL_DEVICE_TEST_RESULT.md
docs/real_device/R8-3B_SAFE_COMMAND_SELECTION.md
docs/real_device/results/R8-3C_SAFE_REAL_DEVICE_CHECK_RESULT.md
docs/release/R8-4_INTERNAL_PRE_RC_RELEASE_DECISION.md
docs/commands/R8-7_COMMAND_COVERAGE_AUDIT.md
docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
docs/commands/R8-7_COMMAND_GAP_LIST.md
docs/real_device/results/R8-8A_REAL_DEVICE_COMMAND_SEND_CHECK_RESULT.md
docs/release/R8-10_V005_PACKAGE_VALIDATION.md
artifacts/utr_s201_ai_v005/README.md
artifacts/utr_s201_ai_v005/MANIFEST.md
artifacts/utr_s201_ai_v005/utr_s201_ai_v005_full_command_internal_release_no_pdf.zip
docs/policy/R9-0_JAPAN_DOMESTIC_SCOPE_POLICY.md
docs/policy/R9-0_EXTERNAL_RELEASE_SCOPE_POLICY.md
docs/policy/R9-0_SUPPORT_BOUNDARY_POLICY.md
docs/policy/R9-0_LICENSE_AND_IP_CHECKLIST.md
docs/ai_ready/R9-0_AI_READY_QUALITY_CRITERIA.md
docs/release/R9-0_EXTERNAL_REVIEW_CANDIDATE_GAP_LIST.md
docs/use_cases/R9-1_REQUIREMENT_CLARIFICATION_GUIDE.md
docs/use_cases/R9-1_READING_OPTIMIZATION_POLICY.md
docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md
docs/use_cases/R9-1_READING_USE_CASE_MATRIX.md
docs/use_cases/R9-1_CLARIFYING_QUESTION_TEMPLATES.md
docs/commands/cards/README.md
docs/commands/cards/SAFETY_INDEX.md
docs/commands/cards/TEST_STATUS_INDEX.md
docs/commands/cards/OPERATION_LEVEL_INDEX.md
docs/commands/cards/AI_RETRIEVAL_INDEX.md
docs/release/R9-4_AI_READY_EXTERNAL_REVIEW_VALIDATION.md
docs/release/R9-4_EXTERNAL_REVIEW_DECISION.md
docs/release/R9-4_REMAINING_HOLD_ITEMS.md
docs/ai_ready/R9-4_AI_RETRIEVAL_VALIDATION_CHECKLIST.md
artifacts/utr_s201_ai_v006/README.md
artifacts/utr_s201_ai_v006/MANIFEST.md
artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip
docs/release/R9-6_V006_PACKAGE_VALIDATION.md
docs/release/R9-6_V006_RELEASE_READINESS_DECISION.md
```

v005 full-command internal release:

- no-PDF
- 正式RCではありません
- 顧客提供版ではありません
- 本番利用可能版ではありません
- UHF_Read standalone remains HOLD

v006では社外向けリリース候補を目指します。ただし、現時点では正式公開版ではありません。

- 日本国内向け
- 日本語利用者向け
- 日本の電波法準拠機器向け
- 海外販売・海外運用向けではありません
- PDF正本の代替ではありません

R9-1では、自然言語の依頼に対する確認質問と読み取り最適化方針を追加しました。

- 危険操作を一律禁止するのではなく、必要性、影響、復旧方法、承認条件に基づいて扱います
- 日本国内仕様の範囲を前提とします
- 海外利用・海外販売は対象外です
- Level 4以上はAIが勝手に実装しません

R9-3では、R8-7で抽出した38コマンドを1コマンド/1カード形式で整理し、AI検索用インデックス、安全分類インデックス、実機確認状況インデックス、操作レベル別インデックスを追加しました。

- R8-7抽出結果を根拠にした構造化カードです
- PDF原本との全件再照合は未完了です
- 日本国内向け、日本の電波法準拠機器向けの整理です
- 海外利用・海外販売は対象外です
- 完成Hex、SUM計算済みコマンド、実機送信用コードは含めません
- 正式な社外公開版ではありません

R9-4では、v006 External Review Candidate package作成前のAI-ready検証を実施し、package作成へ進めるかを判断しました。

- 正式社外公開ではありません
- PDF正本の代替ではありません
- 日本国内仕様前提です
- 海外利用・海外販売は対象外です
- HOLD事項は残ります

R9-5では、v006 External Review Candidate package を作成しました。

- no-PDF package
- 正式社外公開版ではありません
- 正式RCではありません
- 顧客提供版ではありません
- PDF正本の代替ではありません
- 日本国内仕様前提です
- 海外利用・海外販売は対象外です
- HOLD事項があります

R9-6では、v006 package validation を実施し、R9-7 GitHub pre-releaseへ進めるかを判断しました。

- 正式社外公開ではありません
- HOLD事項があります

## 安全上の注意

- 本リポジトリの内容は、全項目が実機確認済みではありません
- 正式RCではありません
- 完成Hex、SUM計算済みコマンド、実機送信用コードの生成を目的としません
- PDF原本は同梱しません
- 実機制御、永続設定変更、送信出力変更、周波数変更、FLASH書き込みは別途明示許可と実機確認が必要です

## 運用方針

- mainブランチを直接変更しない
- 作業ごとに feature ブランチを作成する
- 変更前に git status を確認する
- 変更後に git diff / git diff --check を確認する
- push前に内容をレビューする
- 実機確認が必要な内容は、机上確認だけで完了扱いにしない

## 将来構想

- コマンド仕様の構造化
- safety matrix / source traceability matrix の拡張
- 将来的な UTR Gateway / OpenAPI draft の検討
- ただし現時点では API実装リポジトリではない
