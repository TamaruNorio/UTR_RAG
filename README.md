# UTR_RAG

UTR_RAG は、タカヤ製 UTR-S201 シリーズの通信プロトコル理解、実装支援、レビュー、段階的な実機確認を、AIとのペアプログラミングで進めやすくするための no-PDF ドキュメントリポジトリです。

対象読者は、AIを使ったペアプログラミング経験があり、Git / GitHub の基本操作を理解している開発者です。実装言語は限定しません。Python、C#、C++、JavaScript、その他の言語でも利用できます。

## 1. 現在版

現在版は **V100 Final documentation package** です。

V100 は、過去の作業履歴を前面に出すのではなく、以下を目的に再整理した最終版ドキュメントです。

- UTR-S201 シリーズ制御プログラムを作るための入口を明確にする。
- AIに渡す前提情報を整理する。
- コマンド仕様、レスポンス、NACK、ROM判定、安全条件を探しやすくする。
- 実機送信が必要な作業と、机上確認で済む作業を分ける。
- Python、C#など任意の言語へ移植しやすい形にする。

## 2. このリポジトリでできること

- UTR-S201 シリーズのコマンド一覧を確認する。
- コマンド別カードから、目的、形式、注意点、確認事項を調べる。
- ACK / NACK / timeout / LBT / antenna error などの応答処理方針を確認する。
- ROMバージョンとシリーズ名から対象機種を整理する。
- AIに実装やレビューを依頼する前提資料として使う。
- 実機確認の段階、停止条件、ログ方針を確認する。

## 3. 公式PDFとの関係

公式PDFが一次情報です。このリポジトリは公式PDFの代替ではありません。

このリポジトリは、公式PDFを参照しながら、AIと人間が安全に実装・確認を進めるための補助資料です。仕様判断、顧客提供、社外公開、海外利用、量産適用は、別途正式な確認が必要です。

## 4. 最初に読むファイル

1. `llms.txt`
2. `docs/current/AI_CONTEXT_INDEX.md`
3. `docs/current/00_OVERVIEW.md`
4. `docs/current/09_COMMAND_MASTER_V117.md`
5. `docs/current/commands/cards/`
6. `docs/current/10_RESPONSE_AND_NACK_MASTER.md`
7. `docs/current/11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
8. `docs/current/20_VERIFICATION_RESULT_STATUS.md`
9. `docs/current/45_V100_FINAL_USAGE_GUIDE.md`

## 5. AIペアプログラミングでの使い方

AIへ依頼するときは、次の順に進めます。

1. 対象機種、接続方式、対象コマンドを明示する。
2. コマンドカードと関連ドキュメントをAIに読ませる。
3. 実装対象を「読み取りのみ」「設定変更あり」「タグメモリ操作あり」に分ける。
4. 実装言語、実行環境、タイムアウト、ログ方針を指定する。
5. まず dry-run または机上確認から始める。
6. 実機送信が必要な場合は、明示許可、パラメータ、復旧方法、停止条件を確定する。

## 6. 安全方針

以下は、明示許可なしに実機送信しません。

- FLASH write / init
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- InventoryParam / SelectParam / ExpandSelectParam 変更
- タグメモリ書き込み
- Lock / Kill / Encode / ThroughCmd

プロトコル仕様書に存在するコマンドを、高影響という理由だけで禁止扱いにはしません。ただし、実行許可、条件、パラメータ、影響、復旧方法、停止条件が揃うまで実機送信しません。

## 7. Git運用

- mainを直接変更しない。
- featureブランチで作業する。
- 変更前後に `git status --short` を確認する。
- 差分は `git diff` と `git diff --check` で確認する。
- Pull Requestでレビューしてからmainへ反映する。

## 8. 機密情報とログ

以下はGitに含めません。

- runtime logs
- 実CSVログ
- 顧客情報
- 実IPアドレス
- raw EPC / UII / TID
- 認証情報
- PDF原本
- 完成HexやSUM計算済みの送信用コマンド例
