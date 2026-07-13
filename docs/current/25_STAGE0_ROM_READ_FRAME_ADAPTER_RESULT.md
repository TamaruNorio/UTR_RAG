# Stage 0 ROM Read Frame Adapter Result

## 1. Positioning

v013では、v012でHOLDとなったStage 0 read-only実行について、ROMバージョン読み取り専用のフレームアダプタを確認する。

この文書はマスク済みサマリであり、`runtime_logs/` の生ログはGit管理しない。

## 2. Execution scope

対象:

- ROMバージョンの読み取り

v013対象外:

- チップバージョン読み取り
- エラー情報読み取り
- Stage 1 read-only
- 書き込み系
- FLASH
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- タグメモリ操作
- Lock / Kill / Encode / ThroughCmd

対象外は仕様上禁止ではなく、v013の実行対象外である。

## 3. Frame adapter summary

- Common frame source:
  - PDF Ver.1.17 Chapter 5 common communication frame
- SUM calculation:
  - Lower one byte of byte-wise sum from STX through ETX
- ROM read command:
  - 4Fh / 90h
- ROM read source:
  - PDF Ver.1.17 section 7.3.8
- ACK/NACK source:
  - ACK: PDF Ver.1.17 section 7.3.8
  - NACK: PDF Ver.1.17 section 7.6
- Send frame implementation:
  - `tools/stage01_readonly_verify.py`
- Completed Hex in docs:
  - not included
- SUM-calculated command example in docs:
  - not included

## 4. Execution environment

- repository commit: 9e82dad
- package base: v012 Stage 0 read-only real-device result
- tool: `tools/stage01_readonly_verify.py`
- connection_type: USB serial
- port: COMx
- baudrate: 115200
- timeout_ms: 1000
- execution date/time: 2026-07-13 10:48:16 JST
- operator: masked

## 5. ROM read result

- actual_response_type: ACK
- ROM version: 2.052
- ROM raw: 2052
- series name: USM02
- product type: UTR-SUN02-4CH
- elapsed_ms: 13
- result_status: REAL_DEVICE_PASS_WITH_NOTES
- notes:
  - ROMバージョン読み取りは完了した。
  - 生レスポンスはruntime CSVにのみ保存し、この文書には記載しない。

## 6. Non-executed Stage 0 commands

- チップバージョン読み取り:
  - NOT_EXECUTED_IN_V013
- エラー情報読み取り:
  - NOT_EXECUTED_IN_V013

## 7. Runtime log files

Runtime files were saved under `runtime_logs/stage01_readonly/` and are not committed.

- `stage01_readonly_20260713_104816_COMx_log.csv`
- `stage01_readonly_20260713_104816_COMx_result.md`

## 8. Result decision

V013_STAGE0_ROM_READ_REAL_DEVICE_PASS_WITH_NOTES

## 9. Next action

- Stage 0のチップバージョン読み取り・エラー情報読み取りへ進む。
- Stage 1 read-onlyへ進む前にROM判定結果を確認する。
- Runtime logs remain outside Git.

## 10. v014 follow-up

v014 proceeds to the remaining Stage 0 read-only commands and records the masked result in:

- `docs/current/26_STAGE0_REMAINING_READONLY_RESULT.md`

This does not rewrite the v013 result. v013 remains the ROM read frame adapter result; v014 records the follow-up Stage 0 remaining read-only verification.
