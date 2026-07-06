# UTR-S201 AI v005 Full Command Internal Release

## 1. 位置づけ

- 社内向け全コマンド棚卸し版
- no-PDF package
- 正式RCではない
- 顧客提供版ではない
- 本番利用可能版ではない
- 全コマンド実機送信確認済み版ではない

## 2. 成果物

ZIP名:

```text
utr_s201_ai_v005_full_command_internal_release_no_pdf.zip
```

## 3. 含める内容

- README.md
- docs/OPERATIONS.md
- R8-1 pre-RC checklist
- R8-2 release readiness documents
- R8-3 real-device test plan/result
- R8-3B safe command selection
- R8-3C safe real-device check result
- R8-4 internal pre-RC release decision
- R8-7 command coverage audit
- R8-7 all-command catalog draft
- R8-7 command gap list
- R8-8A real-device command send check result

## 4. 実機確認状況

確認済み:

- UTR-SUN02-4CH
- USB / COM6 / 115200bps
- ROM: 2052USM02
- FW: 2.052
- open / close / reopen
- ROM/status reads
- Inventory 1回
- タグ応答1件

HOLD:

- UHF_Read standalone
- 全38コマンドの個別実機送信確認
- PDF原本との全件再照合
- traceability不足項目の補完

## 5. 安全上の注記

以下は含めない。

- PDF原本
- 完成Hex
- SUM計算済みコマンド
- 実機送信用コード
- 顧客情報
- タグ固有IDの未マスク値

以下は実施していない。

- FLASH書き込み
- 周波数変更
- 送信出力変更
- UHF_SetInventoryParam自動送信
- 8CHアンテナ自動切替
- 永続設定変更
