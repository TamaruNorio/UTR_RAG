#!/usr/bin/env python3
"""Check local Markdown links and frontmatter related_docs references."""

from __future__ import annotations

import pathlib
import re
import sys
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML が必要です。`pip install pyyaml` を実行してください。", file=sys.stderr)
    sys.exit(2)


ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_ROOT = ROOT / "docs" / "current"
TARGET_FILES = [ROOT / "README.md", *sorted(DOCS_ROOT.rglob("*.md"))]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_SCHEMES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
)


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


def strip_code_fences(text: str) -> str:
    lines = text.splitlines()
    result: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            result.append("")
            continue
        result.append("" if in_fence else line)
    return "\n".join(result)


def normalize_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if not target or target.startswith("#"):
        return None
    if target.startswith(SKIP_SCHEMES):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if target.startswith(SKIP_SCHEMES):
        return None

    target = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not target:
        return None
    return target.replace("\\", "/")


def resolve_reference(base_file: pathlib.Path, target: str) -> pathlib.Path:
    return (base_file.parent / target).resolve()


def is_inside_repo(path: pathlib.Path) -> bool:
    try:
        path.relative_to(ROOT)
        return True
    except ValueError:
        return False


def collect_markdown_link_errors(path: pathlib.Path) -> list[str]:
    text = strip_code_fences(path.read_text(encoding="utf-8"))
    errors: list[str] = []

    for match in MARKDOWN_LINK_RE.finditer(text):
        target = normalize_link_target(match.group(1))
        if target is None:
            continue

        resolved = resolve_reference(path, target)
        if not is_inside_repo(resolved):
            errors.append(f"link points outside repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"missing markdown link target: {target}")

    return errors


def collect_related_docs_errors(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    try:
        frontmatter = load_frontmatter(path)
    except Exception as exc:  # noqa: BLE001 - report validation error and continue
        return [f"frontmatter error: {exc}"]

    if not frontmatter or "related_docs" not in frontmatter:
        return errors

    related_docs = frontmatter["related_docs"]
    if related_docs is None:
        return errors
    if not isinstance(related_docs, list):
        return ["related_docs must be a list"]

    for item in related_docs:
        if not isinstance(item, str):
            errors.append(f"related_docs item must be a string: {item!r}")
            continue
        target = normalize_link_target(item)
        if target is None:
            continue

        resolved = resolve_reference(path, target)
        if not is_inside_repo(resolved):
            errors.append(f"related_docs points outside repository: {item}")
            continue
        if not resolved.exists():
            errors.append(f"missing related_docs target: {item}")

    return errors


def main() -> int:
    failures: list[tuple[pathlib.Path, list[str]]] = []
    checked = 0

    for path in TARGET_FILES:
        if not path.exists():
            failures.append((path, ["target file does not exist"]))
            continue

        checked += 1
        errors = collect_markdown_link_errors(path)
        if path.is_relative_to(DOCS_ROOT):
            errors.extend(collect_related_docs_errors(path))
        if errors:
            failures.append((path, errors))

    if failures:
        print("documentation reference check failed")
        for path, errors in failures:
            rel_path = path.relative_to(ROOT).as_posix()
            for error in errors:
                print(f"- {rel_path}: {error}")
        return 1

    print(f"documentation reference check passed: {checked} Markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
