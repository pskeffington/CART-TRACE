#!/usr/bin/env python3
"""Validate Gate 2B readiness metadata and emit deterministic reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from cart_trace.access_gate2_reporting import (
    build_gate2b_readiness_report,
    render_gate2b_readiness_markdown,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "access_gate_2b_readiness_input.schema.json"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate metadata-only Gate 2B readiness input and generate JSON/Markdown reports."
    )
    parser.add_argument("input", type=Path, help="Path to Gate 2B readiness metadata JSON")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA, help="Readiness input JSON schema")
    parser.add_argument("--json-out", type=Path, help="Optional JSON report output path")
    parser.add_argument("--markdown-out", type=Path, help="Optional Markdown report output path")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text())
    schema = json.loads(args.schema.read_text())
    Draft202012Validator(schema).validate(payload)

    report = build_gate2b_readiness_report(payload)
    rendered_json = json.dumps(report, indent=2, sort_keys=True) + "\n"
    rendered_markdown = render_gate2b_readiness_markdown(report)

    if args.json_out:
        args.json_out.write_text(rendered_json)
    if args.markdown_out:
        args.markdown_out.write_text(rendered_markdown)
    if not args.json_out and not args.markdown_out:
        print(rendered_json, end="")

    return 0 if report["ready_for_governed_sample_review"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
