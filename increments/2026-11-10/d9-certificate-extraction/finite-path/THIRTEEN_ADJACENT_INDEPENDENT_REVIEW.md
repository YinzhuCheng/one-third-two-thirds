# Independent audit: thirteen adjacent-bank replacements in the supplied D9 v-first packet

2026-11-10. **PASS_WITH_EXACT_FINITE_SCOPE: targeted mapping, thirteen replacement banks, and full original-tree replay all passed.** This is a finite certificate-support audit, not an analytic D9 proof or a D10 theorem. The whole-tree result is recorded below.

> Public-edition note: this is the mathematical audit record. Historical checker sources, logs and mapping scripts mentioned below were read during that audit but are not all included in this public increment. The supplied files and source-based replay instructions are listed in [REPRODUCTION.md](REPRODUCTION.md).

## Source and method actually checked

Read original Fathi v22 §24.1 and §24.4.1, the supplied singleton-two-leaf independent `PROOF.md`, `verify.py`, `verify.cpp`, `packet.json`, and all files of the thirteen-row replacement bundle. `cmp` confirms that `ORIGINAL_V_FIRST_PACKET.json` and `ORIGINAL_INTEGER_REPLAY.cpp` are byte-identical to the corresponding extracted original independent source members. This verifies the local source correspondence, not independently the HTTP-Range retrieval or Zenodo ZIP transport provenance.

The source CPP was compiled afresh with C++17/O2 and run on the replacement input, then rerun independently on each of the13 input records. Results:

    nodes13 gates67886 inequalities55987 largest extension count166152 minimum slack32

All13 individual applicable-profile counts and minimum raw slacks also agree with the replacement metadata. No numeric LP status or floating margin is used as proof. Exact original-source integer arithmetic checks the new unit banks.

## Exact original-node and event mapping

`INDEPENDENT_MAPPING_CHECK.py` separately reconstructs the flattened packet and detects its nonadjacent banks, without trusting the author's list. It finds exactly13 such occurrences. Each listed state matches exactly ONE original `(stage,node,row)` with its full predecessor array, reference word, fixed set, pivot, mode and original indexed bank. Detailed locations are in `INDEPENDENT_MAPPING_CHECK.json`.

For each reference, the check regenerates ALL consecutive incomparable pairs, directed from the later label toward the earlier label. These equal the stored candidate event list exactly. Selecting its positive replacement coefficients gives1–3 events, all unit weights; each reverses the named reference and has distance1. The regenerated complete13-record integer input is byte-identical to `THIRTEEN_ADJACENT_REPLAY_INPUT.txt`.

This checks a change of bank, NOT a relabeling of a source node, change of profile scope, or omission of an inconvenient reference. The two rows sharing the seven-label predecessor array remain distinct reference-word states.

## Full domain and terminal-scope audit

The source verifier generates deadline vectors subject to:

* h_i<=9−d_Q(i), with nonnegative integer h_i;
* h_x<=h_y for every x<y;
* h_0=0 and h_j=0 for every remembered fixed label j;
* min(h_1,h_2,h_3)=0.

For mode0 it checks ALL generated profiles. For mode1 it checks only profiles with h_pivot=0. The replacement mapping preserves modes:9 mode0 records and4 mode1 records. All4 terminal replacements use pivot3 with no remembered fixed labels. The total67886 counts raw generated profiles, including those inapplicable to mode1. The applicable55987 are the actual checked weighted inequalities. Per-row details are in `INDEPENDENT_THIRTEEN_PER_ROW.json`.

The terminal justification remains the original structural one: the actual pivot's exterior incomparable neighborhood is exhausted, so the pivot lies below EVERY remaining exterior label and has zero deadline in EVERY actual exterior word. Neither the source proof nor this audit permits selecting a terminal bank merely because one conditioned word happens to have h_pivot=0.

## What3469 counts, and what the whole-tree statement means

Direct packet reconstruction gives:

*7 phases;
*1313 marked-ideal OCCURRENCES,1307 distinct predecessor arrays;
*3049 unconditional bank records plus420 terminal bank records =3469 bank OCCURRENCES;
*3469 distinct `(pred,reference,fixed,pivot,mode)` bank states;
*8 bankless switch records, counted separately.

The raw stored index/weight vectors have1648 distinct encodings. That number depends on state-specific pair indexing and is NOT an abstract graph/isomorphism count.

Before replacement,3456 bank occurrences are already reference-adjacent;13 contain a distance2 comparison. After replacement every one of the3469 bank occurrences in THIS SUPPLIED v-first tree can be expressed using reference-adjacent incomparable reversals, with state-dependent nonnegative weights. The8 switches remain switches and retain the original phase coverage argument.

The original `verify.py` reconstructs the full seven-phase route from the four-label root, all admissible canonical children, terminal versus nonterminal alternatives, and all retained reference insertions; it verifies exact equality of generated and stored node/reference domains. It is this structural reconstruction, not the metadata census alone, that licenses the finite whole-tree coverage quantifier.

The whole-tree statement does NOT quantify over all degree9 marked states, all possible reference words on arbitrary ideals, all D9 certificate trees, D10, or unbounded parameters. It does NOT imply equal coefficients suffice everywhere. The original complete theorem still depends on its other structural reductions and separate certificate families.

## Proof status and remaining issue

The13 replacements and node/domain mapping passed direct audit. The unmodified original full `verify.py` separately completed its full structural generation AND all-bank arithmetic replay, exit0, in37.874 seconds wall time:1313 core occurrences,38,836,011 gate profiles,79,763,778 integer inequalities, largest extension count1,605,780, minimum slack0. Complete log: `INDEPENDENT_WHOLE_TREE_REPLAY.log`; scope audit: `WHOLE_TREE_REPLAY_REVIEW.md`. This is a fresh run of the original independent checker, not a newly implemented independent counting algorithm. Together, the unchanged original3456 adjacent-bank occurrences and the13 audited replacements justify the finite modified-whole-tree support claim; running the whole arithmetic a second time with only those13 banks changed is unnecessary for that logical combination and was not done.

No generator bias has been established or ruled out; the original generation program was not found. Adjacent sparsity is a rigorous finite observation here, not a reason to claim a universal path-bank theorem. A parameterized analytic path-bank statement remains a possible conjectural research target.

## Durable full-replay source

The original research audit bundle retained the unmodified structural driver and companion proof as `ORIGINAL_TREE_VERIFY.py` and `ORIGINAL_TREE_PROOF.md`, together with the original packet and C++ verifier. These original-author sources are not duplicated in this public increment. Obtain `verify.py`, `PROOF.md`, `packet.json` and `verify.cpp` from the fixed Fathi v22 source record and keep the original sibling filenames. See [REPRODUCTION.md](REPRODUCTION.md) for the exact member prefix and the supplied thirteen-bank input. Historical full logs and separately implemented mapping scripts are audit artifacts referenced above, not additional files promised by this public edition.
