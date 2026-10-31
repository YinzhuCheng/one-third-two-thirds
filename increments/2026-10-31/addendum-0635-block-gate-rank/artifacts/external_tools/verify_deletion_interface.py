"""Diagnostic only: exact counts for four already archived C2 examples.
No exhaustive search and no new structural theorem is claimed.
"""
import functools, json
from fractions import Fraction
from pathlib import Path
src=Path(__file__).resolve().parent.parent/'poset_research_checkpoint_20261031/examples.json'
by={x['id']:x for x in json.loads(src.read_text())['examples']}
results=[]
for key in ('E08','E13','E16','E17'):
    entry=by[key]; labels=entry['vertices']; index={x:i for i,x in enumerate(labels)}
    pre=[0]*len(labels)
    for edge in entry['relations']:
        a,b=edge.split('<'); pre[index[b]] |= 1<<index[a]
    for k in range(len(labels)):
        for j in range(len(labels)):
            if pre[j]>>k&1: pre[j]|=pre[k]
    assert all(not (pre[j]>>j&1) for j in range(len(labels)))
    full=(1<<len(labels))-1
    @functools.cache
    def count(mask):
        if mask==full:return 1
        return sum(count(mask|1<<i) for i in range(len(labels))
                   if not mask>>i&1 and pre[i]&mask==pre[i])
    def deleted(*xs):return count(sum(1<<index[x] for x in xs))
    assert pre[index['e']]==(1<<index['v'])|(1<<index['d'])
    B=deleted('v','c1','b'); C=deleted('v','c1','d')
    D=deleted('v','c1','b','d'); E=deleted('v','c1','d','e')
    Z=deleted('c1','c2'); V=deleted('v','d','e')
    assert B*E<=2*C*D and Z*V<=C*C
    results.append(dict(example=key,counts=dict(B=B,C=C,D=D,E=E,Z=Z,V=V),
                        BE_over_2CD=str(Fraction(B*E,2*C*D)),
                        ZV_over_Csq=str(Fraction(Z*V,C*C))))
print(json.dumps(results,indent=2))
