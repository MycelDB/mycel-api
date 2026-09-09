#!/usr/bin/env python3
"""Generate docs/legal/dependency-license-inventory.tsv for the API repository."""
from __future__ import annotations

import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "legal" / "dependency-license-inventory.tsv"
BUF = ROOT / "buf.yaml"


def main() -> None:
    text = BUF.read_text() if BUF.exists() else ""
    if "deps:" in text:
        raise SystemExit("buf.yaml declares external deps; extend this script to inventory their licenses before release")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["Ecosystem", "Package", "Version", "Scope", "License", "License files", "Source"])


if __name__ == "__main__":
    main()
