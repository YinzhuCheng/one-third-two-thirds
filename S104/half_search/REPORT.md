# S104: HALF is refuted by real width-three posets

Date: 2026-10-10. Status: **HALF REFUTED**.

This report disproves the exact implication

P(a<x)>2/3, P(a<y)>2/3, P(x<y)>2/3 => 2 P(b<x)>=P(a<x),

under width(P)<=3, minimal x,y, and P minus the union of their upsets equal to the two-element chain a<b. Every probability uses the uniform law on complete linear extensions of the original P.

The examples below do not refute the two-step MC3 menu: (b,x) remains balanced. They also do not refute the weaker proposed bound L. A separate investigation subsequently found a counterexample to L; see `../L_family_counterexample.json`. No general MC3 conclusion follows from either auxiliary refutation.

## A 16-element certificate

Take vertices a,b,x,y,v1,v2,z1,...,z10 and the transitive closure of

- y<v1<v2;
- a<v1 and x<v2;
- a<b<z1<...<z10;
- x<z1.

The three chains {y,v1,v2}, {x}, {a,b,z1,...,z10} cover P, so width<=3. The minimal elements a,x,y form a three-antichain, so width=3. Every vertex besides a,b lies above x or y, while a,b lie above neither. Thus the exact avoidance set is {a,b}. The backend is genuinely non-neutral: every zi requires x as well as b.

There are E=1603 complete linear extensions. In the order

(a<x), (a<y), (b<x), (b<y), (x<y),

the exact counts are

1083, 1269, 539, 935, 1092.

The three strict-majority integer slacks 3K-2E are 43, 601, 70, all positive. Yet

2*539-1083=-5<0.

Hence HALF is false under its full stated hypotheses. Meanwhile

3*539-1603=14>0 and 3*539<2*1603,

so (b,x) is balanced and the example is not an MC3 counterexample. The n=16 size is not claimed globally minimal.

`SMALLER_COUNTEREXAMPLE.json` gives the input; `verified_smaller_counterexample.json` gives a complete cover/chain/count certificate. The verifier independently checks:

1. all 1603 complete linear extensions, by direct vertex-by-vertex enumeration;
2. each event by adding its order relation and recomputing an integer ideal DP;
3. the exact two-deletion insertion-fiber sum, including all original weights.

The first discovered n=20 certificate is preserved in `COUNTEREXAMPLE.json` and `verified_counterexample.json`: E=13665 and oriented counts (9245,10735,4585,7805,9180), HALF slack -75. It is the analogous construction with one extra y-chain vertex and thirteen z vertices.

## An infinite family, with a counting proof

Let P_t be the same construction as the 16-element certificate, with t backend vertices z1,...,zt. Thus |P_t|=t+6. All t>=10 refute HALF with all three strict hypotheses.

Write E=e(P_t), A_x=#(a<x), A_y=#(a<y), B_x=#(b<x), B_y=#(b<y), X_y=#(x<y). Exact formulas are

E   = (t^3+15t^2+64t+66)/2,
A_x = (t^3+15t^2+68t+69)/3,
A_y = (t^3+11t^2+40t+38)/2,
B_x = (t+1)(t^2+14t+54)/6,
B_y = (t+1)(t^2+6t+10)/2,
X_y = (t+2)(t+3)(t+4)/2.

These are derived by the following exact prefix partition; they are not polynomial fits.

Before x occurs, no z_i or v2 can occur. The prefix therefore consists of k members of the initial chain (a,b), and l members of the initial chain (y,v1), with 0<=k,l<=2 and l=2 requiring k>=1. The legal prefix counts H(k,l) are

(k,l): (0,0) (0,1) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)
H:         1     1     1     2     2     1     3     5.

After x, for k>=1 the remaining two chains have no cross relation, giving

C(k,l)=binom(t+5-k-l,3-l).

For k=0, the remaining condition a<v1 gives

C(0,0)=binom(t+5,3)-binom(t+3,1),
C(0,1)=binom(t+3,2).

The subtraction in C(0,0) removes precisely the interleavings beginning y,v1 before a. For C(0,1), y has already occurred, so a must be the first remaining element.

Consequently

E   = sum H(k,l) C(k,l),
A_x = sum over k>=1 of H(k,l) C(k,l),
B_x = sum over k=2 of H(k,l) C(k,l),
X_y = sum over l=0 of H(k,l) C(k,l).

For completeness the other two numerators are

A_y = binom(t+4,3)+C(1,0)+C(1,1)+C(1,2)+C(2,0)+2C(2,1)+3C(2,2),
B_y = 2 binom(t+3,3)+C(2,0)+C(2,1)+C(2,2).

The coefficients in these last formulas count the corresponding a<y or b<y orders within each short prefix. When both endpoints remain after x, imposing a<y makes the first remaining element a; imposing b<y makes the first two a,b. This establishes all six formulas by direct counting.

Their relevant differences simplify to

3A_x-2E = 4t+3,
3A_y-2E = (t^3+3t^2-8t-18)/2,
3X_y-2E = (t^3-3t^2-50t-60)/2,
2B_x-A_x = -5,
3B_x-E = 2(t-3).

Put t=10+u with u>=0. The last two strict-majority cubic numerators become respectively

u^3+33u^2+352u+1202,
u^3+27u^2+190u+140,

so all three hypotheses hold for every integer t>=10. At the same time HALF fails by exactly 5/E, while P(b<x)>1/3. As t grows, P(a<x) tends to 2/3 from above and P(b<x) tends to 1/3 from above, with HALF violated for every t. No uniform positive balance margin is obtained.

`prove_prefix_families.py` checks these algebraic identities and compares them with an independent full-poset three-chain DP for t=1,...,100. It also proves the analogous n=t+7 family used by the initial n=20 certificate: HALF numerator -5(t+2), lower-bound numerator (t-7)(t+2), and all strict premises for t>=13.

## Search scope and reproduction

`search_half.cpp` constructs real width-three posets covered by three chains, with a<b beginning the third chain. Cross-chain edges are allowed throughout, including non-neutral descendants of b. Every accepted model is checked by transitive closure for exact minima and exact avoidance set. All extension and event counts are unsigned 128-bit integers; n<=60 ensures the width-three extension count is at most 3^60, safely below the integer limit. Floating point is used only to choose search moves; all hypothesis and counterexample decisions use exact integers.

Seed 104202610 found the first certificate after 168613 valid evaluations, including 1054 full-hypothesis evaluations (repetitions allowed). It stopped at zero-based restart 212, proposal 800. This is a heuristic search, not an exhaustive size theorem.

A separate complete scan of the expressly parameterized family P(r,g,h,t), with 2<=r<=12, 1<=g<=h<r, and 1<=t<=40, made 11440 evaluations and found 1086 full-hypothesis HALF counterexamples. It found no L violation in that restricted family. Here the chains are Y_0<...<Y_(r-1), {x}, a<b<z1<...<zt, with extra relations a<Y_g, x<Y_h, x<z1. The minimum n in this finite parameter box was 16. No minimum over all posets is asserted.

Reproduce locally:

- g++ -O3 -std=c++17 search_half.cpp -o search_half
- ./search_half 104202610 300 1000 (exit status 2 indicates the found counterexample)
- python verify_counterexample.py
- python verify_counterexample.py SMALLER_COUNTEREXAMPLE.json verified_smaller_counterexample.json
- python structural_family.py
- python prove_prefix_families.py

All scripts write local artifacts only. The earlier 177 supporting samples in `../mc3_search/stronger_summary.json` remain a historical bounded-search result; the explicit counterexample supersedes their conjectural support.
