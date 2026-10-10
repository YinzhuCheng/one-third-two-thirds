#!/usr/bin/env python3
"""Independent check of the rank-chain filters and two-singleton-inner-block theorem."""
import json
from itertools import product
from math import comb
from pathlib import Path
from audit import labelled_graph,core_graph,count,comparison,COVERS,require
ROOT=Path(__file__).resolve().parent

def reduced_core(w):
    return labelled_graph(w,[((i,w[i]),(j,1)) for i,j in COVERS if w[i] and w[j]])

def check(w):
    u,a,b,c,t,d,v=w
    labels,pred,index=core_graph(w);z,_=count(pred)
    qs=[z]+[comparison(pred,index,(1,i),(0,1))[0] for i in range(1,a+1)]
    gaps=[qs[i]-qs[i+1] for i in range(a)]
    require(all(gaps[i]>=gaps[i+1] for i in range(a-1)), 'all(gaps[i]>=gaps[i+1] for i in range(a-1))')
    for i,g in enumerate(gaps):
        rw=(u-1,a-i,b,c,t,d,v)
        rl,rp,ri=reduced_core(rw)
        require(count(rp)[0]==g, 'count(rp)[0]==g')
    numerator=comb(b+t+v+u,u);denominator=comb(a+b+t+v+u,u)
    require(qs[-1]*denominator<=z*numerator, 'qs[-1]*denominator<=z*numerator')
    witnessed=None
    if 3*qs[1]>2*z and 3*qs[-1]<=2*z:
        balanced=[i for i in range(1,a+1) if z<=3*qs[i]<=2*z]
        require(balanced, 'balanced')
        witnessed={'weights':list(w),'extensions':z,'rank_numerators':qs[1:],
                   'balanced_C1_ranks_against_B0':balanced}
    return witnessed

def main():
    examples=[];n=0
    for w in product(range(1,4),repeat=7):
        example=check(w);n+=1
        if example is not None and len(examples)<5:examples.append(example)
    extras=[(1,9,1,1,1,11,1),(3,7,2,4,6,9,5),(4,5,6,7,8,9,10),(1,12,1,5,9,2,13)]
    for w in extras:check(w)
    family=0
    for u,a,t,d,v in product(range(1,6),repeat=5):
        check((u,a,1,1,t,d,v));family+=1
    for u in range(2,10001):
        require(87*u*u+90*u-221>0,('baseline polynomial',u))
        require(23*u*u+12*u-35==(u-1)*(23*u+35)>0,('upgrade polynomial',u))
    result={'status':'PASS','scope':'separate rank-chain and two-singleton-inner-block audit; not part of primary shuffle source',
            'box_cases':n,'extra_cases':len(extras),'inner_singleton_family_box':[1,5],'inner_singleton_family_vectors':family,'polynomial_integer_range':[2,10000],'examples_where_rank_filter_adds_information':examples}
    (ROOT/'rank_chain_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
