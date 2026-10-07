#!/usr/bin/env python3
"""Validate the controlled trilogy shot register and production-count contract."""

from pathlib import Path
import re

REGISTER = Path("production/TRILOGY_MASTER_SHOT_REGISTER.md")
TRACKER = Path("production/PIPELINE_TRACKER.md")

text = REGISTER.read_text(encoding="utf-8")
tracker = TRACKER.read_text(encoding="utf-8")

ids = re.findall(r"\| ((?:PI|PII|PIII)-S\d{2}-SH\d{3}) \|", text)
if len(ids) != 180:
    raise SystemExit(f"Expected 180 controlled coverage records; found {len(ids)}")

if len(ids) != len(set(ids)):
    raise SystemExit("Duplicate shot IDs detected")

expected = {"PI": 50, "PII": 70, "PIII": 60}
for prefix, count in expected.items():
    actual = sum(shot.startswith(prefix + "-") for shot in ids)
    if actual != count:
        raise SystemExit(f"{prefix}: expected {count}, found {actual}")

if "212 controlled coverage records" in tracker or "212+ final shot records" in tracker:
    raise SystemExit("Tracker still contains obsolete 212-shot count")

print("Production register QA: PASS")
print("PI=50, PII=70, PIII=60, total=180")
