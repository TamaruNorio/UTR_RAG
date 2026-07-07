# 送信出力設定の読み取り

## 1. Basic Information
- Command name: 送信出力設定の読み取り
- Command category: reader_setting_read
- Command identifier: 55/43/01
- Source catalog: docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
現在の送信出力設定を確認する。
## 3. Operation Summary
読み取り専用。送信出力変更ではない。
## 4. Expected Use Cases
- 現在設定を確認したい
- 読み取り条件を記録したい
## 5. Safety Classification
- Safety class: READ_ONLY
- Operation level: Level 1
- Requires explicit confirmation: 実機接続時は必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 方針提示まで
- Can be used in external review candidate: 可
- Notes: R8-8Aで確認
## 6. Device Impact
- 読み取り専用か: はい
- 電波送信を伴うか: いいえ
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: いいえ
- 周波数または送信出力に関係するか: 送信出力の読み取り
- 日本国内仕様から外れる可能性があるか: 低
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: 送信出力関連値
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
取得値をログに残し、変更系コマンドと分離する。
## 9. Real Device Test Status
TESTED_READ_ONLY。
## 10. AI Behavior Rules
読み取りを変更と誤認しない。
## 11. Prohibited or Restricted Usage
送信出力変更を明示確認なしに提案しない。
## 12. References
- docs/real_device/results/R8-8A_REAL_DEVICE_COMMAND_SEND_CHECK_RESULT.md
## 13. Current Decision
READY_FOR_REFERENCE
