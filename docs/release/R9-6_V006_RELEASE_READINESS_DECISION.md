# R9-6 v006 Release Readiness Decision

## 1. 結論

判定:

`PROCEED_TO_R9-7_PRE_RELEASE_WITH_HOLD_NOTES`

R9-7で v006 External Review Candidate GitHub pre-release を作成してよい。ただし、正式社外公開版、正式RC、顧客提供版、本番利用保証版としては扱わない。

## 2. 進めてよい理由

- v006 ZIPが存在する
- SHA256が一致している
- no-PDFである
- 既存ZIPを含んでいない
- 完成Hexを含んでいない
- SUM計算済みコマンドを含んでいない
- 実機送信用コードを含んでいない
- README / MANIFEST が存在する
- HOLD事項が明記されている

## 3. まだ正式社外公開にしない理由

- 社内承認前
- PDF原本との全件再照合未完了
- traceability不足補完未完了
- ライセンス/IP方針未確定
- UHF_Read standalone HOLD
- 全38コマンドの個別実機送信確認未完了
- 海外利用・海外販売は対象外

## 4. R9-7 Releaseに添付してよいもの

- `artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip`

## 5. R9-7 Releaseに添付してはいけないもの

- PDF
- 既存ZIP
- 実機送信用コード
- 完成Hex
- SUM計算済みコマンド
- ログ全文
- CSVログ
- 顧客情報
- タグ固有ID
- 実IPアドレス

## 6. R9-7 Release本文に必ず書くこと

- External Review Candidate
- no-PDF
- 日本国内向け
- 日本語利用者向け
- 日本の電波法準拠機器向け
- 正式社外公開版ではない
- 正式RCではない
- 顧客提供版ではない
- 本番利用保証版ではない
- PDF正本の代替ではない
- 海外販売・海外運用向けではない
- HOLD事項あり
