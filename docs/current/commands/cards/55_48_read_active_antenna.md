# 使用アンテナ番号の読み取り

## 1. Basic Information
- Command name: 使用アンテナ番号の読み取り
- Command category: antenna_setting_read
- Command identifier: 55/48
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: なし
- PDF reference: なし。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: MISSING_TRACEABILITY
## 2. Purpose
使用アンテナ番号を確認する。
## 3. Operation Summary
アンテナ設定の読み取り系。完成コマンドは記載しない。
## 4. Expected Use Cases
- 使用アンテナ番号を記録したい
- 特定アンテナ読み取り前に状態確認したい
## 5. Safety Classification
- Safety class: NEEDS_SPEC_CONFIRMATION
- Operation level: Level 1
- Requires explicit confirmation: 必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: HOLD付き
- Notes: trace item不足
## 6. Device Impact
- 読み取り専用か: はい想定
- 電波送信を伴うか: 要仕様確認
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: いいえ
- 周波数または送信出力に関係するか: いいえ
- 日本国内仕様から外れる可能性があるか: 低
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: 使用アンテナ番号
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF再照合
## 8. Implementation Guidance
Python/C#/C++/Node.js/PowerShellでログ項目として扱う。書き込み操作と分離する。
## 9. Real Device Test Status
NOT_TESTED。
## 10. AI Behavior Rules
読み取りと書き込みを混同しない。
## 11. Prohibited or Restricted Usage
完成Hex、SUM計算済みコマンド、実機送信用コード生成禁止。
## 12. References
- docs/current/06_COMMAND_INDEX.md
## 13. Current Decision
HOLD_NEEDS_SPEC_CONFIRMATION
