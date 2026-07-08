# UHF_Inventory

## 1. Basic Information

- Command name: UHF_Inventory
- Command category: uhf_basic_read
- Command identifier: 55/10
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED

## 2. Purpose

既存設定の範囲でタグInventoryを行い、タグ応答を確認する。

## 3. Operation Summary

電波送信を伴うInventory操作。完成Hex、SUM計算済みコマンド、送信用コードは記載しない。

## 4. Expected Use Cases

- タグを1回だけ読みたい
- タグを連続で読みたい
- RSSIや読取チャンネルを記録したい

## 5. Safety Classification

- Safety class: INVENTORY_RF_EMISSION
- Operation level: Level 2
- Requires explicit confirmation: 実機送信時は必要
- Requires recovery procedure: 通常不要
- Can AI implement without confirmation: 実装せず方針提示まで
- Can be used in external review candidate: 可
- Notes: R8-8AでInventory 1回確認済み

## 6. Device Impact

- 読み取り専用か: タグ読取
- 電波送信を伴うか: はい
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: いいえ
- 周波数または送信出力に関係するか: 既存設定を使用
- 日本国内仕様から外れる可能性があるか: 設定変更時は要確認

## 7. Parameters and Response Structure

- Request fields: 要仕様確認
- Response fields: タグ応答数、識別情報、RSSI等
- Required parameters: 既存Inventory条件
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合

## 8. Implementation Guidance

全言語でタイムアウト、ログ、タグIDマスク、例外処理を実装方針に含める。設定値は外部化し、実機確認は短時間・小回数から始める。

## 9. Real Device Test Status

TESTED_INVENTORY。R8-8AでInventory 1回、タグ応答1件を確認。

## 10. AI Behavior Rules

接続方式、タグ条件、ログ方針を確認してから方針を出す。Level 4以上の設定変更を勝手に含めない。

## 11. Prohibited or Restricted Usage

UHF_SetInventoryParam自動送信、周波数変更、送信出力変更、完成Hex生成は禁止または要明示確認。

## 12. References

- docs/current/06_COMMAND_INDEX.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
- PDF reference: PDF原本との再照合が必要

## 13. Current Decision

READY_FOR_REFERENCE
