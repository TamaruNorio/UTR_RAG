# AI用コンテキスト索引

## 1. この文書の目的

この文書は、AIコーディングエージェントやAIレビュー支援が UTR_RAG を読むときの前提と参照順を整理する入口です。

詳細な公開範囲、保証しないこと、公式PDFの扱いは、まず `../../README.md` と `../../RELEASE_SCOPE.md` を確認してください。

## 2. このリポジトリが提供するもの

UTR_RAG は、タカヤ製 UTR-S201シリーズ通信プロトコルの理解、実装支援、レビュー、段階的な実機確認に使うMarkdown文書群を提供します。

主な公開知識は `docs/current/` 配下の文書と `docs/current/commands/cards/` 配下のコマンドカードです。コマンド一覧、ACK/NACK、レスポンス分類、アンテナ番号体系、ROM判定、実装時の安全確認を、AIが直接参照しやすい形に整理しています。

V100では、過去経緯ではなく、現在利用する文書とコマンドカードを中心に整理します。ACK/NACK、RFタグ応答、読取完了ACK、アンテナ切替完了ACK、キャリア検知ACKの実装入口は `RESPONSE_AND_NACK_MASTER.md` と `RESPONSE_CLASSIFICATION_MATRIX.md` を確認してください。

## 3. このリポジトリが提供しないもの

このリポジトリは、ベクトル検索APIや対話型RAGサービスそのものではありません。

以下はこのリポジトリの提供対象ではありません。

- 公開検索API
- ベクトル検索を前提にした本番インデックス
- 再ランキング処理
- 検索性能ベンチマーク
- 公式PDFの代替
- 実機送信の許可
- 完成Hexの無条件利用保証

AIは、検索APIを呼ぶ前提ではなく、`git clone` したMarkdown文書群を直接読み、対象コマンド、関連カード、補助文書を順に確認してください。

## 4. 想定する実運用

想定する主な使い方は、AIコーディングエージェントがこのリポジトリを直接読み、実装・レビュー・実機確認の補助に使う運用です。

標準的な流れは以下です。

1. README、公開範囲、利用ガイドを確認する。
2. 接続方式、対象機種、ROM、対象コマンド、実機送信の有無を確認する。
3. `COMMAND_MASTER_V117.md` で対象コマンドの位置づけを確認する。
4. 対象コマンドカードを開く。
5. コマンドカードの `related_docs` に列挙された文書を省略せず読む。
6. `RESPONSE_AND_NACK_MASTER.md` と `RESPONSE_CLASSIFICATION_MATRIX.md` でACK/NACK、複数レスポンス、非同期レスポンスを確認する。
7. 実装後、固定値やエラーコードを文書中の記述と照合する。

## 5. 参照順の基本方針

最初に読む文書は、`../../README.md` の「最初に読むもの」と「AI/Codexで実装する場合の推奨参照順」を正本として扱います。

実装時は、最低限以下を確認してください。

- `../../README.md`
- `../../RELEASE_SCOPE.md`
- `../../llms.txt`
- `V100_USAGE_GUIDE.md`
- `COMMAND_MASTER_V117.md`
- `RESPONSE_AND_NACK_MASTER.md`
- `RESPONSE_CLASSIFICATION_MATRIX.md`
- `commands/cards/TEST_STATUS_INDEX.md`

対象コマンドが決まっている場合は、`COMMAND_MASTER_V117.md` から該当するコマンドカードへ進み、そのカードの `related_docs` をすべて確認してください。

## 6. よくある誤解

| 誤解 | 正しい扱い |
|---|---|
| UTR_RAGは検索API型のRAGサービスである | UTR_RAGはMarkdown文書群を直接読むためのドキュメントリポジトリです |
| `rag_chunks/` が主知識である | 主たる公開知識は `docs/current/` 配下です。`rag_chunks/` は補助的生成物です |
| コマンドカード1枚だけ読めば実装できる | `related_docs`、ACK/NACK、レスポンス分類、機種・ROM条件を併せて確認します |
| PDF参照と書いてある箇所はAI実装で無視してよい | 公式PDFが一次情報です。RAG側に転記済みの固定値は文書内で照合し、未掲載値は未確認として扱います |
| タグ0枚はNACKで表せる | 正常系と異常系はPDFの応答区分に従って分けます |
| 自動読み取りモードのlistenログをコマンドモードの単発応答試験と同じ評価軸で読める | listenは受信専用の継続受信であり、command-responseの完了通知（completion）を伴わない前提で評価します |

## 7. レビュー前チェックリスト

AIレビューや外部レビューでは、再設計案を出す前に以下を確認してください。

- `../../README.md` で、このリポジトリの目的と「公式PDFの代替ではない」前提を確認したか。
- `FRONTMATTER_SCHEMA.md` で、frontmatterの形式と文書分類を確認したか。
- `COMMAND_MASTER_V117.md` で、対象コマンドの分類と参照導線を確認したか。
- `RESPONSE_AND_NACK_MASTER.md` で、ACK/NACK、エラーコード、設定依存レスポンスを確認したか。
- 対象コマンドカードの `related_docs` を省略せず読んだか。
- `rag_chunks/` を本番検索インデックスと誤認していないか。

## 8. 実装依頼時の最低確認事項

実装を依頼する場合は、少なくとも以下を明示してください。

- 対象機種
- ROMバージョン
- 接続方式
- 対象コマンド
- 必要パラメータ
- 実装言語
- timeout
- ログ方針
- 実機送信の有無
- 停止条件
- 復旧方法

不足がある場合は、完成Hexや実機送信用コードを作らず、確認リストを返してください。詳細は `PARAMETER_CONFIRMATION_GUIDE.md` と `AI_IMPLEMENTATION_GUARDRAILS.md` を確認してください。
