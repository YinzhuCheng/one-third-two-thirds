"""Read-only structural/ratio audit of the frozen finite experiment. No LE counting."""
import json
from pathlib import Path
ROOT=Path(__file__).parent
P=Path(__file__).resolve().parent.parent / 'actual-excursion-targets-20261019'
rows=json.loads((P/'all_counts.json').read_text())
counts={}
for typ in ['II','DI','IU']:
    es=[(r,e) for r in rows for e in r['counts'] if e['kind']==typ]
    for r,e in es:
        a,b,c=r['total'];x,y,z=e['event']
        if typ=='II': assert x*b>y*a and y*c>z*b and 2*z==c
        else: assert x*b<=y*a and y*c<=z*b and z==c
    counts[typ]=len(es)
ngate=0
for case in json.loads((P/'frozen_cases.json').read_text()):
    for side in ['D','U_reverse']:
        sizes=case[side+'_sizes']
        nodes=[(a,j) for a,n in enumerate(sizes) for j in range(1,n+1)]
        ix={x:i for i,x in enumerate(nodes)};pred=[0]*len(nodes)
        for a,n in enumerate(sizes):
            for j in range(2,n+1):pred[ix[a,j]]|=1<<ix[a,j-1]
        for u,v in case[side+'_bridges']:pred[ix[tuple(v)]]|=1<<ix[tuple(u)]
        for k in range(len(nodes)):
            for i in range(len(nodes)):
                if pred[i]>>k&1:pred[i]|=pred[k]
        gs=[]
        for raw in case[side+'_gate_raw']:
            mask=0
            for a,n in enumerate(raw):
                for j in range(1,n+1):mask|=(1<<ix[a,j])|pred[ix[a,j]]
            gs.append(mask)
        if case['I_chain']:
            if side=='D':gs[1]|=gs[0]
            else:gs[0]|=gs[1]
        for mask,saved in zip(gs,case[side+'_gates']):
            maximum=[x for i,x in enumerate(nodes) if mask>>i&1 and not any((mask>>j&1) and (pred[j]>>i&1) for j in range(len(nodes)))]
            assert len(maximum)>=2
            assert [list(t) for t in maximum]==saved['maximal_generators']
            ngate+=1
assert ngate==96 and counts=={'II':12,'DI':48,'IU':48}
out={'checks':'PASS','effective_nonprincipal_gates':ngate,'finite_ordered_ratio_counts':counts,'status':'Only the frozen finite data; no unbounded theorem claimed.'}
(ROOT/'structural_controls.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
