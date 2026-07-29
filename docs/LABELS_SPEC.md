# Labels Spec

## 目的

この文書は、UTR_RAG 用のGitHub labelsを手動作成するための設計メモです。

labels自体はGitHub上で保守者が手動作成します。このリポジトリ内の文書は、作成すべきlabel名、用途、色、使い分けを記録するだけです。

## 方針

- GitHub default labels は残す前提にする
- default labels と役割が重なるlabelは増やしすぎない
- UTR_RAG 固有の分類、RAG運用、公開データ取扱、リリース運用を補う
- 機密情報、実機ログ、raw EPC / UII / TID を扱うIssueでは、`SECURITY.md` と `DATA_HANDLING.md` を確認する

## 作るlabel

| name | purpose | suggested color | when to use |
|---|---|---|---|
| `area:documentation` | README、運用文書、公開入口文書の整理 | `0075ca` | 仕様値そのものではなく、説明や導線を改善するIssue/PR |
| `area:command-card` | 個別コマンドカードに関する作業 | `5319e7` | コマンドカードの構造化、表現整理、参照導線の改善 |
| `area:metadata` | frontmatter、tags、related_docsの整備 | `c2e0c6` | RAG検索や索引で使うメタデータの追加、修正、検証 |
| `area:rag-pipeline` | RAGチャンク生成や検索品質に関する作業 | `0e8a16` | `scripts/build_rag_chunks.py`、`qa/golden_queries.yaml`、チャンク出力確認 |
| `area:qa` | レビュー観点、golden query、検証手順 | `fbca04` | 人間レビュー用の確認項目、回帰確認、QA観点の追加 |
| `area:security` | 脆弱性、安全ガード、公開Issueで扱えない懸念 | `b60205` | SECURITY.mdに関わる相談。機密情報の実値は公開Issueに貼らない |
| `area:data-handling` | 実機ログ、raw EPC / UII / TID、認証情報の扱い | `d93f0b` | DATA_HANDLING.mdに関わる相談や公開範囲の確認 |
| `status:needs-review` | 保守者レビュー待ち | `fbca04` | 仕様値、実機影響、公開範囲などの判断待ち |
| `status:blocked` | 外部条件や判断待ちで進められない状態 | `d93f0b` | PDF原本、実機確認、GitHub権限、方針判断が必要 |
| `release` | 公開版、リリース手順、release asset | `0052cc` | RELEASE_PROCESS.md、CHANGELOG_TEMPLATE.md、GitHub Releases関連 |

## 既定labelの扱い

GitHub default labels は削除前提にしません。次の既定labelは、そのまま使います。

| default label | 使い方 |
|---|---|
| `bug` | 明確な不具合、検証スクリプトの失敗、リンク破綻 |
| `enhancement` | 改善提案、将来の便利機能 |
| `question` | 判断が必要な質問、仕様確認 |
| `documentation` | 汎用的な文書修正。UTR_RAG固有分類が必要な場合は `area:documentation` を併用 |

## 作らなくてよいlabel

- 細かすぎるコマンド番号別label
- 個別ファイル名だけを表すlabel
- 実機ログや顧客情報を示すlabel
- 一時的な作業者名label

## 手動作成時の確認

GitHub上でlabelを作成する前に、次を確認してください。

- 名前がこの文書と一致していること
- 色が見分けやすいこと
- default labels と役割が重複しすぎていないこと
- security / data-handling 関連Issueで機密情報の貼り付けを促していないこと
