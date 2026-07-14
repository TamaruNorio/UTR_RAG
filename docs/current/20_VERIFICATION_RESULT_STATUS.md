# 実機確認結果ステータス

## 目的

実機確認結果を同じ言葉で記録するためのステータス定義です。

## ステータス

| ステータス | 意味 |
| --- | --- |
| READY_FOR_REAL_DEVICE_TEST | 実機確認候補。まだ送信していない |
| REAL_DEVICE_PASS | 実機で期待通りの結果を確認した |
| REAL_DEVICE_PASS_WITH_NOTES | 実機で確認したが補足条件がある |
| REAL_DEVICE_FAIL | 期待と異なる結果を確認した |
| NEEDS_RETEST | 再確認が必要 |
| BLOCKED_BY_DEVICE_OR_ROM | 対象機種またはROM条件で進められない |
| BLOCKED_BY_PARAMETER | 必要パラメータが未確定 |
| NOT_APPLICABLE_TO_TARGET | 対象機種・用途では該当しない |

## 運用

実機未確認を確認済みとして扱わないでください。結果は事実ベースで記録します。
