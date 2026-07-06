# R8-3B Safe Command Selection

## 1. 目的

R8-3でHOLDとなった読み取り系確認とInventory系確認を、安全に進めるための送信対象選定メモである。

この文書は調査・整理・文書化のみを目的とし、実機へのコマンド送信、完成Hex生成、SUM計算済みコマンド生成、実機送信用コード生成は行わない。

## 2. 現在の確認済み事項

- 対象機器: UTR-SUN02-4CH
- 接続方式: USB
- 接続情報: COM6 / 115200bps
- open PASS
- close PASS
- reopen PASS
- 送信なしReadTimeout PASS
- ログ記録 PASS
- 読み取り系 HOLD
- Inventory系 HOLD

## 3. 送信候補の分類表

| No | 分類 | 候補 | 目的 | 実機影響 | 安全条件 | 判定 | 備考 |
|---:|---|---|---|---|---|---|---|
| 1 | 接続確認 | COM6 / 115200bps open | 通信ポートを開けることの確認 | 実機への送信なし | DTR/RTS無効、送信なし、短時間でclose | CANDIDATE | R8-3でPASS済み |
| 2 | 切断確認 | close | 通信ポートを閉じられることの確認 | 実機への送信なし | open後に確実にcloseする | CANDIDATE | R8-3でPASS済み |
| 3 | 送信なしReadTimeout | ReadTimeoutのみ | 送信なしでタイムアウト処理を確認 | 実機への送信なし | 短いtimeout、例外を捕捉、終了後close | CANDIDATE | R8-3でPASS済み |
| 4 | ステータス取得系 | 状態取得コマンド候補 | 機器状態を非破壊に確認 | 仕様未確認のため不明 | 仕様で読み取り専用・非永続・電波条件非変更と確認できること | NEEDS_SPEC_CONFIRMATION | 次回前に仕様根拠を確認する |
| 5 | 読み取り専用に近い確認 | UHF_Read相当の読み取り系候補 | タグまたはメモリ読み取りの基本挙動確認 | タグアクセスまたは電波送信を伴う可能性 | 対象タグ、アンテナ、既存設定、読み取り範囲、非書き込み性を確認すること | NEEDS_SPEC_CONFIRMATION | 55h/15h = UHF_Read の対応は維持。実行可否は別途確認 |
| 6 | Inventory系確認 | UHF_InventoryRead相当のInventory候補 | タグ検出の基本挙動確認 | 電波送信を伴う可能性 | 既存設定の範囲、地域設定確認、アンテナ固定、出力変更なし | NEEDS_SPEC_CONFIRMATION | 55h/14h = UHF_InventoryRead の対応は維持。実行可否は別途確認 |
| 7 | UHF_SetInventoryParam | Inventory設定変更系 | Inventory条件の設定 | 設定変更の可能性 | 次回実機確認では自動送信しない | PROHIBITED | 禁止対象として扱う |
| 8 | FLASH書き込み | FLASH書き込み系 | 永続領域への書き込み | 永続設定変更 | 実施しない | PROHIBITED | 禁止対象として扱う |
| 9 | 周波数変更 | 周波数設定系 | 周波数または地域設定に関わる変更 | 電波法・地域設定に影響する可能性 | 実施しない | PROHIBITED | 禁止対象として扱う |
| 10 | 送信出力変更 | 出力設定系 | 送信出力の変更 | 電波出力に影響 | 実施しない | PROHIBITED | 禁止対象として扱う |
| 11 | 8CHアンテナ自動切替 | アンテナ自動切替系 | 複数アンテナ切替確認 | アンテナ経路と電波送信条件に影響 | 実施しない | PROHIBITED | 禁止対象として扱う |

## 4. 次回実機確認で守る条件

- FLASH書き込みなし
- 周波数変更なし
- 送信出力変更なし
- UHF_SetInventoryParam自動送信なし
- 8CHアンテナ自動切替なし
- 永続設定変更なし
- 既存設定の範囲で実施
- 不明なレスポンスが出たら即HOLD
- ログを保存
- 実IP、顧客名、タグ情報はマスク

## 5. 次工程

次工程は R8-3C とする。

R8-3Cでは、R8-3Bで CANDIDATE とした範囲だけ実機確認する。
