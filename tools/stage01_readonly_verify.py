#!/usr/bin/env python3
"""Stage 0/1 read-only verification helper for UTR-S201 RAG v011.

Dry-run is the default. Real-device communication requires --execute and
an explicit connection target. This tool intentionally defines only Stage 0/1
read-only commands.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
import time
from pathlib import Path


COMMANDS = [{'stage': 'stage0', 'pdf_section': '7.3.1', 'name': 'エラー情報の読み取り', 'command_byte': '4Fh', 'detail_command': '80h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_80_read_error_info.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '低影響の状態確認'}, {'stage': 'stage0', 'pdf_section': '7.3.8', 'name': 'ROMバージョンの読み取り', 'command_byte': '4Fh', 'detail_command': '90h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/rom_version_read.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '最初に実行し機種/シリーズ/ROMを判定', 'notes': '標準フローの起点'}, {'stage': 'stage0', 'pdf_section': '7.3.9', 'name': 'チップバージョンの読み取り', 'command_byte': '55h', 'detail_command': '90h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_90_chip_version_read.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '機種/ROM条件を併記'}, {'stage': 'stage1', 'pdf_section': '7.4.1', 'name': 'リーダライタ動作モードの読み取り', 'command_byte': '4Fh', 'detail_command': '00h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_00_read_reader_mode.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '設定変更は行わない'}, {'stage': 'stage1', 'pdf_section': '7.4.2', 'name': 'UHF_GetSelectParam', 'command_byte': '55h', 'detail_command': '40h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_40_uhf_get_select_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.3', 'name': 'UHF_GetInventoryParam', 'command_byte': '55h', 'detail_command': '41h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_41_uhf_get_inventory_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'SetInventoryParamは対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.4', 'name': 'UHF_GetExpandSelectParam', 'command_byte': '55h', 'detail_command': '42h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_42_uhf_get_expand_select_param.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.5', 'name': 'アンテナ切替設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '00h', 'card_path': 'docs/current/commands/cards/55_43_00_read_antenna_switching.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。切替設定変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.6', 'name': '出力設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '01h', 'card_path': 'docs/current/commands/cards/55_43_01_read_output_power.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。出力変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.7', 'name': '周波数設定の読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '02h', 'card_path': 'docs/current/commands/cards/55_43_02_read_frequency.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。周波数変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.8', 'name': 'RFタグ通信関連パラメータの読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '04h', 'card_path': 'docs/current/commands/cards/55_43_04_read_rf_tag_comm_params.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.9', 'name': 'EPC(UII)関連パラメータの読み取り', 'command_byte': '55h', 'detail_command': '43h', 'subcommand': '05h', 'card_path': 'docs/current/commands/cards/55_43_05_read_epc_uii_params.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.10', 'name': '外部アンテナ自動切替設定の読み取り', 'command_byte': '55h', 'detail_command': '47h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '読み取りのみ。自動切替設定変更は対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.11', 'name': '汎用ポート値の読み取り', 'command_byte': '4Fh', 'detail_command': '9Fh', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_9f_read_general_port.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '外部I/O状態読み取り'}, {'stage': 'stage1', 'pdf_section': '7.4.12', 'name': '拡張ポート値の読み取り', 'command_byte': '4Fh', 'detail_command': 'A0h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_a0_read_extended_port.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '外部I/O状態読み取り'}, {'stage': 'stage1', 'pdf_section': '7.4.13', 'name': 'FLASH設定値の読み取り(1バイトアクセス)', 'command_byte': '4Fh', 'detail_command': 'B4h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/4f_b4_read_flash_settings.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM読み取りで機種判定後に実行', 'notes': '読み取りのみ。FLASH書き込みは対象外'}, {'stage': 'stage1', 'pdf_section': '7.4.14', 'name': 'RSSIフィルタ設定の読み取り', 'command_byte': '55h', 'detail_command': '49h', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_49_read_rssi_filter.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': 'ROM 2.100以降対象の可能性。非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': 'read-only parameter retrieval'}, {'stage': 'stage1', 'pdf_section': '7.4.15', 'name': 'アンテナ個別送信出力設定の読み取り', 'command_byte': '55h', 'detail_command': '4Ah', 'subcommand': '-', 'card_path': 'docs/current/commands/cards/55_4a_read_antenna_output_power.md', 'expected_response': 'ACK/NACK/timeout/no-response', 'device_rom_condition': '8CH系またはROM条件依存の可能性。非対応なら NOT_APPLICABLE_TO_TARGET', 'notes': '読み取りのみ。出力変更は対象外'}]

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
    """Return protocol SUM byte for a frame prefix.

    The actual frame layout must be checked against the protocol manual before
    real-device execution. This function is isolated so no SUM-calculated
    command examples are embedded in documents.
    """
    return sum(frame_without_sum) & 0xFF


def build_readonly_frame(command: dict[str, str]) -> bytes:
    """Build a read-only frame from command identifiers.

    This v011 helper keeps frame construction isolated and limited to the
    Stage 0/1 read-only command table. If the local protocol frame definition
    is not confirmed, keep using dry-run or parse-only workflows.
    """
    raise NotImplementedError(
        "Protocol common frame layout is not encoded in v011. "
        "Use dry-run/sample-log workflows until the execution adapter is confirmed."
    )


def select_commands(command_set: str) -> list[dict[str, str]]:
    if command_set == "all":
        return COMMANDS
    return [command for command in COMMANDS if command["stage"] == command_set]


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
    md_path.write_text(
        "\n".join([
            "# Stage 0/1 Read-only Verification Result",
            "",
            f"- 実行日時: {dt.datetime.now().isoformat(timespec='seconds')}",
            f"- 実行者: {args.operator}",
            f"- リポジトリ版: {args.repository_version}",
            "- package version: v011",
            f"- 接続方式: {args.connection_type}",
            "- ROM読み取り結果: TBD",
            "- 機種判定結果: TBD",
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
            "package_version": "v011",
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
            "result_status": "READY_FOR_REAL_DEVICE_TEST",
            "notes": command["notes"],
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
    with serial.Serial(args.port, args.baudrate, timeout=timeout_sec) as ser:
        for command, row in zip(commands, rows):
            started = time.perf_counter()
            try:
                frame = build_readonly_frame(command)
                ser.write(frame)
                response = ser.read(args.read_size)
                row["elapsed_ms"] = str(int((time.perf_counter() - started) * 1000))
                row["actual_response_type"] = "ACK-or-raw-response" if response else "timeout"
                row["ack_summary"] = response.hex().upper() if response else ""
                row["result_status"] = "REAL_DEVICE_PASS_WITH_NOTES" if response else "NEEDS_RETEST"
            except NotImplementedError as exc:
                row["actual_response_type"] = "not-sent"
                row["result_status"] = "BLOCKED_BY_PARAMETER"
                row["notes"] = str(exc)
                break
    return rows


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stage 0/1 read-only verification helper")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode; default behavior.")
    parser.add_argument("--execute", action="store_true", help="Enable real-device communication.")
    parser.add_argument("--port", help="Serial port such as COM6.")
    parser.add_argument("--host", help="TCP host. Execution adapter is not enabled in v011.")
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
        print(f"- {command['stage']} {command['pdf_section']} {command['name']}")
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
