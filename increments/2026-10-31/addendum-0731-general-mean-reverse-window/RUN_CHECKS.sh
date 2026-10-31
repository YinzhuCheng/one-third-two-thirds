#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python artifacts/general/independent_general_poset_check.py > GENERAL_RERUN.txt
python artifacts/nonuniform/rerun_frontier_independent_check.py > FRONTIER_RERUN.json
python artifacts/nonuniform/rerun_reverse_window_independent_check.py > REVERSE_RERUN.json
python artifacts/nonuniform/verify_gap.py > GAP_RERUN.txt
python artifacts/general/verify_cutoff_counterexample.py > CUTOFF_RERUN.json
printf 'PASS: five checks completed.\n'
