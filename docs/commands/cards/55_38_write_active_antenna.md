# 使用アンテナ番号の書き込み

## 1. Basic Information
- Command name: 使用アンテナ番号の書き込み
- Command category: antenna_setting_write
- Command identifier: 55/38
- Source catalog: docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: なし
- PDF reference: なし。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: MISSING_TRACEABILITY
## 2. Purpose
使用アンテナ番号を変更する。要承認。
## 3. Operation Summary
リーダ設定変更を伴うLevel 4操作。
## 4. Expected Use Cases
- 特定アンテナで読みたい
## 5. Safety Classification
- Safety class: DEVICE_SETTING_RESTRICTED
- Operation level: Level 4
- Requires explicit confirmation: 必須
- Requires recovery procedure: 必須
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: 文書参照のみ
- Notes: trace item不足
## 6. Device Impact
- 読み取り専用か: いいえ
- 電波送信を伴うか: 条件による
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: はい
- FLASHまたは永続設定に関係するか: 保存時は要確認
- 周波数または送信出力に関係するか: アンテナ構成により要確認
- 日本国内仕様から外れる可能性があるか: 要確認
## 7. Parameters and Response Structure
- Request fields: アンテナ番号。要仕様確認
- Response fields: ACK/NACK等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
一時変更か永続変更かを確認し、復旧手順を先に決める。
## 9. Real Device Test Status
PROHIBITED。
## 10. AI Behavior Rules
AIが勝手に実装しない。
## 11. Prohibited or Restricted Usage
8CHアンテナ自動切替禁止、完成Hex生成禁止。
## 12. References
- docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md
## 13. Current Decision
PROHIBITED_DOCUMENT_ONLY
