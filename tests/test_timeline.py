from datetime import UTC, datetime

import pytest

from cart_trace.timeline import relative_day, relative_window


def test_relative_day_after_infusion():
    infusion = datetime(2026, 1, 10, tzinfo=UTC)
    observed = datetime(2026, 1, 13, 12, tzinfo=UTC)
    assert relative_day(observed, infusion) == 3.5


def test_relative_day_before_infusion():
    infusion = datetime(2026, 1, 10, tzinfo=UTC)
    observed = datetime(2026, 1, 9, tzinfo=UTC)
    assert relative_day(observed, infusion) == -1.0


def test_timezone_awareness_must_match():
    infusion = datetime(2026, 1, 10, tzinfo=UTC)
    observed = datetime(2026, 1, 10, tzinfo=UTC).replace(tzinfo=None)
    with pytest.raises(ValueError):
        relative_day(observed, infusion)


def test_relative_window_is_descriptive():
    assert relative_window(0) == "acute_post_infusion"
    assert relative_window(14) == "early_recovery"
    assert relative_window(120) == "long_term_followup"
