# Independent review: three-private-head initial ordering gate

2026-11-10. **PASS**, as a corollary of the independently proved four-equal-full-downset bank. This review replaces a separate initial profile-bank dependency, not any further rows of the seven-phase ledger.

## Exact contract

P is a finite original poset whose ONLY minimal elements are a,b. Three distinct labels u,v,w have full strict downset {a}. The labels b,u,v,w each have full incomparable degree at most nine. Incomparability of b with these three labels follows already from minimality of b and their full downsets, and is also explicitly stated in the author contract. Fix the physical reference before conditioning, with b not first.

The proof is valid under this contract even without the additional source fact that every label other than b is above a. It would not suffice that a,b were merely the only MARKED minima, or that u,v,w had downset {a} only inside a nonideal marked subposet.

## Cell proof and true weights

Every original extension starts with a or b, so these are an exhaustive disjoint partition. Both cells are nonempty because each of a,b is an original minimum.

If b occurs in reference position j>=2, the adjacent charged reversal b before y_(j-1) equals one in every b-first extension. Thus the three charged indicators sum at least one pointwise in that cell.

Deleting the FIRST a, only within the a-first cell, is a bijection onto all extensions of the actual induced poset P minus a. It is crucial that this is a prefix deletion, not arbitrary deletion of a from every extension with a nonuniform insertion multiplicity. The conditional law here really is the uniform law on P minus a. There b,u,v,w have equal empty full downsets. Their incomparable degrees do not increase on deletion (b actually loses its incomparable partner a). The reviewed four-label inequality therefore gives a strict sum greater than one for the SAME fixed reference, with no NB or strict-majority assumption on this remaining law.

If S is the original bank sum and p is the actual positive probability that a starts, the two conditional conclusions give S > p*1+(1-p)*1=1. This uses the actual cell masses, not equal weighting. Strictness is justified by p>0; no quantitative lower bound on p is required.

## Source identification and bank matching

I checked the local extraction of Fathi v22, fixed record 23933091. Section 24.3 states the original exactly-two-minima setup. Section 24.4 begins with the singleton private branch B={b}; A=P minus the principal upset of b is an original ideal. In the immediate three-minimum branch, u,v,w are minima of A minus a, hence their full original downsets are {a}, not merely their marked downsets. They are in A and thus incomparable with b. The ambient degree-nine hypothesis gives the needed individual degree bounds.

The displayed paragraph on printed page 284 (immediate fork introduced on page 283) lists precisely:

    [bu]+[vb]+[wv] >= 1,
    [bv]+[wb]+[vu] >= 1,
    [bw]+[vu]+[wv] >= 1.

With u,v,w named in their strict reference order, the only references having b after u are respectively (u,b,v,w), (u,v,b,w), and (u,v,w,b). Their three adjacent reversals are exactly these three banks, up to summand order. No bank, coefficient or physical label is chosen after taking a first-letter cell.

The source explicitly checks these on 978 profiles, with integer slacks 45,33,54. The corollary proves the required original-P ordering conclusion analytically (indeed strictly), so those three profile-bank verifications are no longer a needed proof dependency for that conclusion. It does not assert new structural coverage or certify any changed profile-domain metadata. The source's subsequent 174-word canonical-prefix tree and 1,820,185 integer inequalities remain untouched.

## Status

This is reuse of Fathi's existing immediate-fork structure and ordering conclusion, not a new balanced-poset class or a claim of novelty. It is outside the separate 3,469-bank two-fork seven-phase packet. Accordingly no number is added to the current 483-row ledger. No external repository or page was changed.
