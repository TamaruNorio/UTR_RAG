# Stage 0/1 Read-only Verification Kit

## 1. Positioning

v011は、v010 real-device verification frameworkに基づき、Stage 0/1のread-only系確認を安全に開始するための検証キットである。

このキットは、設定変更やタグ書き込みを目的としない。

## 2. Standard flow

1. 接続方式を指定する
2. dry-runで対象コマンドを確認する
3. --execute指定時のみ実機へread-onlyコマンドを送信する
4. 最初にROMバージョン読み取りを行う
5. ROMバージョン番号とシリーズ名を解析する
6. USM01/USM02/USM05/USM06/USM08から機種を判定する
7. Stage 0 read-onlyコマンドを実行する
8. Stage 1 read-only設定値読み取りコマンドを実行する
9. ACK/NACK/timeoutを記録する
10. CSVログとMarkdown結果を保存する

## 3. Scope

対象:

- ROMバージョン読み取り
- チップバージョン読み取り
- エラー情報読み取り
- リーダライタ動作モード読み取り
- SelectParam読み取り
- InventoryParam読み取り
- ExpandSelectParam読み取り
- アンテナ切替設定読み取り
- 出力設定読み取り
- 周波数設定読み取り
- RFタグ通信関連パラメータ読み取り
- EPC(UII)関連パラメータ読み取り
- 外部アンテナ自動切替設定読み取り
- 汎用ポート値読み取り
- 拡張ポート値読み取り
- FLASH設定値読み取り
- RSSIフィルタ設定読み取り
- アンテナ個別送信出力設定読み取り

対象外:

- 書き込み系
- FLASH変更
- 周波数変更
- 送信出力変更
- アンテナ切替設定変更
- タグメモリ変更
- Lock / Kill / Encode
- ThroughCmd

対象外は「仕様上禁止」ではなく、v011の確認対象外として扱うこと。

## 4. Tool policy

- `tools/stage01_readonly_verify.py` is dry-run by default.
- `--execute` is required for real-device communication.
- `--port` or `--host` must be explicitly specified before real-device communication.
- The tool contains only Stage 0/1 read-only command definitions.
- The tool does not include write commands, FLASH write, frequency change, output power change, antenna setting change, tag memory operation, Lock, Kill, Encode, or ThroughCmd.
