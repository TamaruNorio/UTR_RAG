# v008 Traceability Completion Plan

## 1. Purpose

v008の各コマンドカードについて、PDF Ver.1.17との対応情報を今後補完するための計画である。

## 2. Completion targets

- 各カードとPDF節番号の対応確認
- command byte
- detail command byte
- subcommand byte
- ACK参照先
- NACK参照先
- 機種/ROM対応参照先
- RAM/FLASH影響参照先
- 補完優先度
- 補完方法
- 結果記録欄

## 3. Completion table

| No | Target | Completion item | Priority | Completion method | Result | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | All command cards | PDF section mapping | High | Compare card identity with PDF Ver.1.17 Chapter 6 and Chapter 7 | TBD | 54 commands |
| 2 | All command cards | command byte | High | Compare command byte with Chapter 6 command list | TBD | 54 commands |
| 3 | All command cards | detail command byte | High | Compare detail command byte with Chapter 6 command list | TBD | 54 commands |
| 4 | Commands with subcommand | subcommand byte | High | Compare subcommand byte with Chapter 6 command list | TBD | Applicable commands |
| 5 | All command cards | ACK reference | High | Link each card to its Chapter 7 ACK section | TBD | Keep no completed Hex |
| 6 | All command cards | NACK reference | High | Link each card to Chapter 7.6 common NACK and command-specific notes | TBD | Error code 1-4 |
| 7 | Device-dependent commands | Device/ROM support reference | High | Link to Chapter 6.2 and ROM version notes | TBD | ROM 2.050, ROM 2.100, 8CH |
| 8 | Setting commands | RAM/FLASH impact reference | Medium | Link to relevant setting and persistence notes | TBD | RAM-only / FLASH / persistent |
| 9 | RF and tag commands | RF/tag memory impact reference | Medium | Link to RF safety, carrier, tag memory, Lock/Kill/Encode notes | TBD | Include recovery notes |
| 10 | Automatic reading behavior | Async response reference | Medium | Separate 7.1/7.2 behavior from normal host commands | TBD | Mode/asynchronous response |


## 4. v009 migration

v009でtraceability completionを実施する。
v009完了後は、v008のtraceability補完計画はv009へ移行済みとする。

残るHOLDは以下に限定する。

- 正式公開承認
- ライセンス/IP
- 顧客提供可否
- 海外判断
- 実機送信確認
