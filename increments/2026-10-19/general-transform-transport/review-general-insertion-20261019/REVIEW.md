# General chain interlacing and insertion transport: independent review

Date: 2026-10-19. Final verdict: both manuscripts PASS analytic independent review. The complete written versions, including their final correction and cross-reference, have been checked. No claim of formal verification or novelty review is made.

## Scope and accepted dependencies

Review the new material in `../general-chain-interlacing-20261019/RESULT.md` and `../insertion-transport-criteria-20261019/RESULT.md`, with the frozen actual controls in `../general-interlacing-tests-20261019`. Read the complete `../slot-theorem-consequences-20261019/RESULT.md` and `../window-polynomial-variation-20261018/RESULT.md` first. Those accepted results are not re-reviewed. The explicit Shepp difference-coordinate sublattice proof in `../principal-filter-slot-bound-20261018/RESULT.md` §2 has also been read.

The audit distinguishes uniform actual linear extensions, their generally tilted deletion images, auxiliary outside-word laws, conditional combinatorial fibers, sufficient coefficient cones, and general theorems. No arbitrary coefficient data are treated as a realizable finite poset. No original global conjecture is enlarged.

## A. Uniform insertion/deletion normalization

Let a fixed outside linear extension have a window of K incomparable elements between the last D element and the first U element, using endpoint conventions if a side is empty. Its actual central-chain fiber has cardinality binom(m+K,K). Write L=m+K+1.

Inserting one new chain point in an arbitrary central gap defines a multigraph: each old LE has L insertion edges, each new LE has m+1 deletion edges, obtained by deleting any one of its chain ranks and relabeling the others. Thus the uniform-new/random-rank-deletion image has density L/E_m L relative to uniform old LEs. The reverse uniform construction first tilts the old law by L and then chooses one of its L insertion edges uniformly. Starting from a uniform old LE without this tilt is generally wrong.

Deleting a fixed new chain rank j instead has density (H_j+1)e(P_m)/e(P_{m+1}), where H_j counts old window elements in its corresponding chain gap. This generally tilts even within one fixed outside-word fiber. Summing H_j+1 over j gives L. The smallest control, one incomparable point x and an old one-point chain, sends deletion of the new top point to probabilities 2/3,1/3 on the old two LEs rather than 1/2,1/2.

The outside-word marginal itself tilts by binom(m+K,K), and its adjacent-length density ratio is (m+K+1)/(m+1+E_m K). All denominators and multiplicities agree.

## B. Exact transport differences and strict budget

For x, let J be the number of old chain points before x, and R its outside window rank, with R=0 on the left and R=K+1 on the right. Insertion before x has exactly J+R legal edges. For 1<=i<=m, put A_i={J>=i},

B_i=E[(i-1+R)1_{J=i-1}],
C_i=E[(L-i-R)1_{J=i}],
V_i=Cov(K,1_{A_i}).

Then the independently derived identities are

Q_i(m+1)-Q_i(m)=(V_i+B_i)/E L,
Q_i(m)-Q_{i+1}(m+1)=(C_i-V_i)/E L.

Consequently weak interlacing is equivalent to -B_i<=V_i<=C_i, and strict interlacing requires both strict inequalities. The central shuffle atoms give

(m+1-i)B_i=i C_i.

The exact deletion barycenter identity also agrees:

Q_i(m)+V_i/E L = [(m+1-i)Q_i(m+1)+i Q_{i+1}(m+1)]/(m+1).

When x is actually incomparable to the chain, there is an outside word putting x inside the window. Its shuffle atoms have positive probability at every J=0,...,m. Hence every B_i and C_i is strictly positive. Comparable-target or degenerate-event cases must not inherit this positivity statement.

The top-insertion formula is independently consistent: S=1+#(I after c_m and before the first U), E S=e(P_{m+1})/e(P_m)=E L/(m+1), and

Q_i(m+1)-Q_i(m)=Cov(1_{A_i},S)/E S,
(m+1)Cov(1_{A_i},S)=V_i+B_i.

## C. General strict interlacing: final analytic PASS

A shorter route than the top-insertion average is to insert immediately after the old c_i, relabeling later chain points. Each new LE deletes its c_{i+1} uniquely. The legal-slot count is S_i=1+#(I between c_i and its next chain point), using the first U point or the right boundary at i=m. Let W_i be the corresponding continuous coordinate gap. On every order-polytope LE simplex, its conditional mean is S_i/(N+1). Thus

Cov_LE(1{c_i<x},S_i)=(N+1)Cov_poly(1{t_ci<t_x},W_i).

Anchor the Shepp coordinates at z=c_i: t=-t_z and d_v=t_v-t_z. The comparison event and W_i=d_{c_{i+1}} are increasing functions; at the top W_i=min_U d_u, or 1+t when U is empty. The transformed order-polytope domain is a coordinate min/max sublattice, as in the accepted proof. FKG proves the weak left inequality. Inserting before c_i uses a decreasing preceding gap and yields the weak right inequality, equivalently obtained by whole-poset duality.

The complete written strictness argument has been checked, including each of its load-bearing steps. Fixed-t slices remain sublattices. For two fixed values t_1<t_2, the union of those two slices remains a sublattice. FKG with the increasing indicator of the upper slice proves that the conditional expectations f(t)=P(t_x>t_z|t_z=-t) and g(t)=E(W_i|t_z=-t) are nondecreasing. This supplies a self-contained monotone-regression proof rather than merely citing MTP2.

For x incomparable to z, the LE simplex slices have weights proportional to s^(k-1)(1-s)^(N-k)/[(k-1)!(N-k)!], where s=t_z and k is its LE rank. Its minimum possible rank is |Pred z|+1, and all those LEs put x after z. The event x<z has strictly larger minimum rank. The dual maximum-rank statement holds at s approaching 1. Therefore f(-1+)=0 and f(0-)=1. The gap has positive conditional expectation at every interior slice, while 0<W_i<=1-s gives g(-1+)=0. Sectional volume formulas imply interior continuity; t has positive density throughout (-1,0). Hence f,g are nonconstant nondecreasing functions with strictly positive covariance. Fixed-slice FKG makes the remaining conditional covariance nonnegative. The resulting total covariance is strictly positive.

The complete manuscript has now been checked, including all empty-side and endpoint cases, finite-LE to continuous normalization, repeated interlacing at arbitrary shorter lengths, dual chain indexing, and the exact scope of its same-side conclusions. Neither nonconstant functions alone nor nonnegative FKG alone would justify strictness without the conditional-regression argument; the manuscript supplies the missing argument explicitly.

## D. Finite simultaneous coefficient certificate

Set a=i-1,b=m-i, so m=a+b+1. For an outside window of size K and target rank r, the actual event count is

S_{K,r}(a,b)=sum_{h=0}^{r-1} binom(a+h,h) binom(b+K-h,K-h).

Here h is the number of outside window points before c_i. The left-window convention r=0 gives an empty sum. The right-window convention r=K+1 gives the entire fiber by Vandermonde. The shifts in the proposed polynomial cross-products F=A(a,b+1)T_{a+b+1}-A(a,b)T_{a+b+2} and G=A(a,b)T_{a+b+2}-A(a+1,b)T_{a+b+1} are correct. The final bound degree at most 2t-1 is correct: rewriting each determinant as one first difference times an undifferenced factor removes at least one total degree. Nonnegative ordinary monomial coefficients or nonnegative coefficients in binom(a,p)binom(b,q) give a sufficient nonnegativity cone on integer a,b>=0; a positive constant coefficient ensures strict positivity including both coordinate axes. No universal cone-membership assertion has been proved or used.

## E. Same-side sufficient bound

For a fixed outside word and an internal atom J=j, 1<=j<m, x in window rank r forces the (j+r)-th central shuffle symbol to be an outside point. Therefore

P(J=j | outside word)<=K/(m+K)<=t/(m+t).

An outside-window target gives J=0 or m and contributes no internal atom. Mixing with the actual, tilted outside-word distribution preserves this bound. At m>=2t every adjacent column drop is <=1/3. A decreasing column strictly avoiding the closed [1/3,2/3] band cannot cross sides, since that requires an adjacent drop strictly greater than 1/3. Weak interlacing already transports an old strictly safe same-side column to every shorter chain length. The size threshold is sufficient, not asserted necessary; t=0 is vacuous and one-point columns are automatically same-side. This gives no control of wholly outside pairs or existence of a globally safe shorter length.

## F. One independent actual control, actually executed

The reviewer wrote and ran `independent_transport_check.py`. It directly enumerates LEs of one fixed actual t=3 family: d<y<z<u plus isolated x, D={d}, U={u}, I={x,y,z}, with the autonomous chain inserted between d and u. For m=1,2,3 and their successor lengths the LE totals are 18,42,80,135.

For every old LE it checks all random-rank-deletion multiplicities L, fixed-top-deletion multiplicities S, and binomial fibers. For all three targets and each old rank, 18 exact Fraction records check both transport differences, the B/C relation, the barycenter identity, the top/random insertion consistency, and positivity of B,C. All checks PASS. This is a fixed implementation/normalization control, not a search or proof of a universal statement. Saved exact records: `independent_transport_check.json`.

## G. Independent exact crossed-column counter-control

The reviewer independently enumerated every actual LE of C_1 disjoint union C_5 and C_2 disjoint union C_5, with x the middle point of C_5. The totals are respectively 6 and 21. The chain-before-x numerators are [3] and [15,6]; the m=2 atom counts of J=0,1,2 are [6,9,6]. Thus the old column is exactly (5/7,2/7), strictly outside the closed band on opposite sides, while the shortened column is 1/2. The new manuscript correctly identifies this as a counterexample only to unconditional shortening of arbitrary band-avoiding columns. It is not a globally unbalanced poset or a counterexample to strict interlacing or the original conjecture. Exact words and counts are saved in `independent_crossed_column.json`. No search was performed.

## H. Remaining transport manuscript: final analytic PASS

Read the full written transport manuscript, including all sections not covered by the early formula exchanges.

The pairwise-tail covariance identity, indicator conditional-mean identity, and exact TV cost eta/E L are correct. The common absolute budget eta bounds every event covariance; taking the finite positive minimum of B_i,C_i gives a sufficient all-target/all-rank certificate. It is not a necessary condition, and its universal success is neither proved nor inferred from universal interlacing.

The finite-polynomial certificate is correct on its stated integer quadrant. The ordinary monomial basis is nonnegative there; the double Newton basis is nonnegative at nonnegative integers, with no assertion about intervening reals. Its coefficients are the appropriate mixed forward differences. A positive constant coefficient gives strict positivity on both axes as well as in the interior. Multiplying by (t!)^2 clears the displayed rational coefficients. Actual input has a_t>0, because an outside word may place all D first, then I, then U; hence deg T=t for t>=1.

For the class I disjoint from D union U, the total count is kappa*h*binom(n+t,t), with h=e(I) and sum_r h_{x,r}=h. Independently deriving the single-rank atom difference gives the manuscript's common factor kappa^2*h/t, rather than an extra h or a missing h. Both factorizations (6.2)-(6.3) have the correct rank arguments, two adjacent-length shifts, and boundary terms r=1,t. After substituting alpha=d+a+1 and n-alpha=u+b, every factor is a binomial rising product with strictly positive constant factors, proving the claimed nonnegative-coefficient cone inclusion and strictly positive constants. This handles arbitrary internal I, D, U without assuming the central outside window K is constant.

The artificial common-external-weight diagnostic was checked separately from actual-poset statements. Its exact probabilities (5+6 epsilon)/(7+8 epsilon) and (7+11 epsilon)/(10+13 epsilon) give -5/4407 at epsilon=1/10. With all six external weights positive this is a legitimate weighted counter-control, but it is not the uniform LE law of that actual poset. One presentation error was found and corrected: not every fixed outside-word fiber is strictly interlacing, because outside-window targets are constant 0 or 1. The final manuscript now correctly says that each fiber is weakly interlacing, while interior-window targets supply strict margins.

The final cross-reference to the general strict-interlacing manuscript has also been checked: the precise iff implies -B_i<Cov(K,1_{A_i})<C_i for every actual input, and actual F,G are strictly positive on the integer quadrant. It does not imply that the stronger common absolute budget always succeeds, or that every actual F,G has nonnegative monomial/Newton coefficients. The final list of open conclusions preserves this distinction.

## I. Frozen actual test report: inspected evidence, not a reviewer rerun

The reviewer read `test_actual.py`, `write_certificates.py`, `verify_minimum_independently.py`, the final `RESULT.md`, run/certificate logs, summary, and the least-gap independent JSON. The grouped labeled-clone multiplicities, I-ideal transfer, actual totals, and signs of both integer cross products agree with the claimed test. No failure was reported, so no failed actual counterexample needs minimization or realization review.

The actual frozen scope is 336 outside parameter instances, 2016 adjacent-length comparisons, and 3,084,480 strict inequalities, all positive. The saved execution record distinguishes 84 tiny full-bitmask controls plus 16 additional clone-multiplicity controls, giving 100 small controls. The separate least-gap verification checks 5 exact large-chain total/event counts, giving 105 checks in the final summary; it would be inaccurate to call these 105 tiny posets. The earlier main run log has 84 controls because the extra 16 were executed by the later certificate writer and are recorded in `certificates.log`. All five least-gap counts have an explicit independent-method PASS record.

The reviewer did not rerun these 100 small controls or the large-chain certificate. The independent computations actually run by this reviewer are exactly the fixed t=3 transport control in section F and the explicit crossed-column control in section G. The general mathematical theorem rests on the complete analytic proof, not on this finite evidence.

## Final scope

Both new manuscripts pass. The load-bearing gain is general strict indexed chain-column interlacing with exact uniform insertion/deletion transport, together with appropriately qualified same-side shortening and computable sufficient transport certificates. A closed-band-avoiding column can cross sides when m<2t, as the actual two-chain control demonstrates. Wholly outside pair preservation, existence of a globally safe shorter landing point, and the original global conjecture remain outside these conclusions.
