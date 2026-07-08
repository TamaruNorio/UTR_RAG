# Restart Reader Command Card

## 1. Command Identity

- Command name: Restart Reader
- Command group: reader control
- Command code reference: 4E/9D
- R8-7 catalog source: `docs/current/06_COMMAND_INDEX.md`

## 2. Purpose

リーダ再起動に関する整理用カードである。永続設定変更ではない可能性がある一方、通信断や状態変化を伴うため、仕様確認までHOLDとする。

## 3. Safety Classification

- Safety class: `DEVICE_SETTING_RESTRICTED`
- Risk: 通信断、処理中断、状態変化
- Default handling: HOLD

## 4. Operation Level

- Operation level: Level 4
- Approval: 実施条件、復旧手順、接続再確立方法の確認が必要

## 5. Parameters Overview

パラメータ詳細はPDF原本との照合対象である。完成Hex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 6. Expected Response Overview

レスポンス仕様および再起動後の通信状態は未確認である。実施時はログ保存と復旧確認が必要。

## 7. Real-device Test Status

- Status: `HOLD`
- R8-8A: 未実施
- Reason: 再起動操作の影響と復旧条件が未確定

## 8. Preconditions

- 実施前に仕様根拠を確認する
- 他の処理が動作していないことを確認する
- 再接続手順とログ保存先を決める

## 9. Prohibited Use

- 自動実行
- 他コマンドと連続した送信
- 復旧手順なしの実機確認
- 顧客環境での確認

## 10. Related Documents

- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/02_SAFETY_AND_HOLD_ITEMS.md`
- `docs/current/02_SAFETY_AND_HOLD_ITEMS.md`

## 11. AI Retrieval Tags

- command: Restart Reader
- category: reader_control
- safety: device_setting_restricted
- operation_level: 4
- test_status: hold

## 12. AI Handling Notes

AIはこのコマンドを安全な疎通確認として提案しない。必要時はHOLD理由と仕様確認項目を返す。

## 13. Current Decision

`HOLD_NEEDS_SPEC_CONFIRMATION`
