# Stage 0/1 Read-only Logging Guide

## 1. Storage paths

- CSVログ保存先案: `runtime_logs/stage01_readonly/`
- Markdown結果保存先案: `runtime_logs/stage01_readonly/`
- `runtime_logs/` は `.gitignore` 対象とし、実機ログは原則としてGit管理しない。

## 2. File naming

- CSV: `stage01_readonly_<date_time>_<connection>_log.csv`
- Markdown: `stage01_readonly_<date_time>_<connection>_result.md`
- date_time: `YYYYMMDD_HHMMSS`
- connection: `COMx` or masked host label

## 3. Required record fields

- 実行時刻
- 実行者
- 接続方式
- COMポート/IPのマスク方針
- ROMバージョン
- シリーズ名
- 機種判定
- 実行コマンド
- ACK/NACK/timeout
- エラーコード1〜4
- 実行結果ステータス
- 備考

## 4. Masking policy

- COM: `COMx`
- IP: `192.168.xxx.xxx`
- tag ID: `EPC_xxxxxxxxxxxx`
- customer: `株式会社XXXX`

## 5. Result handling

- `REAL_DEVICE_PASS` is used only when a real-device response is captured.
- `REAL_DEVICE_PASS_WITH_NOTES` is used when the response is acceptable but notes remain.
- `NOT_APPLICABLE_TO_TARGET` is used when the ROM/product condition does not apply.
- Timeout is not NACK.
- No-response is not NACK.
