import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas" / "access_gate_2b_readiness_input.schema.json").read_text())
TEMPLATE = json.loads((ROOT / "examples" / "templates" / "access_gate_2b_readiness_input.template.json").read_text())
FIXTURES = json.loads((ROOT / "examples" / "synthetic" / "access_gate_2b_readiness_fixtures.json").read_text())
SCRIPT = ROOT / "scripts" / "generate_gate2b_readiness_report.py"


def test_blank_template_validates_and_fails_closed():
    Draft202012Validator(SCHEMA).validate(TEMPLATE)
    completed = subprocess.run(
        [sys.executable, str(SCRIPT), str(ROOT / "examples" / "templates" / "access_gate_2b_readiness_input.template.json")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 2
    report = json.loads(completed.stdout)
    assert report["gate2b_entry_status"] == "not_ready"
    assert "authorization" in report["aggregate_hard_blockers"]


def test_governed_ready_payload_returns_zero_and_writes_reports(tmp_path):
    payload = {
        "readiness_input_version": "0.1.0",
        "sources": [FIXTURES["sources"][0]],
    }
    input_path = tmp_path / "ready.json"
    json_out = tmp_path / "report.json"
    markdown_out = tmp_path / "report.md"
    input_path.write_text(json.dumps(payload))

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(input_path),
            "--json-out",
            str(json_out),
            "--markdown-out",
            str(markdown_out),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0
    report = json.loads(json_out.read_text())
    assert report["gate2b_entry_status"] == "ready"
    assert "Ready for governed sample review:** true" in markdown_out.read_text()


def test_cli_output_is_deterministic(tmp_path):
    payload = {
        "readiness_input_version": "0.1.0",
        "sources": [FIXTURES["sources"][0], FIXTURES["sources"][2]],
    }
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"
    input_a = tmp_path / "a.json"
    input_b = tmp_path / "b.json"
    input_a.write_text(json.dumps(payload))
    reversed_payload = dict(payload)
    reversed_payload["sources"] = list(reversed(payload["sources"]))
    input_b.write_text(json.dumps(reversed_payload))

    for input_path, output_path in [(input_a, first), (input_b, second)]:
        subprocess.run(
            [sys.executable, str(SCRIPT), str(input_path), "--json-out", str(output_path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    assert first.read_text() == second.read_text()
