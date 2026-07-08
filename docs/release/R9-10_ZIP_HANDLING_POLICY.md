# R9-10 ZIP Handling Policy

## 1. 目的

ZIP成果物の削除、改変、再作成、Release添付、次version作成の方針を定義する。

## 2. 基本方針

- 既存ZIPは削除しない
- 既存ZIPは上書きしない
- 既存ZIPは再作成しない
- SHA256が記録済みのZIPは固定成果物として扱う
- Release assetとして添付済みのZIPは特に変更禁止
- ZIPを更新する場合は新versionで作る

## 3. やってよいこと

- ZIPの棚卸し文書を作る
- README/MANIFESTで位置づけを明確化する
- 過去ZIPを履歴保持用として扱う
- 新version作成時に新しいディレクトリを作る
- 新しいZIPを作る場合は別名にする

## 4. やってはいけないこと

- v004/v005/v006 ZIPの削除
- v004/v005/v006 ZIPの再作成
- v004/v005/v006 ZIPの上書き
- Release済みAssetの差し替え
- 既存tagの上書き
- 既存Releaseの意味変更
- 既存ZIPを新ZIPに二重梱包
- PDF混入
- 完成Hex混入
- SUM計算済みコマンド混入
- 実機送信用コード混入
- 顧客情報混入
- タグ固有ID混入
- 実IPアドレス混入

## 5. 次にZIPを作る場合

- R9-8/R9-9を含める必要がある場合は、v006を作り直さない
- 新しく v007 または v006.1 相当として作る
- 新ZIP名、MANIFEST、SHA256、validation、Releaseを新規に作る
- 既存Releaseは変更しない

## 6. 判断フロー

```text
ZIPの中身を直したい
  -> 誤記修正だけか
  -> Release済みか
  -> SHA256記録済みか
  -> 外部共有済みか
  -> YESなら既存ZIPは変更せず新version

ZIPを減らしたい
  -> 削除しない
  -> artifact inventoryで用途と現行性を整理する

外部レビューに渡したい
  -> v006を使う
  -> R9-8/R9-9は別途GitHub文書またはメール本文で渡す
```
