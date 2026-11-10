# Finite adjacent-support result: source and replay

Original source: Kevin Fathi, *Gold Certificates and Balanced Pairs*, fixed v22 at https://zenodo.org/records/23933091. The project ZIP is `Balanced_Pairs_Sequel_Complete_Project(3).zip`; the relevant member prefix is `Balanced_Pairs_Sequel/research/current/continuation_085/verification/degree_nine/singleton_two_leaf/independent/`.

The original `packet.json`, `verify.cpp`, `verify.py`, and `PROOF.md` are source materials, not authored by this project. Obtain them from that fixed record; this increment does not duplicate the entire original packet or verifier. Compile the original `verify.cpp` with C++17/O2, then feed the supplied `THIRTEEN_ADJACENT_REPLAY_INPUT.txt` to it. The independently checked output is:

```
nodes 13 gates 67886 inequalities 55987 largest extension count 166152 minimum slack 32
```

The 67886 raw profiles include terminal-inapplicable cases; 55987 are the applicable inequalities. The state/event/weight mapping is supplied in `THIRTEEN_SKIP_STATES.json` and `THIRTEEN_ADJACENT_REPLACEMENTS.json`; independent per-row results are in `INDEPENDENT_THIRTEEN_PER_ROW.json`. The independent review explains exact mode0/mode1 scope and original-tree coverage.

Separately, the unmodified original full driver completed structural reconstruction and original-bank arithmetic: 7 phases, 1313 marked-ideal occurrences, 38,836,011 profile occurrences, 79,763,778 integer inequalities, exit 0, minimum slack 0. This was a replay of the author's original checker, not a new independently implemented full-tree counting algorithm. Combining unchanged original 3456 adjacent banks with the 13 checked replacements proves the stated finite supplied-tree support result.

No claim is made about all marked states or D10. These checks do not replace the source theorem's other reductions or certificate families. Other diagnostic code and large historical logs are not part of this public increment; their omission is not a new verification claim.
