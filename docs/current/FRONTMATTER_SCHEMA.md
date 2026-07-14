# メタデータ項目定義

## 目的

AI検索や文書整理に使うメタデータ項目を定義します。`doc_type` などのキー名は機械処理用のため英語のまま使います。本文説明は日本語で記載します。

## 書式ルール

空配列は `related_docs: []` のように記載します。`N/A` は必要に応じて引用符で囲みます。GitHub画面でYAMLエラーが出ないことを確認します。

## 主な項目

| キー | 意味 |
| --- | --- |
| title | 文書タイトル |
| doc_type | 文書種別 |
| package_scope | 対象範囲 |
| manual | 参照する公式文書番号 |
| manual_version | 公式文書バージョン |
| verification_status | 確認状態 |
| result_status | 結果状態 |
| operation_profile | 実機確認時の操作影響区分 |
| related_docs | 関連文書 |
| tags | 検索用タグ |
