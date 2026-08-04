---
title: "既知のAI実装失敗パターン"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:
  - RESPONSE_AND_NACK_MASTER.md
  - ANTENNA_NUMBERING_SCHEMES.md
  - UTR_TAG_GUI_IMPLEMENTATION_FEEDBACK.md
  - ../../AGENTS.md
tags:
  - "utr-s201"
  - "guide"
  - "ai-implementation"
  - "failure-patterns"
  - "review"
---

# 既知のAI実装失敗パターン

この文書は、AIコーディングエージェントによるUTR-S201シリーズ実装で起こりやすい失敗を、再発防止のために一般化して整理するものです。

公式PDFが一次情報です。この文書は、特定人物、特定企業、特定プロジェクト、実機ログの生値を記録するためのものではありません。機密情報、顧客情報、実IPアドレス、実機ログ由来のraw EPC / UII / TID、認証情報、パスワードは含めないでください。

## 1. NACKエラーコードの記載漏れ・取り違え

### 何が起きたか

あるNACKエラーコードの値や意味が文書内に明示されていない状態で、AIが名称から推測して実装し、誤ったコード番号や意味を割り当てた。

### 根本原因

「公式PDFを確認する」という注意だけでは、PDF本文にアクセスできないAI実装環境で固定値を正しく再現できない。代表例だけを見て、全量のエラーコード表があると誤解する場合もある。

### 予防のために読むべき文書

- `RESPONSE_AND_NACK_MASTER.md`
- `RESPONSE_CLASSIFICATION_MATRIX.md`
- 対象コマンドカードのNACK分類

### レビュー時の確認ポイント

- `error_code_1` の値が `RESPONSE_AND_NACK_MASTER.md` の「エラーコード1 一覧（完全版）」と一致しているか。
- `SUM_ERROR`、`CMD_LBT_ERROR`、`CMD_ANT_ERROR` などの固定値を名称から推測していないか。
- `error_code_2` を、`error_code_1=0Ah` の場合だけ意味のある値として扱っているか。

## 2. 複数の値域体系が存在するパラメータの混同

### 何が起きたか

アンテナ番号など、同じ名称でも用途やフレーム位置により値域が異なるパラメータについて、別体系の値をそのまま流用した。

### 根本原因

内部アンテナ番号、外部アンテナ番号、RFタグ応答フレームの `ADR` バイトを同じ「アンテナ番号」として扱い、コマンドごとの値域や意味を確認しなかった。

### 予防のために読むべき文書

- `ANTENNA_NUMBERING_SCHEMES.md`
- `commands/cards/55_48_read_active_antenna.md`
- `commands/cards/55_38_write_active_antenna.md`
- `commands/cards/55_44_uhf_check_antenna.md`

### レビュー時の確認ポイント

- コマンドごとに、値域、起点、表示ラベル、フレーム位置を分けて実装しているか。
- RFタグ応答の `ADR` バイトを、使用アンテナ番号の書き込み値へ自動投入していないか。
- 4CH機、8CH機、1CH機のアンテナ番号体系を同一ロジックで決め打ちしていないか。

## 3. related_docsの読み飛ばし

### 何が起きたか

対象コマンドカードだけを読んで実装し、`related_docs` に既に記載されている注意点や正しい分類を読まず、独自に誤った処理を再実装した。

### 根本原因

カード単体で実装判断を閉じ、レスポンス分類、NACK処理、機種・ROM条件、アンテナ番号体系、RAM/FLASH影響を横断確認しなかった。

### 予防のために読むべき文書

- `../../AGENTS.md`
- `COMMAND_MASTER_V117.md`
- `RESPONSE_AND_NACK_MASTER.md`
- `RESPONSE_CLASSIFICATION_MATRIX.md`
- 対象コマンドカードの `related_docs`

### レビュー時の確認ポイント

- 実装前に対象カードの `related_docs` をすべて開いた記録があるか。
- 複数レスポンスや設定依存レスポンスをカード単体のACK例だけで固定していないか。
- 既存文書にある注意を、実装側で別解釈していないか。

## 4. 正常系結果と異常系応答区分の混同

### 何が起きたか

タグ0枚などの正常系の結果を、NACKや例外的なエラーコードに対応付けて処理した。

### 根本原因

ACK、NACK、timeout、無応答、完了レスポンス、RFタグデータを同じ「失敗」または「未検知」としてまとめ、PDFに明記された応答区分を確認しなかった。

### 予防のために読むべき文書

- `RESPONSE_AND_NACK_MASTER.md`
- `RESPONSE_CLASSIFICATION_MATRIX.md`
- `commands/cards/55_10_uhf_inventory.md`
- `UTR_TAG_GUI_IMPLEMENTATION_FEEDBACK.md`

### レビュー時の確認ポイント

- タグ0枚を、読取完了ACKの読み取り枚数 `0000` として扱っているか。
- `error_code_1=68h` をタグ未検知ではなくアンテナ断線エラーとして扱っているか。
- timeout、NACK、正常完了0件を別の状態としてログ・画面表示しているか。

## 5. 特定機種向け実装の別機種流用

### 何が起きたか

特定機種で動いた実装を、アンテナポート数、番号体系、外部アンテナ制御、ROM条件が異なる別機種へそのまま適用した。

### 根本原因

ROMバージョンとシリーズ名による機種判定を起点にせず、実装時の手元機種の前提を全機種共通の仕様として扱った。

### 予防のために読むべき文書

- `DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
- `ANTENNA_NUMBERING_SCHEMES.md`
- `UTR_TAG_GUI_IMPLEMENTATION_FEEDBACK.md`
- `EXAMPLE_IMPLEMENTATION_REQUEST.md`

### レビュー時の確認ポイント

- 起動時にROMバージョンとシリーズ名を読み、機種別の処理へ分岐しているか。
- 未対応または判定不能の機種でクラッシュせず、安全側に倒しているか。
- 機種ごとのアンテナ台数、内部アンテナ番号、外部アンテナ番号、自動切替条件を分けて扱っているか。

## 6. listenログのcompletion不在を異常と誤解

### 何が起きたか

自動読み取りモードの受信専用ログで `RF_TAG_DATA` が継続しているにもかかわらず、読取完了ACK（`COMPLETION`）が現れないことを異常と判断し、不要なエラー処理、再送、モード変更を実装した。

### 根本原因

コマンドモードの単発Inventoryと、自動読み取りモードのpassive receive/listenを同じ評価軸で扱った。`COMPLETION` は単発コマンドの1回の動作終了を示す応答であり、継続受信には対応する完了概念がないことを確認しなかった。

### 予防のために読むべき文書

- `RESPONSE_AND_NACK_MASTER.md`
- `RESPONSE_CLASSIFICATION_MATRIX.md`
- `UTR_TAG_GUI_IMPLEMENTATION_FEEDBACK.md`

### レビュー時の確認ポイント

- listen中の `RF_TAG_DATA` 継続受信を正常な観測結果として扱っているか。
- listen中に `COMPLETION` がないことをtimeout、NACK、タグ未検知、通信異常として扱っていないか。
- 単発コマンド応答試験と継続受信ログの集計項目を分けているか。

## 7. RFタグ応答ADRバイトの断定解釈

### 何が起きたか

RFタグ応答フレームの `ADR` バイトを、起動時スナップショットや設定読戻しで裏取りせず、常にreader addressまたは常にantenna IDとして断定した。

### 根本原因

通常レスポンスのアドレス位置と、アンテナID出力ON時のRFタグ応答における読み取りANT番号を同じ意味として扱った。設定依存で意味が変わる値を、生値だけから判断した。

### 予防のために読むべき文書

- `ANTENNA_NUMBERING_SCHEMES.md`
- `RESPONSE_AND_NACK_MASTER.md`
- `commands/cards/55_10_uhf_inventory.md`

### レビュー時の確認ポイント

- `ADR` バイトを `address_raw` として残し、解釈はスナップショット依存として扱っているか。
- アンテナID出力設定が未確認の場合に、reader addressまたはantenna IDとして断定していないか。
- RFタグ応答の `ADR` を、使用アンテナ番号の書き込み値や別体系のアンテナ番号へそのまま流用していないか。

## 8. 機種専用コマンドの非対応NACKをパラメータミスと誤解

### 何が起きたか

特定機種専用のコマンドを、対応確認なしに別機種へ送信し、NACK（FORMAT_ERRORなど）を受け取った。そのNACKを「送信パラメータの組み立てミス」と誤解し、値だけを変えて再送しようとした。

### 根本原因

コマンドが仕様上存在することと、接続中の機種・ROMで対応していることを分けて確認しなかった。機種専用コマンドの非対応応答を、コマンド自体の適用条件ではなくパラメータ値の問題として扱った。

### 予防のために読むべき文書

- `COMMAND_MASTER_V117.md`
- `DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`
- `ANTENNA_NUMBERING_SCHEMES.md`
- 対象コマンドカードの機種条件

### レビュー時の確認ポイント

- ROMバージョンとシリーズ名から対象機種を判定してから、機種専用コマンドを送信しているか。
- 非対応機種で返るNACKを、パラメータ値の修正だけで解決しようとしていないか。
- NACKログに、対象機種、対象コマンド、対応可否の判断根拠を残しているか。
