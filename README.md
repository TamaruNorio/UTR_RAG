# UTR_RAG

## 1. 目的

このリポジトリは、タカヤ製 UTR-S201 シリーズに関する、仕様・安全ルール・根拠資料・RAGパッケージ成果物を管理するための保管庫です。

API実装リポジトリではありません。実機送信用コード、完成Hex、SUM計算済みコマンドの配布を目的としません。

## 2. 現在の最終整理版

現在の最終整理版は v007 です。

- v007 ZIP: `artifacts/utr_s201_ai_v007/utr_s201_ai_v007_final_minimal_no_pdf.zip`
- v007 SHA256: `3DE8BEAD99BFE25DC30F1EFF85ADB354B3F4AB3322E6F37E75D268F62037BD62`
- docs入口: `docs/README.md`

v007は、v006 External Review Candidate の後続として、不要な作業履歴文書を除外し、必要最小限の最新版ドキュメントに整理した final minimal no-PDF package です。

## 3. v006 Release

v006はRelease済みのExternal Review Candidateです。v006 ZIP、Release、tag、assetは変更しません。

Release URL:

https://github.com/TamaruNorio/UTR_RAG/releases/tag/utr-s201-ai-v006-r9-7-external-review-candidate.1

v006 ZIP:

`artifacts/utr_s201_ai_v006/utr_s201_ai_v006_external_review_candidate_no_pdf.zip`

v006 SHA256:

`A68486F7DCD2EA932D0C6DA63C9AE282A8751BEB03CD6A33F6AB4463BC3333CA`

## 4. 成果物の扱い

- v004/v005/v006は削除しない
- v004/v005は履歴保持用
- v006はRelease済みExternal Review Candidate
- v007は最終整理版
- 次に更新する場合は、既存ZIPを上書きせず新versionを作る

成果物一覧は `artifacts/README.md` を参照してください。

## 5. 位置づけ

- 日本国内向け
- 日本語利用者向け
- 日本の電波法準拠機器向け
- 正式社外公開版ではない
- 正式RCではない
- 顧客提供版ではない
- 本番利用保証版ではない
- PDF正本の代替ではない
- 海外販売・海外運用向けではない
- HOLD事項付き

## 6. 安全上の注意

- PDF原本は同梱しません
- 完成Hexは含めません
- SUM計算済みコマンドは含めません
- 実機送信用コードは含めません
- Level 4以上は明示確認が必要です
- Level 5は明示承認と復旧手順がない場合HOLDです
- UHF_Read standalone はHOLDです
- 全38コマンドの個別実機送信確認は未完了です

## 7. 運用方針

- mainブランチを直接変更しない
- 作業ごとに feature ブランチを作成する
- Release済みZIPは削除・上書き・再作成しない
- ZIPを更新する場合は新versionを作成する
- 実機確認が必要な内容は、机上確認だけで完了扱いにしない
