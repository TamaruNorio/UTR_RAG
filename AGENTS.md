# AI作業指示

このリポジトリは、タカヤ製 UTR-S201シリーズの通信プロトコル理解、実装支援、レビュー、段階的な実機確認をAIと人間で進めやすくするためのドキュメントリポジトリです。

## 最初に読む文書

1. `README.md`
2. `RELEASE_SCOPE.md`
3. `llms.txt`
4. `docs/current/V100_USAGE_GUIDE.md`
5. `docs/current/COMMAND_MASTER_V117.md`
6. `docs/current/RESPONSE_AND_NACK_MASTER.md`
7. `docs/current/RESPONSE_CLASSIFICATION_MATRIX.md`
8. `docs/current/commands/cards/TEST_STATUS_INDEX.md`

対象コマンドが決まっている場合は、`docs/current/COMMAND_MASTER_V117.md` から該当する `docs/current/commands/cards/` 配下のコマンドカードへ進んでください。

## 接続方式別の参照先

USB接続で実装する場合は、USB/COM接続であることを作業指示に明記し、対象コマンドカードと `docs/current/RESPONSE_AND_NACK_MASTER.md` を確認したうえで、必要に応じて USB接続版サンプル `UTR_USB_Python_CodeX` を参照してください。

LAN接続で実装する場合は、LAN/TCP接続であることを作業指示に明記し、対象コマンドカードと `docs/current/RESPONSE_AND_NACK_MASTER.md` を確認したうえで、必要に応じて LAN(TCP)接続版サンプル `UTR_LAN_Python_CodeX` を参照してください。

## 複数アンテナ機種の実装

複数アンテナ機種を実装する場合は、`docs/current/commands/cards/55_10_uhf_inventory.md` 単体で判断しないでください。少なくとも次のカードを併せて確認してください。

- `docs/current/commands/cards/55_48_read_active_antenna.md` - 使用アンテナ番号の読み取り
- `docs/current/commands/cards/55_38_write_active_antenna.md` - 使用アンテナ番号の書き込み
- `docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md` - 外部アンテナ自動切替設定の読み取り
- `docs/current/commands/cards/55_37_write_external_antenna_auto_switch.md` - 外部アンテナ自動切替設定の書き込み

## 実装前に確認すること

- 対象機種
- ROMバージョン
- 接続方式
- 対象コマンド
- 実装言語
- timeout
- ログ方針
- 実機送信の有無
- 停止条件
- 復旧方法

## 安全ルール

公式PDFが一次情報です。このリポジトリは公式PDFを置き換えるものではありません。

完成Hex、SUM計算済みコマンド、実機送信用コード、安全ガード解除コードを安易に出さないでください。周波数、送信出力、FLASH、アンテナ設定などに影響する処理は、対象機種、ROM、地域条件、現場条件、復旧方法を確認してから扱ってください。

runtime logs、実CSVログ、顧客情報、実IPアドレス、実機ログ由来のraw EPC / UII / TID、認証情報、パスワードはGitHubに含めないでください。
