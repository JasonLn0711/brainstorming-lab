"""Small YAML subset reader/writer for Idea OS data files.

The project intentionally avoids runtime dependencies. If PyYAML is available in
the environment we can use it, but the fallback parser handles the subset this
repo writes: mappings, nested mappings, scalar lists, simple list-of-mapping
items, quoted strings, numbers, booleans, nulls, and block strings.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


try:  # Optional convenience only; the fallback is the supported baseline.
    import yaml as _pyyaml  # type: ignore
except Exception:  # pragma: no cover - depends on local environment
    _pyyaml = None


def load_yaml(path: str | Path) -> Any:
    text = Path(path).read_text(encoding="utf-8")
    return loads_yaml(text)


def save_yaml(path: str | Path, data: Any) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(dumps_yaml(data), encoding="utf-8")


def loads_yaml(text: str) -> Any:
    stripped_text = text.strip()
    if stripped_text == "{}":
        return {}
    if stripped_text == "[]":
        return []
    if _pyyaml is not None:  # pragma: no cover - absent in the target env
        loaded = _pyyaml.safe_load(text)
        return {} if loaded is None else loaded

    lines = _prepare_lines(text)
    if not lines:
        return {}
    value, index = _parse_block(lines, 0, _indent_of(lines[0]))
    if index != len(lines):
        raise ValueError(f"Unexpected YAML content near line {index + 1}")
    return value


def dumps_yaml(data: Any) -> str:
    if _pyyaml is not None:  # pragma: no cover - absent in the target env
        return _pyyaml.safe_dump(data, sort_keys=False, allow_unicode=True)
    if data == {}:
        return "{}\n"
    if data == []:
        return "[]\n"
    lines = _dump_value(data, 0)
    return "\n".join(lines).rstrip() + "\n"


def _prepare_lines(text: str) -> list[str]:
    prepared: list[str] = []
    for raw_line in text.splitlines():
        if not raw_line.strip():
            continue
        stripped = raw_line.lstrip()
        if stripped.startswith("#"):
            continue
        prepared.append(raw_line.rstrip())
    return prepared


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _parse_block(lines: list[str], index: int, indent: int) -> tuple[Any, int]:
    if lines[index].lstrip().startswith("- "):
        return _parse_list(lines, index, indent)
    return _parse_mapping(lines, index, indent)


def _parse_mapping(lines: list[str], index: int, indent: int) -> tuple[dict[str, Any], int]:
    result: dict[str, Any] = {}
    while index < len(lines):
        line = lines[index]
        current_indent = _indent_of(line)
        if current_indent < indent:
            break
        if current_indent > indent:
            raise ValueError(f"Unexpected indentation near line {index + 1}: {line}")

        stripped = line.strip()
        if stripped.startswith("- "):
            break
        key, raw_value = _split_key_value(stripped, index)
        if raw_value == "":
            next_index = index + 1
            if (
                next_index < len(lines)
                and _indent_of(lines[next_index]) == indent
                and lines[next_index].lstrip().startswith("- ")
            ):
                value, index = _parse_list(lines, next_index, indent)
                result[key] = value
            elif next_index >= len(lines) or _indent_of(lines[next_index]) <= indent:
                result[key] = None
                index = next_index
            else:
                value, index = _parse_block(lines, next_index, _indent_of(lines[next_index]))
                result[key] = value
        elif raw_value in {">", "|"}:
            result[key], index = _parse_block_string(lines, index + 1, indent, raw_value)
        else:
            result[key], index = _parse_scalar_with_continuation(lines, index, indent, raw_value)
    return result, index


def _parse_list(lines: list[str], index: int, indent: int) -> tuple[list[Any], int]:
    result: list[Any] = []
    while index < len(lines):
        line = lines[index]
        current_indent = _indent_of(line)
        if current_indent < indent:
            break
        if current_indent > indent:
            raise ValueError(f"Unexpected list indentation near line {index + 1}: {line}")
        stripped = line.strip()
        if not stripped.startswith("- "):
            break

        item_text = stripped[2:].strip()
        if item_text == "":
            value, index = _parse_block(lines, index + 1, indent + 2)
            result.append(value)
        elif _looks_like_key_value(item_text) and not item_text.startswith(("'", '"')):
            key, raw_value = _split_key_value(item_text, index)
            item: dict[str, Any] = {key: _parse_scalar(raw_value) if raw_value else None}
            index += 1
            while index < len(lines) and _indent_of(lines[index]) >= indent + 2:
                if _indent_of(lines[index]) != indent + 2:
                    raise ValueError(f"Unexpected nested list mapping near line {index + 1}: {lines[index]}")
                nested_key, nested_value = _split_key_value(lines[index].strip(), index)
                if nested_value == "":
                    next_index = index + 1
                    if (
                        next_index < len(lines)
                        and _indent_of(lines[next_index]) == indent + 2
                        and lines[next_index].lstrip().startswith("- ")
                    ):
                        value, index = _parse_list(lines, next_index, indent + 2)
                        item[nested_key] = value
                    elif next_index < len(lines) and _indent_of(lines[next_index]) > indent + 2:
                        value, index = _parse_block(lines, next_index, _indent_of(lines[next_index]))
                        item[nested_key] = value
                    else:
                        item[nested_key] = None
                        index = next_index
                else:
                    item[nested_key], index = _parse_scalar_with_continuation(
                        lines, index, indent + 2, nested_value
                    )
            result.append(item)
        else:
            value, index = _parse_scalar_with_continuation(lines, index, indent, item_text)
            result.append(value)
    return result, index


def _parse_block_string(
    lines: list[str], index: int, parent_indent: int, style: str
) -> tuple[str, int]:
    block_lines: list[str] = []
    base_indent: int | None = None
    while index < len(lines):
        current_indent = _indent_of(lines[index])
        if current_indent <= parent_indent:
            break
        if base_indent is None:
            base_indent = current_indent
        block_lines.append(lines[index][base_indent:])
        index += 1
    if style == ">":
        return " ".join(part.strip() for part in block_lines).strip(), index
    return "\n".join(block_lines), index


def _split_key_value(text: str, index: int) -> tuple[str, str]:
    if ":" not in text:
        raise ValueError(f"Expected key/value YAML pair near line {index + 1}: {text}")
    key, value = text.split(":", 1)
    return key.strip(), value.strip()


def _parse_scalar(raw: str) -> Any:
    if raw == "":
        return ""
    lowered = raw.lower()
    if lowered in {"null", "none", "~"}:
        return None
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if raw in {"[]", "{}"}:
        return [] if raw == "[]" else {}
    if raw.startswith(('"', "'")):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return raw.strip("\"'")
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        return raw


def _parse_scalar_with_continuation(
    lines: list[str],
    index: int,
    indent: int,
    raw: str,
) -> tuple[Any, int]:
    parts = [raw]
    index += 1
    while index < len(lines):
        current_indent = _indent_of(lines[index])
        if current_indent <= indent:
            break
        stripped = lines[index].strip()
        if stripped.startswith("- ") or _looks_like_key_value(stripped):
            break
        parts.append(stripped)
        index += 1
    return _parse_scalar(" ".join(parts)), index


def _looks_like_key_value(text: str) -> bool:
    return re.match(r"^[A-Za-z0-9_-]+:", text) is not None


def _dump_value(value: Any, indent: int) -> list[str]:
    if isinstance(value, dict):
        return _dump_mapping(value, indent)
    if isinstance(value, list):
        return _dump_list(value, indent)
    return [" " * indent + _format_scalar(value)]


def _dump_mapping(mapping: dict[str, Any], indent: int) -> list[str]:
    lines: list[str] = []
    prefix = " " * indent
    for key, value in mapping.items():
        if isinstance(value, dict):
            if not value:
                lines.append(f"{prefix}{key}: {{}}")
            else:
                lines.append(f"{prefix}{key}:")
                lines.extend(_dump_mapping(value, indent + 2))
        elif isinstance(value, list):
            if not value:
                lines.append(f"{prefix}{key}: []")
            else:
                lines.append(f"{prefix}{key}:")
                lines.extend(_dump_list(value, indent + 2))
        elif isinstance(value, str) and "\n" in value:
            lines.append(f"{prefix}{key}: |")
            for block_line in value.splitlines():
                lines.append(" " * (indent + 2) + block_line)
        else:
            lines.append(f"{prefix}{key}: {_format_scalar(value)}")
    return lines


def _dump_list(values: list[Any], indent: int) -> list[str]:
    lines: list[str] = []
    prefix = " " * indent
    for item in values:
        if isinstance(item, dict):
            if not item:
                lines.append(f"{prefix}- {{}}")
                continue
            first_key = next(iter(item))
            first_value = item[first_key]
            if isinstance(first_value, (dict, list)):
                lines.append(f"{prefix}- {first_key}:")
                lines.extend(_dump_value(first_value, indent + 4))
            else:
                lines.append(f"{prefix}- {first_key}: {_format_scalar(first_value)}")
            for key, value in list(item.items())[1:]:
                if isinstance(value, (dict, list)):
                    lines.append(f"{prefix}  {key}:")
                    lines.extend(_dump_value(value, indent + 4))
                else:
                    lines.append(f"{prefix}  {key}: {_format_scalar(value)}")
        elif isinstance(item, list):
            lines.append(f"{prefix}-")
            lines.extend(_dump_list(item, indent + 2))
        else:
            lines.append(f"{prefix}- {_format_scalar(item)}")
    return lines


def _format_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        if value == "":
            return '""'
        if _is_plain_string(value):
            return value
        return json.dumps(value, ensure_ascii=False)
    return json.dumps(value, ensure_ascii=False)


def _is_plain_string(value: str) -> bool:
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-./")
    if all(char in allowed for char in value):
        return not value.lower() in {"true", "false", "null", "none"}
    return False
