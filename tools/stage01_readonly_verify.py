#!/usr/bin/env python3
"""Stage 0/1 read-only verification helper for UTR-S201 RAG v015.

Dry-run is the default. Real-device communication requires --execute and
an explicit connection target. This tool intentionally defines only Stage 0/1
read-only commands. v015 enables real-device sending for ROM read and Stage 1
read-only commands only.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
import time
from pathlib import Path


PACKAGE_VERSION = "v015"
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


COMMANDS = [{'stage': 'stage0', 'pdf_section': '7.3.1', 'name': 'エラー情報の読み取り', 'command_byte': '4Fh', 'detail_command': '80h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_80_read_error_info.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '低影響の状態確認'}, {'stage': 'stage0', 'pdf_section': '7.3.8', 'name': 'ROMバージョンの読み取り', 'command_byte': '4Fh', 'detail_command': '90h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/rom_version_read.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '最初に実行し機種/シリーズ/ROMを判定', 'notes': '標準フローの起点'}, {'stage': 'stage0', 'pdf_section': '7.3.9', 'name': 'チップバージョンの読み取り', 'command_byte': '55h', 'detail_command': '90h', 'subcommand': '00h', 'card_path': 'docs/current/commands/cards/55_90_chip_version_read.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'v014 executes firmware-version subcommand 00h only; serial-number subcommand 01h is not executed'}, {'stage': 'stage1', 'pdf_section': '7.4.1', 'name': 'リーダライタ動作モードの読み取り', 'command_byte': '4Fh', 'detail_command': '00h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_00_read_reader_mode.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '設定変更は行わない'}, {'stage': 'stage1', 'pdf_section': '7.4.2', 'name': 'UHF_GetSelectParam', 'command_byte': '55h', 'detail_command': '40h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_40_uhf_get_select_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.3', 'name': 'UHF_GetInventoryParam', 'command_byte': '55h', 'detail_command': '41h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_41_uhf_get_inventory_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'SetInventoryParamは対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.4', 'name': 'UHF_GetExpandSelectParam', 'command_byte': '55h', 'detail_command': '42h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_42_uhf_get_expand_select_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.5', 'name': 'アンテナ切替設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '00h', 'card_path': 'docs/current/commands/cards/55_43_00_read_antenna_switching.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。切替設定変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.6', 'name': '出力設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '01h', 'card_path': 'docs/current/commands/cards/55_43_01_read_output_power.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。出力変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.7', 'name': '周波数設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '02h', 'card_path': 'docs/current/commands/cards/55_43_02_read_frequency.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。周波数変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.8', 'name': 'RFタグ通信関連パラメータの読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '04h', 'card_path': 'docs/current/commands/cards/55_43_04_read_rf_tag_comm_params.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.9', 'name': 'EPC(UII)関連パラメータの読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '05h', 'card_path': 'docs/current/commands/cards/55_43_05_read_epc_uii_params.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.10', 'name': '外部アンテナ自動切替設定の読み取り', 'command_byte': '55h', 'detail_command': '47h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '読み取りのみ。自動切替設定変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.11', 'name': '汎用ポート値の読み取り', 'command_byte': '4Fh', 'detail_command': '9Fh', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_9f_read_general_port.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '外部I/O状態読み取り'}, {'stage': 'stage1', 'pdf_section': '7.4.12', 'name': '拡張ポート値の読み取り', 'command_byte': '4Fh', 'detail_command': 'A0h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_a0_read_extended_port.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '外部I/O状態読み取り'}, {'stage': 'stage1', 'pdf_section': '7.4.13', 'name': 'FLASH設定値の読み取り(1バイトアクセス)', 'command_byte': '4Fh', 'detail_command': 'B4h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_b4_read_flash_settings.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。FLASH書き込みは対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.14', 'name': 'RSSIフィルタ設定の読み取り', 'command_byte': '55h', 'detail_command': '49h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_49_read_rssi_filter.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM 2.100以降対象の可能性。非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.15', 'name': 'アンテナ個別送信出力設定の読み取り', 'command_byte': '55h', 'detail_command': '4Ah', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_4a_read_antenna_output_power.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系またはROM条件依存の可能性。非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '読み取りのみ。出力変更は対象外'}]

LOG_FIELDS = ['log_id', 'date_time', 'operator', 'repository_version', 'package_version', 'command_card', 'pdf_section', 'command_name', 'command_byte', 'detail_command', 'subcommand', 'device_series', 'product_type', 'rom_version', 'connection_type', 'port_or_ip', 'baudrate_or_socket', 'antenna_count', 'active_antenna', 'antenna_switching_mode', 'target_tag_count', 'target_memory_bank', 'parameter_summary', 'ram_flash_impact', 'rf_impact', 'tag_memory_impact', 'recovery_required', 'pre_read_required', 'expected_response_type', 'actual_response_type', 'ack_summary', 'nack_error_code_1', 'nack_error_code_2', 'nack_error_code_3', 'nack_error_code_4', 'timeout_ms', 'elapsed_ms', 'raw_log_file', 'result_status', 'notes']


def mask_value(value: str, enabled: bool = True) -> str:
    if not enabled:
        return value
    if value.upper().startswith("COM"):
        return "COMx"
    parts = value.split(".")
    if len(parts) == 4 and all(part.isdigit() for part in parts):
        return f"{parts[0]}.{parts[1]}.xxx.xxx"
    return value


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


def v015_scope_label(command: dict[str, str]) -> str:
    if command["pdf_section"] == ROM_READ_PDF_SECTION or command["pdf_section"] in STAGE1_READABLE_PDF_SECTIONS:
        return "sendable-in-v015"
    if command["stage"] == "stage1":
        return "gated-in-v015"
    return "not-executed-in-v015"


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
    return commands


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
    md_path.write_text(
        "\n".join([
            "# Stage 0/1 Read-only Verification Result",
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
            "- v015 real-device send target is limited to ROM read plus Stage 1 read-only commands.",
            "- ROM version read is executed first. If it fails, Stage 1 commands are not sent.",
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
            "target_tag_count": "not-applicable",
            "target_memory_bank": "not-applicable",
            "parameter_summary": command["device_rom_condition"],
            "ram_flash_impact": "read-only",
            "rf_impact": "no setting change",
            "tag_memory_impact": "none",
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
            "raw_log_file": "",
            "result_status": "READY_FOR_REAL_DEVICE_TEST" if (is_v014_sendable(command) or command["stage"] == "stage1") else "NOT_EXECUTED_IN_V015",
            "notes": command["notes"] if (is_v014_sendable(command) or command["stage"] == "stage1") else "v015 execution scope is ROM read plus Stage 1 read-only only.",
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
    with serial.Serial(args.port, args.baudrate, timeout=timeout_sec) as ser:
        for command, row in zip(commands, rows):
            # v015はROM読み取りとStage 1 read-onlyだけを送信対象にする。設定変更や書き込み系に広げないため。
            if not is_v015_sendable(command):
                row["actual_response_type"] = "not-sent"
                row["result_status"] = "NOT_EXECUTED_IN_V015"
                row["notes"] = "v015 sends only ROM read plus Stage 1 read-only commands."
                continue
            # ROM読み取りで機種/ROMを先に確定し、対象条件が不明なまま後続確認を進めない。
            if command["pdf_section"] != ROM_READ_PDF_SECTION and not rom_ok:
                row["actual_response_type"] = "not-sent"
                row["result_status"] = "BLOCKED_BY_DEVICE_OR_ROM"
                row["notes"] = "ROM version read did not pass; v015 does not proceed to Stage 1 commands."
                continue
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
                else:
                    raise ValueError("command is outside v015 execution scope")
                ser.write(frame)
                response = read_until_cr(ser, timeout_sec)
                row["elapsed_ms"] = str(int((time.perf_counter() - started) * 1000))
                parsed = parse_common_response(response)
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
                    row["result_status"] = "REAL_DEVICE_PASS_WITH_NOTES"
                    row["notes"] = "Read-only command completed. Raw response is retained only in runtime CSV."
                    row["raw_log_file"] = "runtime_logs only; not committed"
                elif parsed["type"] == "NACK" and parsed["valid"]:
                    nack = parse_nack_errors(parsed)
                    row["nack_error_code_1"] = nack["error_code_1"]
                    row["nack_error_code_2"] = nack["error_code_2"]
                    row["nack_error_code_3"] = nack["error_code_3"]
                    row["nack_error_code_4"] = nack["error_code_4"]
                    row["result_status"] = "REAL_DEVICE_FAIL"
                    row["notes"] = "Stage 0 read-only command returned NACK."
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
    parser.add_argument("--host", help="TCP host. Execution adapter is not enabled in v015.")
    parser.add_argument("--socket-port", type=int, default=None)
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--timeout-ms", type=int, default=1000)
    parser.add_argument("--read-size", type=int, default=256)
    parser.add_argument("--output-dir", default="runtime_logs/stage01_readonly")
    parser.add_argument("--mask-sensitive", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--command-set", choices=["stage0", "stage1", "all"], default="all")
    parser.add_argument("--operator", default="TBD")
    parser.add_argument("--repository-version", default="main")
    parser.add_argument("--connection-type", default="USB")
    parser.add_argument("--sample-log", help="Optional CSV log to parse for row count only.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    commands = select_commands(args.command_set)
    target = args.port or args.host or "not-specified"
    connection_label = mask_value(target, args.mask_sensitive).replace(".", "_")
    csv_path, md_path = output_paths(Path(args.output_dir), connection_label)

    print("Stage 0/1 read-only command targets:")
    for command in commands:
        scope = v015_scope_label(command)
        print(f"- {command['stage']} {command['pdf_section']} {command['name']} [{scope}]")
    print("v015 Stage 1 read-only adapter:")
    print("- common frame: STX/address/command/data-length/data/ETX/SUM/CR")
    print("- real-device send target: ROM read plus Stage 1 read-only commands only")
    print("- ROM version read runs first; Stage 1 commands are skipped if ROM read fails")
    print("- 8CH-only or ROM-unsupported commands are recorded without sending")
    print("- commands requiring unspecified parameters are recorded without sending")
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
