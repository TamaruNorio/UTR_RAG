# FLASH設定値の読み取り

## 1. Basic Information
- Command name: FLASH設定値の読み取り
- Command category: reader_setting_read
- Command identifier: 4F/B4
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
FLASHに保存された設定値を読み取る。
## 3. Operation Summary
読み取り専用。FLASH書き込みではない。
## 4. Expected Use Cases
- 永続設定の現在値を確認したい
## 5. Safety Classification
- Safety class: READ_ONLY
- Operation level: Level 1
- Requires explicit confirmation: 実機接続時は必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 方針提示まで
- Can be used in external review candidate: 可
- Notes: FLASH書き込みと分離
## 6. Device Impact
- 読み取り専用か: はい
- 電波送信を伴うか: いいえ
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: 読み取りのみ
- 周波数または送信出力に関係するか: 設定内容による
- 日本国内仕様から外れる可能性があるか: 低
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: FLASH設定値
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
読み取り結果はログ化し、書き込みや初期化へ自動連携しない。
## 9. Real Device Test Status
NOT_TESTED。
## 10. AI Behavior Rules
FLASH読み取りとFLASH書き込みを混同しない。
## 11. Prohibited or Restricted Usage
FLASH書き込みはLevel 5。
## 12. References
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
## 13. Current Decision
PARTIAL_WITH_NOTES
