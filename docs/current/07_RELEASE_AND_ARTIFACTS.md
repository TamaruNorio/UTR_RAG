# Release And Artifacts

この文書では、UTR_RAGの現在版と成果物の位置づけを整理します。

## 1. 現在版

現在版は **V100 Final documentation package** です。

V100は、AIペアプログラミングでUTR-S201シリーズ制御プログラムを作成・移植・レビューするための最終版ドキュメントセットです。

## 2. 成果物の考え方

V100では、過去の経緯ではなく、現在利用する入口を重視します。

- 最新の利用入口: `README.md`
- AI向け入口: `llms.txt`
- 詳細ナビゲーション: `docs/current/AI_CONTEXT_INDEX.md`
- 使い方: `docs/current/45_V100_FINAL_USAGE_GUIDE.md`
- コマンド一覧: `docs/current/09_COMMAND_MASTER_V117.md`
- 個別コマンドカード: `docs/current/commands/cards/`

既存の v022 ZIP はFinal RC時点のno-PDF成果物として残します。V100での最新利用入口は、mainブランチ上の現在版ドキュメントです。

## 3. V100に含むもの

- UTR-S201シリーズ向けAI補助ドキュメント
- 54件のコマンドカード
- ACK / NACK / timeout 関連資料
- ROM / 機種判定資料
- 検証ステージと結果ステータス
- Stage 3+高影響コマンドの実行ゲート
- AI向けナビゲーション

## 4. V100に含めないもの

- 公式PDF原本
- runtime logs
- 実CSVログ
- 顧客情報
- 実IPアドレス
- raw EPC / UII / TID
- 完成Hex
- SUM計算済み送信用コマンド例

## 5. 正式判断が別途必要なもの

- 顧客提供
- 正式社外公開
- 海外利用、海外販売
- Stage 3+の実機送信
- 周波数、出力、FLASH、アンテナ設定に影響する操作
