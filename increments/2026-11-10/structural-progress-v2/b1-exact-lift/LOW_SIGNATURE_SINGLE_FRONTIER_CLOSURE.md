# SG1: low-signature single-frontier degree gates

2026-11-10 UTC. Analytic author candidate, independent review requested. Exact original B1 lift, actual full Delta10 and0<=m<=k<=7, no OLD moment. Use original K,N,X,Y,e(C).

## Two coupled gates
Let c be a C-minimum above x, and f a distinct C-minimum missing x with support<=1. Either of the following suffices for strict original fixed-u/b balance:

A. degC(c)<=8 (degC(f)<=8 is automatic):

    3K-N >=(4/3)e(C)+2X+Y>0.

B. degC(c)<=9 and f has empty signature (thus degC(f)<=7):

    3K-N >=(4/5)e(C)+2X+Y>0.

The original universal upper cap is5/9. Since f belongs to Mx-E, its existence implies m<=k-1<=6. The separate m0 bound F>=48 pays both margins. No claim of full B1 or net-new population.

## Genuine shared-gamma representation
Delete c,f, fixing an actual gamma but not their relative order. Original degrees give actual deadlines R<=degC(c)-1, S<=degC(f)-1. Thus casesA/B have rectangles(R<=7,S<=7)/(R<=8,S<=6). Both selected orders share these actual R,S.

Use the exact original-word sums from CT1:

    W(R,S)=(R+1)(S+1)+min(R,S)+1,
    T(R,S)=sum_(a=0)^S sum_(b=a)^R Psi(a,b)
            +sum_(a=0)^R (S-a+1)_+G(a).

The first term is f-first; the second is c-first. Equal gaps count two genuine words. Since m<=6,k<=7, use worst cap m6,k7:

    G(0..7)=(48,46,36,18,-8,-42,-84,-126), G(a>=7)=-126,
    h*=min(7,b+1), q*=min(6,a),
    Psi(a,b)=48 if a0; otherwise48+(6-8q*)h*+4q*(q*-1).

The original h/q bounds and two-order multiplicities are exactly CT1's; f outside E stops q and contributes one missing-x token before c. Increasing actual h then q lowers the relaxed kernel for q>=1; at q0 the actual kernel is>=48. Hence total original kernel in this genuine gamma fiber is>=T. No union-FKG or equal order weighting is used.

## Analytic deadline inequalities
Let P_s(h)=sum_(a=0)^s Psi_a(h), where Psi_0=48 and positive a uses q*=min(6,a). Then

    P_s(7), s0..7 =48,82,68,14,-72,-182,-308,-434.

For s<=3, P_s(h)>0 for1<=h<=7. At h6, the values at s4,5 are-16,-92. For n>=1,

    T(n,S)-T(n-1,S)=P_min(S,n)(min(7,n+1))+(S-n+1)_+G(n).

If S<=3 all these increments are positive. If S>=4, n1..4 give92+46S,80+36S,68+18S,64-8S, all positive for S<=7. At n5 the increment is-16 for S4, otherwise76-42S<0. At n6 it is a negative P_S(7) when n>S, otherwise112-84S<0. At n7 it is negative P_S(7) when n>S, or-560 for S7. At n8 (needed only inB, where S<=6) it is negative P_S(7). Thus T first increases and then decreases in R. Its minimum is always at R0 or the relevant maximum7/8.

The R0 endpoint is48(S+2)>=96.

For caseA, U(S)=T(7,S). Its S-increments, evaluated from

    U(s)-U(s-1)=sum_(b=s)^7 Psi(s,b)+sum_(a=0)^s G(a),

are362,146,-14,-126,-198,-238,-238. They are nonincreasing, so U is discretely concave. Its endpoints are U0=432,U7=126. Therefore T>=96. Since W<=72, the original gamma-fiber mean F is>=96/72=4/3.

For caseB, V(S)=T(8,S), S0..6. Its increments are396,132,-68,-212,-308,-364, again nonincreasing by the same displayed polynomial-sum formula with upper8. Its endpoints are V0=480,V6=56. Therefore T>=56, while W<=70, giving mean F>=56/70=4/5.

These short exact polynomial sums and sign arguments are analytic, not a computed positivity-table dependency or an original-poset scan. Multiply each actual gamma mean by its actual fiber size and sum. The exact identity3K-N=sum F+2X+Y proves both gates.

## Ordinary consequence with root-cover closure
If the unique x-containing C-minimum c has signature{x}, its original C-degree<=8. If there is a missing-x support<=1 C-minimum f, caseA applies. If not, every Mx-minimum has signature yz, so all Mx signatures are yz and RC1 (ROOT_COVER_IDEAL_BANK_CLOSURE.md) supplies ordinary existence. Thus, conditional on the separately reviewed RC1 theorem, the entire unique-signature{x} frontier branch is ordinary-balanced without OLD moment. This does not certify fixed u/b in the RC1-only alternative.

If c has signature xy or xz, its C-degree<=9, so caseB pays whenever an empty-signature C-minimum exists. More generally B uses only the actual displayed degrees, not a forced c signature.

## Nonvacuity and deduplication
Take E a yz six-chain, and c,f C-parallel singletons with c signature{x},f empty. Then k7,m6, cC-degree7,fC-degree7, actual full Delta10. This realizesA; y,z are old twins. Replacing c's signature byxy realizesB; the original y,z exclusive upper sets are singleton/empty, so old VG pays. These illustrate only true-degree feasibility, not new population or an object escaping all guards.

All degree and gap constraints are original, and no moment is assumed on any deleted or conditioned object. 
