#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python artifacts/exact_mean/independent_mean_separation_check.py > MEAN_SEPARATION_RERUN.json
python artifacts/obstruction/verify_scope.py > SCOPE_RERUN.json
python artifacts/exact_mean/independent_elasticity_search.py > ELASTICITY_RERUN.txt
python artifacts/exact_mean/verify_module_and_threshold.py > MODULE_THRESHOLD_RERUN.json
printf 'PASS: all four checks completed.\n'
