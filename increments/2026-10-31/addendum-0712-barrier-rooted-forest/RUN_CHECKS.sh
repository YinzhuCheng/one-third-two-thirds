#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python artifacts/stage3/rerun_fork.py > FORK_RERUN.json
python artifacts/stage3/independent_barrier_small_check.py > BARRIER_RERUN.txt
python artifacts/stage3/independent_forest_capacity_check.py > FOREST_RERUN.txt
printf 'PASS: all three finite check scripts completed.\n'
