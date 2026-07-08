# R9-6 v006 Package Validation

## 1. 結論

判定:

`R9-6_V006_PACKAGE_VALIDATED_WITH_HOLD_NOTES`

R9-5で作成した v006 External Review Candidate no-PDF package を検証し、SHA256、MANIFEST記載値、ZIP内容、除外条件、README/MANIFESTの位置づけとHOLD事項を確認した。R9-7 GitHub pre-release 作成へ、HOLD事項付きで進めてよい。

## 2. 検証対象

- ZIP名: `utr_s201_ai_v006_external_review_candidate_no_pdf.zip`
- ZIPパス: `artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip`
- 期待SHA256: `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA`
- MANIFEST記載SHA256: `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA`
- README: `artifacts/utr_s201_ai_v006/README.md`
- MANIFEST: `artifacts/utr_s201_ai_v006/MANIFEST.md`

## 3. SHA256確認

- 期待SHA256: `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA`
- 実測SHA256: `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA`
- MANIFEST記載SHA256: `A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA`
- 判定: PASS

## 4. ZIP内容確認結果

| No | 確認項目 | 期待結果 | 実結果 | 判定 | 備考 |
|---:|---|---|---|---|---|
| 1 | ZIP存在 | 対象ZIPが存在する | 存在確認済み | PASS | R9-5成果物 |
| 2 | `README.md` | 含まれている | 含まれている | PASS | ルートREADME |
| 3 | `docs/OPERATIONS.md` | 含まれている | 含まれている | PASS | 運用文書 |
| 4 | `docs/policy/` | 含まれている | 含まれている | PASS | R9-0 |
| 5 | `docs/use_cases/` | 含まれている | 含まれている | PASS | R9-1 |
| 6 | `docs/implementation/` | 含まれている | 含まれている | PASS | R9-2 |
| 7 | `docs/ai_ready/` | 含まれている | 含まれている | PASS | R9-0/R9-2/R9-4 |
| 8 | `docs/commands/` | 含まれている | 含まれている | PASS | R8-7/R9-3 |
| 9 | `docs/commands/cards/` | 含まれている | 含まれている | PASS | R9-3カード/インデックス |
| 10 | `docs/release/` | 含まれている | 含まれている | PASS | R8/R9リリース文書 |
| 11 | `docs/release/R9-4_EXTERNAL_REVIEW_DECISION.md` | 含まれている | 含まれている | PASS | R9-5進行判断 |
| 12 | `artifacts/utr_s201_ai_v006/README.md` | 含まれている | 含まれている | PASS | v006 README |
| 13 | `artifacts/utr_s201_ai_v006/MANIFEST.md` | 含まれている | 含まれている | PASS | v006 MANIFEST |

## 5. 除外確認結果

以下はZIP展開先で該当なしを確認した。

- PDF
- 既存ZIP
- v006 ZIP自身
- `.git`
- `.github`
- `venv`
- `.venv`
- `__pycache__`
- `.pytest_cache`
- `node_modules`
- `.log`
- `.csv`
- 完成Hex
- SUM計算済みコマンド
- 実機送信用コード
- 顧客情報
- タグ固有ID
- 実IPアドレス

## 6. README / MANIFEST確認結果

- no-PDF packageである: PASS
- External Review Candidateである: PASS
- 日本国内向けである: PASS
- 日本語利用者向けである: PASS
- 日本の電波法準拠機器向けである: PASS
- 正式社外公開版ではない: PASS
- 正式RCではない: PASS
- 顧客提供版ではない: PASS
- 本番利用保証版ではない: PASS
- PDF正本の代替ではない: PASS
- 海外販売・海外運用向けではない: PASS
- HOLD事項が記載されている: PASS

## 7. 安全確認

- 実機送信なし
- 実コード追加なし
- 完成Hexなし
- SUM計算済みコマンドなし
- 実機送信用コードなし
- PDF追加なし
- 既存ZIP変更なし
- Release/tag変更なし

## 8. HOLD事項

- 正式社外公開は社内承認待ち
- PDF原本との全件再照合
- traceability不足項目の補完
- ライセンス/IP方針の最終確定
- UHF_Read standalone
- 全38コマンドの個別実機送信確認
- Level 4以上の実機操作
- Level 5操作
- 海外利用・海外販売

## 9. 判定

`R9-6_V006_PACKAGE_VALIDATED_WITH_HOLD_NOTES`

## 10. 次工程

R9-7:
v006 External Review Candidate GitHub pre-release を作成する。
