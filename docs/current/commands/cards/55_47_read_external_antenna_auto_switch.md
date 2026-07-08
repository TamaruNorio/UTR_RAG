# 外部アンテナ自動切替設定の読み取り

## 1. Basic Information
- Command name: 外部アンテナ自動切替設定の読み取り
- Command category: reader_setting_read
- Command identifier: 55/47
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
外部アンテナ自動切替設定の現在値を確認する。
## 3. Operation Summary
読み取り専用。8CH関連は注意して扱う。
## 4. Expected Use Cases
- 外部アンテナ設定を確認したい
## 5. Safety Classification
- Safety class: READ_ONLY
- Operation level: Level 1
- Requires explicit confirmation: 実機接続時は必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 方針提示まで
- Can be used in external review candidate: 可
- Notes: 8CH関連注意
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
- Response fields: 外部アンテナ自動切替設定
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
取得のみ。自動切替設定変更と分離する。
## 9. Real Device Test Status
NOT_TESTED。
## 10. AI Behavior Rules
8CH自動切替を勝手に実装しない。
## 11. Prohibited or Restricted Usage
設定変更、完成Hex生成、送信用コード生成禁止。
## 12. References
- docs/current/06_COMMAND_INDEX.md
## 13. Current Decision
PARTIAL_WITH_NOTES
