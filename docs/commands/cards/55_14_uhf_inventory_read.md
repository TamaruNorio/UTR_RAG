# UHF_InventoryRead

## 1. Basic Information

- Command name: UHF_InventoryRead
- Command category: uhf_tag_memory_read
- Command identifier: 55/14
- Source catalog: docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED

## 2. Purpose

Inventoryと読み取りを組み合わせたタグメモリ読取系操作。55h/14hはUHF_Readではない。

## 3. Operation Summary

電波送信を伴う読取系操作。完成Hex、SUM計算済みコマンド、送信用コードは記載しない。

## 4. Expected Use Cases

- TIDを読みたい
- Inventoryしながら追加情報を読みたい

## 5. Safety Classification

- Safety class: INVENTORY_RF_EMISSION
- Operation level: Level 2
- Requires explicit confirmation: 実機送信時は必要
- Requires recovery procedure: 通常不要
- Can AI implement without confirmation: 不可。方針提示まで
- Can be used in external review candidate: HOLD付きで参照可
- Notes: UHF_Readとの混同禁止

## 6. Device Impact

- 読み取り専用か: 読み取り系
- 電波送信を伴うか: はい
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: いいえ
- 周波数または送信出力に関係するか: 既存設定を使用
- 日本国内仕様から外れる可能性があるか: 設定変更時は要確認

## 7. Parameters and Response Structure

- Request fields: 読み取り対象、範囲等は要仕様確認
- Response fields: タグ応答、読取データ等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合

## 8. Implementation Guidance

Python/C#/C++/Node.js/PowerShellでは、UHF_Readと誤認しない。タイムアウト、ログ、タグIDマスク、HOLD条件を明示する。

## 9. Real Device Test Status

HOLD。R8-8AではUHF_InventoryRead単体確認は未実施。

## 10. AI Behavior Rules

55h/14hをUHF_Readと書かない。対象メモリや範囲が不明ならHOLD。

## 11. Prohibited or Restricted Usage

完成Hex、SUM計算済みコマンド、実機送信用コード生成禁止。

## 12. References

- docs/commands/R8-7_ALL_COMMAND_CATALOG_DRAFT.md
- docs/commands/R8-7_COMMAND_COVERAGE_AUDIT.md
- docs/use_cases/R9-1_OPERATION_LEVELS_AND_APPROVAL.md
- PDF reference: PDF原本との再照合が必要

## 13. Current Decision

PARTIAL_WITH_NOTES
