# UHF_GetExpandSelectParam

## 1. Basic Information
- Command name: UHF_GetExpandSelectParam
- Command category: uhf_parameter_read
- Command identifier: 55/42
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED
## 2. Purpose
拡張Select条件の現在値を読み取る。
## 3. Operation Summary
読み取り専用の設定取得。完成コマンドは記載しない。
## 4. Expected Use Cases
- 拡張Select条件を確認したい
- 読み取り条件を確認したい
## 5. Safety Classification
- Safety class: READ_ONLY
- Operation level: Level 1
- Requires explicit confirmation: 実機接続時は必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 方針提示まで
- Can be used in external review candidate: 可
- Notes: 未実機確認
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
- Response fields: Expand Select Param
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合
## 8. Implementation Guidance
取得値をログ化し、変更処理と分離する。
## 9. Real Device Test Status
NOT_TESTED。
## 10. AI Behavior Rules
仕様不明ならHOLD。Set系を勝手に実装しない。
## 11. Prohibited or Restricted Usage
完成Hex、SUM計算済みコマンド、実機送信用コード生成禁止。
## 12. References
- docs/current/06_COMMAND_INDEX.md
- docs/current/03_AI_USAGE_GUIDE.md
## 13. Current Decision
PARTIAL_WITH_NOTES
