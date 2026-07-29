# メタデータ項目定義

## 目的

AI検索や文書整理に使うfrontmatter項目を定義します。`doc_type` などのキー名は機械処理用のため英語のまま使います。本文説明は日本語で記載します。

この定義は、RAG登録時に壊れたメタデータが混入することを防ぐための最小ルールです。既存文書の現物を尊重し、初期段階では過度に厳しい値チェックは行いません。

## 書式ルール

Markdownファイルの先頭にYAML frontmatterを置きます。空配列は `related_docs: []` のように記載します。`N/A` は必要に応じて引用符で囲みます。GitHub画面でYAMLエラーが出ないことを確認します。

## command_card の必須項目

`docs/current/commands/cards/` 配下で `doc_type: "command_card"` として扱うファイルは、最低限以下のキーを持つ必要があります。

| キー | 意味 |
| --- | --- |
| title | 文書タイトル |
| doc_type | 文書種別。コマンドカードでは `command_card` |
| package_scope | 対象範囲 |
| manual | 参照する公式文書番号 |
| manual_version | 公式文書バージョン |
| pdf_section | PDF上の節番号 |
| command_group | コマンド分類 |
| command_name | コマンド名 |
| command_byte | コマンドバイト |
| operation_profile | 実機確認時の操作影響区分 |
| operation_level | 操作レベル |
| rf_emission | RF送信有無 |
| write_operation | 書き込み操作有無 |
| flash_operation | FLASH操作有無 |
| tag_memory_operation | タグメモリ操作有無 |
| requires_rom_check | ROM確認要否 |
| requires_antenna | アンテナ要否 |
| requires_tag | タグ要否 |
| requires_access_password | Accessパスワード要否 |
| requires_parameters | パラメータ確認要否 |
| verification_status | 確認状態 |
| result_status | 結果状態 |
| related_docs | 関連文書 |
| tags | 検索用タグ |

## command_card の条件付き必須項目

| キー | 条件 |
| --- | --- |
| detail_command | 詳細コマンドが存在するコマンドでは値を入れる。存在しない場合は `null` |
| subcommand | サブコマンドが存在するコマンドでは値を入れる。存在しない場合は `null` |

`detail_command` と `subcommand` は、キー自体は常に持たせ、値がない場合は `null` とします。これにより、RAG登録時に「未記載」と「仕様上なし」を区別しやすくします。

## 任意項目

以下は文書種別や用途に応じて使用します。初期バリデータでは必須扱いしません。

| キー | 意味 |
| --- | --- |
| related_commands | 関連コマンド |
| source_pdf_pages | 参照ページ |
| notes | 補足 |
| owner | 管理者 |
| updated_at | 更新日 |

## 初期バリデーション方針

`scripts/validate_frontmatter.py` は、まず `docs/current/commands/cards/` 配下の `command_card` を対象に、必須キーの存在、`related_docs` と `tags` が配列であること、主要な真偽値項目がboolであることを確認します。

仕様値の正誤、コマンドの意味、ACK/NACK定義、本文内容はこのバリデータでは判定しません。これらは公式PDFとレビューで確認します。
