# 周波数設定の書き込み

## 1. Basic Information
- Command name: 周波数設定の書き込み
- Command category: reader_setting_write
- Command identifier: 55/33/02
- Source catalog: docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
周波数設定を変更する。国内仕様確認が必須。
## 3. Operation Summary
RF条件変更を伴うLevel 4操作。
## 4. Expected Use Cases
- 周波数を扱う必要がある
## 5. Safety Classification
- Safety class: RF_PARAM_CHANGE_RESTRICTED
- Operation level: Level 4
- Requires explicit confirmation: 必須
- Requires recovery procedure: 必須
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: 文書参照のみ
- Notes: 周波数変更
## 6. Device Impact
- 読み取り専用か: いいえ
- 電波送信を伴うか: 条件による
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: はい
- FLASHまたは永続設定に関係するか: 保存時は要確認
- 周波数または送信出力に関係するか: 周波数
- 日本国内仕様から外れる可能性があるか: 高
## 7. Parameters and Response Structure
- Request fields: 周波数設定値。要仕様確認
- Response fields: ACK/NACK等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
日本国内仕様、承認、復旧、ログがない場合HOLD。
## 9. Real Device Test Status
PROHIBITED。
## 10. AI Behavior Rules
海外用途や地域不明ならHOLD。
## 11. Prohibited or Restricted Usage
明示確認なしの周波数変更、完成Hex生成は禁止。
## 12. References
- docs/policy/R9-0_JAPAN_DOMESTIC_SCOPE_POLICY.md
## 13. Current Decision
PROHIBITED_DOCUMENT_ONLY
