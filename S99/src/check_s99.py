#!/usr/bin/env python3
"""Run S99's small, exact mathematical diagnostics; not a proof of MC3."""
from pathlib import Path
import json
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    for name in ("check_release_and_fork.py", "check_mc3_boundaries.py"):
        subprocess.run([sys.executable, str(root / "src" / name)], check=True)
    evidence = {}
    for name in ("release_and_fork.json", "mc3_boundaries.json"):
        evidence[name] = json.loads((root / "evidence" / name).read_text())
    report = {
        "status": "PASSED",
        "scope": "Targeted exact diagnostics only; analytic proofs are in S99/notes.",
        "files": list(evidence),
    }
    (root / "evidence" / "summary.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
