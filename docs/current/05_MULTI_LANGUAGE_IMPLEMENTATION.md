# 05 Multi-language Implementation

## 1. 対象言語

- Python
- C#
- C++
- JavaScript / Node.js
- PowerShell

## 2. 言語別の役割

- Python: 検証、ログ取得、簡易確認に向く
- C#: 業務アプリ開発で需要が高い可能性がある
- C++: 低レベル制御や既存組込み周辺との連携候補
- JavaScript / Node.js: 管理画面、Web連携、軽量ツール候補
- PowerShell: Windows環境での確認や運用補助に向く

## 3. 実装設計方針

接続、送信、受信、切断、タイムアウト、ログ、例外処理を分ける。危険操作と読み取り操作を同じ入口で混在させない。

## 4. 注意

この文書では実コードは作らない。完成Hex、SUM計算済みコマンド、実機送信用コードも作らない。