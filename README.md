# UTR_RAG

## 目的

このリポジトリは、タカヤ製 UTR-S201 シリーズに関する、仕様・安全ルール・根拠資料・RAGパッケージ成果物を管理するための保管庫です。

このリポジトリは、実機制御プログラム本体ではありません。

## 現在の収録物

- UTR-S201 AI補助パッケージ v004
- R7-5A front matter notes cleanup
- no-PDF package
- pre-RC候補
- 実機確認未実施
- 正式RCではない
- R8-1 pre-RC 社内共有用チェックリスト
- R8-2 リリース準備文書
- R8-3 実機確認計画

## 成果物

現在の成果物は以下です。

```text
artifacts/utr_s201_ai_v004/utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip
```

SHA256:

```text
2103B818045608383FD94F0047B471D4B2E3A3610BC8E46EAA644DF29F738521
```

## チェックリスト

R8-1 pre-RC 社内共有用チェックリスト:

```text
docs/R8-1_PRE_RC_INTERNAL_SHARE_CHECKLIST.md
```

R8-2 / R8-3 リリース準備文書:

```text
docs/release/R8-2_RELEASE_READINESS_PLAN.md
docs/release/R8-2_RELEASE_DECISION_TABLE.md
docs/real_device/R8-3_REAL_DEVICE_TEST_PLAN.md
docs/real_device/results/R8-3_REAL_DEVICE_TEST_RESULT.md
docs/real_device/R8-3B_SAFE_COMMAND_SELECTION.md
docs/real_device/results/R8-3C_SAFE_REAL_DEVICE_CHECK_RESULT.md
```

## 安全上の注意

- 本リポジトリの内容は、実機確認済みではありません
- 正式RCではありません
- 完成Hex、SUM計算済みコマンド、実機送信用コードの生成を目的としません
- PDF原本は同梱しません
- 実機制御、永続設定変更、送信出力変更、周波数変更、FLASH書き込みは別途明示許可と実機確認が必要です

## 運用方針

- mainブランチを直接変更しない
- 作業ごとに feature ブランチを作成する
- 変更前に git status を確認する
- 変更後に git diff / git diff --check を確認する
- push前に内容をレビューする
- 実機確認が必要な内容は、机上確認だけで完了扱いにしない

## 将来構想

- コマンド仕様の構造化
- safety matrix / source traceability matrix の拡張
- 将来的な UTR Gateway / OpenAPI draft の検討
- ただし現時点では API実装リポジトリではない
