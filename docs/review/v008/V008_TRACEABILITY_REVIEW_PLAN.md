# v008 Traceability Review Plan

## 1. Purpose

v008の各コマンドカードがPDF Ver.1.17の該当箇所に正しく対応しているか、人間レビューで確認するための計画である。

## 2. Review approach

54コマンドをPDF第6章のコマンド一覧、PDF第6章のリーダライタ別対応表、PDF第7章の各コマンドフォーマット、PDF第7.6章のNACKレスポンスとエラーコードに突合する。

## 3. Traceability checklist

| No | Review item | Priority | Reviewer | Result | Fix needed | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | コマンド名がPDF第6章と一致しているか | High | TBD | TBD | TBD | 54件全件 |
| 2 | command byteがPDF第6章と一致しているか | High | TBD | TBD | TBD | 54件全件 |
| 3 | detail command byteがPDF第6章と一致しているか | High | TBD | TBD | TBD | 54件全件 |
| 4 | subcommand byteがPDF第6章と一致しているか | High | TBD | TBD | TBD | 対象コマンド |
| 5 | ACKレスポンス説明がPDF第7章と矛盾しないか | High | TBD | TBD | TBD | 各コマンドカード |
| 6 | NACKレスポンス説明がPDF第7.6章と矛盾しないか | High | TBD | TBD | TBD | 共通NACK |
| 7 | 注意事項がPDF第7章/第8章の記載と矛盾しないか | Medium | TBD | TBD | TBD | RFタグ通信を重点確認 |
| 8 | 機種/ROM対応がPDF第6.2章と一致しているか | High | TBD | TBD | TBD | ROM 2.050/2.100、8CH系 |
| 9 | RAM/FLASH影響の説明が設定対象と合っているか | High | TBD | TBD | TBD | 設定変更系 |
| 10 | 自動読み取りモード/非同期レスポンスを通常コマンドと混同していないか | Medium | TBD | TBD | TBD | 7.1/7.2 |
| 11 | AIが勝手に使用不可と判断する表現がないか | Medium | TBD | TBD | TBD | 方針文書とカード |
| 12 | PDF正本の代替と誤解される表現がないか | Medium | TBD | TBD | TBD | README/Release含む |

## 4. Review outputs

- 確認担当
- 確認日
- 確認結果
- 修正要否
- 修正対象ファイル
- 次版へ送るHOLD事項
