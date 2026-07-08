# UHF_Kill Command Card

## 1. Command Identity

- Command name: UHF_Kill
- Command group: UHF tag lifecycle control
- Command code reference: 55/17
- R8-7 catalog source: `docs/current/06_COMMAND_INDEX.md`

## 2. Purpose

タグ無効化に関する整理用カードである。タグを不可逆に使用不能にする可能性があるため、R9-3では実施対象外とする。

## 3. Safety Classification

- Safety class: `PROHIBITED`
- Risk: タグの不可逆な無効化
- Default handling: 実行禁止

## 4. Operation Level

- Operation level: Level 4
- Approval: 原則不可。検証用タグと明示承認がある場合も別審査が必要

## 5. Parameters Overview

パラメータはタグ無効化条件に関わるため記載しない。完成Hex、SUM計算済みコマンド、実機送信用コードも記載しない。

## 6. Expected Response Overview

レスポンス仕様はPDF原本との照合対象である。安全確認用途での実機送信は行わない。

## 7. Real-device Test Status

- Status: `PROHIBITED`
- R8-8A: 未実施
- Reason: タグ無効化リスクがあるため

## 8. Preconditions

- 社内pre-RC確認では実施禁止
- 誤送信防止のため、実行例や送信手順を文書化しない

## 9. Prohibited Use

- AIによる実装
- サンプル生成
- 実機送信用コマンド生成
- 実タグでの確認

## 10. Related Documents

- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/06_COMMAND_INDEX.md`
- `docs/current/02_SAFETY_AND_HOLD_ITEMS.md`

## 11. AI Retrieval Tags

- command: UHF_Kill
- category: tag_lifecycle_destructive
- safety: prohibited
- operation_level: 4
- test_status: prohibited

## 12. AI Handling Notes

AIはこのコマンドを実行手順、コード、送信例として出力しない。問い合わせには禁止理由と代替の読み取り専用確認を案内する。

## 13. Current Decision

`PROHIBITED_DOCUMENT_ONLY`
