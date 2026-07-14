#!/usr/bin/env python3
"""Stage 0/1 read-only and Stage 2 RF-read verification helper.

Dry-run is the default. Real-device communication requires --execute and
an explicit connection target. Stage 2 command sets intentionally avoid writes,
setting changes, FLASH operations, and tag memory writes.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
import time
from pathlib import Path


PACKAGE_VERSION = "v020"
ROM_READ_PDF_SECTION = "7.3.8"
ROM_READ_COMMAND_BYTE = 0x4F
ROM_READ_DETAIL_BYTE = 0x90
ERROR_INFO_PDF_SECTION = "7.3.1"
ERROR_INFO_COMMAND_BYTE = 0x4F
ERROR_INFO_DETAIL_BYTE = 0x80
CHIP_VERSION_PDF_SECTION = "7.3.9"
CHIP_VERSION_COMMAND_BYTE = 0x55
CHIP_VERSION_DETAIL_BYTE = 0x90
CHIP_FIRMWARE_SUBCOMMAND_BYTE = 0x00
ACK_COMMAND_BYTE = 0x30
NACK_COMMAND_BYTE = 0x31
STAGE1_READABLE_PDF_SECTIONS = {
    "7.4.1",
    "7.4.2",
    "7.4.3",
    "7.4.4",
    "7.4.5",
    "7.4.6",
    "7.4.7",
    "7.4.8",
    "7.4.9",
    "7.4.11",
}
STAGE2_MINIMAL_PDF_SECTIONS = {
    "7.3.5",
    "7.3.12",
    "7.5.1",
}
STAGE2_READ_PDF_SECTIONS = {
    "7.3.5",
    "7.3.12",
    "7.5.1",
    "7.5.2",
    "7.5.3",
}
EIGHT_CHANNEL_ONLY_PDF_SECTIONS = {"7.4.10", "7.4.12"}
ROM_2100_OR_LATER_PDF_SECTIONS = {"7.4.14", "7.4.15"}
PARAMETER_BLOCKED_PDF_SECTIONS = {"7.4.13"}
SERIES_TO_PRODUCT = {
    "USM01": "UTR-S201",
    "USM02": "UTR-SUN02-4CH",
    "USM05": "UTR-SHR201",
    "USM06": "UTR-SUN02V-8CH",
    "USM08": "UTR-SUN02-8CH",
}
MEMORY_BANKS = {
    "reserved": 0x00,
    "epc": 0x01,
    "tid": 0x02,
    "user": 0x03,
}
MEMORY_BANK_LABELS = {value: name.upper() for name, value in MEMORY_BANKS.items()}
SAFE_TID_PROFILE = {
    "memory_bank": MEMORY_BANKS["tid"],
    "read_address": 0,
    "read_word_count": 2,
    "access_password": "00000000",
}


COMMANDS = [{'stage': 'stage0', 'pdf_section': '7.3.1', 'name': 'エラー情報の読み取り', 'command_byte': '4Fh', 'detail_command': '80h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_80_read_error_info.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '低影響の状態確認'}, {'stage': 'stage0', 'pdf_section': '7.3.8', 'name': 'ROMバージョンの読み取り', 'command_byte': '4Fh', 'detail_command': '90h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/rom_version_read.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '最初に実行し機種/シリーズ/ROMを判定', 'notes': '標準フローの起点'}, {'stage': 'stage0', 'pdf_section': '7.3.9', 'name': 'チップバージョンの読み取り', 'command_byte': '55h', 'detail_command': '90h', 'subcommand': '00h', 'card_path': 'docs/current/commands/cards/55_90_chip_version_read.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'v014 executes firmware-version subcommand 00h only; serial-number subcommand 01h is not executed'}, {'stage': 'stage1', 'pdf_section': '7.4.1', 'name': 'リーダライタ動作モードの読み取り', 'command_byte': '4Fh', 'detail_command': '00h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_00_read_reader_mode.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '設定変更は行わない'}, {'stage': 'stage1', 'pdf_section': '7.4.2', 'name': 'UHF_GetSelectParam', 'command_byte': '55h', 'detail_command': '40h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_40_uhf_get_select_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.3', 'name': 'UHF_GetInventoryParam', 'command_byte': '55h', 'detail_command': '41h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_41_uhf_get_inventory_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'SetInventoryParamは対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.4', 'name': 'UHF_GetExpandSelectParam', 'command_byte': '55h', 'detail_command': '42h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_42_uhf_get_expand_select_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.5', 'name': 'アンテナ切替設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '00h', 'card_path': 'docs/current/commands/cards/55_43_00_read_antenna_switching.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。切替設定変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.6', 'name': '出力設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '01h', 'card_path': 'docs/current/commands/cards/55_43_01_read_output_power.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。出力変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.7', 'name': '周波数設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '02h', 'card_path': 'docs/current/commands/cards/55_43_02_read_frequency.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。周波数変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.8', 'name': 'RFタグ通信関連パラメータの読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '04h', 'card_path': 'docs/current/commands/cards/55_43_04_read_rf_tag_comm_params.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.9', 'name': 'EPC(UII)関連パラメータの読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '05h', 'card_path': 'docs/current/commands/cards/55_43_05_read_epc_uii_params.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.10', 'name': '外部アンテナ自動切替設定の読み取り', 'command_byte': '55h', 'detail_command': '47h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '読み取りのみ。自動切替設定変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.11', 'name': '汎用ポート値の読み取り', 'command_byte': '4Fh', 'detail_command': '9Fh', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_9f_read_general_port.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '外部I/O状態読み取り'}, {'stage': 'stage1', 'pdf_section': '7.4.12', 'name': '拡張ポート値の読み取り', 'command_byte': '4Fh', 'detail_command': 'A0h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_a0_read_extended_port.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '外部I/O状態読み取り'}, {'stage': 'stage1', 'pdf_section': '7.4.13', 'name': 'FLASH設定値の読み取り(1バイトアクセス)', 'command_byte': '4Fh', 'detail_command': 'B4h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_b4_read_flash_settings.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。FLASH書き込みは対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.14', 'name': 'RSSIフィルタ設定の読み取り', 'command_byte': '55h', 'detail_command': '49h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_49_read_rssi_filter.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM 2.100以降対象の可能性。非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.15', 'name': 'アンテナ個別送信出力設定の読み取り', 'command_byte': '55h', 'detail_command': '4Ah', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_4a_read_antenna_output_power.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系またはROM条件依存の可能性。非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '読み取りのみ。出力変更は対象外'}]
STAGE2_MINIMAL_COMMANDS = [
    {
        "stage": "stage2-minimal",
        "pdf_section": "7.3.5",
        "name": "UHF_CheckAntenna",
        "command_byte": "55h",
        "detail_command": "44h",
        "subcommand": "-",
        "card_path": "docs/current/commands/cards/55_44_uhf_check_antenna.md",
        "expected_response": "ACK/NACK/timeout/antenna-error/LBT-error",
        "device_rom_condition": "ROM読み取りでUSM02 / ROM 2.052を確認後に実行",
        "notes": "v017 minimal target. No antenna setting change.",
    },
    {
        "stage": "stage2-minimal",
        "pdf_section": "7.3.12",
        "name": "UHF_GetHandle",
        "command_byte": "55h",
        "detail_command": "46h",
        "subcommand": "-",
        "card_path": "docs/current/commands/cards/55_46_uhf_get_handle.md",
        "expected_response": "ACK/NACK/timeout/no-tag",
        "device_rom_condition": "ROM 2.050以降。対象ROM 2.052で実行対象",
        "notes": "v017 minimal target. Tag not detected is recorded honestly, not forced to PASS.",
    },
    {
        "stage": "stage2-minimal",
        "pdf_section": "7.5.1",
        "name": "UHF_Inventory",
        "command_byte": "55h",
        "detail_command": "10h",
        "subcommand": "-",
        "card_path": "docs/current/commands/cards/55_10_uhf_inventory.md",
        "expected_response": "ACK/NACK/timeout/no-tag/multiple-response",
        "device_rom_condition": "ROM読み取りで機種判定後に実行",
        "notes": "v017 minimal target. InventoryRead and UHF_Read are outside v017 scope.",
    },
]
STAGE2_READ_EXTRA_COMMANDS = [
    {
        "stage": "stage2-read",
        "pdf_section": "7.5.2",
        "name": "UHF_InventoryRead",
        "command_byte": "55h",
        "detail_command": "14h",
        "subcommand": "-",
        "card_path": "docs/current/commands/cards/55_14_uhf_inventory_read.md",
        "expected_response": "ACK/NACK/timeout/multiple-response/completion-response",
        "device_rom_condition": "Inventoryでタグを検出し、MemBank/address/word countが確定した場合のみ実行",
        "notes": "v018 target only when read parameters are explicitly confirmed.",
    },
    {
        "stage": "stage2-read",
        "pdf_section": "7.5.3",
        "name": "UHF_Read",
        "command_byte": "55h",
        "detail_command": "15h",
        "subcommand": "-",
        "card_path": "docs/current/commands/cards/55_15_uhf_read.md",
        "expected_response": "ACK/NACK/timeout",
        "device_rom_condition": "Inventoryでタグを検出し、MemBank/address/word countが確定した場合のみ実行",
        "notes": "v018 target only when read parameters are explicitly confirmed.",
    },
]
STAGE3PLUS_COMMANDS = [
    {
        "stage_bucket": "Stage 3 tag memory write",
        "pdf_section": "7.5.4",
        "name": "UHF_Write",
        "command_bytes": "55h/16h",
        "command_group": "RFタグ通信",
        "operation_category": "write/tag-memory",
        "impact_category": "TAG_MEMORY_WRITE",
        "persistent_change": "tag memory",
        "tag_memory_change": "yes",
        "irreversible_operation": "no",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "yes",
        "requires_target_epc_uii": "yes",
        "requires_memory_bank": "yes",
        "requires_address": "yes",
        "requires_word_count": "yes",
        "requires_access_password": "depends",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_16_uhf_write.md",
        "notes": "Tag memory write. Explicit approval, target tag, write data, and recovery limits are required.",
    },
    {
        "stage_bucket": "Stage 3 irreversible tag operation",
        "pdf_section": "7.5.5",
        "name": "UHF_Kill",
        "command_bytes": "55h/17h",
        "command_group": "RFタグ通信",
        "operation_category": "irreversible/tag-kill",
        "impact_category": "IRREVERSIBLE_TAG_OPERATION",
        "persistent_change": "tag state",
        "tag_memory_change": "irreversible",
        "irreversible_operation": "yes",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "yes",
        "requires_target_epc_uii": "yes",
        "requires_memory_bank": "no",
        "requires_address": "no",
        "requires_word_count": "no",
        "requires_access_password": "yes",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_17_uhf_kill.md",
        "notes": "Irreversible tag kill. Requires explicit approval and isolated disposable target tag conditions.",
    },
    {
        "stage_bucket": "Stage 3 irreversible tag operation",
        "pdf_section": "7.5.6",
        "name": "UHF_Lock",
        "command_bytes": "55h/18h",
        "command_group": "RFタグ通信",
        "operation_category": "lock/tag-memory",
        "impact_category": "TAG_LOCK_OR_PERMISSION_CHANGE",
        "persistent_change": "tag lock state",
        "tag_memory_change": "lock state",
        "irreversible_operation": "possible",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "yes",
        "requires_target_epc_uii": "yes",
        "requires_memory_bank": "depends",
        "requires_address": "no",
        "requires_word_count": "no",
        "requires_access_password": "yes",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_18_uhf_lock.md",
        "notes": "Lock state may be irreversible depending on parameters. Do not execute without recovery decision.",
    },
    {
        "stage_bucket": "Stage 3 tag memory write",
        "pdf_section": "7.5.7",
        "name": "UHF_BlockWrite",
        "command_bytes": "55h/1Ah",
        "command_group": "RFタグ通信",
        "operation_category": "block-write/tag-memory",
        "impact_category": "TAG_MEMORY_WRITE",
        "persistent_change": "tag memory",
        "tag_memory_change": "yes",
        "irreversible_operation": "no",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "yes",
        "requires_target_epc_uii": "yes",
        "requires_memory_bank": "yes",
        "requires_address": "yes",
        "requires_word_count": "yes",
        "requires_access_password": "depends",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_1a_uhf_block_write.md",
        "notes": "Block write changes tag memory and requires explicit data and recovery limits.",
    },
    {
        "stage_bucket": "Stage 3 tag memory write",
        "pdf_section": "7.5.8",
        "name": "UHF_BlockErase",
        "command_bytes": "55h/1Bh",
        "command_group": "RFタグ通信",
        "operation_category": "block-erase/tag-memory",
        "impact_category": "TAG_MEMORY_ERASE",
        "persistent_change": "tag memory",
        "tag_memory_change": "erase",
        "irreversible_operation": "possible",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "yes",
        "requires_target_epc_uii": "yes",
        "requires_memory_bank": "yes",
        "requires_address": "yes",
        "requires_word_count": "yes",
        "requires_access_password": "depends",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_1b_uhf_block_erase.md",
        "notes": "Erase operation may not be recoverable from device side.",
    },
    {
        "stage_bucket": "Stage 3 tag memory write",
        "pdf_section": "7.5.9",
        "name": "UHF_BlockWrite2",
        "command_bytes": "55h/1Dh",
        "command_group": "RFタグ通信",
        "operation_category": "block-write/tag-memory",
        "impact_category": "TAG_MEMORY_WRITE_PARTIAL_FAILURE_RISK",
        "persistent_change": "tag memory",
        "tag_memory_change": "yes",
        "irreversible_operation": "possible",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "yes",
        "requires_target_epc_uii": "yes",
        "requires_memory_bank": "yes",
        "requires_address": "yes",
        "requires_word_count": "yes",
        "requires_access_password": "depends",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_1d_uhf_block_write2.md",
        "notes": "Partial-failure diagnostics must be planned before execution.",
    },
    {
        "stage_bucket": "Stage 3 tag memory write",
        "pdf_section": "7.5.10",
        "name": "UHF_Encode",
        "command_bytes": "55h/1Eh",
        "command_group": "RFタグ通信",
        "operation_category": "encode/tag-memory",
        "impact_category": "TAG_ENCODING",
        "persistent_change": "tag memory and lock state possible",
        "tag_memory_change": "yes",
        "irreversible_operation": "possible",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "yes",
        "requires_target_epc_uii": "yes",
        "requires_memory_bank": "yes",
        "requires_address": "yes",
        "requires_word_count": "yes",
        "requires_access_password": "depends",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_1e_uhf_encode.md",
        "notes": "Encode can affect multiple tag fields. Use isolated disposable tags only after explicit approval.",
    },
    {
        "stage_bucket": "Stage 3 advanced RF command",
        "pdf_section": "7.5.11",
        "name": "UHF_ThroughCmd",
        "command_bytes": "55h/FFh",
        "command_group": "RFタグ通信",
        "operation_category": "through/advanced",
        "impact_category": "ADVANCED_UNBOUNDED_TAG_OPERATION",
        "persistent_change": "depends on payload",
        "tag_memory_change": "depends on payload",
        "irreversible_operation": "depends on payload",
        "rf_emission": "yes",
        "requires_rom_check": "yes",
        "requires_antenna": "yes",
        "requires_tag": "depends",
        "requires_target_epc_uii": "depends",
        "requires_memory_bank": "depends",
        "requires_address": "depends",
        "requires_word_count": "depends",
        "requires_access_password": "depends",
        "requires_recovery_plan": "yes",
        "card_path": "docs/current/commands/cards/55_ff_uhf_through_cmd.md",
        "notes": "Through command impact depends on payload. Payload review is mandatory.",
    },
]

STAGE3PLUS_COMMANDS += [
    {
        "stage_bucket": "Stage 4 reader configuration write",
        "pdf_section": section,
        "name": name,
        "command_bytes": command_bytes,
        "command_group": "リーダライタ設定",
        "operation_category": operation,
        "impact_category": impact,
        "persistent_change": persistent,
        "tag_memory_change": "no",
        "irreversible_operation": irreversible,
        "rf_emission": rf,
        "requires_rom_check": "yes",
        "requires_antenna": antenna,
        "requires_tag": "no",
        "requires_target_epc_uii": "no",
        "requires_memory_bank": "no",
        "requires_address": address,
        "requires_word_count": "no",
        "requires_access_password": access,
        "requires_recovery_plan": "yes",
        "card_path": card,
        "notes": notes,
    }
    for section, name, command_bytes, operation, impact, persistent, irreversible, rf, antenna, address, access, card, notes in [
        ("7.4.16", "リーダライタ動作モードの書き込み", "4Eh/00h/10h", "configuration-write", "READER_MODE_CHANGE", "RAM or FLASH depending on target", "no", "no", "no", "no", "no", "docs/current/commands/cards/4e_00_10_write_reader_mode.md", "Reader operating mode change requires rollback plan."),
        ("7.4.17", "UHF_SetSelectParam", "55h/30h", "configuration-write", "SELECT_PARAM_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_30_uhf_set_select_param.md", "Selection parameter changes affect subsequent RF tag operations."),
        ("7.4.18", "UHF_SetInventoryParam", "55h/31h", "configuration-write", "INVENTORY_PARAM_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_31_uhf_set_inventory_param.md", "Inventory parameter changes affect RF behavior and read results."),
        ("7.4.19", "UHF_SetExpandSelectParam", "55h/32h", "configuration-write", "EXPAND_SELECT_PARAM_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_32_uhf_set_expand_select_param.md", "Expanded selection parameters require current-setting backup."),
        ("7.4.20", "アンテナ切替設定の書き込み", "55h/33h/00h", "configuration-write", "ANTENNA_SWITCH_SETTING_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_33_00_write_antenna_switching.md", "Antenna switching setting changes can affect RF routing."),
        ("7.4.21", "出力設定の書き込み", "55h/33h/01h", "configuration-write", "OUTPUT_POWER_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_33_01_write_output_power.md", "Output power changes require legal/site confirmation."),
        ("7.4.22", "周波数設定の書き込み", "55h/33h/02h", "configuration-write", "FREQUENCY_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_33_02_write_frequency.md", "Frequency changes require legal/site confirmation."),
        ("7.4.23", "Accessパスワードの書き込み", "55h/33h/03h", "configuration-write", "ACCESS_PASSWORD_CHANGE", "RAM/configuration", "possible", "no", "no", "no", "yes", "docs/current/commands/cards/55_33_03_write_access_password.md", "Password changes require credential and recovery policy."),
        ("7.4.24", "RFタグ通信関連パラメータの書き込み", "55h/33h/04h", "configuration-write", "RF_TAG_COMM_PARAM_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_33_04_write_rf_tag_comm_params.md", "RF communication parameter changes require baseline backup."),
        ("7.4.25", "EPC(UII)関連パラメータの書き込み", "55h/33h/05h", "configuration-write", "EPC_UII_PARAM_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_33_05_write_epc_uii_params.md", "EPC/UII parameter changes affect tag parsing and response behavior."),
        ("7.4.26", "外部アンテナ自動切替設定の書き込み", "55h/37h", "configuration-write", "EXTERNAL_ANTENNA_AUTO_SWITCH_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_37_write_external_antenna_auto_switch.md", "8CH-related automatic switching requires device/ROM and wiring confirmation."),
        ("7.4.27", "汎用ポート値の書き込み", "4Eh/9Fh", "configuration-write", "GENERAL_PORT_OUTPUT_CHANGE", "external I/O", "no", "no", "no", "no", "no", "docs/current/commands/cards/4e_9f_write_general_port.md", "External I/O state changes require connected equipment review."),
        ("7.4.28", "拡張ポート値の書き込み", "4Eh/A0h", "configuration-write", "EXTENDED_PORT_OUTPUT_CHANGE", "external I/O", "no", "no", "no", "no", "no", "docs/current/commands/cards/4e_a0_write_extended_port.md", "Extended I/O changes require connected equipment review."),
        ("7.4.29", "FLASH設定値の書き込み(1バイトアクセス)", "4Eh/B4h", "flash-write", "FLASH_ONE_BYTE_WRITE", "FLASH/persistent", "possible", "no", "no", "yes", "no", "docs/current/commands/cards/4e_b4_flash_write.md", "Persistent FLASH write requires backup and recovery plan."),
        ("7.4.30", "RSSIフィルタ設定の書き込み", "55h/39h", "configuration-write", "RSSI_FILTER_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_39_write_rssi_filter.md", "RSSI filtering changes tag detection behavior."),
        ("7.4.31", "アンテナ個別送信出力設定の書き込み", "55h/3Ah", "configuration-write", "ANTENNA_OUTPUT_POWER_CHANGE", "RAM/configuration", "no", "yes", "yes", "no", "no", "docs/current/commands/cards/55_3a_write_antenna_output_power.md", "Per-antenna output changes require legal/site confirmation."),
    ]
]

STAGE3PLUS_COMMANDS += [
    {
        "stage_bucket": "Stage 5 reader control high-impact",
        "pdf_section": section,
        "name": name,
        "command_bytes": command_bytes,
        "command_group": "リーダライタ制御",
        "operation_category": operation,
        "impact_category": impact,
        "persistent_change": persistent,
        "tag_memory_change": "no",
        "irreversible_operation": irreversible,
        "rf_emission": rf,
        "requires_rom_check": "yes",
        "requires_antenna": antenna,
        "requires_tag": "no",
        "requires_target_epc_uii": "no",
        "requires_memory_bank": "no",
        "requires_address": "no",
        "requires_word_count": "no",
        "requires_access_password": "no",
        "requires_recovery_plan": "yes",
        "card_path": card,
        "notes": notes,
    }
    for section, name, command_bytes, operation, impact, persistent, irreversible, rf, antenna, card, notes in [
        ("7.3.4", "RF送信信号の制御", "4Eh/9Eh", "rf-carrier-control", "RF_CARRIER_CONTROL", "runtime state", "no", "yes", "yes", "docs/current/commands/cards/4e_9e_rf_carrier_control.md", "RF carrier control requires site/legal confirmation and stop conditions."),
        ("7.3.7", "使用アンテナ番号の書き込み", "55h/38h", "antenna-selection-write", "ACTIVE_ANTENNA_CHANGE", "runtime configuration", "no", "yes", "yes", "docs/current/commands/cards/55_38_write_active_antenna.md", "Active antenna changes require wiring and recovery confirmation."),
        ("7.3.10", "リスタート", "4Eh/9Dh", "restart", "READER_RESTART", "device runtime state", "no", "no", "no", "docs/current/commands/cards/4e_9d_restart_reader.md", "Restart interrupts device operation and requires reconnection plan."),
        ("7.3.11", "FLASH設定の初期化", "4Eh/6Fh", "flash-initialize", "FLASH_INITIALIZE", "FLASH/persistent", "possible", "no", "no", "docs/current/commands/cards/4e_6f_flash_initialize.md", "FLASH initialization requires backup and recovery plan."),
    ]
]

LOG_FIELDS = ['log_id', 'date_time', 'operator', 'repository_version', 'package_version', 'command_card', 'pdf_section', 'command_name', 'command_byte', 'detail_command', 'subcommand', 'device_series', 'product_type', 'rom_version', 'connection_type', 'port_or_ip', 'baudrate_or_socket', 'antenna_count', 'active_antenna', 'antenna_switching_mode', 'target_tag_count', 'target_memory_bank', 'parameter_summary', 'ram_flash_impact', 'rf_impact', 'tag_memory_impact', 'recovery_required', 'pre_read_required', 'expected_response_type', 'actual_response_type', 'ack_summary', 'nack_error_code_1', 'nack_error_code_2', 'nack_error_code_3', 'nack_error_code_4', 'timeout_ms', 'elapsed_ms', 'raw_response_hex', 'raw_log_file', 'result_status', 'notes']


def mask_value(value: str, enabled: bool = True) -> str:
    if not enabled:
        return value
    if value.upper().startswith("COM"):
        return "COMx"
    parts = value.split(".")
    if len(parts) == 4 and all(part.isdigit() for part in parts):
        return f"{parts[0]}.{parts[1]}.xxx.xxx"
    return value


def mask_epc(hex_value: str, enabled: bool = True) -> str:
    cleaned = "".join(ch for ch in hex_value.upper() if ch in "0123456789ABCDEF")
    if not cleaned:
        return ""
    if not enabled:
        return cleaned
    visible = cleaned[:4] if len(cleaned) >= 4 else cleaned
    return f"EPC_{visible}{'x' * max(len(cleaned) - len(visible), 0)}"


def mask_tag_identifier(hex_value: str, enabled: bool = True, prefix: str = "TAG") -> str:
    cleaned = "".join(ch for ch in hex_value.upper() if ch in "0123456789ABCDEF")
    if not cleaned:
        return ""
    if not enabled:
        return f"{prefix}_{cleaned}"
    visible = cleaned[:4] if len(cleaned) >= 4 else cleaned
    return f"{prefix}_{visible}{'x' * max(len(cleaned) - len(visible), 0)}"


def calculate_sum(frame_without_sum: bytes) -> int:
    """Return lower one byte of the byte-wise sum from STX through ETX."""
    return sum(frame_without_sum) & 0xFF


def build_common_frame(address: int, command_byte: int, data: bytes) -> bytes:
    prefix = bytes([0x02, address, command_byte, len(data)]) + data + bytes([0x03])
    return prefix + bytes([calculate_sum(prefix), 0x0D])


def is_v014_sendable(command: dict[str, str]) -> bool:
    return command["pdf_section"] in {
        ROM_READ_PDF_SECTION,
        CHIP_VERSION_PDF_SECTION,
        ERROR_INFO_PDF_SECTION,
    }


def is_v015_sendable(command: dict[str, str]) -> bool:
    return command["pdf_section"] == ROM_READ_PDF_SECTION or command["stage"] == "stage1"


def is_v017_stage2_minimal_sendable(command: dict[str, str]) -> bool:
    return command["pdf_section"] == ROM_READ_PDF_SECTION or command["pdf_section"] in STAGE2_MINIMAL_PDF_SECTIONS


def is_v018_stage2_read_sendable(command: dict[str, str]) -> bool:
    return command["pdf_section"] == ROM_READ_PDF_SECTION or command["pdf_section"] in STAGE2_READ_PDF_SECTIONS


def v015_scope_label(command: dict[str, str]) -> str:
    if command["pdf_section"] == ROM_READ_PDF_SECTION or command["pdf_section"] in STAGE1_READABLE_PDF_SECTIONS:
        return "sendable-in-v015"
    if command["stage"] == "stage1":
        return "gated-in-v015"
    return "not-executed-in-v015"


def command_scope_label(command: dict[str, str], command_set: str) -> str:
    if command_set == "stage2-minimal":
        if is_v017_stage2_minimal_sendable(command):
            return "sendable-in-v017-stage2-minimal"
        return "not-executed-in-v017"
    if command_set == "stage2-read":
        if is_v018_stage2_read_sendable(command):
            return "sendable-or-gated-in-v019-stage2-read"
        return "not-executed-in-v019"
    return v015_scope_label(command)


def build_rom_version_read_frame(address: int = 0x00) -> bytes:
    return build_common_frame(address, ROM_READ_COMMAND_BYTE, bytes([ROM_READ_DETAIL_BYTE]))


def build_chip_version_read_frame(address: int = 0x00) -> bytes:
    return build_common_frame(
        address,
        CHIP_VERSION_COMMAND_BYTE,
        bytes([CHIP_VERSION_DETAIL_BYTE, CHIP_FIRMWARE_SUBCOMMAND_BYTE]),
    )


def build_error_info_read_frame(address: int = 0x00) -> bytes:
    return build_common_frame(address, ERROR_INFO_COMMAND_BYTE, bytes([ERROR_INFO_DETAIL_BYTE]))


def build_stage1_readonly_frame(command: dict[str, str], address: int = 0x00) -> bytes:
    section = command["pdf_section"]
    if section == "7.4.1":
        return build_common_frame(address, 0x4F, bytes([0x00]))
    if section == "7.4.2":
        return build_common_frame(address, 0x55, bytes([0x40, 0x00]))
    if section == "7.4.3":
        return build_common_frame(address, 0x55, bytes([0x41, 0x00]))
    if section == "7.4.4":
        return build_common_frame(address, 0x55, bytes([0x42, 0x00, 0x01]))
    if section == "7.4.5":
        return build_common_frame(address, 0x55, bytes([0x43, 0x00, 0x00]))
    if section == "7.4.6":
        return build_common_frame(address, 0x55, bytes([0x43, 0x01, 0x00]))
    if section == "7.4.7":
        return build_common_frame(address, 0x55, bytes([0x43, 0x02, 0x00]))
    if section == "7.4.8":
        return build_common_frame(address, 0x55, bytes([0x43, 0x04, 0x00]))
    if section == "7.4.9":
        return build_common_frame(address, 0x55, bytes([0x43, 0x05, 0x00]))
    if section == "7.4.11":
        return build_common_frame(address, 0x4F, bytes([0x9F]))
    raise ValueError("Stage 1 command requires device/ROM/parameter gating before send")


def build_stage2_minimal_frame(command: dict[str, str], address: int = 0x00) -> bytes:
    section = command["pdf_section"]
    if section == "7.3.5":
        return build_common_frame(address, 0x55, bytes([0x44]))
    if section == "7.3.12":
        return build_common_frame(address, 0x55, bytes([0x46]))
    if section == "7.5.1":
        return build_common_frame(address, 0x55, bytes([0x10]))
    raise ValueError("command is outside v017 Stage 2 minimal execution scope")


def memory_bank_label(value: int | None) -> str:
    if value is None:
        return "not-specified"
    return f"{MEMORY_BANK_LABELS.get(value, 'UNKNOWN')}({value})"


def resolve_read_profile(args: argparse.Namespace) -> argparse.Namespace:
    if args.read_profile in (None, "none"):
        return args
    if args.read_profile != "safe-tid":
        raise ValueError(f"unsupported read profile: {args.read_profile}")
    if args.read_memory_bank is None:
        args.read_memory_bank = SAFE_TID_PROFILE["memory_bank"]
    if args.read_address is None:
        args.read_address = SAFE_TID_PROFILE["read_address"]
    if args.read_word_count is None:
        args.read_word_count = SAFE_TID_PROFILE["read_word_count"]
    if args.access_password is None:
        args.access_password = SAFE_TID_PROFILE["access_password"]
    return args


def read_parameter_summary(args: argparse.Namespace) -> str:
    if args.read_memory_bank is None or args.read_address is None or args.read_word_count is None:
        return "read parameters: not fully specified"
    password_policy = "default-zero" if args.access_password == "00000000" else "specified-or-not-used"
    return (
        f"read_profile={args.read_profile or 'none'}; "
        f"memory_bank={memory_bank_label(args.read_memory_bank)}; "
        f"word_address={args.read_address}; "
        f"word_count={args.read_word_count}; "
        f"access_password_policy={password_policy}; "
        f"max_tags={args.max_tags}"
    )


def read_parameter_bytes(args: argparse.Namespace) -> bytes | None:
    if args.read_memory_bank is None or args.read_address is None or args.read_word_count is None:
        return None
    if not 0 <= args.read_memory_bank <= 0x03:
        raise ValueError("--read-memory-bank must be between 0 and 3")
    if not 0 <= args.read_address <= 0xFFFFFFFF:
        raise ValueError("--read-address must be between 0 and 0xFFFFFFFF")
    if not 1 <= args.read_word_count <= 32:
        raise ValueError("--read-word-count must be between 1 and 32")
    return bytes([args.read_memory_bank]) + int(args.read_address).to_bytes(4, "big") + bytes([args.read_word_count])


def build_inventory_read_frame(args: argparse.Namespace, address: int = 0x00) -> bytes:
    params = read_parameter_bytes(args)
    if params is None:
        raise ValueError("read parameters are not fully specified")
    return build_common_frame(address, 0x55, bytes([0x14]) + params)


def build_uhf_read_frame(args: argparse.Namespace, address: int = 0x00) -> bytes:
    params = read_parameter_bytes(args)
    if params is None:
        raise ValueError("read parameters are not fully specified")
    return build_common_frame(address, 0x55, bytes([0x15]) + params)


def build_stage2_read_frame(command: dict[str, str], args: argparse.Namespace, address: int = 0x00) -> bytes:
    section = command["pdf_section"]
    if section in {"7.3.5", "7.3.12", "7.5.1"}:
        return build_stage2_minimal_frame(command, address)
    if section == "7.5.2":
        return build_inventory_read_frame(args, address)
    if section == "7.5.3":
        return build_uhf_read_frame(args, address)
    raise ValueError("command is outside v018 Stage 2 read execution scope")


def parse_common_response(raw_response: bytes) -> dict[str, object]:
    if not raw_response:
        return {"type": "timeout", "valid": False, "error": "no response"}
    if len(raw_response) < 7:
        return {"type": "invalid", "valid": False, "error": "response shorter than common frame"}
    if raw_response[0] != 0x02:
        return {"type": "invalid", "valid": False, "error": "missing STX"}
    data_length = raw_response[3]
    expected_length = data_length + 7
    if len(raw_response) < expected_length:
        return {"type": "invalid", "valid": False, "error": "incomplete response"}
    frame = raw_response[:expected_length]
    etx_index = 4 + data_length
    sum_index = etx_index + 1
    cr_index = sum_index + 1
    if frame[etx_index] != 0x03:
        return {"type": "invalid", "valid": False, "error": "missing ETX at expected position"}
    if frame[cr_index] != 0x0D:
        return {"type": "invalid", "valid": False, "error": "missing CR at expected position"}
    expected_sum = calculate_sum(frame[: etx_index + 1])
    if frame[sum_index] != expected_sum:
        return {"type": "invalid", "valid": False, "error": "SUM mismatch"}

    command_byte = frame[2]
    if command_byte == ACK_COMMAND_BYTE:
        response_type = "ACK"
    elif command_byte == NACK_COMMAND_BYTE:
        response_type = "NACK"
    else:
        response_type = "unknown-response"
    return {
        "type": response_type,
        "valid": True,
        "address": frame[1],
        "command_byte": command_byte,
        "data_length": data_length,
        "data": frame[4:etx_index],
        "frame_length": expected_length,
    }


def split_common_frames(raw_response: bytes) -> list[bytes]:
    frames: list[bytes] = []
    index = 0
    while index < len(raw_response):
        try:
            stx_index = raw_response.index(0x02, index)
        except ValueError:
            break
        if stx_index + 4 > len(raw_response):
            break
        data_length = raw_response[stx_index + 3]
        expected_length = data_length + 7
        frame = raw_response[stx_index : stx_index + expected_length]
        if len(frame) < expected_length:
            break
        frames.append(frame)
        index = stx_index + expected_length
    return frames


def receive_until_completion(ser: object, timeout_sec: float, command: dict[str, str]) -> bytes:
    deadline = time.perf_counter() + timeout_sec
    chunks = bytearray()
    while time.perf_counter() < deadline:
        chunk = ser.read(1)
        if chunk:
            chunks.extend(chunk)
            frames = split_common_frames(bytes(chunks))
            if command["pdf_section"] not in {"7.5.1", "7.5.2"} and chunk == b"\x0d":
                break
            if command["pdf_section"] in {"7.5.1", "7.5.2"} and inventory_completion_seen(frames):
                break
    return bytes(chunks)


def parsed_frames(raw_response: bytes) -> list[dict[str, object]]:
    return [parse_common_response(frame) for frame in split_common_frames(raw_response)]


def inventory_completion_seen(frames: list[bytes]) -> bool:
    for frame in frames:
        parsed = parse_common_response(frame)
        if parsed.get("type") == "NACK":
            return True
        data = parsed.get("data", b"")
        if isinstance(data, (bytes, bytearray)) and len(data) >= 3 and data and data[0] in {0x10, 0x14}:
            return True
    return False


def parse_inventory_response(raw_response: bytes, mask_sensitive: bool = True, max_tags: int = 3) -> dict[str, str]:
    frames = parsed_frames(raw_response)
    valid_frames = [frame for frame in frames if frame.get("valid")]
    nacks = [frame for frame in valid_frames if frame.get("type") == "NACK"]
    completions = []
    tag_frames = []
    masked_epcs = []
    for frame in valid_frames:
        data = frame.get("data", b"")
        if not isinstance(data, (bytes, bytearray)) or not data:
            continue
        if len(data) >= 3 and data[0] in {0x10, 0x14} and frame.get("type") == "ACK":
            if len(data) >= 4:
                count = data[2] + (data[3] << 8)
            else:
                count = data[1] + (data[2] << 8)
            completions.append(count)
        elif frame.get("type") != "NACK":
            tag_frames.append(frame)
            if len(data) > 7:
                if len(masked_epcs) < max_tags:
                    masked_epcs.append(mask_tag_identifier(bytes(data[7:]).hex(), mask_sensitive, "EPC"))
    completion_count = completions[-1] if completions else None
    parsed_tag_count = completion_count if completion_count is not None else len(tag_frames)
    return {
        "frame_count": str(len(frames)),
        "valid_frame_count": str(len(valid_frames)),
        "nack_count": str(len(nacks)),
        "completion_count": "" if completion_count is None else str(completion_count),
        "parsed_tag_count": str(parsed_tag_count),
        "masked_epc_summary": ",".join(masked_epcs[:3]),
        "raw_summary": f"frames={len(frames)}; valid={len(valid_frames)}; completion={completion_count}; tag_frames={len(tag_frames)}",
    }


def parse_inventory_read_response(raw_response: bytes, mask_sensitive: bool = True, max_tags: int = 3) -> dict[str, str]:
    summary = parse_inventory_response(raw_response, mask_sensitive, max_tags)
    summary["operation"] = "InventoryRead"
    return summary


def parse_uhf_read_response(raw_response: bytes, mask_sensitive: bool = True) -> dict[str, str]:
    frames = parsed_frames(raw_response)
    valid_frames = [frame for frame in frames if frame.get("valid")]
    nacks = [frame for frame in valid_frames if frame.get("type") == "NACK"]
    ack_frames = [frame for frame in valid_frames if frame.get("type") == "ACK"]
    return {
        "frame_count": str(len(frames)),
        "valid_frame_count": str(len(valid_frames)),
        "nack_count": str(len(nacks)),
        "ack_count": str(len(ack_frames)),
        "raw_summary": f"frames={len(frames)}; valid={len(valid_frames)}; ack={len(ack_frames)}; nack={len(nacks)}",
    }


def format_rom_version(rom_raw: str) -> str:
    if len(rom_raw) == 4 and rom_raw.isdigit():
        return f"{int(rom_raw[0])}.{rom_raw[1:]}"
    return rom_raw


def parse_rom_version_ack(parsed: dict[str, object]) -> dict[str, str]:
    data = parsed.get("data", b"")
    if not isinstance(data, (bytes, bytearray)):
        raise ValueError("ACK data is not bytes")
    if len(data) != 10:
        raise ValueError("ROM ACK data length is not 10")
    if data[0] != ROM_READ_DETAIL_BYTE:
        raise ValueError("ROM ACK detail command is not 90h")
    rom_raw = bytes(data[1:5]).decode("ascii", errors="replace")
    series_name = bytes(data[5:10]).decode("ascii", errors="replace")
    return {
        "rom_raw": rom_raw,
        "rom_version": format_rom_version(rom_raw),
        "series_name": series_name,
        "product_type": SERIES_TO_PRODUCT.get(series_name, "UNKNOWN_SERIES"),
    }


def parse_chip_version_ack(parsed: dict[str, object]) -> dict[str, str]:
    data = parsed.get("data", b"")
    if not isinstance(data, (bytes, bytearray)):
        raise ValueError("ACK data is not bytes")
    if len(data) != 11:
        raise ValueError("chip version ACK data length is not 11")
    if data[0] != CHIP_VERSION_DETAIL_BYTE or data[1] != CHIP_FIRMWARE_SUBCOMMAND_BYTE:
        raise ValueError("chip version ACK detail/subcommand mismatch")
    chip_raw = bytes(data[2:6]).decode("ascii", errors="replace")
    chip_name = bytes(data[6:11]).decode("ascii", errors="replace")
    return {
        "chip_raw": chip_raw,
        "chip_version": format_rom_version(chip_raw),
        "chip_name": chip_name,
    }


def parse_error_info_ack(parsed: dict[str, object]) -> dict[str, str]:
    data = parsed.get("data", b"")
    if not isinstance(data, (bytes, bytearray)):
        raise ValueError("ACK data is not bytes")
    if len(data) != 4:
        raise ValueError("error information ACK data length is not 4")
    if data[0] != ERROR_INFO_DETAIL_BYTE:
        raise ValueError("error information ACK detail command mismatch")
    error_info = data[1]
    return {
        "error_info": f"{error_info:02X}h",
        "error_status": "normal" if error_info == 0 else "abnormal",
        "reserved_1": f"{data[2]:02X}h",
        "reserved_2": f"{data[3]:02X}h",
    }


def parse_stage1_ack_summary(command: dict[str, str], parsed: dict[str, object]) -> str:
    data = parsed.get("data", b"")
    if not isinstance(data, (bytes, bytearray)) or not data:
        return "ACK data unavailable"
    section = command["pdf_section"]
    if section == "7.4.1":
        mode = data[1] if len(data) > 1 else None
        mode_label = {0x00: "command mode", 0x65: "UHF continuous inventory mode", 0x66: "UHF continuous inventory-read mode"}.get(mode, "unknown")
        return f"reader mode={mode_label}; data_length={parsed.get('data_length')}"
    if section in {"7.4.2", "7.4.3", "7.4.4"}:
        parameter_kind = f"{data[1]:02X}h" if len(data) > 1 else "unknown"
        return f"parameter kind={parameter_kind}; data_length={parsed.get('data_length')}"
    if section in {"7.4.5", "7.4.6", "7.4.7", "7.4.8", "7.4.9"}:
        subcommand = f"{data[1]:02X}h" if len(data) > 1 else "unknown"
        parameter_kind = f"{data[2]:02X}h" if len(data) > 2 else "unknown"
        return f"subcommand={subcommand}; parameter kind={parameter_kind}; data_length={parsed.get('data_length')}"
    if section == "7.4.11":
        return f"general port values read; data_length={parsed.get('data_length')}"
    return f"ACK; data_length={parsed.get('data_length')}"


def parse_stage2_minimal_ack_summary(command: dict[str, str], parsed: dict[str, object]) -> str:
    data = parsed.get("data", b"")
    if not isinstance(data, (bytes, bytearray)):
        return "ACK data unavailable"
    section = command["pdf_section"]
    if section == "7.3.5":
        return f"antenna check ACK; data_length={parsed.get('data_length')}"
    if section == "7.3.12":
        return f"handle response ACK; data_length={parsed.get('data_length')}"
    if section == "7.5.1":
        return f"inventory response ACK; data_length={parsed.get('data_length')}"
    return f"ACK; data_length={parsed.get('data_length')}"


def rom_version_to_number(rom_version: str) -> int | None:
    digits = "".join(ch for ch in rom_version if ch.isdigit())
    if len(digits) == 4:
        return int(digits)
    return None


def stage1_block_reason(command: dict[str, str], rom_context: dict[str, str]) -> tuple[str | None, str | None]:
    section = command["pdf_section"]
    series = rom_context.get("device_series", "")
    rom_number = rom_version_to_number(rom_context.get("rom_version", ""))
    if section in EIGHT_CHANNEL_ONLY_PDF_SECTIONS and series not in {"USM06", "USM08"}:
        return "NOT_APPLICABLE_TO_TARGET", "8CH-specific command; target is not USM06/USM08."
    if section in ROM_2100_OR_LATER_PDF_SECTIONS and (rom_number is None or rom_number < 2100):
        return "BLOCKED_BY_DEVICE_OR_ROM", "Command requires ROM 2.100 or later; target ROM is lower."
    if section in PARAMETER_BLOCKED_PDF_SECTIONS:
        return "BLOCKED_BY_PARAMETER", "Read address is required and was not specified for v015."
    return None, None


def parse_nack_errors(parsed: dict[str, object]) -> dict[str, str]:
    data = parsed.get("data", b"")
    if not isinstance(data, (bytes, bytearray)) or len(data) < 5:
        return {
            "detail_command": "",
            "error_code_1": "",
            "error_code_2": "",
            "error_code_3": "",
            "error_code_4": "",
        }
    return {
        "detail_command": f"{data[0]:02X}h",
        "error_code_1": f"{data[1]:02X}h",
        "error_code_2": f"{data[2]:02X}h",
        "error_code_3": f"{data[3]:02X}h",
        "error_code_4": f"{data[4]:02X}h",
    }


def read_until_cr(ser: object, timeout_sec: float) -> bytes:
    deadline = time.perf_counter() + timeout_sec
    chunks = bytearray()
    while time.perf_counter() < deadline:
        chunk = ser.read(1)
        if chunk:
            chunks.extend(chunk)
            if chunk == b"\x0d":
                break
    return bytes(chunks)


def select_commands(command_set: str) -> list[dict[str, str]]:
    if command_set == "stage3plus-plan":
        return []
    if command_set == "all":
        stage0_order = {ROM_READ_PDF_SECTION: 0, CHIP_VERSION_PDF_SECTION: 1, ERROR_INFO_PDF_SECTION: 2}
        stage1_order = {f"7.4.{number}": number for number in range(1, 16)}
        return sorted(
            COMMANDS,
            key=lambda command: (
                0 if command["stage"] == "stage0" else 1,
                stage0_order.get(command["pdf_section"], 99) if command["stage"] == "stage0" else stage1_order.get(command["pdf_section"], 99),
            ),
        )
    commands = [command for command in COMMANDS if command["stage"] == command_set]
    if command_set == "stage0":
        order = {ROM_READ_PDF_SECTION: 0, CHIP_VERSION_PDF_SECTION: 1, ERROR_INFO_PDF_SECTION: 2}
        return sorted(commands, key=lambda command: order.get(command["pdf_section"], 99))
    if command_set == "stage1":
        rom_command = next(command for command in COMMANDS if command["pdf_section"] == ROM_READ_PDF_SECTION)
        return [rom_command, *commands]
    if command_set == "stage2-minimal":
        rom_command = next(command for command in COMMANDS if command["pdf_section"] == ROM_READ_PDF_SECTION)
        return [rom_command, *STAGE2_MINIMAL_COMMANDS]
    if command_set == "stage2-read":
        rom_command = next(command for command in COMMANDS if command["pdf_section"] == ROM_READ_PDF_SECTION)
        return [rom_command, *STAGE2_MINIMAL_COMMANDS, *STAGE2_READ_EXTRA_COMMANDS]
    return commands


def print_stage3plus_plan(execute_requested: bool = False) -> None:
    print("Stage 3+ high-impact command readiness plan:")
    print("- mode: plan-only / dry-run")
    print("- real-device command send: no")
    if execute_requested:
        print("- stage3plus-plan is plan-only. No real-device command was sent.")
    print("- protocol support and execution permission are separated.")
    print("- high-impact commands require explicit approval, complete parameters, impact review, and recovery plan.")
    print("")
    headers = [
        "PDF",
        "Command",
        "Bytes",
        "Impact",
        "Category",
        "ROM",
        "Antenna",
        "Tag",
        "Target",
        "Bank",
        "Address",
        "Words",
        "Password",
        "Recovery",
        "v020 status",
    ]
    print(" | ".join(headers))
    print(" | ".join(["---"] * len(headers)))
    for command in STAGE3PLUS_COMMANDS:
        print(" | ".join([
            command["pdf_section"],
            command["name"],
            command["command_bytes"],
            command["impact_category"],
            command["operation_category"],
            command["requires_rom_check"],
            command["requires_antenna"],
            command["requires_tag"],
            command["requires_target_epc_uii"],
            command["requires_memory_bank"],
            command["requires_address"],
            command["requires_word_count"],
            command["requires_access_password"],
            command["requires_recovery_plan"],
            "READY_FOR_EXPLICIT_APPROVAL",
        ]))
    print("")
    print("Execution gate:")
    print("- NOT_EXECUTED_IN_V020")
    print("- Explicit approval required before any real-device execution.")
    print("- No completed Hex or SUM-calculated command is emitted.")


def output_paths(output_dir: Path, connection_label: str) -> tuple[Path, Path]:
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir.mkdir(parents=True, exist_ok=True)
    return (
        output_dir / f"stage01_readonly_{stamp}_{connection_label}_log.csv",
        output_dir / f"stage01_readonly_{stamp}_{connection_label}_result.md",
    )


def write_logs(
    csv_path: Path,
    md_path: Path,
    commands: list[dict[str, str]],
    args: argparse.Namespace,
    rows: list[dict[str, str]],
) -> None:
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=LOG_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    passes = [row for row in rows if row["result_status"] in ("REAL_DEVICE_PASS", "REAL_DEVICE_PASS_WITH_NOTES")]
    failures = [row for row in rows if row["result_status"] == "REAL_DEVICE_FAIL"]
    nacks = [row for row in rows if row["actual_response_type"] == "NACK"]
    timeouts = [row for row in rows if row["actual_response_type"] == "timeout"]
    not_applicable = [row for row in rows if row["result_status"] == "NOT_APPLICABLE_TO_TARGET"]
    rom_rows = [row for row in rows if row["pdf_section"] == ROM_READ_PDF_SECTION]
    rom_summary = rom_rows[0]["ack_summary"] if rom_rows else "TBD"
    product_summary = rom_rows[0]["product_type"] if rom_rows else "TBD"
    if args.command_set in {"stage2-minimal", "stage2-read"}:
        title = "# Stage 2 RF Read Minimal Verification Result"
        if args.command_set == "stage2-read":
            title = "# Stage 2 RF Read Operations Result"
            scope_note = "- v019 real-device send target is limited to ROM read and Stage 2 RF read operations."
            rom_gate_note = "- ROM version read is executed first. If it fails, Stage 2 commands are not sent."
        else:
            scope_note = "- v017 real-device send target is limited to ROM read, UHF_CheckAntenna, UHF_GetHandle, and UHF_Inventory."
            rom_gate_note = "- ROM version read is executed first. If it fails, Stage 2 minimal commands are not sent."
    else:
        title = "# Stage 0/1 Read-only Verification Result"
        scope_note = "- v015 real-device send target is limited to ROM read plus Stage 1 read-only commands."
        rom_gate_note = "- ROM version read is executed first. If it fails, Stage 1 commands are not sent."
    md_path.write_text(
        "\n".join([
            title,
            "",
            f"- 実行日時: {dt.datetime.now().isoformat(timespec='seconds')}",
            f"- 実行者: {args.operator}",
            f"- リポジトリ版: {args.repository_version}",
            f"- package version: {PACKAGE_VERSION}",
            f"- 接続方式: {args.connection_type}",
            f"- 接続先: {mask_value(args.port or args.host or 'not-specified', args.mask_sensitive)}",
            f"- ROM読み取り結果: {rom_summary or 'TBD'}",
            f"- 機種判定結果: {product_summary or 'TBD'}",
            "- raw response: not recorded in this masked Markdown summary",
            "",
            "## 実行コマンド一覧",
            *[f"- {command['pdf_section']} {command['name']}" for command in commands],
            "",
            "## PASS一覧",
            *[f"- {row['command_name']}" for row in passes],
            "",
            "## FAIL一覧",
            *[f"- {row['command_name']}" for row in failures],
            "",
            "## NACK一覧",
            *[f"- {row['command_name']}" for row in nacks],
            "",
            "## timeout一覧",
            *[f"- {row['command_name']}" for row in timeouts],
            "",
            "## NOT_APPLICABLE_TO_TARGET一覧",
            *[f"- {row['command_name']}" for row in not_applicable],
            "",
            "## 備考",
            "- Dry-run rows use READY_FOR_REAL_DEVICE_TEST and do not indicate real-device pass.",
            scope_note,
            rom_gate_note,
            "- Runtime CSV may contain raw response details and must not be committed.",
        ]),
        encoding="utf-8",
    )


def dry_run_rows(commands: list[dict[str, str]], args: argparse.Namespace) -> list[dict[str, str]]:
    now = dt.datetime.now().isoformat(timespec="seconds")
    target = args.port or args.host or "not-specified"
    masked_target = mask_value(target, args.mask_sensitive)
    rows = []
    for index, command in enumerate(commands, start=1):
        rows.append({
            "log_id": f"dryrun-{index:03d}",
            "date_time": now,
            "operator": args.operator,
            "repository_version": args.repository_version,
            "package_version": PACKAGE_VERSION,
            "command_card": command["card_path"],
            "pdf_section": command["pdf_section"],
            "command_name": command["name"],
            "command_byte": command["command_byte"],
            "detail_command": command["detail_command"],
            "subcommand": command["subcommand"],
            "device_series": "TBD",
            "product_type": "TBD",
            "rom_version": "TBD",
            "connection_type": args.connection_type,
            "port_or_ip": masked_target,
            "baudrate_or_socket": str(args.baudrate if args.port else args.socket_port or ""),
            "antenna_count": "TBD",
            "active_antenna": "TBD",
            "antenna_switching_mode": "read-only",
            "target_tag_count": "TBD" if command["stage"] in {"stage2-minimal", "stage2-read"} else "not-applicable",
            "target_memory_bank": memory_bank_label(getattr(args, "read_memory_bank", None))
            if command["pdf_section"] in {"7.5.2", "7.5.3"}
            else "not-applicable",
            "parameter_summary": read_parameter_summary(args)
            if command["pdf_section"] in {"7.5.2", "7.5.3"}
            else command["device_rom_condition"],
            "ram_flash_impact": "read-only",
            "rf_impact": "RF emission possible" if command["stage"] in {"stage2-minimal", "stage2-read"} else "no setting change",
            "tag_memory_impact": "read-only RF access" if command["stage"] in {"stage2-minimal", "stage2-read"} else "none",
            "recovery_required": "no",
            "pre_read_required": "ROM read first",
            "expected_response_type": command["expected_response"],
            "actual_response_type": "dry-run",
            "ack_summary": "",
            "nack_error_code_1": "",
            "nack_error_code_2": "",
            "nack_error_code_3": "",
            "nack_error_code_4": "",
            "timeout_ms": str(args.timeout_ms),
            "elapsed_ms": "",
            "raw_response_hex": "",
            "raw_log_file": "",
            "result_status": "READY_FOR_REAL_DEVICE_TEST"
            if (
                is_v014_sendable(command)
                or command["stage"] == "stage1"
                or (args.command_set == "stage2-minimal" and is_v017_stage2_minimal_sendable(command))
                or (args.command_set == "stage2-read" and is_v018_stage2_read_sendable(command))
            )
            else "NOT_EXECUTED_IN_V015",
            "notes": command["notes"]
            if (
                is_v014_sendable(command)
                or command["stage"] == "stage1"
                or (args.command_set == "stage2-minimal" and is_v017_stage2_minimal_sendable(command))
                or (args.command_set == "stage2-read" and is_v018_stage2_read_sendable(command))
            )
            else "v015 execution scope is ROM read plus Stage 1 read-only only.",
        })
    return rows


def execute_commands(commands: list[dict[str, str]], args: argparse.Namespace) -> list[dict[str, str]]:
    if not args.port and not args.host:
        raise SystemExit("--execute requires --port COMx or --host address.")
    if args.host:
        raise SystemExit("TCP execution adapter is not implemented in v011; use dry-run or specify a reviewed adapter.")
    try:
        import serial  # type: ignore
    except ImportError as exc:
        raise SystemExit("pyserial is required for --execute with --port. Install pyserial first.") from exc

    rows = dry_run_rows(commands, args)
    timeout_sec = args.timeout_ms / 1000.0
    rom_ok = False
    rom_context: dict[str, str] = {}
    inventory_tag_count = 0
    with serial.Serial(args.port, args.baudrate, timeout=timeout_sec) as ser:
        for command, row in zip(commands, rows):
            # Execution scope is deliberately narrow. Do not expand into writes or setting changes.
            if args.command_set == "stage2-read":
                sendable = is_v018_stage2_read_sendable(command)
                not_executed_status = "NOT_EXECUTED_IN_V018"
                not_executed_note = "v018 sends only ROM read and Stage 2 RF read operations; no writes or setting changes."
            elif args.command_set == "stage2-minimal":
                sendable = is_v017_stage2_minimal_sendable(command)
                not_executed_status = "NOT_EXECUTED_IN_V017"
                not_executed_note = "v017 sends only ROM read, UHF_CheckAntenna, UHF_GetHandle, and UHF_Inventory."
            else:
                sendable = is_v015_sendable(command)
                not_executed_status = "NOT_EXECUTED_IN_V015"
                not_executed_note = "v015 sends only ROM read plus Stage 1 read-only commands."
            if not sendable:
                row["actual_response_type"] = "not-sent"
                row["result_status"] = not_executed_status
                row["notes"] = not_executed_note
                continue
            if command["pdf_section"] != ROM_READ_PDF_SECTION and not rom_ok:
                row["actual_response_type"] = "not-sent"
                row["result_status"] = "BLOCKED_BY_DEVICE_OR_ROM"
                row["notes"] = "ROM version read did not pass; later commands are not sent."
                continue
            if args.command_set == "stage2-read" and command["pdf_section"] in {"7.5.2", "7.5.3"}:
                if inventory_tag_count < 1:
                    row.update(rom_context)
                    row["actual_response_type"] = "not-sent"
                    row["result_status"] = "BLOCKED_BY_SITE_CONDITION"
                    row["notes"] = "No parsed Inventory tag count; InventoryRead/UHF_Read are not sent."
                    continue
                if read_parameter_bytes(args) is None:
                    row.update(rom_context)
                    row["actual_response_type"] = "not-sent"
                    row["result_status"] = "BLOCKED_BY_PARAMETER"
                    row["notes"] = "Read memory bank, address, and word count are not fully specified."
                    continue
            block_status, block_note = (None, None)
            if command["stage"] == "stage1":
                block_status, block_note = stage1_block_reason(command, rom_context)
            if block_status:
                row.update(rom_context)
                row["actual_response_type"] = "not-sent"
                row["result_status"] = block_status
                row["notes"] = block_note or ""
                continue
            started = time.perf_counter()
            try:
                if command["pdf_section"] == ROM_READ_PDF_SECTION:
                    frame = build_rom_version_read_frame()
                elif command["stage"] == "stage1":
                    frame = build_stage1_readonly_frame(command)
                elif command["stage"] == "stage2-minimal":
                    frame = build_stage2_minimal_frame(command)
                elif command["stage"] == "stage2-read":
                    frame = build_stage2_read_frame(command, args)
                else:
                    raise ValueError("command is outside execution scope")
                ser.write(frame)
                if args.command_set == "stage2-read" and command["pdf_section"] in {"7.5.1", "7.5.2"}:
                    response = receive_until_completion(ser, timeout_sec, command)
                else:
                    response = read_until_cr(ser, timeout_sec)
                row["raw_response_hex"] = response.hex().upper()
                row["elapsed_ms"] = str(int((time.perf_counter() - started) * 1000))
                parsed = parse_common_response(response)
                frames = parsed_frames(response)
                if args.command_set == "stage2-read" and command["pdf_section"] in {"7.5.1", "7.5.2"}:
                    row["actual_response_type"] = "multi-frame" if len(frames) > 1 else str(parsed["type"])
                else:
                    row["actual_response_type"] = str(parsed["type"])
                if parsed["type"] == "ACK" and parsed["valid"]:
                    if command["pdf_section"] == ROM_READ_PDF_SECTION:
                        rom_info = parse_rom_version_ack(parsed)
                        rom_context = {
                            "device_series": rom_info["series_name"],
                            "product_type": rom_info["product_type"],
                            "rom_version": rom_info["rom_version"],
                        }
                        row.update(rom_context)
                        row["ack_summary"] = (
                            f"ROM raw={rom_info['rom_raw']}; "
                            f"ROM={rom_info['rom_version']}; "
                            f"series={rom_info['series_name']}; "
                            f"product={rom_info['product_type']}"
                        )
                        rom_ok = True
                    elif command["stage"] == "stage1":
                        row.update(rom_context)
                        row["ack_summary"] = parse_stage1_ack_summary(command, parsed)
                    elif command["stage"] == "stage2-minimal":
                        row.update(rom_context)
                        row["ack_summary"] = parse_stage2_minimal_ack_summary(command, parsed)
                    elif command["stage"] == "stage2-read":
                        row.update(rom_context)
                        row["ack_summary"] = parse_stage2_minimal_ack_summary(command, parsed)
                    row["result_status"] = "REAL_DEVICE_PASS_WITH_NOTES"
                    row["notes"] = "Command completed within the selected narrow execution scope. Raw response is retained only in runtime CSV."
                    row["raw_log_file"] = "runtime_logs only; not committed"
                elif args.command_set == "stage2-read" and command["pdf_section"] in {"7.5.1", "7.5.2"} and frames:
                    row.update(rom_context)
                    if command["pdf_section"] == "7.5.1":
                        inv = parse_inventory_response(response, args.mask_sensitive, args.max_tags)
                    else:
                        inv = parse_inventory_read_response(response, args.mask_sensitive, args.max_tags)
                    inventory_tag_count = int(inv.get("parsed_tag_count") or "0") if command["pdf_section"] == "7.5.1" else inventory_tag_count
                    row["target_tag_count"] = inv.get("parsed_tag_count", "")
                    row["ack_summary"] = "; ".join(
                        item for item in [
                            inv.get("raw_summary", ""),
                            f"masked_epc={inv.get('masked_epc_summary', '')}" if inv.get("masked_epc_summary") else "",
                            read_parameter_summary(args) if command["pdf_section"] == "7.5.2" else "",
                        ] if item
                    )
                    row["result_status"] = "REAL_DEVICE_PASS_WITH_NOTES" if inventory_tag_count > 0 or command["pdf_section"] == "7.5.2" else "REAL_DEVICE_PASS_WITH_NOTES"
                    row["notes"] = "RF response loop completed. Raw frames are retained only in runtime CSV."
                    row["raw_log_file"] = "runtime_logs only; not committed"
                elif args.command_set == "stage2-read" and command["pdf_section"] == "7.5.3" and frames and parsed["valid"]:
                    row.update(rom_context)
                    read_summary = parse_uhf_read_response(response, args.mask_sensitive)
                    row["ack_summary"] = "; ".join(
                        item for item in [
                            read_summary["raw_summary"],
                            read_parameter_summary(args),
                        ] if item
                    )
                    row["result_status"] = "REAL_DEVICE_PASS_WITH_NOTES" if parsed["type"] == "ACK" else "REAL_DEVICE_FAIL"
                    row["notes"] = "UHF_Read response parsed conservatively. Raw response is retained only in runtime CSV."
                    row["raw_log_file"] = "runtime_logs only; not committed"
                elif parsed["type"] == "NACK" and parsed["valid"]:
                    nack = parse_nack_errors(parsed)
                    row["nack_error_code_1"] = nack["error_code_1"]
                    row["nack_error_code_2"] = nack["error_code_2"]
                    row["nack_error_code_3"] = nack["error_code_3"]
                    row["nack_error_code_4"] = nack["error_code_4"]
                    row["result_status"] = "REAL_DEVICE_FAIL"
                    row["notes"] = "Command returned NACK. Record error codes and do not force PASS."
                elif parsed["type"] == "timeout":
                    row["result_status"] = "NEEDS_RETEST"
                    row["notes"] = "No response before timeout."
                else:
                    row["result_status"] = "REAL_DEVICE_FAIL"
                    row["notes"] = f"Invalid or unexpected response: {parsed.get('error', 'unknown')}"
            except Exception as exc:
                row["elapsed_ms"] = str(int((time.perf_counter() - started) * 1000))
                row["actual_response_type"] = "exception"
                row["result_status"] = "REAL_DEVICE_FAIL"
                row["notes"] = str(exc)
    return rows


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stage 0/1 read-only verification helper")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode; default behavior.")
    parser.add_argument("--execute", action="store_true", help="Enable real-device communication.")
    parser.add_argument("--port", help="Serial port such as COM6.")
    parser.add_argument("--host", help="TCP host. Execution adapter is not enabled.")
    parser.add_argument("--socket-port", type=int, default=None)
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--timeout-ms", type=int, default=1000)
    parser.add_argument("--read-size", type=int, default=256)
    parser.add_argument("--output-dir", default="runtime_logs/stage01_readonly")
    parser.add_argument("--mask-sensitive", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument(
        "--command-set",
        choices=["stage0", "stage1", "stage2-minimal", "stage2-read", "stage3plus-plan", "all"],
        default="all",
    )
    parser.add_argument("--read-profile", choices=["none", "safe-tid"], default="none")
    parser.add_argument("--memory-bank", choices=sorted(MEMORY_BANKS.keys()), default=None)
    parser.add_argument("--read-memory-bank", type=lambda value: int(value, 0), default=None)
    parser.add_argument("--word-address", dest="read_address_alias", type=lambda value: int(value, 0), default=None)
    parser.add_argument("--read-address", type=lambda value: int(value, 0), default=None)
    parser.add_argument("--read-word-count", type=int, default=None)
    parser.add_argument("--word-count", dest="read_word_count_alias", type=int, default=None)
    parser.add_argument("--access-password", default=None)
    parser.add_argument("--max-tags", type=int, default=1)
    parser.add_argument("--operator", default="TBD")
    parser.add_argument("--repository-version", default="main")
    parser.add_argument("--connection-type", default="USB")
    parser.add_argument("--sample-log", help="Optional CSV log to parse for row count only.")
    args = parser.parse_args(argv)
    if args.memory_bank is not None:
        args.read_memory_bank = MEMORY_BANKS[args.memory_bank]
    if args.read_address_alias is not None:
        args.read_address = args.read_address_alias
    if args.read_word_count_alias is not None:
        args.read_word_count = args.read_word_count_alias
    if args.access_password is not None:
        cleaned = "".join(ch for ch in args.access_password.upper() if ch in "0123456789ABCDEF")
        if len(cleaned) != 8:
            raise SystemExit("--access-password must be 8 hexadecimal characters.")
        args.access_password = cleaned
    if args.max_tags < 1:
        raise SystemExit("--max-tags must be 1 or greater.")
    return resolve_read_profile(args)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.command_set == "stage3plus-plan":
        print_stage3plus_plan(args.execute)
        return 0
    commands = select_commands(args.command_set)
    target = args.port or args.host or "not-specified"
    connection_label = mask_value(target, args.mask_sensitive).replace(".", "_")
    csv_path, md_path = output_paths(Path(args.output_dir), connection_label)

    print("UTR-S201 verification command targets:")
    for command in commands:
        scope = command_scope_label(command, args.command_set)
        print(f"- {command['stage']} {command['pdf_section']} {command['name']} [{scope}]")
    print("Verification adapter:")
    print("- common frame: STX/address/command/data-length/data/ETX/SUM/CR")
    if args.command_set == "stage2-read":
        print("- real-device send target: ROM read, UHF_CheckAntenna, UHF_GetHandle, UHF_Inventory, UHF_InventoryRead, and UHF_Read")
        print("- InventoryRead and UHF_Read are sent only when Inventory detects tags and read parameters are specified")
        print(f"- read profile: {args.read_profile}")
        print(f"- read parameters: {read_parameter_summary(args)}")
        print("- writes, FLASH, frequency, output, antenna setting, and tag memory write operations are not sent")
    elif args.command_set == "stage2-minimal":
        print("- real-device send target: ROM read, UHF_CheckAntenna, UHF_GetHandle, and UHF_Inventory only")
        print("- InventoryRead, UHF_Read, writes, FLASH, frequency, output, antenna setting, and tag memory operations are not sent")
    else:
        print("- real-device send target: ROM read plus Stage 1 read-only commands only")
        print("- 8CH-only or ROM-unsupported commands are recorded without sending")
        print("- commands requiring unspecified parameters are recorded without sending")
    print("- ROM version read runs first; later commands are skipped if ROM read fails")
    print("- dry-run does not send a frame.")
    print(f"CSV log: {csv_path}")
    print(f"Markdown result: {md_path}")

    if args.sample_log:
        with open(args.sample_log, newline="", encoding="utf-8") as handle:
            print(f"sample-log rows: {sum(1 for _ in csv.DictReader(handle))}")

    if args.execute:
        rows = execute_commands(commands, args)
    else:
        print("dry-run: no real-device communication performed.")
        rows = dry_run_rows(commands, args)

    write_logs(csv_path, md_path, commands, args, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
