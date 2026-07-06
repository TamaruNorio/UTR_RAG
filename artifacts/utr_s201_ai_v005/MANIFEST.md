# UTR-S201 AI v005 Full Command Internal Release Manifest

## 1. ZIP

```text
utr_s201_ai_v005_full_command_internal_release_no_pdf.zip
```

## 2. SHA256

```text
20F87EE55FC3B555EABE38BB3492CFEB303754E7539DAD8D0BC46BEBD7B29712
```

## 3. 作成日時

```text
2026-07-06 JST
```

## 4. 含めた主要ディレクトリとファイル

- `README.md`
- `docs/OPERATIONS.md`
- `docs/R8-1_PRE_RC_INTERNAL_SHARE_CHECKLIST.md`
- `docs/release/`
- `docs/real_device/`
- `docs/commands/`
- `artifacts/utr_s201_ai_v005/README.md`

## 5. 除外したもの

- `.git`
- PDF原本
- `venv`
- `__pycache__`
- 一時ファイル
- ログ全文
- タグ固有IDを含むファイル
- 顧客情報
- 実機送信用コード
- R7-5A ZIPそのもの

## 6. no-PDF

この成果物は no-PDF package であり、PDF原本を含まない。

## 7. リリース位置づけ

- 社内向け全コマンド棚卸し版
- 正式RCではない
- 顧客提供版ではない
- 本番利用可能版ではない
- 全コマンド実機送信確認済み版ではない

## 8. HOLD事項

- UHF_Read standalone
- 全38コマンドの個別実機送信確認
- PDF原本との全件再照合
- traceability不足項目の補完

## 9. 実機確認状況

確認済み:

- UTR-SUN02-4CH
- USB / COM6 / 115200bps
- ROM: 2052USM02
- FW: 2.052
- open / close / reopen
- ROM/status reads
- Inventory 1回
- タグ応答1件

未確認 / HOLD:

- UHF_Read standalone
- 全38コマンドの個別実機送信確認

## 10. R8-8A結果

R8-8A実機確認結果:

```text
docs/real_device/results/R8-8A_REAL_DEVICE_COMMAND_SEND_CHECK_RESULT.md
```

判定:

```text
R8-8A_REAL_DEVICE_COMMAND_SEND_CHECK_PASS_WITH_NOTES
```
