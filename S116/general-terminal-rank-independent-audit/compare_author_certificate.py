"""Compare every author reduced-case witness against independent all-pair counts."""
from fractions import Fraction as F
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
ours=json.loads((HERE/'reduced_normal.json').read_text())['records']
lookup={tuple(r['weights']):r for r in ours}
author=json.loads((HERE/'author_normal/reduced_41_certificate.json').read_text())
if len(author)!=len(lookup) or {tuple(r['weights']) for r in author}!=set(lookup):
    raise RuntimeError('reduced vector sets differ')
checks=0
for record in author:
    own=lookup[tuple(record['weights'])];Z=own['extensions']
    if record['extensions']!=Z:raise RuntimeError('denominator mismatch')
    pairs={(tuple(x),tuple(y)):N for x,y,N in own['all_incomparable_pair_numerators']}
    for pair_key,value_key in [('balanced_pair','probability'),('failed_forced_arrow','forced_arrow_probability')]:
        x,y=[(p[0],p[1]-1) for p in record[pair_key]]
        if (x,y) in pairs:N=pairs[(x,y)]
        elif (y,x) in pairs:N=Z-pairs[(y,x)]
        else:raise RuntimeError(('not an actual incomparable pair',record,pair_key))
        if F(N,Z)!=F(record[value_key]):raise RuntimeError(('witness probability mismatch',record,pair_key))
        if pair_key=='balanced_pair' and not Z<=3*N<=2*Z:raise RuntimeError('unbalanced witness')
        if pair_key=='failed_forced_arrow':
            known={(tuple(a),tuple(b),num) for a,b,num,p in own['failed_forced_arrows']}
            if (x,y,N) not in known:raise RuntimeError('failed arrow is not structurally certified')
        checks+=1
result={'status':'PASS','author_vectors_matched':len(author),'denominators_matched':len(author),'independently_verified_author_pair_witnesses':checks,'author_labels':'one-based within blocks','independent_labels':'zero-based within blocks','checks_use_assert':False}
(HERE/'author_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
