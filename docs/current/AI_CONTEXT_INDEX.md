# AI Context Index

## 1. Purpose

This file is the navigation map for Codex, ChatGPT, GitHub, and future RAG/search workflows.

UTR_RAG uses hierarchy, index documents, standard Markdown links, and frontmatter metadata together.

## 2. First files to read

- [Repository README](../../README.md)
- [Docs README](../README.md)
- [Current Overview](00_OVERVIEW.md)
- [Command Master](09_COMMAND_MASTER_V117.md)
- [Traceability Index](16_TRACEABILITY_INDEX_V117.md)
- [Verification Result Status](20_VERIFICATION_RESULT_STATUS.md)

## 3. Command lookup flow

1. [Command Master](09_COMMAND_MASTER_V117.md)
2. [Traceability Index](16_TRACEABILITY_INDEX_V117.md)
3. Target command card under [commands/cards](commands/cards/)
4. [Response and NACK Master](10_RESPONSE_AND_NACK_MASTER.md)
5. [Device ROM Identification and Support](11_DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md)
6. [RAM FLASH Impact Matrix](12_RAM_FLASH_IMPACT_MATRIX.md)
7. [RF Safety and Carrier Rules](13_RF_SAFETY_AND_CARRIER_RULES.md)

## 4. Real-device verification flow

- [Real Device Verification Framework](17_REAL_DEVICE_VERIFICATION_FRAMEWORK.md)
- [Real Device Log Schema](18_REAL_DEVICE_LOG_SCHEMA.md)
- [Verification Stage Plan](19_VERIFICATION_STAGE_PLAN.md)
- [Verification Result Status](20_VERIFICATION_RESULT_STATUS.md)
- Stage/result documents 21 and later.

## 5. Stage 2 flow

- [Stage 2 RF Read Preflight](28_STAGE2_RF_READ_PREFLIGHT.md)
- [Stage 2 RF Read Command Plan](29_STAGE2_RF_READ_COMMAND_PLAN.md)
- [Stage 2 RF Read Log Template](30_STAGE2_RF_READ_LOG_TEMPLATE.md)
- [Stage 2 Stop Conditions](31_STAGE2_STOP_CONDITIONS.md)
- [Stage 2 RF Read Minimal Result](32_STAGE2_RF_READ_MINIMAL_RESULT.md)
- [Stage 2 RF Read Operations Result](33_STAGE2_RF_READ_OPERATIONS_RESULT.md)
- [Stage 2 Read Completion Result](34_STAGE2_READ_COMPLETION_RESULT.md)

## 6. Link policy

Use standard Markdown links. Do not add new Obsidian-style wikilinks. Relative links are preferred.

## 7. Safety policy

A protocol-defined command is not automatically executable. Do not mark a protocol-defined command as prohibited unless it is out of scope, unsupported, or explicitly prohibited by user/project policy.

High-impact commands need conditions, parameters, impact notes, and recovery notes. Runtime logs remain outside Git.
