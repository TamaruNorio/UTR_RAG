# UHF_SetSelectParam

## 1. Basic Information
- Command name: UHF_SetSelectParam
- Command category: uhf_parameter_write
- Command identifier: 55/30
- Source catalog: docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
Select条件を設定する。要件と影響の確認が必要。
## 3. Operation Summary
リーダの読み取り条件を変更するLevel 4操作。
## 4. Expected Use Cases
- 特定タグだけを読みたい
- Select条件を調整したい
## 5. Safety Classification
- Safety class: DEVICE_SETTING_RESTRICTED
- Operation level: Level 4
- Requires explicit confirmation: 必須
- Requires recovery procedure: 必須
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: 文書参照のみ
- Notes: Select条件変更
## 6. Device Impact
- 読み取り専用か: いいえ
- 電波送信を伴うか: 条件による
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: はい
- FLASHまたは永続設定に関係するか: 保存時は要確認
- 周波数または送信出力に関係するか: 直接ではない
- 日本国内仕様から外れる可能性があるか: 要確認
## 7. Parameters and Response Structure
- Request fields: Select Param。要仕様確認
- Response fields: ACK/NACK等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合
## 8. Implementation Guidance
設定前後ログと復旧方針を必須にする。実コードは対象実装リポジトリで扱う。
## 9. Real Device Test Status
PROHIBITED。
## 10. AI Behavior Rules
明示確認なしに実装しない。
## 11. Prohibited or Restricted Usage
自動送信、完成Hex、SUM計算済みコマンド生成禁止。
## 12. References
- docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- docs/ai_ready/R9-2_LLM_BEHAVIOR_RULES.md
## 13. Current Decision
PROHIBITED_DOCUMENT_ONLY
