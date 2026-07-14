# AI Context Index

## 1. 目的

この文書は、Codex、ChatGPT、GitHub、将来のRAG / 検索処理が、UTR_RAGを迷わず読むためのナビゲーションです。

UTR_RAGでは、階層構造、index文書、標準Markdownリンク、frontmatter metadataを併用します。

## 2. 最初に読むファイル

1. [Repository README](../../README.md)
2. [Docs README](../README.md)
3. [Current Overview](00_OVERVIEW.md)
4. [Final RC Review](43_FINAL_RC_REVIEW.md)
5. [Release Decision Notes](44_RELEASE_DECISION_NOTES.md)
6. [Command Master](09_COMMAND_MASTER_V117.md)
7. [Traceability Index](16_TRACEABILITY_INDEX_V117.md)
8. [Verification Result Status](20_VERIFICATION_RESULT_STATUS.md)

## 3. コマンド調査の流れ

1. [Command Master](09_COMMAND_MASTER_V117.md) で対象コマンドを確認する。
2. [Traceability Index](16_TRACEABILITY_INDEX_V117.md) でPDF節、カード、関連文書を確認する。
3. [commands/cards](commands/cards/) 配下の個別コマンドカードを見る。
4. [Response and NACK Master](10_RESPONSE_AND_NACK_MASTER.md) でACK / NACK / timeoutを確認する。
5. [Device ROM Identification and Support](11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md) で機種・ROM条件を確認する。
6. [RAM FLASH Impact Matrix](12_RAM_FLASH_IMPACT_MATRIX.md) でRAM / FLASH影響を確認する。
7. [RF Safety and Carrier Rules](13_RF_SAFETY_AND_CARRIER_RULES.md) でRF送信・キャリア関連の注意を確認する。

## 4. 実機確認の流れ

- [Real Device Verification Framework](17_REAL_DEVICE_VERIFICATION_FRAMEWORK.md)
- [Real Device Log Schema](18_REAL_DEVICE_LOG_SCHEMA.md)
- [Verification Stage Plan](19_VERIFICATION_STAGE_PLAN.md)
- [Verification Result Status](20_VERIFICATION_RESULT_STATUS.md)
- Stage/result documents 21以降

## 5. Stage 2の流れ

- [Stage 2 RF Read Preflight](28_STAGE2_RF_READ_PREFLIGHT.md)
- [Stage 2 RF Read Command Plan](29_STAGE2_RF_READ_COMMAND_PLAN.md)
- [Stage 2 RF Read Log Template](30_STAGE2_RF_READ_LOG_TEMPLATE.md)
- [Stage 2 Stop Conditions](31_STAGE2_STOP_CONDITIONS.md)
- [Stage 2 RF Read Minimal Result](32_STAGE2_RF_READ_MINIMAL_RESULT.md)
- [Stage 2 RF Read Operations Result](33_STAGE2_RF_READ_OPERATIONS_RESULT.md)
- [Stage 2 Read Completion Result](34_STAGE2_READ_COMPLETION_RESULT.md)

## 6. Stage 3+ high-impact readinessの流れ

- [Stage 3+ High Impact Readiness](35_STAGE3PLUS_HIGH_IMPACT_READINESS.md)
- [Stage 3+ Command Matrix](36_STAGE3PLUS_COMMAND_MATRIX.md)
- [Stage 3+ Execution Gates](37_STAGE3PLUS_EXECUTION_GATES.md)
- [Stage 3+ Recovery And Stop Plan](38_STAGE3PLUS_RECOVERY_AND_STOP_PLAN.md)
- [Stage 3+ First Execution Batch Plan](39_STAGE3PLUS_FIRST_EXECUTION_BATCH_PLAN.md)
- [Stage 3+ First Batch Parameter Sheet](40_STAGE3PLUS_FIRST_BATCH_PARAMETER_SHEET.md)
- [Stage 3+ Operator Approval Template](41_STAGE3PLUS_OPERATOR_APPROVAL_TEMPLATE.md)
- [Stage 3+ v021 Plan Result](42_STAGE3PLUS_V021_PLAN_RESULT.md)

Stage 3+コマンドを実機送信するには、明示許可と完全なパラメータが必要です。protocol support と execution permission は別物として扱います。

## 7. v022 Final RC

v022は、現在のno-PDF UTR-S201 AI assistant packageをFinal RCとして統合したものです。

- [Final RC Review](43_FINAL_RC_REVIEW.md)
- [Release Decision Notes](44_RELEASE_DECISION_NOTES.md)
- `artifacts/utr_s201_ai_v022/README.md`
- `artifacts/utr_s201_ai_v022/MANIFEST.md`
- `artifacts/utr_s201_ai_v022/utr_s201_ai_v022_final_rc_no_pdf.zip`

## 8. リンク方針

標準Markdownリンクを使用します。新規のObsidian形式wikilinkは追加しません。相対リンクを優先します。

## 9. 安全方針

プロトコル仕様書に定義されたコマンドは、高影響という理由だけで禁止扱いしません。ただし、実行には条件、パラメータ、影響、復旧方法、明示許可が必要です。

runtime logs、顧客情報、実IPアドレス、raw EPC / UII / TID、実CSVログはGitに含めません。
