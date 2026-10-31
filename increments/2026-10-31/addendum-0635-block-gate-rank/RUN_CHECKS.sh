#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python artifacts/block/verify_block_witness_standalone.py artifacts/block/block_witness_validation.json > BLOCK_RERUN.txt
python artifacts/free_gate/verify_obstruction.py > OBSTRUCTION_RERUN.txt
python artifacts/independent_audit/rerun_independent_audit.py > INDEPENDENT_RERUN.txt
python artifacts/free_gate/verify_analytic_integrals.py > ANALYTIC_RERUN.txt
python artifacts/external_tools/verify_deletion_interface.py > DELETION_RERUN.txt
python artifacts/rank_budget/audit_rank_budget_independent.py > RANK_BUDGET_RERUN.txt
python artifacts/rank_budget/check.py artifacts/rank_budget/candidate.json > RANK_WITNESS_RERUN.txt
printf 'PASS: all archived checks completed. Requires Python 3 and SymPy.\n'
