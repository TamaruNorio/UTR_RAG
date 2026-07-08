# UTR-S201 AI Assistant Package v006 External Review Candidate

## 1. 位置づけ

- 社外レビュー候補
- 日本国内向け
- 日本語利用者向け
- 日本の電波法準拠機器向け
- no-PDF package
- 正式社外公開版ではない
- 正式RCではない
- 顧客提供版ではない
- 本番利用保証版ではない
- PDF正本の代替ではない
- 海外販売・海外運用向けではない

## 2. 目的

UTR-S201シリーズの通信仕様、安全条件、実機確認結果、自然言語からの要件確認、多言語実装支援、複数生成AI対応、構造化コマンドカードを、生成AIが参照しやすい形で整理する。

## 3. 主な追加内容

- R9-0 国内スコープ・社外向け範囲・サポート境界
- R9-1 要件確認・読み取り最適化
- R9-2 多言語・複数LLM対応
- R9-3 構造化コマンドカード
- R9-4 AI-ready外部レビュー検証

## 4. 対象生成AI

- ChatGPT
- Codex
- Gemini
- Claude
- Copilot
- Cursor
- 社内AI

## 5. 対象言語

- Python
- C#
- C++
- JavaScript / Node.js
- PowerShell

## 6. 安全上の注意

- 完成Hexは含めない
- SUM計算済みコマンドは含めない
- 実機送信用コードは含めない
- PDF原本は含めない
- Level 4以上は明示確認が必要
- Level 5は明示承認と復旧手順がなければHOLD
- 海外利用・海外販売は対象外
- UHF_Read standalone はHOLD
- 全38コマンドの個別実機送信確認は未完了

## 7. HOLD事項

- 正式社外公開は社内承認待ち
- PDF原本との全件再照合
- traceability不足項目の補完
- ライセンス/IP方針の最終確定
- UHF_Read standalone
- 全38コマンドの個別実機送信確認
- Level 4以上の実機操作
- Level 5操作
- 海外利用・海外販売

## 8. まず見る文書

- README.md
- docs/release/R9-4_EXTERNAL_REVIEW_DECISION.md
- docs/ai_ready/R9-4_AI_RETRIEVAL_VALIDATION_CHECKLIST.md
- docs/use_cases/R9-1_CLARIFYING_QUESTION_TEMPLATES.md
- docs/implementation/R9-2_EXTERNAL_DEVELOPER_WORKFLOW.md
- docs/commands/cards/AI_RETRIEVAL_INDEX.md
