---
title: "コマンドマスタ Ver.1.17"
doc_type: "index"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "V100_FINAL_DOCUMENTATION"
related_docs:
  - RESPONSE_CLASSIFICATION_MATRIX.md
  - RESPONSE_AND_NACK_MASTER.md
  - DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md
  - RAM_FLASH_IMPACT_MATRIX.md
  - RF_SAFETY_AND_CARRIER_RULES.md
tags:
  - "utr-s201"
  - "command-master"
  - "v100"
---

# コマンドマスタ Ver.1.17

## 1. 対象仕様

対象は `UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17` です。

公式PDFが一次情報です。PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

## 2. コマンド件数

PDF 6.1 のコマンド一覧に基づき、上位から送信する通常コマンドは54件です。

| 区分 | 件数 |
|---|---:|
| リーダライタ制御コマンド | 12 |
| リーダライタ設定コマンド | 31 |
| RFタグ通信コマンド | 11 |
| 合計 | 54 |

PDF 7.1 と 7.2 は自動読み取りや非同期レスポンス動作の説明として扱い、通常の上位送信コマンド54件には含めません。

## 3. コマンドカード

全54コマンドの一覧、カードへのリンク、レスポンス分類、受信ループ方針は、
[レスポンス分類マトリクス](RESPONSE_CLASSIFICATION_MATRIX.md)の第4節を正本索引として参照してください。
本ファイルはV1.17コマンド体系の概要と分類方針を示す文書であり、
個別コマンドの実装確認には必ず各コマンドカードを参照してください。

各コマンドの詳細は `docs/current/commands/cards/` 配下のコマンドカードを参照してください。

コマンドカードでは、以下を整理しています。

- コマンドの目的
- PDF章番号
- コマンドバイト、詳細コマンド、サブコマンド
- 読み取り、制御、設定変更、タグメモリ操作などの分類
- 実装前に確認すること
- ACK / NACK / timeout の扱い
- 実機確認時の注意点

## 4. 利用手順

1. 対象機種とROMバージョンを確認する。
2. 対象応答の解釈に必要な設定を、[応答マスタのACK解釈の前提](RESPONSE_AND_NACK_MASTER.md)と対象カードから選ぶ。物理アンテナ容量、動作モード、アンテナID出力などの一覧を全コマンド共通の一括読戻し指示としない。現在のモードで取得できる範囲を確認し、未取得値を推測しない。
3. このコマンドマスタで対象コマンドの分類を確認する。
4. 対象コマンドカードを開く。
5. 応答処理は `RESPONSE_AND_NACK_MASTER.md` を確認する。
6. 機種・ROM条件は `DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md` を確認する。
7. RAM / FLASH / RF影響は `RAM_FLASH_IMPACT_MATRIX.md` と `RF_SAFETY_AND_CARRIER_RULES.md` を確認する。

自動読み取り中は、モード読取りを含む通常の設定取得が保証されません。p.19–20の受付例外と[モード切替の条件](RESPONSE_MODE_APPLICABILITY.md)を先に確認します。コマンドモードへ戻す操作は動作変更なので、取得できない元設定を推測したり、観測のみの作業に停止を追加したりしません。

全54コマンドのACK/NACK処理は、各カードだけで個別に完結させず、共通ルールとして `RESPONSE_AND_NACK_MASTER.md` の起動時スナップショットを参照してください。コマンド番号だけでACK内バイトの意味や後続レスポンス有無を固定しないでください。

## 5. 実機送信に関する注意

プロトコル仕様書に存在し、対象機種、ROMバージョン、地域条件、現場条件を満たすコマンドは、実装・実機送信の対象にできます。

ただし、完成HexやSUM計算済みの送信用コマンド例は、このドキュメントには記載しません。実機送信する場合は、対象、設定値、影響範囲、復旧方法、停止条件、ログ方針を明確にしてください。

