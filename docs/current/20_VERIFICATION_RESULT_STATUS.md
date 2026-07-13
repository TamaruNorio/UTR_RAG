# Verification Result Status

## 1. Positioning

v010では、実機確認結果を同じ語彙で記録するためのstatusを定義する。

BLOCKEDは「仕様上禁止」ではない。対象機器、ROM、パラメータ、現場条件、復旧方法が未確定で、その条件下では実行できないという意味で使う。

## 2. Status definitions

| Status | Meaning | Use condition | Next action |
| --- | --- | --- | --- |
| NOT_TESTED | まだ実機確認も机上確認も結果登録していない。 | 初期登録時。 | 机上確認またはtraceability確認へ進む。 |
| DESK_REVIEWED | 文書上の机上確認が完了している。 | PDF節、カード、関連文書を確認済み。 | AI_TRACE_REVIEWEDまたは実機準備へ進む。 |
| AI_TRACE_REVIEWED | ChatGPT AI specification reviewとtraceability確認が完了している。 | v009/v010のカードとtraceability indexがある。 | 実機条件を確認する。 |
| READY_FOR_REAL_DEVICE_TEST | 実機確認に必要な前提が揃っている。 | 対象機器、ROM、パラメータ、ログ、復旧観点が明確。 | 実機確認計画に従って実施する。 |
| REAL_DEVICE_PASS | 期待通りに実機確認が完了した。 | ACK/応答/ログが期待通り。 | 結果を記録し次stageへ進む。 |
| REAL_DEVICE_PASS_WITH_NOTES | 実機確認は通ったが注記がある。 | timeout差、環境依存、復旧手順などの注記がある。 | 注記付きで結果を記録する。 |
| REAL_DEVICE_FAIL | 期待結果と異なる実機結果になった。 | NACK、timeout、無応答、異常応答など。 | ログを保存し原因調査する。 |
| NEEDS_RETEST | 再試験が必要。 | 条件不足、ログ不足、再現確認が必要。 | 条件を補って再実施する。 |
| BLOCKED_BY_DEVICE_OR_ROM | 対象機器またはROM条件が未確定または非該当。 | ROM/series/support tableの確認が不足。 | ROM読み取りと対応表確認を行う。 |
| BLOCKED_BY_PARAMETER | 必要パラメータが未確定。 | 設定値、タグメモリ、アドレス、長さ等が不足。 | ユーザーまたは現場条件から補完する。 |
| BLOCKED_BY_SITE_CONDITION | 現場条件が未確定。 | アンテナ、タグ、RF環境、顧客環境が不足。 | 現場条件を記録する。 |
| BLOCKED_BY_RECOVERY_PLAN | 復旧方法または戻し手順が未確定。 | FLASH、永続設定、Lock/Kill等。 | 復旧手順と承認条件を確定する。 |
| NOT_APPLICABLE_TO_TARGET | 対象機種/ROMでは確認対象外。 | 仕様上の対応外や構成非該当。 | 理由と根拠を記録する。 |

## 3. Recording rules

- 実機送信済みでないものをREAL_DEVICE_PASSとしない。
- Timeout and no-response must not be recorded as NACK.
- Multiple responses and completion responses must be recorded separately.
- Protocol-defined commands remain usable unless target device/ROM applicability says otherwise.

## 4. v011 Stage 0/1 status usage

v011 Stage 0/1では、以下のstatusを主に使う。

- READY_FOR_REAL_DEVICE_TEST
- REAL_DEVICE_PASS
- REAL_DEVICE_PASS_WITH_NOTES
- REAL_DEVICE_FAIL
- NEEDS_RETEST
- BLOCKED_BY_DEVICE_OR_ROM
- BLOCKED_BY_PARAMETER
- NOT_APPLICABLE_TO_TARGET

## 5. v012 Stage 0 result summary reference

v012 Stage 0 read-only real-device result summary:

- docs/current/24_STAGE0_READONLY_REAL_DEVICE_RESULT.md

The v012 attempt did not record REAL_DEVICE_PASS. Runtime logs are not committed.
