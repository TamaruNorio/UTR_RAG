# UHF_Read

## 1. Basic Information

- Command name: UHF_Read
- Command category: tag_memory_read
- Command identifier: 55/15
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED

## 2. Purpose

タグメモリを読み取る。55h/15hはUHF_InventoryReadではない。

## 3. Operation Summary

電波送信を伴うタグメモリ読み取り操作。完成Hex、SUM計算済みコマンド、送信用コードは記載しない。

## 4. Expected Use Cases

- EPCだけでなくTIDも読みたい
- USER領域を読みたい
- タグメモリの内容を確認したい

## 5. Safety Classification

- Safety class: READ_WITH_RF
- Operation level: Level 2
- Requires explicit confirmation: 実機送信時は必要
- Requires recovery procedure: 通常不要
- Can AI implement without confirmation: 不可。方針提示まで
- Can be used in external review candidate: HOLD付きで参照可
- Notes: standalone確認はHOLD

## 6. Device Impact

- 読み取り専用か: はい
- 電波送信を伴うか: はい
- タグメモリ変更を伴うか: いいえ
- リーダ設定変更を伴うか: いいえ
- FLASHまたは永続設定に関係するか: いいえ
- 周波数または送信出力に関係するか: 既存設定を使用
- 日本国内仕様から外れる可能性があるか: 設定変更時は要確認

## 7. Parameters and Response Structure

- Request fields: メモリバンク、開始位置、Word数等は要仕様確認
- Response fields: 読取データ、状態、エラー情報等
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合

## 8. Implementation Guidance

多言語実装では読取対象、範囲、Access Password要否を確認する。タグIDやメモリ内容はマスクする。

## 9. Real Device Test Status

HOLD。R8-8AではUHF_Read standaloneは未実施。

## 10. AI Behavior Rules

55h/15hをUHF_InventoryReadと書かない。対象メモリが不明ならHOLD。

## 11. Prohibited or Restricted Usage

完成Hex、SUM計算済みコマンド、実機送信用コード生成禁止。

## 12. References

- docs/current/06_COMMAND_INDEX.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
- docs/current/03_AI_USAGE_GUIDE.md
- PDF reference: PDF原本との再照合が必要

## 13. Current Decision

PARTIAL_WITH_NOTES
