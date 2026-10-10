#!/usr/bin/env python3
"""Additional fully finite check of the two analytically handled D branches."""
import runpy,json
from pathlib import Path
B=Path(__file__).resolve().parent
# Load the independent arithmetic routines, without its module-level execution.
ns={'__file__':str(B/'audit_small_minimality_independent.py')};exec((B/'audit_small_minimality_independent.py').read_text().split('rows=[];records=[]')[0],ns)
g=ns['natural_posets'];ex=ns['exts'];C=ns['Counter'];comb=ns['combinations'];cert=ns['certify']
summary=[];records=[]
for m in range(0,6):
    seen=set();cases=C();fail=[]
    for pred in g(m):
        succ=[sum(1<<v for v in range(m) if pred[v]>>w&1) for w in range(m)]; linear=None
        for D in range(1<<m):
            if any(D>>v&1 and pred[v]&~D for v in range(m)):continue
            maxima=[v for v in range(m) if D>>v&1 and not succ[v]&D]
            if len(maxima)>=2:continue
            common=sum(1<<v for v in range(m) if pred[v]&D==D and not D>>v&1)
            ups=[U for U in range(1<<m) if not U&~common and not any(U>>v&1 and succ[v]&~U for v in range(m))]
            if linear is None:linear=ex(pred)
            for U,V in comb(ups,2):
                cases['empty_D' if not D else 'unique_max_D']+=1;hist=C()
                for seq in linear:
                    pos={v:k+1 for k,v in enumerate(seq)}
                    a=max([pos[v] for v in range(m) if D>>v&1],default=0)
                    b=min([pos[v] for v in range(m) if U>>v&1],default=m+1)
                    c=min([pos[v] for v in range(m) if V>>v&1],default=m+1)
                    hist[b-a,c-a]+=1
                key=tuple(sorted(hist.items()))
                if key in seen:continue
                seen.add(key)
                try:
                    certificate=cert(hist,m)
                    records.append({'m':m,'pred':pred,'D':D,'U':U,'V':V,'histogram':[[p,q,c] for (p,q),c in key],'certificate':certificate})
                except AssertionError:fail.append({'pred':pred,'D':D,'U':U,'V':V,'histogram':[[p,q,c] for (p,q),c in key]})
    summary.append({'m':m,'cases':dict(cases),'histograms':len(seen),'not_nonnegative_coefficient_certified':len(fail),'first_failures':fail[:3]})
R={'status':'PASS' if all(x['not_nonnegative_coefficient_certified']==0 for x in summary) else 'SOME_CERTIFICATES_INCONCLUSIVE','by_m':summary}
(B/'all_branches_full_coefficients.json').write_text(json.dumps(records,separators=(',',':'))+'\n')
(B/'all_branches_coefficient_check.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(R,indent=2))
