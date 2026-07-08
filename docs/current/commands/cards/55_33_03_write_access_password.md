# Accessパスワードの書き込み

## 1. Basic Information
- Command name: Accessパスワードの書き込み
- Command category: reader_setting_write
- Command identifier: 55/33/03
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
Accessパスワード関連設定を書き込む。認証条件に影響する。
## 3. Operation Summary
制限付き書き込み操作。完成Hex等は記載しない。
## 4. Expected Use Cases
- 認証条件を扱う必要がある
## 5. Safety Classification
- Safety class: TAG_MEMORY_WRITE_RESTRICTED
- Operation level: Level 4
- Requires explicit confirmation: 必須
- Requires recovery procedure: 必須
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: 文書参照のみ
- Notes: 認証条件に影響
## 6. Device Impact
- 読み取り専用か: いいえ
- 電波送信を伴うか: 条件による
- タグメモリ変更を伴うか: 要確認
- リーダ設定変更を伴うか: はい
- FLASHまたは永続設定に関係するか: 要確認
- 周波数または送信出力に関係するか: いいえ
- 日本国内仕様から外れる可能性があるか: 要確認
## 7. Parameters and Response Structure
- Request fields: パスワード関連。要仕様確認
- Response fields: ACK/NACK等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
認証情報をログに残さない。承認と復旧手順がない場合HOLD。
## 9. Real Device Test Status
PROHIBITED。
## 10. AI Behavior Rules
AIが勝手に実装しない。
## 11. Prohibited or Restricted Usage
認証情報露出、完成Hex生成、実機送信用コード生成禁止。
## 12. References
- docs/current/03_AI_USAGE_GUIDE.md
## 13. Current Decision
PROHIBITED_DOCUMENT_ONLY
