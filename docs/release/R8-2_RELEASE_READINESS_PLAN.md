# R8-2 Release Readiness Plan

## 目的

この文書は、R7-5A成果物を社内pre-RCまたはRC候補として判断するための準備計画です。

R8-2では、リリース判断に必要な確認項目、最短工程、安全上の前提を整理します。実機確認そのものはこの変更では実施しません。

## 現在の成果物

- 成果物ZIP名: `utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip`
- 成果物パス: `artifacts/utr_s201_ai_v004/utr_s201_ai_v004_r7_5a_frontmatter_notes_cleanup_no_pdf.zip`
- SHA256: `2103B818045608383FD94F0047B471D4B2E3A3610BC8E46EAA644DF29F738521`
- no-PDF package
- 正式RCではない
- 実機確認未実施

## リリースまでの最短工程

1. R8-2 リリース準備文書作成
2. R8-3 実機確認
3. R8-4 実機確認結果の反映
4. R8-5 RC候補または社内pre-RCリリース判断

## リリース判定条件

- GitHub mainに成果物ZIPが登録済み
- SHA256一致
- PDF混入なし
- README参照あり
- OPERATIONSあり
- pre-RCチェックリストあり
- 実機確認ログあり
- 実機確認で重大問題なし
- 安全禁止事項に抵触していない
- 正式RCにする場合は、別途明示判断が必要

## 安全上の注意

- 実機確認までは正式RCではない
- 実機確認は未実施または別記録扱い
- 完成Hex、SUM計算済みコマンド、実機送信用コードは生成しない
- PDFはGitHubに追加しない
- 永続設定変更はしない
- 電波法・地域設定に影響する変更はしない
