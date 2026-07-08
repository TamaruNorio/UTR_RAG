# UHF_GetInventoryParam

## 1. Basic Information
- Command name: UHF_GetInventoryParam
- Command category: uhf_parameter_read
- Command identifier: 55/41
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
Inventory条件の現在値を読み取る。
## 3. Operation Summary
読み取り専用の設定取得。完成Hex、SUM計算済みコマンド、送信用コードは書かない。
## 4. Expected Use Cases
- 読み取り条件を確認したい
- 読み取り安定化前に現在設定を見たい
## 5. Safety Classification
- Safety class: READ_ONLY
- Operation level: Level 1
- Requires explicit confirmation: 実機接続時は必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 方針提示まで
- Can be used in external review candidate: 可
- Notes: R8-8Aで取得確認
## 6. Device Impact
- 読み取り専用か: はい
- 電波送信を伴うか: いいえ
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: いいえ
- 周波数または送信出力に関係するか: 間接的に読取条件確認
- 日本国内仕様から外れる可能性があるか: 低
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: Inventory Param
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合
## 8. Implementation Guidance
全言語でログとタイムアウトを用意し、取得値を変更値として扱わない。
## 9. Real Device Test Status
TESTED_READ_ONLY。R8-8Aで取得成功。
## 10. AI Behavior Rules
取得と設定を混同しない。UHF_SetInventoryParamを自動送信しない。
## 11. Prohibited or Restricted Usage
完成Hex、SUM計算済みコマンド、実機送信用コード生成禁止。
## 12. References
- docs/current/06_COMMAND_INDEX.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
- PDF reference: PDF原本との再照合が必要
## 13. Current Decision
READY_FOR_REFERENCE
