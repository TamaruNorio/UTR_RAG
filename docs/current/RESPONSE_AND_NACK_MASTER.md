---
title: "レスポンス・NACKマスタ"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs: []
tags:
  - "utr-s201"
  - "guide"
  - "response"
  - "nack"
---

# レスポンス・NACKマスタ

## 1. 目的

この文書は、UTR-S201シリーズの実装で必要になるレスポンス処理とNACK処理の考え方を整理します。

公式PDFが一次情報です。この文書は、AIに実装・レビューを依頼するときの補助資料です。

## 2. 区別するレスポンス

実装では、少なくとも以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- 複数レスポンス
- 完了レスポンス
- 自動読み取りやRFタグ応答に伴う非同期レスポンス

RFタグ通信系では、1回の送信に対して複数フレームを受信する場合があります。単純な「1送信1応答」と決め打ちしないでください。

## 3. NACK処理

NACKは、共通NACK形式と各コマンドの該当節を併せて確認します。

確認する代表例は以下です。

- SUMエラー
- フォーマットエラー
- timeout
- LBTエラー
- アンテナエラー
- UHF ICエラー
- RFタグ無応答
- Accessパスワード関連エラー
- メモリロック関連エラー

予約バイトは、PDFで意味が定義されていない限り独自解釈しません。

## 4. 実装時の注意

- timeout値を固定値だけで扱わず、接続方式とコマンド種別に応じて設定する。
- ACK、NACK、timeout、無応答を同じエラーとして扱わない。
- NACK時はエラーコードをログに残す。
- 複数レスポンスがあるコマンドでは受信ループを設計する。
- 完了レスポンスがあるコマンドでは、完了を受けるまで処理を閉じない。

## 5. ログに残す情報

- 実行日時
- 操作者
- 対象機種
- ROMバージョン
- 接続方式
- 対象コマンド
- 送信目的
- ACK / NACK / timeout
- NACKエラーコード
- 経過時間
- 停止判断
- 復旧判断

runtime logs、実CSVログ、raw EPC / UII / TID はGitHubにアップロードしないでください。必要な場合はマスク・要約してください。