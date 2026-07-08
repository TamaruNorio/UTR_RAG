# R8-2 Release Decision Table

この表は、R7-5A成果物を社内pre-RCまたはRC候補として判断するための確認表です。

判定は `PASS`、`HOLD`、`TODO`、`N/A` のいずれかで記録します。実機確認が必要な項目は初期状態では `TODO` とします。

| No | 確認項目 | 判定 | 必須度 | 確認方法 | 結果 | 備考 |
|---:|---|---|---|---|---|---|
| 1 | GitHub mainに成果物ZIPが存在する | PASS | 必須 | GitHub mainの成果物パス確認 | main登録済み | `artifacts/utr_s201_ai_v004/utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip` |
| 2 | ZIP SHA256が一致する | PASS | 必須 | `Get-FileHash` またはGitHub記載値確認 | 一致 | `2103B818045608383FD94F0047B471D4B2E3A3610BC8E46EAA644DF29F738521` |
| 3 | README.mdから成果物とR8-1チェックリストを参照できる | PASS | 必須 | README.md確認 | 参照あり | R8-2/R8-3参照は本変更で追加 |
| 4 | docs/OPERATIONS.mdが存在する | PASS | 必須 | ファイル存在確認 | 存在 | 運用ルールあり |
| 5 | R8-1チェックリストが存在する | PASS | 必須 | ファイル存在確認 | 存在 | `docs/R8-1_PRE_RC_INTERNAL_SHARE_CHECKLIST.md` |
| 6 | PDFがGitHubに含まれていない | PASS | 必須 | 追加差分確認 | 追加なし | R8-2ではPDFを追加しない |
| 7 | 完成Hexが生成されていない | PASS | 必須 | 追加差分確認 | 生成なし | 生成禁止 |
| 8 | SUM計算済みコマンドが生成されていない | PASS | 必須 | 追加差分確認 | 生成なし | 生成禁止 |
| 9 | 実機送信用コードが生成されていない | PASS | 必須 | 追加差分確認 | 生成なし | 生成禁止 |
| 10 | 55h/14h = UHF_InventoryRead が維持されている | PASS | 必須 | 既存資料の対応関係確認 | 維持 | 本変更ではRAG本文を修正しない |
| 11 | 55h/15h = UHF_Read が維持されている | PASS | 必須 | 既存資料の対応関係確認 | 維持 | 本変更ではRAG本文を修正しない |
| 12 | rag/commands/55_14_uhf_read.md が存在しない | PASS | 必須 | ファイル存在確認 | 存在しない前提 | 誤命名防止 |
| 13 | 実機接続確認が完了している | PASS | 必須 | R8-3実機確認 | COM6 / 115200bpsでopen成功 | 送信なし、DTR/RTS無効 |
| 14 | 実機切断確認が完了している | PASS | 必須 | R8-3実機確認 | close成功、再接続後の再close成功 | 送信なし |
| 15 | 読み取り系確認が完了している | PASS | 必須 | R8-8A実機確認 | Inventoryに伴うタグ読み取り応答を確認 | `UHF_Read` 単体確認は未実施のためHOLD事項として継続 |
| 16 | Inventory系確認が完了している | PASS | 必須 | R8-8A実機確認 | Inventory 1回実行、タグ応答1件 | タグ固有IDは記録しない |
| 17 | タイムアウト時の挙動が確認されている | PASS | 必須 | R8-3C実機確認 | 送信なしの1秒ReadTimeoutを再確認 | タグ読み取りコマンドは送信していない |
| 18 | エラー時のログ確認ができる | PASS | 必須 | R8-3C実機確認 | open/close/reopen/timeoutログを結果本文に記録 | 外部ログファイルは保存していない |
| 19 | FLASH書き込みを行っていない | PASS | 必須 | 実施手順と差分確認 | 実施なし | 実施可能な手順として書かない |
| 20 | 周波数変更を行っていない | PASS | 必須 | 実施手順と差分確認 | 実施なし | 実施可能な手順として書かない |
| 21 | 送信出力変更を行っていない | PASS | 必須 | 実施手順と差分確認 | 実施なし | 実施可能な手順として書かない |
| 22 | UHF_SetInventoryParam自動送信を行っていない | PASS | 必須 | 実施手順と差分確認 | 実施なし | 自動送信しない |
| 23 | 8CHアンテナ自動切替を行っていない | PASS | 必須 | 実施手順と差分確認 | 実施なし | 実施可能な手順として書かない |
| 24 | 実機確認結果が記録されている | PASS | 必須 | R8-8A記録フォーマット確認 | 記録済み | `docs/real_device/results/R8-8A_REAL_DEVICE_COMMAND_SEND_CHECK_RESULT.md` にPASS_WITH_NOTES結果を記録 |
| 25 | ステータス取得系確認が完了している | PASS | 必須 | R8-8A実機確認 | ROM、送信出力、周波数チャンネル、Inventory Paramを取得 | 設定変更なし |
| 26 | 社内pre-RCリリース判断 | PASS | 必須 | R8-4レビュー | 共有可 | HOLD事項付きで社内pre-RCとして共有可能 |
| 27 | 正式RC判断 | HOLD | 必須 | R8-8A実機確認 | 不可 | `UHF_Read` 単体確認、アンテナ物理構成、実施場所、全コマンド網羅確認が未完了 |
| 28 | RC候補判断 | HOLD | 必須 | R8-8A実機確認 | HOLD | `UHF_Read` 単体確認、アンテナ物理構成、実施場所が未確認 |
| 29 | 全コマンド棚卸しが実施されている | PASS | 必須 | R8-7レビュー | 実施済み | command_safety_matrix基準で38件を抽出 |
| 30 | コマンド安全分類の不足が一覧化されている | PASS | 必須 | R8-7レビュー | 一覧化済み | safety matrix上は不足0、実行候補化はしない |
| 31 | コマンド根拠参照の不足が一覧化されている | PASS | 必須 | R8-7レビュー | 一覧化済み | traceability不足5件 |
| 32 | 全コマンド網羅確認は未完了またはHOLDである | HOLD | 必須 | R8-7レビュー | HOLD | PDF原本照合と不足補完が未完了 |
| 33 | 実機へのコマンド送信確認が完了している | PASS | 必須 | R8-8A実機確認 | 既存サンプルでステータス取得とInventoryを実施 | `UHF_Read` 単体確認は未実施のためHOLD事項として継続 |
| 34 | v005 full-command no-PDF package が作成されている | PASS | 必須 | R8-9成果物確認 | 作成済み | `artifacts/utr_s201_ai_v005/utr_s201_ai_v005_full_command_internal_release_no_pdf.zip` |
| 35 | v005 MANIFEST が作成されている | PASS | 必須 | R8-9成果物確認 | 作成済み | `artifacts/utr_s201_ai_v005/MANIFEST.md` |
| 36 | v005 SHA256 が記録されている | PASS | 必須 | R8-9成果物確認 | 記録済み | `20F87EE55FC3B555EABE38BB3492CFEB303754E7539DAD8D0BC46BEBD7B29712` |
| 37 | UHF_Read standalone は HOLD | HOLD | 必須 | R8-8A実機確認 | 未実施 | 既存入口に含まれないため単体確認は未実施 |
| 38 | v005 package validation が実施されている | PASS | 必須 | R8-10成果物検証 | 検証済み | `docs/release/R8-10_V005_PACKAGE_VALIDATION.md` |
| 39 | v005 ZIP SHA256 が一致している | PASS | 必須 | R8-10成果物検証 | 一致 | `20F87EE55FC3B555EABE38BB3492CFEB303754E7539DAD8D0BC46BEBD7B29712` |
| 40 | v005 ZIP が no-PDF である | PASS | 必須 | R8-10成果物検証 | PDFなし | 展開先でPDF混入なしを確認 |
| 41 | v005 ZIP にR7-5A ZIPが二重梱包されていない | PASS | 必須 | R8-10成果物検証 | 二重梱包なし | 展開先でZIP混入なしを確認 |
| 42 | 日本国内向けスコープ方針が作成されている | PASS | 必須 | R9-0文書確認 | 作成済み | `docs/policy/R9-0_JAPAN_DOMESTIC_SCOPE_POLICY.md` |
| 43 | 社外向けスコープ方針が作成されている | PASS | 必須 | R9-0文書確認 | 作成済み | `docs/policy/R9-0_EXTERNAL_RELEASE_SCOPE_POLICY.md` |
| 44 | サポート範囲方針が作成されている | PASS | 必須 | R9-0文書確認 | 作成済み | `docs/policy/R9-0_SUPPORT_BOUNDARY_POLICY.md` |
| 45 | ライセンス/IPチェックリストが作成されている | PASS | 必須 | R9-0文書確認 | 作成済み | `docs/policy/R9-0_LICENSE_AND_IP_CHECKLIST.md` |
| 46 | AI-ready品質基準が作成されている | PASS | 必須 | R9-0文書確認 | 作成済み | `docs/ai_ready/R9-0_AI_READY_QUALITY_CRITERIA.md` |
| 47 | 外部レビュー候補GAPリストが作成されている | PASS | 必須 | R9-0文書確認 | 作成済み | `docs/release/R9-0_EXTERNAL_REVIEW_CANDIDATE_GAP_LIST.md` |
| 48 | 正式社外公開判断 | HOLD | 必須 | 社内承認 | 未承認 | v006候補準備段階であり、正式公開ではない |
| 49 | 要件確認ガイドが作成されている | PASS | 必須 | R9-1文書確認 | 作成済み | `docs/use_cases/R9-1_REQUIREMENT_CLARIFICATION_GUIDE.md` |
| 50 | 読み取り最適化ポリシーが作成されている | PASS | 必須 | R9-1文書確認 | 作成済み | `docs/use_cases/R9-1_READING_OPTIMIZATION_POLICY.md` |
| 51 | 操作レベルと承認条件が定義されている | PASS | 必須 | R9-1文書確認 | 作成済み | `docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md` |
| 52 | 読み取りユースケースマトリクスが作成されている | PASS | 必須 | R9-1文書確認 | 作成済み | `docs/use_cases/R9-1_READING_USE_CASE_MATRIX.md` |
| 53 | 確認質問テンプレートが作成されている | PASS | 必須 | R9-1文書確認 | 作成済み | `docs/use_cases/R9-1_CLARIFYING_QUESTION_TEMPLATES.md` |
| 54 | リリース判断者が確認している | TODO | 必須 | 判断者レビュー | 未実施 | R9-2以降で判断 |
| 55 | structured command cards が作成されている | PASS | 必須 | R9-3文書確認 | 38件作成 | `docs/commands/cards/README.md` |
| 56 | safety index が作成されている | PASS | 必須 | R9-3文書確認 | 作成済み | `docs/commands/cards/SAFETY_INDEX.md` |
| 57 | test status index が作成されている | PASS | 必須 | R9-3文書確認 | 作成済み | `docs/commands/cards/TEST_STATUS_INDEX.md` |
| 58 | operation level index が作成されている | PASS | 必須 | R9-3文書確認 | 作成済み | `docs/commands/cards/OPERATION_LEVEL_INDEX.md` |
| 59 | AI retrieval index が作成されている | PASS | 必須 | R9-3文書確認 | 作成済み | `docs/commands/cards/AI_RETRIEVAL_INDEX.md` |
| 60 | PDF原本との全件再照合が完了している | HOLD | 必須 | R9-3文書確認 | 未完了 | R8-7抽出結果を根拠に整理。PDF正本との全件再照合は次工程以降 |
| 61 | 正式な社外公開判断 | HOLD | 必須 | 社内承認 | 未承認 | R9-3はAI-ready構造化段階であり正式社外公開版ではない |
| 62 | AI-ready external review validation が実施されている | PASS | 必須 | R9-4文書確認 | 実施済み | `docs/release/R9-4_AI_READY_EXTERNAL_REVIEW_VALIDATION.md` |
| 63 | External review decision が作成されている | PASS | 必須 | R9-4文書確認 | 作成済み | `docs/release/R9-4_EXTERNAL_REVIEW_DECISION.md` |
| 64 | Remaining HOLD items が整理されている | PASS | 必須 | R9-4文書確認 | 整理済み | `docs/release/R9-4_REMAINING_HOLD_ITEMS.md` |
| 65 | AI retrieval validation checklist が作成されている | PASS | 必須 | R9-4文書確認 | 作成済み | `docs/ai_ready/R9-4_AI_RETRIEVAL_VALIDATION_CHECKLIST.md` |
| 66 | v006 package作成へ進める | PASS | 必須 | R9-4判断 | 進行可 | HOLD事項付きでR9-5 package作成へ進める |
| 67 | 正式社外公開判断はHOLD | HOLD | 必須 | 社内承認 | 未承認 | R9-4時点では正式社外公開ではない |
| 68 | v006 External Review Candidate package が作成されている | PASS | 必須 | R9-5成果物確認 | 作成済み | `artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip` |
| 69 | v006 README が作成されている | PASS | 必須 | R9-5成果物確認 | 作成済み | `artifacts/utr_s201_ai_v006/README.md` |
| 70 | v006 MANIFEST が作成されている | PASS | 必須 | R9-5成果物確認 | 作成済み | `artifacts/utr_s201_ai_v006/MANIFEST.md` |
| 71 | v006 ZIP SHA256 が記録されている | PASS | 必須 | R9-5成果物確認 | 記録済み | `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA` |
| 72 | v006 ZIP が no-PDF である | PASS | 必須 | R9-5 ZIP確認 | PDFなし | no-PDF packageとして作成 |
| 73 | v006 ZIP に既存ZIPが二重梱包されていない | PASS | 必須 | R9-5 ZIP確認 | 二重梱包なし | R7-5A/v005/v006 ZIP自身を含めない |
| 74 | 正式社外公開判断はHOLD | HOLD | 必須 | 社内承認 | 未承認 | v006はExternal Review Candidateであり正式社外公開版ではない |
| 75 | v006 package validation が実施されている | PASS | 必須 | R9-6検証 | 実施済み | `docs/release/R9-6_V006_PACKAGE_VALIDATION.md` |
| 76 | v006 ZIP SHA256 が一致している | PASS | 必須 | R9-6検証 | 一致 | `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA` |
| 77 | v006 ZIP が no-PDF である | PASS | 必須 | R9-6検証 | PDFなし | 展開先でPDFなしを確認 |
| 78 | v006 ZIP に既存ZIPが二重梱包されていない | PASS | 必須 | R9-6検証 | 二重梱包なし | 既存ZIPおよびv006 ZIP自身なし |
| 79 | v006 Release readiness decision が作成されている | PASS | 必須 | R9-6判断 | 作成済み | `docs/release/R9-6_V006_RELEASE_READINESS_DECISION.md` |
| 80 | R9-7 pre-releaseへ進める | PASS | 必須 | R9-6判断 | 進行可 | HOLD事項付きでGitHub pre-releaseへ進める |
| 81 | 正式社外公開判断はHOLD | HOLD | 必須 | 社内承認 | 未承認 | R9-6時点では正式社外公開ではない |
| 82 | 社内共有文面が作成されている | PASS | 必須 | R9-8文書確認 | 作成済み | `docs/release/R9-8_INTERNAL_SHARE_MESSAGE.md` |
| 83 | 外部レビュー依頼文面が作成されている | PASS | 必須 | R9-9文書確認 | 作成済み | `docs/release/R9-9_EXTERNAL_REVIEW_REQUEST_MESSAGE.md` |
| 84 | 外部共有は社内判断後である | HOLD | 必須 | 社内承認 | 判断待ち | 共有範囲、レビュー先、期限は社内確認後に決定 |
| 85 | 正式社外公開判断はHOLD | HOLD | 必須 | 社内承認 | 未承認 | R9-8/R9-9時点では正式社外公開ではない |
| 86 | artifact inventory が作成されている | PASS | 必須 | R9-10文書確認 | 作成済み | `docs/release/R9-10_ARTIFACT_AND_ZIP_INVENTORY.md` |
| 87 | ZIP handling policy が作成されている | PASS | 必須 | R9-10文書確認 | 作成済み | `docs/release/R9-10_ZIP_HANDLING_POLICY.md` |
| 88 | post-release document status が整理されている | PASS | 必須 | R9-10文書確認 | 整理済み | `docs/release/R9-10_POST_RELEASE_DOCUMENT_STATUS.md` |
| 89 | 現在の外部レビュー候補ZIPはv006である | PASS | 必須 | R9-10文書確認 | v006 | `artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip` |
| 90 | Release済みZIPは変更しない | PASS | 必須 | R9-10方針確認 | 方針化済み | v004/v005/v006 ZIPは削除・上書き・再作成しない |
| 91 | R9-8/R9-9はv006 ZIP未収録で問題ない | PASS | 必須 | R9-10文書確認 | 問題なし | Release後文書として扱い、必要なら別途参照する |
| 92 | 正式社外公開判断はHOLD | HOLD | 必須 | 社内承認 | 未承認 | R9-10時点では正式社外公開ではない |
