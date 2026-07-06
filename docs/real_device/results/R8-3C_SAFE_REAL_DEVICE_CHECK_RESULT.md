# R8-3C Safe Real-Device Check Result

## 1. 結論

判定: `R8-3C_PASS_WITH_NOTES`

R8-3Bで `CANDIDATE` とされた範囲だけを実施し、COM6 / 115200bpsでの open、close、reopen、送信なしReadTimeout を確認した。

読み取り系確認、Inventory系確認、ステータス取得系確認は `NEEDS_SPEC_CONFIRMATION` のため実施していない。

## 2. 実機情報

- 対象機器: UTR-SUN02-4CH
- 接続方式: USB
- 接続情報: COM6 / 115200bps
- アンテナ構成: 未確認
- 使用タグ: 未使用
- 実施者: Codex記録担当
- 実施日時: 2026-07-06 JST
- 実施場所: 未確認

実IP、顧客名、認証情報、タグの機密情報は記録していない。

## 3. R8-3B CANDIDATE確認

| No | 候補 | R8-3B判定 | 今回実施可否 | 理由 | 備考 |
|---:|---|---|---|---|---|
| 1 | COM6 / 115200bps open | CANDIDATE | 実施 | 実機への送信なしで確認できるため | PASS |
| 2 | close | CANDIDATE | 実施 | 実機への送信なしで確認できるため | PASS |
| 3 | ReadTimeoutのみ | CANDIDATE | 実施 | 実機への送信なしで確認できるため | PASS |
| 4 | 状態取得コマンド候補 | NEEDS_SPEC_CONFIRMATION | 未実施 | R8-3BでCANDIDATEではないため | 仕様確認後に再判断 |
| 5 | UHF_Read相当の読み取り系候補 | NEEDS_SPEC_CONFIRMATION | 未実施 | R8-3BでCANDIDATEではないため | 読み取り系はHOLD継続 |
| 6 | UHF_InventoryRead相当のInventory候補 | NEEDS_SPEC_CONFIRMATION | 未実施 | R8-3BでCANDIDATEではないため | Inventory系はHOLD継続 |

## 4. 実行前安全レビュー

| No | 確認項目 | 結果 | 備考 |
|---:|---|---|---|
| 1 | FLASH書き込み処理がないこと | PASS | 使用手順はSerialPort open/read timeout/closeのみ |
| 2 | 周波数変更処理がないこと | PASS | 設定変更コマンド送信なし |
| 3 | 送信出力変更処理がないこと | PASS | 設定変更コマンド送信なし |
| 4 | UHF_SetInventoryParam自動送信がないこと | PASS | コマンド送信なし |
| 5 | 8CHアンテナ自動切替がないこと | PASS | アンテナ制御なし |
| 6 | 永続設定変更がないこと | PASS | 書き込み処理なし |
| 7 | 実行時に危険操作が自動で走らないこと | PASS | open、ReadByte timeout、closeのみ |
| 8 | COM6 / 115200bps を指定できること | PASS | COM6 / 115200bpsで実行 |
| 9 | ログを保存できること | PASS | 最小ログを本文に記録 |

使用した既存手順:

- PowerShell / .NET `System.IO.Ports.SerialPort`
- 既存のR8-3接続確認と同じ送信なし確認手順

実行コマンド:

```text
PowerShell SerialPort open / ReadTimeout / close / reopen check
```

## 5. 実機確認結果

| No | 実施日時 | シナリオ | 操作内容 | 期待結果 | 実結果 | 判定 | ログファイル | 備考 |
|---:|---|---|---|---|---|---|---|---|
| 1 | 2026-07-06 JST | R8-3C Candidate 1 | COM6 / 115200bps open | openできる | `open:success IsOpen=True` | PASS | 本文に記録 | 実機への送信なし、DTR/RTS無効 |
| 2 | 2026-07-06 JST | R8-3C Candidate 2 | close | closeできる | `close:success IsOpen=False` | PASS | 本文に記録 | 実機への送信なし |
| 3 | 2026-07-06 JST | R8-3C Candidate 2 | reopen / reclose | 再open後にcloseできる | `reopen:success IsOpen=True`、`reclose:success IsOpen=False` | PASS | 本文に記録 | 実機への送信なし |
| 4 | 2026-07-06 JST | R8-3C Candidate 3 | 送信なしReadTimeout | 異常終了せずtimeoutする | `read:timeout-ok-without-send` | PASS | 本文に記録 | コマンド送信なし |

## 6. ログ

```text
open:start
open:success IsOpen=True
bytes_to_read=0
read:timeout-ok-without-send
close:success IsOpen=False
reopen:success IsOpen=True
reclose:success IsOpen=False
```

## 7. 安全確認

- FLASH書き込みなし
- 周波数変更なし
- 送信出力変更なし
- UHF_SetInventoryParam自動送信なし
- 8CHアンテナ自動切替なし
- 永続設定変更なし
- PDF追加なし
- R7-5A ZIP変更なし
- 完成Hexの文書化なし
- SUM計算済みコマンドの文書化なし
- 実機送信用コードの新規作成なし

## 8. HOLD事項

- 読み取り系確認は未実施
- Inventory系確認は未実施
- ステータス取得系確認は未実施
- アンテナ構成は未確認
- 使用タグは未使用
- 実施場所は未確認
- 外部ログファイル保存は未実施
