"""Independent controls on two already-budgeted structures; no new search."""
import json
from pathlib import Path
from itertools import combinations
from math import comb
OUT=Path(__file__).resolve().parent
cases=json.loads((OUT/'all_counts.json').read_text())

def moments_by_D_words(c):
    p,q=c['p'],c['q'];d=p+q
    rows=[(0,0,0) for _ in range(13)]
    rows=[list(row) for row in rows]
    # Explicitly enumerate D words, never external subsets or chain lengths.
    for apos in combinations(range(1,d+1),p):
        aset=set(apos);bpos=tuple(x for x in range(1,d+1) if x not in aset)
        def L(g):
            a,b=g
            release=max(apos[a-1] if a else 0,bpos[b-1] if b else 0)
            return d-release
        ly,lz=L(c['y']),L(c['z'])
        contribution=(ly*lz+min(ly,lz),ly+lz,2)
        for k,v in enumerate(contribution):rows[0][k]+=v
        for idx,e in enumerate(c['counts'],1):
            if apos[e['r']-1]<bpos[e['s']-1]:
                for k,v in enumerate(contribution):rows[idx][k]+=v
    assert rows[0]==c['total']
    assert all(rows[j+1]==e['event'] for j,e in enumerate(c['counts']))
    return dict(case_index=c['case_index'],label=c['label'],D_words=comb(d,p),total=rows[0],events=rows[1:])

def directly_enumerate_C1(c):
    p,q=c['p'],c['q'];n=p+q+3;Y=p+q;Z=Y+1;C=Z+1
    pred=[0]*n
    for k in range(1,p):pred[k]|=1<<(k-1)
    for k in range(p+1,p+q):pred[k]|=1<<(k-1)
    for node,gate in [(Y,c['y']),(Z,c['z'])]:
        a,b=gate
        if a:pred[node]|=1<<(a-1)
        if b:pred[node]|=1<<(p+b-1)
    pred[C]=(1<<(p+q))-1
    total=0;counts=[0]*12;column=[0,0]
    def rec(word,mask):
        nonlocal total
        if len(word)==n:
            total+=1;pos={v:j for j,v in enumerate(word)}
            for idx,e in enumerate(c['counts']):counts[idx]+=pos[e['r']-1]<pos[p+e['s']-1]
            column[0]+=pos[C]<pos[Y];column[1]+=pos[C]<pos[Z]
            return
        for node in range(n):
            if not mask>>node&1 and pred[node]&~mask==0:rec(word+[node],mask|1<<node)
    rec([],0)
    a,b,d=c['total'];assert total==a+2*b+3*d
    for count,e in zip(counts,c['counts']):
        a,b,d=e['event'];assert count==a+2*b+3*d
    return dict(case_index=c['case_index'],label=c['label'],m=1,total=total,event_counts=counts,
                chain_columns={'C1_before_y':column[0],'C1_before_z':column[1]},
                chain_column_balanced={k:total<=3*v<=2*total for k,v in zip(['C1_before_y','C1_before_z'],column)})

controls=dict(moment_controls=[moments_by_D_words(cases[i-1]) for i in [1,28]],
              direct_C1_control=directly_enumerate_C1(cases[0]))
(OUT/'controls.json').write_text(json.dumps(controls,indent=2)+'\n')
print(json.dumps(controls,indent=2))
print('PASS: independent D-word moments and direct C1 LE enumeration')
