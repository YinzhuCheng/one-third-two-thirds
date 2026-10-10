# Eight-core weight audit

Independent exact verification of the 17 frozen C02–C18 chain-inflation cores. See AUDIT.md for theorem proof, scope, counts, class restrictions and caveats.

Run `python verify_snapshot.py` for hash verification and a fresh temporary reproduction, or run `python audit.py` and `python audit_windows.py` directly. Python standard library only. All files in this directory are text.

Only the top-level `elapsed_seconds` field in audit_results.json and its log rendering vary on reproduction. all_pair_counts.json and window_results.json reproduce byte for byte.
