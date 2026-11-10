# Independent audit: natural-reference source-bank stopping line

2026-11-10. PASS for NATURAL_BRANCH_BANK_STOPLINE.md, with its explicitly limited scope. No ledger change follows.

For each fixed internal word of an n-label p-rooted branch, the isolated q has n+1 tail insertion positions, so F=n+1. Adding independent v gives G=(n+1)(n+2). The audited zero-gap root decomposition then gives per-branch-word counts

    N=(n+1)(3n+11),
    K_(u<b)=(n+1)(n+4),
    K_(v<u)=4(n+1),
    K_(p<v)=3n(n+2),
    K_(q<p)=3n+11.

For the fourth count, only the three G root types allow p before v, and each has G-(n+2)=n(n+2) such tail interleavings. For the fifth, the ordinary F types have q before p in one tail position each; in a G type there are n+2 such interleavings, giving 5+3(n+2). These arguments depend only on the fixed internal branch word, not on the internal branch shape.

Direct symbolic substitution yields

    3(14K_(u<b)+8K_(v<u)+4K_(p<v)+K_(q<p))-27N
       =3n(3-n)

per branch word. Summing over all e(B) internal branch words proves the stated general formula 3n(3-n)e(B) with actual original counts. Thus n=3 is tight, and every n>=4 fails this exact fixed bank on the no-exterior model, regardless of the internal branch shape. The formula alone is not a degree-nine statement for arbitrary n; the separately specified smallest example is.

For the n=4 star branch, independent direct enumeration of every full original extension of pred=(0,0,1,1,7,7,23,23,23) gives N=690 and event counts (240,120,432,138), independently agreeing with the author's subset DP. The maximal full incomparable degree is seven and the signed margin is -72. The branch has six internal words; multiplying the independent per-word formulas by six produces the same five counts. See NATURAL_BRANCH_BANK_STOPLINE_INDEPENDENT.py/.json.

This is only a stopping line for the displayed weights14/8/4/1 and the displayed natural-reference event orientations. It does not rule out other coefficients or event sets. The three top leaves are fair twins, and u<b itself is 240/690=8/23, so the actual example is not NB. The isolated-head rooted-branch theorem charges p<q in the opposite head reference with weights7/2/1 and is unaffected.
