# R8-8A Real Device Command Send Check Result

## 1. 結論

判定:

`R8-8A_REAL_DEVICE_COMMAND_SEND_CHECK_PASS_WITH_NOTES`

ユーザー明示許可に基づき、当社開発品 UTR-SUN02-4CH に対して、既存の当社実機確認済みUSBサンプルを用いた実機確認を実施した。

COM6 / 115200bps で接続し、ステータス取得系、Inventory系、Inventoryに伴うタグ読み取り応答を確認した。タグメモリを対象にした `UHF_Read` 単体確認は、既存実行入口に含まれないため未実施とした。

## 2. 実機情報

| 項目 | 内容 |
|---|---|
| 対象機器 | UTR-SUN02-4CH |
| 接続方式 | USB |
| 接続情報 | COM6 / 115200bps |
| ROM情報 | 2052USM02 |
| ファームウェアバージョン | 2.052 |
| アンテナ構成 | UTR-SUN02-4CH（内蔵1CH + 外付け3CH）。実接続アンテナ詳細は未記録 |
| 使用タグ | 1件検出。タグ固有IDは記録しない |
| 実施者 | Codex |
| 実施日時 | 2026-07-06 JST |
| 実施場所 | 未記録 |

タグ固有情報、顧客情報、認証情報は記録していない。

## 3. ユーザー明示許可

ユーザーから、当社開発品である対象機器に対して、当社実機確認済みサンプルコードを用いた実機確認を進めてよい旨の明示許可があった。

## 4. 実行前レビュー

| No | 使用ファイルまたは手順 | 実行目的 | 主な処理 | 実機影響 | 実施判断 | 備考 |
|---:|---|---|---|---|---|---|
| 1 | `D:\My documents\Python Scripts\CodeX\UTR_USB_Python_CodeX\tools\usb_inventory_batch.py` | ステータス取得とInventory確認 | USB接続、ROM確認、コマンドモード切替、送信出力読み取り、周波数チャンネル読み取り、Inventory Param取得、Inventory 1回、CSV保存、切断 | 電波送信を伴うInventoryを実施。設定変更は行わない入口 | 実行可 | `--no-buzzer`を指定し、ブザー制御は抑止 |
| 2 | 実行コマンド | COM6 / 115200bps 指定実行 | 既存CLI引数でCOMポート、ボーレート、実行回数、CSV保存先、ブザー抑止を指定 | 実機へ既存サンプルの通常範囲で送信 | 実行可 | UTR_RAG内には送信用コードを追加しない |
| 3 | `README.md` 記載の安全ルール確認 | 実行範囲確認 | USB Inventory batch runner の安全方針を確認 | FLASH、送信出力、周波数、Inventory Param、8CHアンテナ切替を変更しない | 実行可 | ユーザー明示許可あり |

実行コマンドは既存サンプルのCLI実行であり、Markdown本文には完成Hex、SUM計算済みコマンド、実機送信用コードを記載しない。

## 5. ステータス取得系確認結果

| No | 確認名 | 目的 | 実施可否 | 実結果 | 判定 | 備考 |
|---:|---|---|---|---|---|---|
| 1 | COM接続 | COM6 / 115200bps で接続できること | 実施 | 接続成功 | PASS | closeまで完了 |
| 2 | ROMバージョン確認 | 機器応答と機種照合 | 実施 | ACK受信、ROM情報とファームウェアバージョン取得 | PASS | UTR-SUN02-4CHとして照合 |
| 3 | コマンドモード切替 | 既存サンプル通常初期化 | 実施 | 切替成功 | PASS_WITH_NOTES | サンプル通常動作範囲として実施 |
| 4 | 送信出力情報取得 | 現在設定の読み取り | 実施 | 24.0 dBmとして読み取り | PASS | 変更なし |
| 5 | 周波数チャンネル情報取得 | 現在設定の読み取り | 実施 | 27 ch / 921.2 MHzとして読み取り | PASS | 変更なし |
| 6 | Inventory Param取得 | 現在設定の読み取り | 実施 | 取得成功 | PASS | `UHF_SetInventoryParam`は送信していない |

## 6. Inventory系確認結果

| No | 確認名 | 目的 | 実施可否 | 実結果 | 判定 | 備考 |
|---:|---|---|---|---|---|---|
| 1 | Inventory 1回実行 | 既存設定範囲でタグInventoryが実行できること | 実施 | 読み取り完了レスポンス1件、タグ応答1件 | PASS_WITH_NOTES | タグ固有IDは記録しない |
| 2 | 読み取りチャンネル確認 | Inventory応答の概要確認 | 実施 | 27 chで応答 | PASS | 周波数変更なし |
| 3 | NACK/エラー確認 | 異常有無確認 | 実施 | NACKなし、実行エラーなし | PASS | タイムアウトなし |
| 4 | CSV保存 | 後追い可能性確認 | 実施 | TEMP配下にCSV保存 | PASS_WITH_NOTES | GitHubへは追加しない |

## 7. 読み取り系確認結果

| No | 確認名 | 目的 | 実施可否 | 実結果 | 判定 | 備考 |
|---:|---|---|---|---|---|---|
| 1 | Inventoryに伴うタグ読み取り応答 | タグ応答を取得できること | 実施 | タグ応答1件、RSSI要約取得 | PASS_WITH_NOTES | タグ固有IDはマスク扱いで本文に記載しない |
| 2 | TID関連設定の確認 | Inventory Param上の読み取り設定確認 | 実施 | MemBankはTID、読み取りWord数は2として取得 | PASS_WITH_NOTES | 設定取得のみ。設定変更なし |
| 3 | `UHF_Read` 単体確認 | タグメモリ読み取りコマンド単体の確認 | 未実施 | 既存実行入口に含まれない | HOLD | 次工程で仕様と安全条件を整理 |

## 8. ログ概要

実行概要:

- 既存実行ファイル: `D:\My documents\Python Scripts\CodeX\UTR_USB_Python_CodeX\tools\usb_inventory_batch.py`
- 実行環境: Windows / PowerShell / Python
- 接続: COM6 / 115200bps
- 実行回数: Inventory 1回
- ブザー制御: `--no-buzzer`により抑止
- CSV保存先: `C:\Users\tamaru\AppData\Local\Temp\utr_r8_8a_inventory.csv`
- 接続結果: 成功
- ROM確認: ACK受信
- Inventory結果: タグ応答1件
- RSSI概要: -49.8 dBm
- 終了処理: シリアル接続close完了

タグ固有ID、生レスポンスHex、SUM計算済みコマンド、実機送信用コードは記載しない。

## 9. 安全確認

| 項目 | 実施有無 | 備考 |
|---|---|---|
| FLASH書き込み | なし | 既存サンプルのInventory batch runnerでは実施しない |
| 周波数変更 | なし | 周波数チャンネル情報の読み取りのみ |
| 送信出力変更 | なし | 送信出力情報の読み取りのみ |
| UHF_SetInventoryParam送信 | なし | 取得のみ。設定変更なし |
| UHF_SetInventoryParam自動送信 | なし | サンプル出力上も自動送信なしを確認 |
| 8CHアンテナ自動切替 | なし | 4CH対象。8CH切替なし |
| 永続設定変更 | なし | 実施なし |
| ブザー制御 | なし | `--no-buzzer`指定 |
| PDF追加 | なし | 追加差分なし |
| R7-5A ZIP変更 | なし | 変更なし |
| GitHub Release変更 | なし | 変更なし |
| 完成Hexの文書化 | なし | 記載なし |
| SUM計算済みコマンドの文書化 | なし | 記載なし |
| UTR_RAGへの実機送信用コード追加 | なし | Markdown記録のみ |

## 10. HOLD事項

- `UHF_Read` 単体確認は未実施
- アンテナの物理接続構成詳細は未記録
- 実施場所は未記録
- CSVにはタグ固有情報が含まれる可能性があるため、GitHubへ追加しない

## 11. 次工程

R8-8B:

- `UHF_Read` 単体確認を行うか、仕様確認と対象タグ、メモリバンク、読み取り範囲、安全条件を整理する。

または、R8-8Aの確認範囲で十分と判断する場合は、R8-9として v005 full-command no-PDF package 作成へ進む。
