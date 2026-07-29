#!/usr/bin/env python3
"""Validate minimal frontmatter requirements for command cards."""

from __future__ import annotations

import pathlib
import sys
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML が必要です。`pip install pyyaml` を実行してください。", file=sys.stderr)
    sys.exit(2)


ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS_DIR = ROOT / "docs" / "current" / "commands" / "cards"

REQUIRED_COMMAND_CARD_KEYS = [
    "title",
    "doc_type",
    "package_scope",
    "manual",
    "manual_version",
    "pdf_section",
    "command_group",
    "command_name",
    "command_byte",
    "detail_command",
    "subcommand",
    "operation_profile",
    "operation_level",
    "rf_emission",
    "write_operation",
    "flash_operation",
    "tag_memory_operation",
    "requires_rom_check",
    "requires_antenna",
    "requires_tag",
    "requires_access_password",
    "requires_parameters",
    "verification_status",
    "result_status",
    "related_docs",
    "tags",
]

BOOL_KEYS = [
    "rf_emission",
    "write_operation",
    "flash_operation",
    "tag_memory_operation",
    "requires_rom_check",
    "requires_antenna",
    "requires_tag",
    "requires_access_password",
    "requires_parameters",
]

LIST_KEYS = ["related_docs", "tags"]


def load_frontmatter(path: pathlib.Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8").lstrip("\ufeff")
    if not text.startswith("---"):
        return None

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("frontmatter terminator not found")

    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data


def validate_command_card(path: pathlib.Path, frontmatter: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for key in REQUIRED_COMMAND_CARD_KEYS:
        if key not in frontmatter:
            errors.append(f"missing required key: {key}")

    if frontmatter.get("doc_type") != "command_card":
        errors.append("doc_type must be command_card")

    for key in LIST_KEYS:
        if key in frontmatter and not isinstance(frontmatter[key], list):
            errors.append(f"{key} must be a list")

    for key in BOOL_KEYS:
        if key in frontmatter and not isinstance(frontmatter[key], bool):
            errors.append(f"{key} must be a boolean")

    if "tags" in frontmatter and isinstance(frontmatter["tags"], list) and not frontmatter["tags"]:
        errors.append("tags must not be empty")

    return errors


def main() -> int:
    failures: list[tuple[pathlib.Path, list[str]]] = []
    checked = 0

    for path in sorted(CARDS_DIR.glob("*.md")):
        try:
            frontmatter = load_frontmatter(path)
        except Exception as exc:  # noqa: BLE001 - report validation error and continue
            failures.append((path, [str(exc)]))
            continue

        if frontmatter is None or frontmatter.get("doc_type") != "command_card":
            continue

        checked += 1
        errors = validate_command_card(path, frontmatter)
        if errors:
            failures.append((path, errors))

    if failures:
        print("frontmatter validation failed")
        for path, errors in failures:
            rel_path = path.relative_to(ROOT).as_posix()
            for error in errors:
                print(f"- {rel_path}: {error}")
        return 1

    print(f"frontmatter validation passed: {checked} command_card files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
