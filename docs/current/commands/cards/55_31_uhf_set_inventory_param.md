# UHF_SetInventoryParam

## 1. Basic Information
- Command name: UHF_SetInventoryParam
- Command category: uhf_parameter_write
- Command identifier: 55/31
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
Inventory条件を設定する。必要性、影響、復旧方法の確認が必要。
## 3. Operation Summary
読み取り動作条件を変更するLevel 4操作。完成Hex等は記載しない。
## 4. Expected Use Cases
- 読み取りを安定化したい
- 複数タグ条件を調整したい
## 5. Safety Classification
- Safety class: DEVICE_SETTING_RESTRICTED
- Operation level: Level 4
- Requires explicit confirmation: 必須
- Requires recovery procedure: 必須
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: 文書参照のみ
- Notes: 自動送信禁止
## 6. Device Impact
- 読み取り専用か: いいえ
- 電波送信を伴うか: 実施条件による
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: はい
- FLASHまたは永続設定に関係するか: 保存時は要確認
- 周波数または送信出力に関係するか: 間接影響あり
- 日本国内仕様から外れる可能性があるか: 要確認
## 7. Parameters and Response Structure
- Request fields: Inventory Param。詳細は要仕様確認
- Response fields: ACK/NACK等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合
## 8. Implementation Guidance
全言語で自動実行禁止。承認、復旧、ログ、変更前値の記録を必須にする。
## 9. Real Device Test Status
PROHIBITED。R8-8Aでは送信していない。
## 10. AI Behavior Rules
AIが勝手に実装しない。Level 4として明示確認を求める。
## 11. Prohibited or Restricted Usage
UHF_SetInventoryParam自動送信禁止。完成Hex、SUM計算済みコマンド、送信用コード生成禁止。
## 12. References
- docs/current/06_COMMAND_INDEX.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
## 13. Current Decision
PROHIBITED_DOCUMENT_ONLY
