# Release Process

## 目的

この文書は、UTR_RAG の公開版を切る前に確認することと、変更点を記録する作法を整理します。

GitHub Releases の作成、tag push、release asset のアップロードは、この文書を確認したうえで保守者が実行します。

GitHubのAbout欄、branch protection、required checks などの管理設定は `docs/MAINTAINER_ADMIN_CHECKLIST.md` を確認してください。

## リリース前チェック

- `main` が最新であること
- 未コミット変更がないこと
- 対応する公式仕様書版が明記されていること
- 仕様値、コマンドカード本文、ACK/NACK、周波数、送信出力の変更有無を確認していること
- `git diff --check` が通っていること
- 必要な検証スクリプトを実行していること
- 生成物、実機ログ、認証情報、raw EPC / UII / TID が混入していないこと

## 対応する公式仕様書版の明記方法

リリース説明には、対象とする公式仕様書を明記します。

```text
対象仕様書: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17
manual: TDR-MNL-PRC-UTR-S201-117
```

公式PDFが一次情報です。リリース説明は公式PDFの代替ではありません。

## 変更点分類

変更点は、次の分類で整理します。

| 分類 | 内容 |
|---|---|
| Documentation | README、運用文書、説明文の改善 |
| Command Card | 個別コマンドカードの整理 |
| Metadata | frontmatter、tags、related_docs など |
| RAG Pipeline | チャンク生成、索引、検証ツール |
| QA | golden query、レビュー用確認項目 |
| Security / Data Handling | 機密情報、実機ログ、公開範囲に関する文書 |

仕様値に関わる変更は、分類とは別に「仕様値変更あり」と明記します。

## 既知制限の書き方

既知制限は、次の形で短く書きます。

```text
Known limitations:
- 公式PDF原本はGitHubに含めない。
- 実機確認状態は各カードの「9. 実機確認」と TEST_STATUS_INDEX.md を参照する。
- 完成HexやSUM計算済み送信用コマンド例を無条件に提供するものではない。
```

## 実機確認の扱い

実機確認済みと書く場合は、根拠となるカード、索引、結果文書を確認します。

全54コマンドを個別に実機送信済みである、という意味に読める表現は避けてください。実機送信の有無、対象機種、ROM、接続方式、確認範囲を分けて書きます。

## Release asset の方針

release asset に含める候補は、公開可能な生成物に限定します。

含めてよいもの:

- README、公開範囲、運用手順などの公開文書
- `docs/current` 配下のMarkdown
- RAG登録用に再生成可能な公開データ

含めないもの:

- 公式PDF原本
- 実機ログ、実CSVログ
- raw EPC / UII / TID
- 認証情報、パスワード、実IPアドレス
- 顧客情報や現場固有情報

release asset を作成する場合も、公開前に `SECURITY.md` と `DATA_HANDLING.md` を確認してください。
