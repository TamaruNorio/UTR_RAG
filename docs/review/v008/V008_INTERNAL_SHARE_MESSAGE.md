# v008 Internal Share Message

関係者各位

UTR-S201シリーズ通信プロトコル説明書 Ver.1.17 を前提にしたAI補助RAG成果物として、v008 pre-releaseを作成しました。社内レビュー候補として共有します。

Release:
https://github.com/TamaruNorio/UTR_RAG/releases/tag/utr-s201-ai-v008-v117-clean-full-coverage.1

対象asset:
`utr_s201_ai_v008_v117_full_coverage_no_pdf.zip`

SHA256:
`2729C1D1D4BD8C8CDFABDFB44B6C7589AAEF2D4F9FD302821B38395FA90B60D1`

## 概要

本パッケージは、PDF Ver.1.17 第6章基準の54コマンドカード版です。ACK/NACK、エラーコード、ROM判定、RAM/FLASH影響、RF安全、アンテナ切替、AI実装ガードレールを整理しています。

接続可能な場合は、ROMバージョン読み取りにより、機種名・シリーズ名・ROMバージョンを自動判定する方針です。プロトコル仕様書に記載されたコマンドは、AIが勝手に禁止せず、対象機種・ROM・必要パラメータ・影響範囲を確認したうえで使用可能なものとして整理しています。

## 注意事項

本成果物はpre-releaseです。正式社外公開版ではありません。PDF正本の代替ではありません。顧客提供版ではありません。本番利用保証版ではありません。海外販売・海外運用向けではありません。

## 確認していただきたい観点

- PDF Ver.1.17 第6章基準の54コマンド整理が妥当か
- ACK/NACK、エラーコード、ROM判定、RAM/FLASH影響、RF安全の説明が実務上使えるか
- アンテナ切替、設定変更、タグメモリ変更などの影響説明が不足していないか
- AI実装支援時に誤解を招く表現がないか

## HOLD事項

- 正式社外公開承認
- PDF原本との人間レビュー
- traceability補完
- ライセンス/IP最終確認
- 全54コマンド個別実機送信確認
- 海外利用・海外販売
