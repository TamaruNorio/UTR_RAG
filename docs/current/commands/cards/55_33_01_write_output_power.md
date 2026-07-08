# 送信出力設定の書き込み

## 1. Basic Information
- Command name: 送信出力設定の書き込み
- Command category: reader_setting_write
- Command identifier: 55/33/01
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
送信出力設定を変更する。日本国内仕様、承認、復旧が必要。
## 3. Operation Summary
RF条件変更を伴うLevel 4操作。
## 4. Expected Use Cases
- 読み取り距離を調整したい
## 5. Safety Classification
- Safety class: RF_PARAM_CHANGE_RESTRICTED
- Operation level: Level 4
- Requires explicit confirmation: 必須
- Requires recovery procedure: 必須
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: 文書参照のみ
- Notes: 送信出力変更
## 6. Device Impact
- 読み取り専用か: いいえ
- 電波送信を伴うか: 条件による
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: はい
- FLASHまたは永続設定に関係するか: 保存時は要確認
- 周波数または送信出力に関係するか: 送信出力
- 日本国内仕様から外れる可能性があるか: 要確認
## 7. Parameters and Response Structure
- Request fields: 出力設定値。要仕様確認
- Response fields: ACK/NACK等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
承認、復旧、変更前値、ログ保存を必須とする。
## 9. Real Device Test Status
PROHIBITED。
## 10. AI Behavior Rules
明示確認なしに実装しない。
## 11. Prohibited or Restricted Usage
国内仕様不明、復旧手順なし、完成Hex生成は禁止。
## 12. References
- docs/current/04_REQUIREMENT_CLARIFICATION.md
## 13. Current Decision
PROHIBITED_DOCUMENT_ONLY
