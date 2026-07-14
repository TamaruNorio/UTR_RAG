# AI利用ガイド

## 1. 最初に読むもの

対象が広い場合は、リポジトリ全体、または主要ドキュメント一式をAIに読ませて構いません。

対象コマンドが決まっている場合は、以下を中心に読みます。

1. `README.md`
2. `llms.txt`
3. `docs/current/AI_CONTEXT_INDEX.md`
4. `docs/current/09_COMMAND_MASTER_V117.md`
5. `docs/current/commands/cards/` の対象カード
6. `docs/current/10_RESPONSE_AND_NACK_MASTER.md`
7. `docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

## 2. AIへ依頼するときに渡す情報

- 目的
- 対象機種
- 接続方式
- 対象コマンド
- 実装言語
- 実行環境
- 実機送信の有無
- 変更してよい範囲
- 変更してはいけない範囲
- 確認方法
- 完了条件

## 3. 実装前の流れ

1. ROMバージョンを読み取り、対象機種とROMを確認する。
2. コマンドマスタとコマンドカードで仕様を確認する。
3. パラメータ、影響範囲、応答処理、NACK処理、timeout処理を整理する。
4. 実装言語に合わせて、接続、送信、受信、解析、切断を分けて設計する。
5. 机上確認または dry-run を行う。
6. 実機送信する場合は、対象、値、停止条件、復旧方法、ログ方針を確認する。

## 4. AIに禁止すること

AIに、作業指示にない高影響操作を勝手に追加させないでください。

特に、周波数、送信出力、アンテナ設定、FLASH、タグメモリ、Lock、Kill、Encode、ThroughCmdについては、対象・値・影響・停止条件を明確にしてから実装します。