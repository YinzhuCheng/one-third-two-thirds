Bounded weighted-seven-core obstruction census, 2026-10-10

Run using Python 3.10+; standard library only:
  python census.py --max-spine 3 --output census.json
  python verify_census.py
  python analytic_filters.py

census.py explicitly refuses a spine bound above 3. No external files are needed
for arithmetic reproduction. Run without python -O, since assertions implement
verification checks. Recorded timings may differ between machines.

Read ANALYSIS.md for scope and results. Check cone_audit.json before interpreting
finite coverage as an infinite-family consequence. The generalized cone has frozen
independent proof PASS. The rank-chain diagnostic proof supplement and a
separate computational census peer audit remain pending.

census.json stores all 2767 weights, all 18 endpoint numerators, rejection sets,
minimum covering menus, and full labelled-pair ledgers for all 21 old-menu
survivors. verification.json stores independent actual-label DP deltas and
maximizers for every weight. analytic_filters.json stores all 185 survivors of
only the four binomial bounds and their actual balanced-pair information.

Empty full-menu survivor lists mean no survivors in this explicitly finite
region. Surviving an analytic or abbreviated menu is never a counterexample.
