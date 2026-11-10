# DG2 fresh independent mathematical review

2026-11-10 UTC. **PASS for the stated DG2 theorem.** This reviewer did not participate in deriving DG2. This is a non-blind internal independent mathematical review, not external peer review, formal verification, or an originality certificate.

Reviewed source: `TWO_LOW_MINIMUM_DOUBLE_GAP_CLOSURE.md`, SHA256 `7a3c20fa38415d9ef87b09a0d129c2a7a4fe001854b08db94bd06bb73ea30382`.

## Conclusion first

Under the complete original exact-lift contract and actual full Delta10, two distinct actual C-minima missing x and of old T-support at most1, with at least one empty, imply

    3K_ub-N >=3e(C)>0.

This is payment for the same original physical pair (u,b) in every word. With its inherited upper bound5/9, that pair is strictly balanced. The manuscript correctly permits arbitrary additional minima, actual tail structure, and actual word multiplicities. It does not require OLD moment or zero x-frontier outside the specified two minima.

No hard gap was found. In particular the rectangle reduction is valid, but its split at the diagonal is important: blindly claiming global concavity across disappearance of a negative diagonal duplicate would not be valid. The source does not make that mistake.

The final assembly claiming ordinary payment for every exact-D10 lift is outside this review's assigned scope. DG2 supplies its stated component; the already proved residual classification and UL1 must still be checked independently for that composition. No statement about arbitrary degree-ten posets, all B1, or arbitrary T4 follows from DG2 alone.

## 1. Original contract and true deletion fibers

I checked the source against the original correlated-kernel contract and the full-prefix F formula retained in WB5/WB6. In P+, f has three incomparable old roots outside C, hence C-degree<=7. A singleton-y/z g has two, hence C-degree<=8; an empty g has the stronger C-degree<=7. Both lie outside E and are original C-minima, so they are mutually incomparable and incomparable with every E label. Deleting the other selected minimum removes one actual incomparable label at each endpoint. Thus their actual retained-word deadlines are bounded by6 and7.

These are bounds from the complete original order, not degree claims inherited by a new poset. Each selected minimum can be inserted in all retained gaps up to its first original successor. Its own deadline is unaffected by inserting the other incomparable minimum. Therefore the fiber really is the Cartesian gap rectangle, with two orders exactly on the diagonal and one order elsewhere. Its exact cardinality is

    W=(A+1)(B+1)+min(A,B)+1<=63.

When the retained word starts in E, both deadlines are at least1. When q0, no reinsertion of the two non-E labels can create a positive initial E run, so every true F is at least48. This includes the empty retained word and avoids an implicit first-letter assumption there.

## 2. Direction of both scalar lower bounds and exact prefix extras

Since both selected labels miss x, H=h+1_(a<=h)+1_(b<=h). The original E-run is Q=min(q,a,b), and q<=h. Raising Q to min(h,a,b) changes the original base by successive increments8(Q-H)<=0. The exact prefix terms are not changed by this scalar relaxation.

For empty g, replacing its prefix role by singleton-y can only shorten the initial missing-y run, leaving H,Q unchanged. Every Y/Z-dependent term of F, including the exact pair-gap counts, is increasing in these runs. Thus the singleton model is indeed a pointwise lower bound, not a hypothetical replacement-order theorem.

I recomputed the first-gap extras directly. At the two zero-gap orders the root runs are respectively (H,1,2) and (H,0,2), with H=h+2, giving36+3H and20+2H. On the empty-first axis they are (H,1,1), giving24+2H; on the singleton-first axis they are (H,0,1), giving10+H. Elsewhere the word starts in E and all prefix extras vanish. These agree with every entry in the source and count the two diagonal orders once each.

## 3. Independent verification of the rectangle-minimum reduction

For fixed retained h and fixed second deadline B, inspect the increment when a new positive a-row is added.

- While a<=min(B,h), each ordinary cell either keeps its minimum-gap parameter or increases it, and the base kernel decreases by8(j-H)<0. The diagonal duplicate also decreases. The b0 extra is constant in this interval. Thus row increments are nonincreasing, and the deadline sum is discretely concave.
- If B<h and a>B but a<=h, all cells have fixed minimum parameter b, there is no diagonal duplicate, and the b0 extra remains constant. The new rows are identical, so this segment is linear. Splitting here is essential even when the discarded diagonal base is negative.
- If a>h while B<h, the H-regime is fixed for every cell and there are still no diagonal duplicates; these rows are again identical. The endpoint at a=h is a valid endpoint for the linear total from h onward.

The corresponding column argument has the same monotonicity despite the asymmetric axis extras: that extra is constant within its relevant <=h regime. Applying these arguments reduces any possible global minimum to a thin edge, a diagonal t<=h, or the block A,B>=h. The deadline maxima6 and7 are both greater than h<=5, so no endpoint used by the reduction is outside its declared scalar domain. This proves the reduction for every actual deadline pair without changing its fiber mass.

## 4. Independent sums and positivity

On a thin edge, min(a,b)<=1, H<=7, so each base is at least34; every extra is nonnegative and W>=6. Thus the sum is at least204.

On the small diagonal A=B=t<=h, the minimum gap j has exactly2(t-j+1) true words. I independently summed these bases and the two axis extras, recovering

    D(t,h)=[-8ht^3-6ht^2+47ht+51h
              +2t^4-12t^3+130t^2+624t+558]/3.

At t1 and t2 this is28h+434 and19h+754. At3<=t<=5 its h coefficient is negative; setting h5 produces the stated quartic. Its second derivative8t^2-104t+200/3 is negative on[3,5], and its endpoint values1016,786 give the source's lower bound. The small diagonal is therefore uniformly above204.

For A,B>=h, independently separating the inner corner, its two exterior strips, their rectangular intersection, and their extra diagonal gives

    B00=2(h+1)(h+2)(30-h^2),
    S=-2(h+1)(4h^2-h-81)/3,
    C=48+2h-4h^2,
    P=-2h^4-6h^3+59h^2+225h+186,

and exactly the source's formula

    P+d(S+h+11)+e(S+2h+26)+(de+min(d,e))C.

For h<=3 all extra coefficients are positive and B00>=252. At h4, the coordinate-increment lower bounds53 and80 are correct, so the minimum is1134. At h5 both increments are negative; the endpoint d1,e2 gives580. All cases exceed204.

Small symbolic expansions were used to check the independently derived closed sums and endpoint values. They did not enumerate original posets or supply a finite positivity-certificate dependency; the written algebra, monotonicity, and concavity arguments are sufficient on their own.

## 5. Original law and accepted scope

Every q>=1 true gamma fiber has original F-total at least204, and its actual cardinality is at most63, hence this total is at least3W. Every q0 fiber has original F>=48 per word. The deletion fibers partition LE(C), so summing yields3K_ub-N>=3e(C) exactly as stated. There is no equal weighting of gamma fibers, no swapped physical pair, and no conditional OLD moment or arbitrary tail completion mass.


