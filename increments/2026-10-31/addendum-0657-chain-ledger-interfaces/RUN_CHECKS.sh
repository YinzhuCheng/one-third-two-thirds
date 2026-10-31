#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python artifacts/ledger/rerun_ledger.py > LEDGER_RERUN.txt
python artifacts/ledger/verify_cardinality_examples.py > CARDINALITY_RERUN.json
python artifacts/rank/rerun_sharp_audit.py > SHARP_RERUN.txt
python artifacts/common_successor/rerun_common_pair_roof.py > ROOF_RERUN.txt
python artifacts/motif/verify_examples.py > MOTIF_RERUN.txt
python artifacts/chain/verify_chain_compensation_standalone.py artifacts/chain/chain_compensation_witness_delayed_validation.json > CHAIN_WITNESS_RERUN.txt
python artifacts/chain/chain_compensation_delayed_independent_check.py artifacts/chain/chain_compensation_witness_delayed_validation.json artifacts/chain/chain_compensation_delayed_independent_validation.json > CHAIN_INDEPENDENT_RERUN.txt
# Optional longer finite stress test (not needed for general proof):
# python artifacts/chain/audit_chain_compensation_small.py
printf 'PASS: seven archived checks completed.\n'
