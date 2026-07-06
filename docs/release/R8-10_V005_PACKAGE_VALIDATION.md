# R8-10 v005 Package Validation

## 1. 結論

判定:

`R8-10_V005_PACKAGE_VALIDATED_WITH_HOLD_NOTES`

v005 full-command internal no-PDF package を検証し、期待SHA256との一致、主要文書の含有、除外対象の未混入、no-PDFおよびHOLD事項の明記を確認した。

## 2. 検証対象

- ZIP名: `utr_s201_ai_v005_full_command_internal_release_no_pdf.zip`
- ZIPパス: `artifacts/utr_s201_ai_v005/utr_s201_ai_v005_full_command_internal_release_no_pdf.zip`
- SHA256: `20F87EE55FC3B555EABE38BB3492CFEB303754E7539DAD8D0BC46BEBD7B29712`
- MANIFEST: `artifacts/utr_s201_ai_v005/MANIFEST.md`
- README: `artifacts/utr_s201_ai_v005/README.md`

## 3. 検証結果

| No | 確認項目 | 期待結果 | 実結果 | 判定 | 備考 |
|---:|---|---|---|---|---|
| 1 | v005 README存在 | 存在する | 存在確認済み | PASS | `artifacts/utr_s201_ai_v005/README.md` |
| 2 | v005 MANIFEST存在 | 存在する | 存在確認済み | PASS | `artifacts/utr_s201_ai_v005/MANIFEST.md` |
| 3 | v005 ZIP存在 | 存在する | 存在確認済み | PASS | 対象ZIPを変更せず検証 |
| 4 | SHA256一致 | 期待SHA256と一致 | 一致 | PASS | `20F87EE55FC3B555EABE38BB3492CFEB303754E7539DAD8D0BC46BEBD7B29712` |
| 5 | ZIP展開 | リポジトリ外の一時フォルダへ展開できる | 展開成功 | PASS | `$env:TEMP\utr_rag_r8_10_v005_validation` |
| 6 | 主要文書含有 | README、OPERATIONS、release、real_device、commands、v005 READMEを含む | すべて確認済み | PASS | no-PDF package |
| 7 | 除外対象 | PDF、.git、venv、__pycache__、ZIP二重梱包、実機送信用コードなし | 混入なし | PASS | 拡張子およびディレクトリ名で確認 |
| 8 | 位置づけ明記 | 正式RCではない、顧客提供版ではない、本番利用可能版ではない | 明記確認済み | PASS | README/MANIFESTで確認 |
| 9 | HOLD事項明記 | UHF_Read standalone、全38コマンド個別実機送信確認、PDF原本全件再照合、traceability不足 | 明記確認済み | PASS | README/MANIFESTで確認 |

## 4. ZIP内容確認結果

含まれていた主要内容:

- `README.md`
- `docs/OPERATIONS.md`
- `docs/R8-1_PRE_RC_INTERNAL_SHARE_CHECKLIST.md`
- `docs/release/`
- `docs/real_device/`
- `docs/commands/`
- `artifacts/utr_s201_ai_v005/README.md`

除外確認結果:

- PDFなし
- `.git`なし
- `venv`なし
- `__pycache__`なし
- R7-5A ZIP二重梱包なし
- 実機送信用コードなし
- ログ全文なし
- CSVなし
- タグ固有IDや顧客情報を含む追加ファイルなし

## 5. 安全確認

- PDFなし
- R7-5A ZIP二重梱包なし
- 完成Hexなし
- SUM計算済みコマンドなし
- 実機送信用コードなし
- 顧客情報なし
- タグ固有IDなし
- GitHub Release変更なし
- 実機送信なし

## 6. HOLD事項

- UHF_Read standalone
- 全38コマンドの個別実機送信確認
- PDF原本との全件再照合
- traceability不足項目の補完

## 7. 次工程

R8-11:

v005 full-command internal no-PDF package を GitHub pre-release として作成する。

ただし、正式RC、顧客提供版、本番利用可能版とはしない。
