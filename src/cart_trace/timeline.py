"""Treatment-relative time utilities.

The primary analytic anchor is CAR T-cell infusion (Day 0). Original timestamps
must always be retained by calling code; this module derives relative time only.
"""

from __future__ import annotations

from datetime import datetime


def relative_day(observed_at: datetime, infusion_at: datetime) -> float:
    """Return fractional days from CAR T-cell infusion.

    Negative values are pre-infusion; zero is infusion time; positive values are
    post-infusion. Both datetimes must either be timezone-aware or timezone-naive.
    """
    if (observed_at.tzinfo is None) != (infusion_at.tzinfo is None):
        raise ValueError("observed_at and infusion_at must have matching timezone awareness")
    return (observed_at - infusion_at).total_seconds() / 86400.0


def relative_window(day: float) -> str:
    """Map a relative day to a coarse research window.

    These bins are descriptive defaults only and are not clinical management rules.
    """
    if day < -30:
        return "remote_pre_infusion"
    if day < -7:
        return "pre_infusion"
    if day < 0:
        return "lymphodepletion_window"
    if day <= 7:
        return "acute_post_infusion"
    if day <= 30:
        return "early_recovery"
    if day <= 100:
        return "intermediate_followup"
    return "long_term_followup"
