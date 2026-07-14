---
title: "Stage 3+ Command Matrix"
doc_type: "index"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
operation_stage: "Stage 3+"
verification_status: "PLAN_ONLY"
result_status: "NOT_EXECUTED_IN_V020"
related_docs:
  - "35_STAGE3PLUS_HIGH_IMPACT_READINESS.md"
  - "37_STAGE3PLUS_EXECUTION_GATES.md"
  - "38_STAGE3PLUS_RECOVERY_AND_STOP_PLAN.md"
tags:
  - "utr-s201"
  - "index"
  - "stage3"
  - "stage4"
  - "stage5"
  - "write-operation"
  - "flash-operation"
  - "tag-memory"
  - "needs-real-device-test"
  - "needs-review"
---

# Stage 3+ Command Matrix

## 1. Positioning

This matrix organizes Stage 3+ high-impact commands for readiness review.
The commands remain protocol-defined commands, but v020 does not execute them.

## 2. Matrix

| Stage bucket | PDF section | Command name | Command bytes | Command group | Operation category | Impact category | Persistent change | Tag memory change | Irreversible operation | RF emission | Requires ROM check | Requires antenna | Requires tag | Requires target EPC/UII | Requires memory bank | Requires address | Requires word count | Requires access password | Requires recovery plan | v020 status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stage 3 tag memory write | 7.5.4 | UHF_Write | 55h/16h | RFタグ通信 | write/tag-memory | TAG_MEMORY_WRITE | tag memory | yes | no | yes | yes | yes | yes | yes | yes | yes | yes | depends | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Target tag, memory bank, address, word count, write data, and recovery limits required. |
| Stage 3 irreversible tag operation | 7.5.5 | UHF_Kill | 55h/17h | RFタグ通信 | irreversible/tag-kill | IRREVERSIBLE_TAG_OPERATION | tag state | irreversible | yes | yes | yes | yes | yes | yes | no | no | no | yes | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Use only explicitly approved disposable target tags. |
| Stage 3 irreversible tag operation | 7.5.6 | UHF_Lock | 55h/18h | RFタグ通信 | lock/tag-memory | TAG_LOCK_OR_PERMISSION_CHANGE | tag lock state | lock state | possible | yes | yes | yes | yes | yes | depends | no | no | yes | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Lock state may be irreversible depending on parameters. |
| Stage 3 tag memory write | 7.5.7 | UHF_BlockWrite | 55h/1Ah | RFタグ通信 | block-write/tag-memory | TAG_MEMORY_WRITE | tag memory | yes | no | yes | yes | yes | yes | yes | yes | yes | yes | depends | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Explicit write data and target range required. |
| Stage 3 tag memory write | 7.5.8 | UHF_BlockErase | 55h/1Bh | RFタグ通信 | block-erase/tag-memory | TAG_MEMORY_ERASE | tag memory | erase | possible | yes | yes | yes | yes | yes | yes | yes | yes | depends | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Erase may not be recoverable from device side. |
| Stage 3 tag memory write | 7.5.9 | UHF_BlockWrite2 | 55h/1Dh | RFタグ通信 | block-write/tag-memory | TAG_MEMORY_WRITE_PARTIAL_FAILURE_RISK | tag memory | yes | possible | yes | yes | yes | yes | yes | yes | yes | yes | depends | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Partial-failure diagnostics must be planned. |
| Stage 3 tag memory write | 7.5.10 | UHF_Encode | 55h/1Eh | RFタグ通信 | encode/tag-memory | TAG_ENCODING | tag memory and lock state possible | yes | possible | yes | yes | yes | yes | yes | yes | yes | yes | depends | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Encode can affect multiple tag fields. |
| Stage 3 advanced RF command | 7.5.11 | UHF_ThroughCmd | 55h/FFh | RFタグ通信 | through/advanced | ADVANCED_UNBOUNDED_TAG_OPERATION | depends on payload | depends on payload | depends on payload | yes | yes | yes | depends | depends | depends | depends | depends | depends | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Payload review is mandatory. |
| Stage 4 reader configuration write | 7.4.16 | リーダライタ動作モードの書き込み | 4Eh/00h/10h | リーダライタ設定 | configuration-write | READER_MODE_CHANGE | RAM or FLASH depending on target | no | no | no | yes | no | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Reader operating mode change requires rollback plan. |
| Stage 4 reader configuration write | 7.4.17 | UHF_SetSelectParam | 55h/30h | リーダライタ設定 | configuration-write | SELECT_PARAM_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Affects subsequent RF tag operations. |
| Stage 4 reader configuration write | 7.4.18 | UHF_SetInventoryParam | 55h/31h | リーダライタ設定 | configuration-write | INVENTORY_PARAM_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Affects RF behavior and read results. |
| Stage 4 reader configuration write | 7.4.19 | UHF_SetExpandSelectParam | 55h/32h | リーダライタ設定 | configuration-write | EXPAND_SELECT_PARAM_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires current-setting backup. |
| Stage 4 reader configuration write | 7.4.20 | アンテナ切替設定の書き込み | 55h/33h/00h | リーダライタ設定 | configuration-write | ANTENNA_SWITCH_SETTING_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Can affect RF routing. |
| Stage 4 reader configuration write | 7.4.21 | 出力設定の書き込み | 55h/33h/01h | リーダライタ設定 | configuration-write | OUTPUT_POWER_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires legal/site confirmation. |
| Stage 4 reader configuration write | 7.4.22 | 周波数設定の書き込み | 55h/33h/02h | リーダライタ設定 | configuration-write | FREQUENCY_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires legal/site confirmation. |
| Stage 4 reader configuration write | 7.4.23 | Accessパスワードの書き込み | 55h/33h/03h | リーダライタ設定 | configuration-write | ACCESS_PASSWORD_CHANGE | RAM/configuration | no | possible | no | yes | no | no | no | no | no | no | yes | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires credential and recovery policy. |
| Stage 4 reader configuration write | 7.4.24 | RFタグ通信関連パラメータの書き込み | 55h/33h/04h | リーダライタ設定 | configuration-write | RF_TAG_COMM_PARAM_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires baseline backup. |
| Stage 4 reader configuration write | 7.4.25 | EPC(UII)関連パラメータの書き込み | 55h/33h/05h | リーダライタ設定 | configuration-write | EPC_UII_PARAM_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Affects tag parsing and response behavior. |
| Stage 4 reader configuration write | 7.4.26 | 外部アンテナ自動切替設定の書き込み | 55h/37h | リーダライタ設定 | configuration-write | EXTERNAL_ANTENNA_AUTO_SWITCH_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | 8CH-related wiring and ROM conditions must be confirmed. |
| Stage 4 reader configuration write | 7.4.27 | 汎用ポート値の書き込み | 4Eh/9Fh | リーダライタ設定 | configuration-write | GENERAL_PORT_OUTPUT_CHANGE | external I/O | no | no | no | yes | no | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Connected equipment must be reviewed. |
| Stage 4 reader configuration write | 7.4.28 | 拡張ポート値の書き込み | 4Eh/A0h | リーダライタ設定 | configuration-write | EXTENDED_PORT_OUTPUT_CHANGE | external I/O | no | no | no | yes | no | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Connected equipment must be reviewed. |
| Stage 4 reader configuration write | 7.4.29 | FLASH設定値の書き込み(1バイトアクセス) | 4Eh/B4h | リーダライタ設定 | flash-write | FLASH_ONE_BYTE_WRITE | FLASH/persistent | no | possible | no | yes | no | no | no | no | yes | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires backup and recovery plan. |
| Stage 4 reader configuration write | 7.4.30 | RSSIフィルタ設定の書き込み | 55h/39h | リーダライタ設定 | configuration-write | RSSI_FILTER_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Changes tag detection behavior. |
| Stage 4 reader configuration write | 7.4.31 | アンテナ個別送信出力設定の書き込み | 55h/3Ah | リーダライタ設定 | configuration-write | ANTENNA_OUTPUT_POWER_CHANGE | RAM/configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires legal/site confirmation. |
| Stage 5 reader control high-impact | 7.3.4 | RF送信信号の制御 | 4Eh/9Eh | リーダライタ制御 | rf-carrier-control | RF_CARRIER_CONTROL | runtime state | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires site/legal confirmation and stop conditions. |
| Stage 5 reader control high-impact | 7.3.7 | 使用アンテナ番号の書き込み | 55h/38h | リーダライタ制御 | antenna-selection-write | ACTIVE_ANTENNA_CHANGE | runtime configuration | no | no | yes | yes | yes | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires wiring and recovery confirmation. |
| Stage 5 reader control high-impact | 7.3.10 | リスタート | 4Eh/9Dh | リーダライタ制御 | restart | READER_RESTART | device runtime state | no | no | no | yes | no | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires reconnection plan. |
| Stage 5 reader control high-impact | 7.3.11 | FLASH設定の初期化 | 4Eh/6Fh | リーダライタ制御 | flash-initialize | FLASH_INITIALIZE | FLASH/persistent | no | possible | no | yes | no | no | no | no | no | no | no | yes | READY_FOR_EXPLICIT_APPROVAL / NOT_EXECUTED_IN_V020 | Requires backup and recovery plan. |
