#!/usr/bin/env python3
from independent_labeled_extensions import audit, ROOT
from fractions import Fraction
from math import comb
import json

def positional_formula(a,b,i,j):
    t=i+j-1
    num=0
    # Count full binary words by choosing A positions on both sides of cut.
    for k in range(t+1):
        if k>=i and 0<=k<=a and 0<=a-k<=a+b-t:
            num+=comb(t,k)*comb(a+b-t,a-k)
    return Fraction(num,comb(a+b,a))

out=[]
for a,u in [(7,6),(48,35)]:
    assert (a+1)*(a+2)==2*u*u
    row={'a':a,'u':u,'before':audit([], [a,2]),
         'children':[audit([], [a-1,2]),audit([], [a,1])]}
    for result in [row['before']]+row['children']:
        x,y=result['lengths']
        assert result['extensions']==comb(x+y,x)
        for pair in result['pairs']:
            assert Fraction(pair['p'])==positional_formula(x,y,pair['x'][1],pair['y'][1])
    assert Fraction(row['before']['delta'])==Fraction(u-1,2*u)
    assert all(Fraction(r['delta'])>Fraction(row['before']['delta']) for r in row['children'])
    print(a,u,row['before']['extensions'],row['before']['delta'],[(c['lengths'],c['extensions'],c['delta']) for c in row['children']],flush=True)
    out.append(row)
(ROOT/'pell_full_labeled_counts.json').write_text(json.dumps(out,indent=2)+'\n')
