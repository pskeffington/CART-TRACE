"""Simple provenance records for reproducible research transformations."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
from typing import Any


@dataclass(frozen=True)
class TransformationRecord:
    name: str
    parameters: dict[str, Any]
    input_ids: tuple[str, ...]
    created_at: datetime

    @classmethod
    def create(cls, name: str, parameters: dict[str, Any], input_ids: list[str]) -> "TransformationRecord":
        return cls(
            name=name,
            parameters=parameters,
            input_ids=tuple(input_ids),
            created_at=datetime.now(timezone.utc),
        )

    def fingerprint(self) -> str:
        payload = {
            "name": self.name,
            "parameters": self.parameters,
            "input_ids": self.input_ids,
            "created_at": self.created_at.isoformat(),
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return sha256(encoded).hexdigest()
