# 周波数設定の読み取り

## 1. Basic Information
- Command name: 周波数設定の読み取り
- Command category: reader_setting_read
- Command identifier: 55/43/02
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
現在の周波数チャンネル設定を確認する。
## 3. Operation Summary
読み取り専用。周波数変更ではない。
## 4. Expected Use Cases
- 現在設定を確認したい
- 国内仕様範囲を確認したい
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
- 周波数または送信出力に関係するか: 周波数の読み取り
- 日本国内仕様から外れる可能性があるか: 低
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: 周波数チャンネル情報
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
取得値をログ化し、周波数書き込みと分離する。
## 9. Real Device Test Status
TESTED_READ_ONLY。
## 10. AI Behavior Rules
周波数変更を勝手に提案しない。
## 11. Prohibited or Restricted Usage
周波数変更はLevel 4で明示確認必須。
## 12. References
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
## 13. Current Decision
READY_FOR_REFERENCE
