# rag_chunks

`rag_chunks/` は、RAGチャンク生成などの補助的生成物を置くための作業用ディレクトリです。公開RAGサービスの本番インデックスではありません。

主たる公開知識ソースは `docs/current/` 配下の文書群と原典PDFです。AIコーディングエージェントやAIレビュー支援は、まず `README.md` と `docs/current/AI_CONTEXT_INDEX.md` を確認し、必要なコマンドカードと関連文書を直接参照してください。

このディレクトリ配下の生成物自体は、原則としてコミット対象外です。runtime logs、実CSVログ、顧客情報、実IPアドレス、実機ログ由来のraw EPC / UII / TID、認証情報、パスワードを含めないでください。

詳細な公開方針とデータ取り扱いは、`../DATA_HANDLING.md` と `../README.md` を参照してください。
