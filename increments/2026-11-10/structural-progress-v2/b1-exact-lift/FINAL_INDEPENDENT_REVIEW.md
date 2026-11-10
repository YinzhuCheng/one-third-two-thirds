# Independent audit: correlated-hole boundary

Date: 2026-11-10 UTC. **PASS for Sections 1–6 and the scope bookkeeping in Section 7.**

Target `PROOF_CANDIDATE.md`, SHA256
`f3fef1e0a8887e57532bde636314b71c65e7cb697ebb0ff827dc3cbd7a5dbb46`.

This is a nonblind internal independent mathematical audit. This reviewer did not participate in the author's or collaborative reviewer's derivation. I reconstructed the counting and inequalities below after reading the fixed manuscript. It is not formal verification, external peer review, or originality certification. No new-object enumeration, LE DP, was performed.

Inherited input: the private-predecessor lift manuscript at SHA256 `0301a8d346f5c538d99445ebb2e95f6d0818effb816764c265ecd22418e84ed3`, with its final independent audit at `b4a0dca04b635b378d3761e26c468cd46edb825843bba1aa362495cbc71ffa34`. I read both; their structural lift and original-root insertion law are accepted dependencies, not claimed as newly proved contributions here.

## 1. Exact law, not an interface-average substitute

Delete T from an R-word. For each resulting beta in LE(C), the K=3 fiber consists of six private orders. For K=2 missing i, choose either order of the other two labels and insert i after j initial beta letters, for exactly 1<=j<=h_i. Every such insertion is legal and uniquely reversible. Thus A3=6e(C), A2=2 sum(h_x+h_y+h_z), and I=2 sum(h_y+h_z).

For the K=2 fiber missing x, the two leading labels are y,z. Its leading E run after inserting x at j is min(q,j). Because E has exact signature {y,z}, q<=h_x. Consequently

    L=2 sum_beta sum_(j=1)^h_x min(q,j)
     =2 sum_beta [q h_x-q(q-1)/2].

If q>0 the first C point is above both y,z, so h_y=h_z=0. Substituting into the accepted complete-P+ root-slot count gives exactly

    3K-N=sum_beta [48+(6-8q)h_x+9(h_y+h_z)+4q(q-1)]+2X+Y.

This reconstruction retains the true word fibers and original root multiplicities throughout. It does not transfer the C-word uniform distribution to P+ without its insertion weights.

## 2. Sharp parameter-only guarantee

For q>0 the coefficient of h_x is negative. Hence h_x<=k gives F>=Phi(k,q), and Phi(k,q+1)-Phi(k,q)=8(q-k)<=0 for q<m<=k. The q=0 kernel is at least48, while Phi(k,m)<=48. Thus Phi(k,m)>=0 suffices. When m=0, every kernel is at least48.

For necessity, take E any m-point order, C=E ordinal-sum chain_(k-m), and put every C label above y,z but not above x. In every C-word q=m,h_x=k,h_y=h_z=0; X=Y=A0=I=0. Direct substitution yields

    K/e(C)=40+12k,
    N/e(C)=72+(30+8m)k-4m(m-1),
    (3K-N)/e(C)=Phi(k,m).

This is an actual original-order construction for every integer k>=m>=1. With E antichain, x has degree k+3, y,z have new degree4, each E label has degree m+1, the new u has degree m+3, b has degree5 (including b||a), and chain labels have degree2. Therefore Delta(P+)=max(k+3,5), as claimed. The D10 table follows by integer inequalities, not enumeration. The five displayed rational controls check exactly.

The quantifier is important: Phi<0 disproves a universal guarantee from only (k,m), not payment on every object with these parameters, and not existence of another balanced pair. These sharpness controls have fair twins y,z.

## 3. The m3,k4 endpoint

At this endpoint, the only zero kernel has q=3,h_x=4. Therefore equality 3K=N forces every C-word into that state, and X=Y=0. Every C-minimum can start a C-word, so every C-minimum belongs to E. Every C point is above some C-minimum, and hence above y,z. In the lifted original order the two labels y,z have exactly lower set {a} and upper set C. They are fair twins. Non-twin objects under this contract therefore have strict lower inequality. This checks the endpoint deduction without invoking any V2 numerical data.

## 4. Chord, moment closure, quantitative ratio

Write eta=8m-6-4m(m-1)/k. For q>0,

    F=48-a(q,h_x)h_x,
    a(q,h)=8q-6-4q(q-1)/h.

a increases in h, and a(q+1,k)-a(q,k)=8(1-q/k)>=0. Thus a<=eta and F>=48-eta s, where s=h_x+h_y+h_z. For q=0 the same inequality follows directly. Also eta>=4m-2>=2.

The old seed moment is precisely sum s+A1+A0<=3e(C), giving

    3K-N>=(48-3eta)e(C)+eta(A1+A0)+2X+Y.

For m3 this leading coefficient is72/k-6, so all legal D10 lifts (k<=7) are strictly safe.

Separately, the same chord proves 4L<=(eta+6)Hx. Substituting in the exact N,K formulas and eliminating e(C) with nonnegative slack Z gives the stated coefficient arrays. For eta>=2 the Hx ratio 76/(180+3eta) is no larger than each other coordinate ratio: 64/117,46/84,49/96,43/81,40/72. This proves the advertised probability lower bound. At m3,k7 it is266/783, whose difference from1/3 is5/783. The inherited upper bound is5/9.

## 5. Audit boundary

The rho implications follow from k<=rho under the inherited nested-ideal definition. No hard gap was found in the analytic scalar classification, actual sharpness family, endpoint twin claim, or old-moment quantitative closure.

I have not independently recounted the stored V2 lift histogram, nor re-audited the collaborative review's additional V2 graph-module/guard assertions. Those are not required for the accepted general theorem; the manuscript explicitly refuses new population credit for that example. No whole B1, T4, J18, NB, or all-history coverage follows from this audit.

The extension in `MOMENT_PARAMETER_EXTENSION.md` was derived by this reviewer and is consequently **not** independently audited by this document.


Degree-list corrigendum (same day): the original draft of this review listed deg(b)=4 in the sharpness family, omitting a||b. The correct lifted degree is5. The accepted exact maximum max(k+3,5), all D10 controls and every analytic conclusion are unchanged; no author manuscript bytes were changed.
