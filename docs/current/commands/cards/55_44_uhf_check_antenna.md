# UHF_CheckAntenna

## 1. Basic Information
- Command name: UHF_CheckAntenna
- Command category: antenna_inspection
- Command identifier: 55/44
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: なし
- PDF reference: なし。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: MISSING_TRACEABILITY
## 2. Purpose
アンテナ状態確認。要仕様確認。
## 3. Operation Summary
アンテナ確認系操作。完成Hex等は記載しない。
## 4. Expected Use Cases
- アンテナ接続状態を確認したい
## 5. Safety Classification
- Safety class: NEEDS_SPEC_CONFIRMATION
- Operation level: Level 1
- Requires explicit confirmation: 必要
- Requires recovery procedure: 通常不要
- Can AI implement without confirmation: 不可
- Can be used in external review candidate: HOLD付き
- Notes: trace item不足
## 6. Device Impact
- 読み取り専用か: 要仕様確認
- 電波送信を伴うか: 要仕様確認
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ想定
- FLASHまたは永続設定に関係するか: いいえ想定
- 周波数または送信出力に関係するか: 要仕様確認
- 日本国内仕様から外れる可能性があるか: 要仕様確認
## 7. Parameters and Response Structure
- Request fields: 要仕様確認
- Response fields: アンテナ状態。要仕様確認
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: traceabilityとPDF再照合
## 8. Implementation Guidance
多言語実装では仕様確認までに留める。実機送信前にアンテナ構成とログ方針を確認する。
## 9. Real Device Test Status
NOT_TESTED。
## 10. AI Behavior Rules
仕様不明のまま実装しない。
## 11. Prohibited or Restricted Usage
完成Hex、SUM計算済みコマンド、実機送信用コード生成禁止。
## 12. References
- docs/current/06_COMMAND_INDEX.md
- PDF reference: PDF原本との再照合が必要
## 13. Current Decision
HOLD_NEEDS_SPEC_CONFIRMATION
