# Maintainer Admin Checklist

## 目的

この文書は、ローカルcommitやPR作成では変更できないGitHub上の管理項目を、保守者が手動で確認するためのチェックリストです。

この文書は手順の記録だけを扱います。GitHub Settings、branch protection、Releases を自動変更するものではありません。

## About欄

GitHubリポジトリ画面のAbout欄で、説明とtopicsを確認します。

推奨description:

```text
タカヤ製UTR-S201シリーズ（UHF帯RFIDリーダライタ）通信プロトコルを、生成AIとのペアプログラミング（バイブコーディング）で扱いやすくするためのAI向けドキュメント・RAGパイプライン
```

推奨topics:

- `rfid`
- `uhf`
- `rag`
- `ai-agent`
- `documentation`
- `takaya`
- `utr-s201`
- `vibe-coding`
- `llm`

## Branch protection

`main` ブランチに対して、次の設定を推奨します。

- Pull Request 経由の変更を必須にする
- force push を禁止する
- branch deletion を禁止する
- required reviews を有効にする
- required status checks を有効にする
- CODEOWNERS review requirement を有効にする場合は、`.github/CODEOWNERS` のownerと担当範囲を確認する

## Required reviews

推奨値:

- required approving reviews: `1` 以上
- stale review dismissal: 有効を推奨
- review from CODEOWNERS: CODEOWNERS設定後に有効化

仕様値、コマンドカード本文、RF安全、FLASH、周波数、送信出力に関わるPRは、通常の文書修正より慎重に確認します。

## Required status checks

required status checks は、実際にGitHub Actionsや検証ジョブが存在するものだけを指定します。

候補:

- Markdownリンク確認
- frontmatter検証
- RAGチャンク生成確認
- Pythonスクリプトの構文確認

存在しないチェック名をrequiredにするとPRをmergeできなくなるため、先にActions名と成功状態を確認してください。

`Documentation Validation / Validate documentation metadata and RAG build` をrequired status checksに指定する場合は、GitHub Actions上で実際に表示されるworkflow名とjob名を確認してから設定してください。

## CODEOWNERS review requirement

`.github/CODEOWNERS` は、実ownerとして `@TamaruNorio` を指定しています。

有効化前に確認すること:

- ownerに実在するGitHubユーザーを指定していること
- ownerがリポジトリへの適切な権限を持つこと
- README、`docs/current/`、`scripts/`、`.github/` の担当範囲が過不足ないこと

## Releases作成時の確認

GitHub Releaseを作成する前に、次を確認します。

- `RELEASE_PROCESS.md` を確認した
- `CHANGELOG_TEMPLATE.md` を使って変更点を整理した
- 対応する公式仕様書版を明記した
- 既知制限を書いた
- 実機確認の有無と範囲を書いた
- release asset に公式PDF原本、実機ログ、raw EPC / UII / TID、認証情報、実IPアドレスが含まれていない
- `SECURITY.md` と `DATA_HANDLING.md` の方針に反していない

## 手動作業後の記録

GitHub SettingsやReleaseを変更した場合は、PRまたはIssueに次を記録します。

- 変更日
- 変更者
- 変更した設定
- 変更理由
- 確認結果
