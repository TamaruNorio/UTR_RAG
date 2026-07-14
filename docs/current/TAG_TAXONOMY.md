# タグ分類

## 目的

AI検索や文書整理で使うタグを分類します。タグ名は機械処理用に英数字を含みますが、意味は日本語で管理します。

## 分類

| 分類 | 例 | 意味 |
| --- | --- | --- |
| 対象範囲 | `utr-s201` | UTR-S201シリーズ関連 |
| 文書種別 | `command-card`, `guide`, `result-summary` | 文書の種類 |
| コマンド分類 | `reader-control`, `reader-setting`, `rf-tag` | コマンドの大分類 |
| 確認区分 | `read-only`, `rf-read`, `write-operation`, `high-impact` | 実機確認時の操作影響 |
| 影響分類 | `read-only`, `setting-change`, `tag-memory`, `high-impact` | 操作の影響範囲 |

## 注意

タグは検索補助です。タグだけで実機送信可否を判断せず、公式PDF、対象機種、ROM、地域条件、現場条件を確認してください。
