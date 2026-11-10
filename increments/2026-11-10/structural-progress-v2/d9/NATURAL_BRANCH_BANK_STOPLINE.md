# Natural-reference rooted-branch extension: exact stopping line

2026-11-10. Actual original-poset control, internally independently reviewed PASS in NATURAL_BRANCH_BANK_STOPLINE_INDEPENDENT_REVIEW.md; not a coverage addition or NB counterexample.

The Q7 natural-reference source bank is

    14Pr(u<b)+8Pr(v<u)+4Pr(p<v)+Pr(q<p)>=9.

It cannot be extended unchanged to arbitrary larger p-rooted branches beside an isolated common head q, even in degree seven.

Take P=Q with a,b,u,v as usual and H={q} disjoint from an arbitrary n-point branch B with unique minimum p. Every H point is above b,u, and H is incomparable with v. There is no exterior. For each internal branch word, all branch gaps are zero. In the original root insertion calculation put d=e=0, Z=n and F=n+1. The exact three-times-bank margin is

    (6-3Z)F-6+6Z=3n(3-n).

Thus the total margin is 3n(3-n)e(B), independent of the internal shape of B. The original n=2 branch has positive margin; n=3 is tight; every n>=4 gives a negative margin for this fixed bank. This statement concerns the displayed coefficients, not all possible coefficient choices or event sets.

For the smallest failure choose B to be p below three incomparable leaves. Then

    pred(P)=(0,0,1,1,7,7,23,23,23),
    Delta(P)=7,
    N=690,
    (K_ub,K_vu,K_pv,K_qp)=(240,120,432,138),
    3(14K_ub+8K_vu+4K_pv+K_qp)-27N=-72.

NATURAL_BRANCH_BANK_STOPLINE.py/.json reconstruct this actual nine-point poset and verify all counts by full ideal-subset DP. Its three branch leaves are fair twins, so the example is not NB and does not contradict ordinary balance. It also does not affect the new isolated-head bank in the OPPOSITE reference direction, which charges p<q rather than q<p and uses weights7,2,1.

No live ledger change follows from this stopping line.
