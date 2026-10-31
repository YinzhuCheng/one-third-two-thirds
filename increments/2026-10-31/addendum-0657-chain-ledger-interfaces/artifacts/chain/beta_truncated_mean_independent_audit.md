# Independent probability lemma: beta truncated means

## Statement and verdict

Let q≥0 and l,m>0 be real numbers. Let X have Beta(q+1,l) law and Y have Beta(1,m) law. Then

E[min(X,t)] ≥ E[min(Y,t)] for every real t

**if and only if** l≤m(q+1).

This is an independent probability statement. No poset construction or conditional distribution claim is assumed or verified here. For intended chain-count applications, explicitly state q is a nonnegative integer and l,m are positive integers; the analytic result itself holds for the larger real parameter domain above.

## Proof

For 0≤t≤1 write
A(t)=E[min(X,t)]−E[min(Y,t)]
    =∫_0^t (S_X(u)−S_Y(u))du,
where S denotes survival probability. Thus A(0)=0 and
A(1)=E[X]−E[Y]=(q+1)/(q+1+l)−1/(m+1).
Necessity of the proposed condition follows immediately at t=1. Values t≤0 give equality; for t≥1 the difference equals A(1).

On (0,1), the positive density ratio is
r(x)=f_X(x)/f_Y(x)=C x^q(1−x)^(l−m),
where C>0 is the normalization constant.

### Case l≤m

The logarithmic derivative is q/x+(m−l)/(1−x)≥0. Unless q=0 and l=m, the ratio is strictly increasing. Since both densities integrate to 1, their difference has one crossing from negative to positive. Hence S_X≥S_Y throughout, and A(t)≥0. If q=0,l=m the laws coincide. This case automatically satisfies the required mean condition.

### Case l>m

The mean condition implies q>0. Now r(0+)=r(1−)=0 and
(log r)'=q/x−(l−m)/(1−x)
changes sign exactly once. Thus r is strictly unimodal. Its maximum exceeds 1, since otherwise f_X≤f_Y everywhere and strict inequality on an interval would contradict normalization. There are exactly two roots a<b of r=1. Consequently h=f_X−f_Y has signs −,+,− on the successive intervals.

Let g=S_X−S_Y. We have g'=-h. Therefore g is positive on (0,a], strictly decreasing on [a,b], and g(b)=∫_b^1 h(u)du<0. It has exactly one zero c∈(a,b), is positive on (0,c), and negative on (c,1). (On (b,1), it increases to its endpoint value 0 from below.)

It follows that A increases up to c and then decreases to A(1). Thus its minimum on [0,1] is min(A(0),A(1))=0 under the mean condition. This proves sufficiency.

Except when the two laws coincide, A(t)>0 for every 0<t<1. At t≥1 it is zero exactly when the means agree.

## Why q≥0 must be stated

Merely requiring the beta parameters to be positive is insufficient. Take q=−1/2,l=1/2,m=1. Then l=m(q+1), but X is Beta(1/2,1/2) and Y is uniform. At t=1/2,

E[min(X,1/2)]=1/2−1/(2π)<3/8=E[min(Y,1/2)].

Thus the claimed all-t inequality fails for allowed negative q, even at equal means. Degenerate zero-length chains (l=0 or m=0) also require a separately stated limiting convention; they are not beta laws with positive shape parameters.

## Scope warning

The proof establishes only this probability comparison. A poset application must independently justify the specific beta distributions, their independence if used, the conditioning measure and its weighting, and how this truncated-mean comparison enters the proposed combinatorial count.
