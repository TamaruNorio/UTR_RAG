# UHF_GetSelectParam

## 1. Basic Information
- Command name: UHF_GetSelectParam
- Command category: uhf_parameter_read
- Command identifier: 55/40
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
Select条件の現在値を読み取る。
## 3. Operation Summary
読み取り専用の設定取得。完成Hex等は記載しない。
## 4. Expected Use Cases
- Select条件を確認したい
- 読み取り条件を確認したい
## 5. Safety Classification
- Safety class: READ_ONLY
- Operation level: Level 1
- Requires explicit confirmation: 実機接続時は必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 方針提示まで
- Can be used in external review candidate: 可
- Notes: 未実機確認
## 6. Device Impact
- 読み取り専用か: はい
- 電波送信を伴うか: いいえ
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: いいえ
- 周波数または送信出力に関係するか: いいえ
- 日本国内仕様から外れる可能性があるか: 低
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: Select Param
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合
## 8. Implementation Guidance
取得専用として扱い、Set系へ自動連携しない。
## 9. Real Device Test Status
NOT_TESTED。
## 10. AI Behavior Rules
設定変更を提案する場合はLevel 4扱いとして確認する。
## 11. Prohibited or Restricted Usage
完成Hex、SUM計算済みコマンド、実機送信用コード生成禁止。
## 12. References
- docs/current/06_COMMAND_INDEX.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
## 13. Current Decision
PARTIAL_WITH_NOTES
