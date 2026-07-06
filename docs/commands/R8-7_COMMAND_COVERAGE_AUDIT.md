# R8-7 Command Coverage Audit

## 1. 目的

UTR-S201関連コマンドについて、既存RAG成果物・安全分類・根拠参照の網羅性を確認するための棚卸しである。

今回は調査・文書化のみを行い、実機送信、実装、完成Hex生成、SUM計算済みコマンド生成、実機送信用コード生成は行わない。

## 2. 調査対象

- UTR_RAG main
- R7-5A no-PDF ZIP
- README.md
- docs/OPERATIONS.md
- command_safety_matrix
- source_traceability_matrix
- rag/commands
- R8系リリース判断文書

調査時のZIP展開先:

```text
$env:TEMP\utr_rag_r8_7_audit
```

## 3. 調査結果サマリー

| 項目 | 件数 | 備考 |
|---|---:|---|
| 抽出したコマンド総数 | 38 | command_safety_matrix の commands を基準 |
| RAG文書あり | 36 | canonical RAG pathが存在するもの |
| safety matrixあり | 38 | command_safety_matrixに存在 |
| source traceabilityあり | 33 | command trace itemとして存在。CHECKSUM_SUMはframe_ruleのため除外 |
| PDF参照あり | 33 | source_traceability_matrixにPDF参照があるcommand |
| 安全分類不足 | 0 | safety matrix基準では全38件にrisk_levelあり |
| 根拠参照不足 | 5 | trace item不足 |
| 名称または番号の矛盾 | 0 | 55h/14hと55h/15hの既知誤り復活なし |
| GAPあり | 6 | trace不足5件、canonical RAG path不足2件の重複を統合 |
| PROHIBITED | 16 | critical相当として実行・生成禁止扱い |
| HOLD | 6 | GAPあり、または全網羅未確認によりHOLD |
| NEEDS_SPEC_CONFIRMATION | 5 | source traceability不足コマンド |

## 4. 重要確認結果

- 55h/14h = UHF_InventoryRead: source_traceability_matrixとcommand_safety_matrixで確認済み
- 55h/15h = UHF_Read: source_traceability_matrixとcommand_safety_matrixで確認済み
- rag/commands/55_14_uhf_read.md: 存在しない
- UHF_SetInventoryParam: high risk、automatic_send_allowed=false、実機送信候補にしない
- FLASH書き込み系: critical、実行・生成禁止扱い
- 周波数変更系: critical、実行・生成禁止扱い
- 送信出力変更系: critical、実行・生成禁止扱い

## 5. 判定

`R8-7_COMMAND_COVERAGE_AUDIT_HOLD`

理由:

- command_safety_matrix上の全38コマンドは抽出できた
- ただし、source_traceability_matrixに存在しないコマンドが5件ある
- canonical RAG pathが未登録または未検出のコマンドが2件ある
- PDF原本を同梱しない前提のため、全コマンド網羅性の最終確認は未完了

## 6. 次工程

R8-8:
不足コマンド、未分類コマンド、根拠不足コマンドをどう補うかを決める。

ただし、危険系コマンドは実機送信・実装対象にしない。
