# Real Device Verification Framework

## 1. Positioning

v010では、v009 traceability completed packageを前提に、全54コマンドの実機確認を段階的に進めるための確認フレームワークを定義する。

この文書は、実機送信を直接指示するものではなく、実機確認時の前提、ログ、判定、復旧観点を整理するものである。

## 2. Standard verification flow

1. 接続方式を確認する
2. ROMバージョン読み取りを実行する
3. ROMバージョン番号とシリーズ名を取得する
4. シリーズ名から機種を判定する
5. 対応コマンドとROM条件を確認する
6. 接続アンテナ数、使用アンテナ、現場条件を確認する
7. 対象コマンドのTraceability節を確認する
8. パラメータを決定する
9. 実行前ログを記録する
10. コマンドを実行する
11. ACK/NACK/timeout/複数レスポンス/無応答を記録する
12. 必要に応じて復旧または設定戻しを行う
13. 実行後ログを記録する
14. 判定を記録する

## 3. Verification principles

- プロトコル仕様書にあるコマンドは使用可能な機能として扱う
- 実行前に、対象機種、ROM、パラメータ、影響範囲を確認する
- ROMから取れる情報はユーザーに聞かず、ROM読み取りで取得する
- ユーザーに確認するのは、ROMから取れない現場条件と不足パラメータ
- timeoutはNACKではない
- 無応答はNACKではない
- 複数レスポンスと完了レスポンスは分ける
- FLASH、永続設定、タグメモリ、Lock/Kill/Encodeは復旧観点を記録する

## 4. Required references

- Command card Traceability section
- docs/current/10_RESPONSE_AND_NACK_MASTER.md
- docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md
- docs/current/12_RAM_FLASH_IMPACT_MATRIX.md
- docs/current/13_RF_SAFETY_AND_CARRIER_RULES.md
- docs/current/15_PARAMETER_CONFIRMATION_GUIDE.md
- docs/current/18_REAL_DEVICE_LOG_SCHEMA.md
- docs/current/19_VERIFICATION_STAGE_PLAN.md
- docs/current/20_VERIFICATION_RESULT_STATUS.md

## 5. Safety notes

- v010 does not perform real-device command send.
- v010 does not add executable control code.
- v010 does not include completed Hex, SUM-calculated commands, or device-sendable code.
- Commands are not marked unusable merely because they require device, ROM, parameter, site, or recovery confirmation.
