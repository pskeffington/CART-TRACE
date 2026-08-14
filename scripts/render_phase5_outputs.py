"""Render deterministic Phase 5 scholarly artifacts from controlled JSON outputs.

Run from the repository root after generating the Phase 5 JSON artifacts:

    python scripts/generate_phase5_outputs.py
    python scripts/render_phase5_outputs.py

This module does not reconstruct episodes or calculate metrics. It only converts
controlled Phase 5 JSON outputs into manuscript-facing Markdown tables and SVG
figures using the Python standard library.
"""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "examples" / "outputs"
OUTPUT_DIR = ROOT / "examples" / "rendered"

STATE_LABELS = {
    "outpatient": "Outpatient",
    "emergency": "Emergency",
    "routine_inpatient": "Routine inpatient",
    "intermediate_care": "Intermediate care",
    "intensive_care": "Intensive care",
    "discharged": "Discharged",
    "unknown": "Unknown",
}


def _load(name: str, input_dir: Path = INPUT_DIR) -> Any:
    path = input_dir / name
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run scripts/generate_phase5_outputs.py first."
        )
    return json.loads(path.read_text())


def _format(value: Any) -> str:
    if value is None:
        return "NA"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, float):
        return f"{value:.3f}".rstrip("0").rstrip(".")
    return str(value)


def _markdown_table(headers: Sequence[str], rows: Iterable[Sequence[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        values = [str(_format(value)).replace("|", "\\|") for value in row]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines) + "\n"


def render_table3(
    reconstruction: Mapping[str, Any], validation_rows: Sequence[Mapping[str, Any]]
) -> str:
    metric_total = len(validation_rows)
    metric_pass = sum(bool(row.get("exact_match")) for row in validation_rows)
    rows = [
        (
            "Interval signatures",
            reconstruction.get("interval_fixture_count"),
            reconstruction.get("interval_fixture_pass_count"),
            reconstruction.get("interval_exact_agreement_fraction"),
            "Exact agreement with prespecified synthetic oracle",
        ),
        (
            "Transition signatures",
            reconstruction.get("transition_fixture_count"),
            reconstruction.get("transition_fixture_pass_count"),
            reconstruction.get("transition_exact_agreement_fraction"),
            "Exact agreement with prespecified synthetic oracle",
        ),
        (
            "Metric expected values",
            metric_total,
            metric_pass,
            metric_pass / metric_total if metric_total else None,
            "Exact agreement across generated validation rows",
        ),
    ]
    heading = (
        "# Table 3. Synthetic reconstruction and metric validation results\n\n"
        "Synthetic demonstration only; these results establish computational fidelity "
        "to the CART-TRACE specification, not external clinical validity.\n\n"
    )
    return heading + _markdown_table(
        ["Validation domain", "Denominator", "Exact matches", "Agreement fraction", "Interpretation"],
        rows,
    )


def render_table4(summary_rows: Sequence[Mapping[str, Any]]) -> str:
    rows = [
        (
            row.get("metric_id"),
            row.get("episode_count"),
            row.get("available_count"),
            row.get("not_applicable_count"),
            row.get("not_calculable_count"),
            row.get("incomplete_followup_count"),
            row.get("mean"),
            row.get("median"),
            row.get("minimum"),
            row.get("maximum"),
        )
        for row in summary_rows
    ]
    heading = (
        "# Table 4. Descriptive utilization summary for the synthetic demonstration cohort\n\n"
        "Numeric summaries use observed values and observed zeros only. Availability and "
        "incomplete follow-up remain explicit.\n\n"
    )
    return heading + _markdown_table(
        [
            "Metric",
            "Episodes",
            "Available n",
            "Not applicable n",
            "Not calculable n",
            "Incomplete follow-up n",
            "Mean",
            "Median",
            "Minimum",
            "Maximum",
        ],
        rows,
    )


def render_table5(summary: Mapping[str, Any]) -> str:
    status_counts = summary.get("metric_status_counts", {})
    rows = [
        ("Episodes", summary.get("episode_count")),
        (
            "Episodes with uncertain or unknown state",
            summary.get("episodes_with_uncertain_or_unknown_state"),
        ),
    ]
    rows.extend((f"Metric status: {status}", count) for status, count in sorted(status_counts.items()))
    heading = (
        "# Table 5. Missingness, uncertainty, and metric availability\n\n"
        "Synthetic demonstration only. Unknown-state burden and metric availability are "
        "reported explicitly rather than converted to observed zeros.\n\n"
    )
    return heading + _markdown_table(["Measure", "Count"], rows)


def render_supplementary_metric_matrix(
    metric_results: Sequence[Mapping[str, Any]],
) -> str:
    """Render one row per episode with each metric value paired to its status."""
    metric_ids = sorted(
        {
            metric_id
            for result in metric_results
            for metric_id in (result.get("values") or {}).keys()
        }
    )
    headers = ["Episode"] + metric_ids
    rows = []
    for result in sorted(metric_results, key=lambda item: str(item.get("episode_id"))):
        values = result.get("values") or {}
        statuses = result.get("status") or {}
        row = [result.get("episode_id")]
        for metric_id in metric_ids:
            row.append(f"{_format(values.get(metric_id))} [{statuses.get(metric_id, 'NA')}]")
        rows.append(row)
    heading = (
        "# Supplementary Table S1. Complete metric-result matrix by synthetic episode\n\n"
        "Synthetic demonstration only. Each cell reports the controlled metric value followed "
        "by its metric status in brackets; unavailable results are not coerced to zero.\n\n"
    )
    return heading + _markdown_table(headers, rows)


def _trajectory_selection(
    trajectories: Mapping[str, Sequence[Mapping[str, Any]]]
) -> list[str]:
    selected: list[str] = []
    predicates = [
        lambda rows: all(row.get("state") not in {"intermediate_care", "intensive_care", "unknown"} for row in rows),
        lambda rows: any(row.get("state") == "intermediate_care" for row in rows),
        lambda rows: any(row.get("state") == "intensive_care" for row in rows),
        lambda rows: any(row.get("state") == "unknown" or row.get("uncertain") for row in rows),
    ]
    for predicate in predicates:
        for episode_id, rows in trajectories.items():
            if episode_id not in selected and predicate(rows):
                selected.append(episode_id)
                break
    for episode_id in trajectories:
        if len(selected) >= 4:
            break
        if episode_id not in selected:
            selected.append(episode_id)
    return selected[:4]


def render_trajectory_svg(
    trajectories: Mapping[str, Sequence[Mapping[str, Any]]],
    episode_ids: Sequence[str],
    title: str,
) -> str:
    width = 1100
    left = 210
    right = 40
    top = 90
    row_height = 58
    plot_width = width - left - right
    height = top + row_height * len(episode_ids) + 80

    def x(hour: float) -> float:
        return left + (max(0.0, min(720.0, hour)) / 720.0) * plot_width

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{left}" y="35" font-family="sans-serif" font-size="22" font-weight="bold">{html.escape(title)}</text>',
        f'<text x="{left}" y="58" font-family="sans-serif" font-size="13">Synthetic demonstration; infusion = 0 h; analytic boundary = 720 h (Day +30)</text>',
    ]

    for tick in (0, 168, 336, 504, 720):
        xpos = x(float(tick))
        parts.append(f'<line x1="{xpos:.1f}" y1="{top-12}" x2="{xpos:.1f}" y2="{height-48}" stroke="#dddddd"/>')
        parts.append(f'<text x="{xpos:.1f}" y="{height-25}" text-anchor="middle" font-family="sans-serif" font-size="11">{tick} h</text>')

    patterns = {
        "outpatient": "#f2f2f2",
        "emergency": "#d9d9d9",
        "routine_inpatient": "#bdbdbd",
        "intermediate_care": "#969696",
        "intensive_care": "#737373",
        "discharged": "#eeeeee",
        "unknown": "#ffffff",
    }

    for row_index, episode_id in enumerate(episode_ids):
        y = top + row_index * row_height
        parts.append(f'<text x="{left-12}" y="{y+23}" text-anchor="end" font-family="sans-serif" font-size="12">{html.escape(episode_id)}</text>')
        for interval in trajectories.get(episode_id, []):
            start = interval.get("start_relative_hours")
            end = interval.get("end_relative_hours")
            if start is None or end is None:
                continue
            state = str(interval.get("state"))
            xpos = x(float(start))
            xend = x(float(end))
            rect_width = max(1.0, xend - xpos)
            dash = ' stroke-dasharray="5 3"' if state == "unknown" or interval.get("uncertain") else ""
            parts.append(
                f'<rect x="{xpos:.1f}" y="{y+5}" width="{rect_width:.1f}" height="28" '
                f'fill="{patterns.get(state, "#ffffff")}" stroke="#222222"{dash}/>'
            )
            if rect_width >= 75:
                label = STATE_LABELS.get(state, state)
                parts.append(f'<text x="{xpos+4:.1f}" y="{y+23}" font-family="sans-serif" font-size="10">{html.escape(label)}</text>')

    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def render_utilization_availability_svg(summary_rows: Sequence[Mapping[str, Any]]) -> str:
    """Render Figure 3 with descriptive values and explicit metric availability."""
    rows = list(summary_rows)
    width = 1200
    left = 280
    right = 70
    top = 110
    row_height = 54
    height = top + row_height * len(rows) + 95
    plot_width = width - left - right
    maximum = max(
        [
            float(row.get("maximum"))
            for row in rows
            if isinstance(row.get("maximum"), (int, float)) and not isinstance(row.get("maximum"), bool)
        ]
        or [1.0]
    )

    def x(value: float) -> float:
        return left + max(0.0, value) / maximum * plot_width

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{left}" y="35" font-family="sans-serif" font-size="22" font-weight="bold">Figure 3. Synthetic cohort utilization and metric availability</text>',
        f'<text x="{left}" y="58" font-family="sans-serif" font-size="13">Synthetic demonstration; numeric summaries use observed and observed-zero results only.</text>',
        f'<text x="{left}" y="78" font-family="sans-serif" font-size="13">Availability labels retain not-applicable, not-calculable, and incomplete-follow-up counts.</text>',
    ]

    for row_index, row in enumerate(rows):
        y = top + row_index * row_height
        metric = str(row.get("metric_id"))
        median = row.get("median")
        minimum = row.get("minimum")
        maximum_value = row.get("maximum")
        parts.append(
            f'<text x="{left-12}" y="{y+18}" text-anchor="end" font-family="sans-serif" font-size="11">{html.escape(metric)}</text>'
        )
        if all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in (minimum, median, maximum_value)):
            xmin = x(float(minimum))
            xmed = x(float(median))
            xmax = x(float(maximum_value))
            parts.append(f'<line x1="{xmin:.1f}" y1="{y+12}" x2="{xmax:.1f}" y2="{y+12}" stroke="#555555" stroke-width="2"/>')
            parts.append(f'<circle cx="{xmed:.1f}" cy="{y+12}" r="4" fill="#222222"/>')
        availability = (
            f"available {row.get('available_count', 0)}/{row.get('episode_count', 0)}; "
            f"NAp {row.get('not_applicable_count', 0)}; "
            f"NC {row.get('not_calculable_count', 0)}; "
            f"IFU {row.get('incomplete_followup_count', 0)}"
        )
        parts.append(
            f'<text x="{left}" y="{y+34}" font-family="sans-serif" font-size="10">{html.escape(availability)}</text>'
        )

    parts.append(
        f'<text x="{left}" y="{height-42}" font-family="sans-serif" font-size="11">Horizontal segment = observed minimum-to-maximum; dot = observed median. NAp = not applicable; NC = not calculable; IFU = incomplete follow-up.</text>'
    )
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def render_all(input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR) -> list[Path]:
    trajectories = _load("phase5_patient_trajectories.json", input_dir)
    metric_results = _load("phase5_metric_results.json", input_dir)
    cohort = _load("phase5_cohort_summary.json", input_dir)
    metric_validation = _load("phase5_metric_validation.json", input_dir)
    reconstruction = _load("phase5_reconstruction_validation.json", input_dir)
    uncertainty = _load("phase5_uncertainty_summary.json", input_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    artifacts = {
        "table3_validation.md": render_table3(reconstruction, metric_validation),
        "table4_cohort_summary.md": render_table4(cohort),
        "table5_uncertainty.md": render_table5(uncertainty),
        "supplementary_table_s1_metric_matrix.md": render_supplementary_metric_matrix(metric_results),
        "figure2_representative_trajectories.svg": render_trajectory_svg(
            trajectories,
            _trajectory_selection(trajectories),
            "Figure 2. Representative synthetic post-infusion hospital care trajectories",
        ),
        "figure3_utilization_availability.svg": render_utilization_availability_svg(cohort),
        "figure_s1_all_trajectories.svg": render_trajectory_svg(
            trajectories,
            list(trajectories),
            "Supplementary Figure S1. Full six-episode synthetic trajectory panel",
        ),
    }
    paths = []
    for name, content in artifacts.items():
        path = output_dir / name
        path.write_text(content)
        paths.append(path)
    return paths


def main() -> None:
    for path in render_all():
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
