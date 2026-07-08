# R9-10 Post-release Document Status

## 1. 目的

R9-7 Release後に追加された文書の扱いを明確化する。

## 2. R9-7 Releaseに含まれるもの

R9-7 Release asset のv006 ZIPには、R9-0からR9-6までの外部レビュー候補関連文書、R8系の実機確認・リリース判断文書、R9-3の38コマンドカードとインデックス、v006 README/MANIFESTが含まれる。

## 3. R9-7 Release後に追加されたもの

- `docs/release/R9-8_INTERNAL_SHARE_MESSAGE.md`
- `docs/release/R9-9_EXTERNAL_REVIEW_REQUEST_MESSAGE.md`

## 4. R9-8/R9-9の位置づけ

- v006 ZIP本体には含まれていない
- Release後の社内共有・外部レビュー依頼用文書
- v006 ZIPを変更する理由にはしない
- 必要に応じてGitHub上の文書として参照する
- 次versionを作る場合は含める候補にできる

## 5. 外部レビュー時の渡し方

- v006 ZIPはRelease assetを渡す
- 社内共有文面は社内向け
- 外部レビュー依頼文面は必要に応じてメール本文として使う
- R9-8/R9-9のGitHub文書URLを渡すかどうかは社内判断
- 外部共有範囲は社内承認後に決める

## 6. 判断

R9-8/R9-9がv006 ZIPに含まれていないことは問題ではない。
v006 ZIPを作り直す必要はない。
次にZIPを作る場合は新versionとする。
