# ROMバージョンの読み取り

## 1. Basic Information

- Command name: ROMバージョンの読み取り
- Command category: reader_control
- Command identifier: 4F/90
- Source catalog: docs/current/06_COMMAND_INDEX.md
- Existing RAG document: あり
- Safety matrix status: あり
- Source traceability status: あり
- PDF reference: あり。PDF原本との再照合が必要
- Japan domestic scope: 日本国内仕様前提
- Current coverage status: COVERED

## 2. Purpose

リーダライタのROM情報を読み取り、対象機器の確認に使う。

## 3. Operation Summary

機器状態を取得する読み取り専用操作。完成Hex、SUM計算済みコマンド、送信用コードは記載しない。

## 4. Expected Use Cases

- 現在接続している機器を確認したい
- 実機確認ログにROM情報を残したい
- UTR-SUN02-4CHか確認したい

## 5. Safety Classification

- Safety class: READ_ONLY
- Operation level: Level 1
- Requires explicit confirmation: 実機接続時は必要
- Requires recovery procedure: 不要
- Can AI implement without confirmation: 接続情報確認後に方針提示まで可
- Can be used in external review candidate: 可
- Notes: R8-8Aで確認済み

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
- Response fields: ROM情報、ファームウェア情報
- Required parameters: 要仕様確認
- Optional parameters: 要仕様確認
- Unknown / needs confirmation: PDF原本との再照合

## 8. Implementation Guidance

Python/C#/C++/Node.js/PowerShellでは、接続、送信、受信、切断を分ける。タイムアウト、ログ出力、例外処理、設定値外部化を必須とし、実機確認前に対象機器と接続方式を確認する。

## 9. Real Device Test Status

PASS_WITH_NOTES。R8-8AでROM/status readsとして確認済み。

## 10. AI Behavior Rules

対象機器、接続方式、地域条件が不明なまま実装しない。PDF正本との照合が必要な場合は断定しない。

## 11. Prohibited or Restricted Usage

完成Hex生成、SUM計算済みコマンド生成、実機送信用コード生成は禁止。

## 12. References

- docs/current/06_COMMAND_INDEX.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
- docs/current/02_SAFETY_AND_HOLD_ITEMS.md
- PDF reference: PDF原本との再照合が必要

## 13. Current Decision

READY_FOR_REFERENCE
