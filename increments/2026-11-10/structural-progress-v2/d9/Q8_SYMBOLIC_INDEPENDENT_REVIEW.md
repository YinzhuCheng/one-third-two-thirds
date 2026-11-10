CURRENT UPDATE: this audits the historical finite-symbolic proof. Its two rows have since been reclassified using Q8_COMPLETE_ANALYTIC_PROOF.md and Q8_COMPLETE_ANALYTIC_INDEPENDENT_REVIEW.md; the old1512/81 positivity checks are no longer proof dependencies. The explicit nine-term positive identity and structural/integer case splits remain, so this is not coefficient-free or case-free.

# Independent audit: Q8 source bank, finite symbolic certificate

2026-11-10. PASS as an exact finite symbolic certificate, not as a purely hand-analytic replacement.

## Contract and actual law

The original marked ideal is Q8=(0,0,1,1,7,7,7,23), with physical labels a,b,u,v,t1,t2,t3,z. All original exterior labels are above v. The fixed bank is

    15 Pr(u<b)+3 Pr(v<u)+2 Pr(t2<t1)+2 Pr(t3<t2)+Pr(z<t3) > 23/3.

Each conditioning step fixes only an original exterior word, leaving all legal z insertions in the marked-ideal count. It does not condition on a projected exterior word that already includes z. Thus the negative finer-fibre example in Q8_PROJECTED_WORD_CONTROL remains compatible with this proof.

The actual D9 caps have h_t1,h_z<=6 and h_t2,h_t3<=5, with h_t1<=h_z. Root caps B,U are at most every tail cap. The certificate proves the remaining tail statement on the larger domain in which all four caps are <=6. Each possible weak deadline order has a tie breaking with t1 before z, so the twelve chambers cover the complete domain, including boundaries. The physical tail events and source coefficients never change between chambers; chambers only change the polynomial formula used to count the same events.

## Independent polynomial construction

Q8_SYMBOLIC_INDEPENDENT_REVIEW.py does not call the author's flag recursion. For each fixed tail word, it takes suffix minima of the word's upper flags c_i and uses the flagged-chain determinant

    det[ binom(c_i+1, j-i+1) ]_(i,j=1..n),

with entries 1 for binomial order zero and 0 for negative order. This standard lattice-path count enumerates weakly increasing gaps bounded by those flags. It is valid after suffix minima since gap order is weakly increasing.

The twelve tail words satisfy t1<z. The independent computation constructs G by inserting the deadline-zero v in all five positions of each tail word, applying the determinant directly to all sixty five-letter words, rather than using the author's suffix formula. Scores remain 2[t2<t1]+2[t3<t2]+[z<t3]. The reduced source margin is reconstructed as

    11F_0-24G+15W_0+9W_G
       +sum_(j=1..min cap)(9W_j-42F_j).

In each chamber the resulting degree-five polynomial agrees identically with the author's polynomial over the rationals.

## Independent Bernstein verification

For each reconstructed gap polynomial p(t,p,q,r), substitute the four variables as six times four barycentric coordinates and homogenize each monomial to degree five using the sum of all five coordinates (the fifth is slack). Dividing each degree-five monomial coefficient by its multinomial coefficient gives the Bernstein coefficients. This is independent of the author's falling-factorial basis transform.

There are 126 coefficients per chamber and 1,512 in total. All are strictly positive: minimum 363/10 in chamber (t1,t2,t3,z), and minimum 132 in each other chamber. The independent replay also compares every coefficient with the saved author certificate, accounting for the different slack-coordinate ordering. Since the Bernstein basis is nonnegative and sums to one on the simplex, positivity proves the required reduced margin throughout the simplex. The 1,512 rational sign checks are a genuine finite proof dependency and must not be relabeled as a purely analytic inequality proof.

As corroboration only, an independent actual-Q8-plus-chain event-count DP checks all 1,372 integer tail-cap configurations in the enlarged domain (all four caps <=6, h_t1<=h_z), using B=0,U=min cap. Its full original counts agree with the reconstructed polynomials. The diagnostic integer minimum is 132 at all-zero tail caps. This integer enumeration is not required for the Bernstein proof and does not prove a sharper real minimum.

## Generic FD/RC audit

FLAG_TRANSLATION_ROOT_COMPRESSION.md FD1/FD2 and RC1/RC2/RC3 are valid under their stated contract. In FD1, swapping the initial bar with a marked star and restoring each color's fixed order moves every affected named star weakly earlier; upper-gap constraints therefore remain legal. The marked-bar inverse is unique. Summing this injection over fixed internal H words gives the stated depletion ratio. The falling-factorial sum gives FD2, including zero-count cases. Surplus final bars do not change counts.

For RC1, its gap-zero coefficients follow from root multiplicities (N,A,D)=(5,2,4)F_0+(3,1,0)G; tail-score multiplicities are 5W_0+3W_G. Direct subtraction at B=k gives exactly the two increments in RC2. Applying FD2 to the possibly negative (mu-rho) tail term gives C3; C1 makes the k>U increment nonnegative; C2 makes each B=0 increment in U nonpositive. Hence the full cone is sufficient as written. A lower-envelope W may be used only when it is independent of B,U, is a valid lower bound for the physical score, and obeys the stated 0<=W<=sF bounds. No monotonicity of the true bank is inferred from mere monotonicity of a lower envelope.

The Q8 source application has n=4,M=6,(lambda,mu,rho)=(45,9,23), score cap s=4, and C(k)=(169k+111)/5>0. Thus the root compression is fully analytic even in the enlarged all-six domain. The simpler six-bank and the old three-tail applications also have the displayed C(k) values and satisfy C1-C3. FD/RC alone does not pay a terminal bank or add any ledger coverage.

## Coverage classification

Together, analytic root compression and this finite symbolic certificate pay the original source bank on the two remaining first-head references of this Q8 shape, interchanging the unsupported physical leaves as necessary before fixing their names. Record these as two finite-symbolic replacements, separate from the 400 purely analytic replacements. Do not merge the two counts into a claim of 402 purely analytic rows, and do not infer additional source coverage without checking its actual ideal and exhaustion contract. The standalone simpler 6/1/1/1/1 tail-payment target remains open in its separate note.

## Actual cap-seven stopping control (degree eleven)

Independently reconstruct Q8 plus a seven-label exterior chain with original upper gaps (a,b,u,v,t1,t2,t3,z)=(0,0,7,0,7,7,7,7). A forward subset DP accumulating all five physical event indicators gives

    N=54252;
    (K_A,K_B,K_C,K_D,K_E)=(13860,32472,18084,27126,18084);
    3(15K_A+3K_B+2K_C+2K_D+K_E)-23N=-6336.

The complete incomparable-degree list is (1,3,9,6,10,11,11,10,5,5,5,5,5,5,5), so this is an actual degree-eleven example, not degree ten. Independently, in the symmetric equal-cap tail model F_0=12 binom(11,4)=3960, G=12 sum_(k=0..4)binom(7+k,k)=5940, and sum_(j=1..7)F_j=12 binom(11,5)=5544. The tail score average is 2, also after adding the independent gap-zero v, so the closed root formula gives the same -6336 margin and the same N,K_A,K_B.

The original source root-compression cone still holds at M=7: C(k)=(169k+97)/5>0 and the other conditions are unchanged. Thus this failure belongs to the reduced tail-payment bound, not to either root-axis reduction. It prevents replacing the uniform cap-six certificate by cap seven for the same fixed source bank. B is already balanced (32472/54252 lies between 1/3 and 2/3), C and E each have probability exactly 1/3, and D is fair. No NB or general balance counterexample is asserted. See Q8_CAP7_INDEPENDENT_CONTROL.py/.json.

The author's final Q8_SOURCE_BERNSTEIN_CERTIFICATE.md was also checked: its original-P contract, the two reference words, and flagged recurrence (2) agree with this independent reconstruction. Its finite-symbolic classification and the retained negative finer-fibre example are accurate.
