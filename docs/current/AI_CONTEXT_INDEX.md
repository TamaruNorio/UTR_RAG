# AI Context Index

## 1. 目的

この文書は、Codex、ChatGPT、GitHub、将来のRAG / 検索処理が、UTR_RAGを迷わず読むためのナビゲーションです。

UTR_RAGでは、階層構造、index文書、標準Markdownリンク、frontmatter metadataを併用します。

現在版は **V100 Final documentation package** です。

## 2. 最初に読むファイル

1. [Repository README](../../README.md)
2. [V100 Final Usage Guide](45_V100_FINAL_USAGE_GUIDE.md)
3. [Current Overview](00_OVERVIEW.md)
4. [Command Master](09_COMMAND_MASTER_V117.md)
5. [Traceability Index](16_TRACEABILITY_INDEX_V117.md)
6. [Verification Result Status](20_VERIFICATION_RESULT_STATUS.md)
7. [Docs README](../README.md)

## 3. コマンド調査の流れ

1. [Command Master](09_COMMAND_MASTER_V117.md) で対象コマンドを確認する。
2. [Traceability Index](16_TRACEABILITY_INDEX_V117.md) でPDF節、カード、関連文書を確認する。
3. [commands/cards](commands/cards/) 配下の個別コマンドカードを見る。
4. [Response and NACK Master](10_RESPONSE_AND_NACK_MASTER.md) でACK / NACK / timeoutを確認する。
5. [Device ROM Identification and Support](11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md) で機種・ROM条件を確認する。
6. [RAM FLASH Impact Matrix](12_RAM_FLASH_IMPACT_MATRIX.md) でRAM / FLASH影響を確認する。
7. [RF Safety and Carrier Rules](13_RF_SAFETY_AND_CARRIER_RULES.md) でRF送信・キャリア関連の注意を確認する。

## 4. AIペアプログラミングで使うとき

AIに実装やレビューを依頼するときは、以下を明示します。

- 対象機種
- 接続方式
- 対象コマンド
- 実装言語
- 実行環境
- 実機送信の有無
- タイムアウト方針
- ログ方針
- 明示的に変更してよい範囲
- 変更してはいけない範囲

## 5. 実機確認の流れ

- [Real Device Verification Framework](17_REAL_DEVICE_VERIFICATION_FRAMEWORK.md)
- [Real Device Log Schema](18_REAL_DEVICE_LOG_SCHEMA.md)
- [Verification Stage Plan](19_VERIFICATION_STAGE_PLAN.md)
- [Verification Result Status](20_VERIFICATION_RESULT_STATUS.md)

Stage 3+コマンドを実機送信するには、明示許可と完全なパラメータが必要です。protocol support と execution permission は別物として扱います。

## 6. PDF原本と機密情報の扱い

公式PDFが一次情報です。PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

runtime logs、顧客情報、実IPアドレス、raw EPC / UII / TID、実CSVログ、完成Hex、SUM計算済み送信用コマンド例はGitHubに含めません。

## 7. リンク方針

標準Markdownリンクを使用します。新規のObsidian形式wikilinkは追加しません。相対リンクを優先します。

## 8. 安全方針

プロトコル仕様書に定義されたコマンドは、高影響という理由だけで禁止扱いしません。ただし、実行には条件、パラメータ、影響、復旧方法、明示許可が必要です。
