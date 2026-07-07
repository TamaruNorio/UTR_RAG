# UHF_BlockWrite

## 1. Basic Information
- Command name: UHF_BlockWrite
- Command category: tag_memory_write
- Command identifier: 55/1A
- Source catalog: docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
タグメモリをブロック単位で書き込む。
## 3. Operation Summary
タグメモリ変更を伴うLevel 4操作。
## 4. Expected Use Cases
- タグ書き込みを検討したい
## 5. Safety Classification
- Safety class: TAG_MEMORY_WRITE_RESTRICTED
- Operation level: Level 4
- Requires explicit confirmation: 必須
- Requires recovery procedure: 必須
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: 文書参照のみ
- Notes: タグ書き込み
## 6. Device Impact
- 読み取り専用か: いいえ
- 電波送信を伴うか: はい
- タグメモリ変更を伴うか: はい
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: タグ側永続影響あり
- 周波数または送信出力に関係するか: 既存RF設定を使用
- 日本国内仕様から外れる可能性があるか: 要確認
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: ACK/NACK等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
書き込み前後確認、復旧可否、ログ方針を必須にする。
## 9. Real Device Test Status
PROHIBITED。
## 10. AI Behavior Rules
勝手に実装しない。
## 11. Prohibited or Restricted Usage
完成Hex、SUM計算済みコマンド、送信用コード生成禁止。
## 12. References
- docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
## 13. Current Decision
PROHIBITED_DOCUMENT_ONLY
