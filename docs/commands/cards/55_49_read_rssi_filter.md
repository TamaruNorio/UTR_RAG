# RSSIフィルタ設定の読み取り

## 1. Basic Information
- Command name: RSSIフィルタ設定の読み取り
- Command category: reader_setting_read
- Command identifier: 55/49
- Source catalog: docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
RSSIフィルタ設定を確認する。
## 3. Operation Summary
読み取り専用の設定確認。
## 4. Expected Use Cases
- RSSI条件を確認したい
- 読み取り安定化前に設定を見たい
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
- Response fields: RSSIフィルタ設定
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
取得値をログ化し、RSSIフィルタ書き込みと分離する。
## 9. Real Device Test Status
NOT_TESTED。
## 10. AI Behavior Rules
安定化目的でも変更前に確認質問を行う。
## 11. Prohibited or Restricted Usage
変更はLevel 4で明示確認必須。
## 12. References
- docs/use_cases/R9-1_READING_OPTIMIZATION_POLICY.md
## 13. Current Decision
PARTIAL_WITH_NOTES
