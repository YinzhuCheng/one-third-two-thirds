#!/usr/bin/env python3
"""Independent exact audit of the four-spine-singleton chain family.
Standard library only; no author counting routine is imported.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb
from fractions import Fraction
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parent
COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
PRED=[set() for _ in range(7)]
for i,j in COVERS: PRED[j].add(i)
for _ in range(7):
    for j in range(7):
        PRED[j]|=set().union(*(PRED[i] for i in tuple(PRED[j]))) if PRED[j] else set()


def oracle(u,t,v, enumerate_words=False):
    """Seven chain-height states, independently built transitive prerequisites.
    Count event 2<4 by the forward edge placing first 4 with 2 already present.
    """
    w=(u,1,1,1,t,1,v); zero=(0,)*7
    @lru_cache(None)
    def edges(s):
        out=[]
        for i in range(7):
            if s[i]<w[i] and all(s[j]==w[j] for j in PRED[i]):
                z=list(s);z[i]+=1;out.append((i,tuple(z)))
        return tuple(out)
    @lru_cache(None)
    def back(s):
        if s==w:return 1
        return sum(back(z) for _,z in edges(s))
    z=back(zero); layers={zero:1}; n=0; n10=0
    for level in range(sum(w)):
        nxt=defaultdict(int)
        for s,f in layers.items():
            for i,r in edges(s):
                nxt[r]+=f
                if i==4 and s[4]==0 and s[2]==1:n+=f*back(r)
                if i==0 and s[0]==0 and s[1]==1:n10+=f*back(r)
        layers=nxt
    assert layers=={w:z}
    result={'u':u,'t':t,'v':v,'Z':z,'N_2_before_4':n,'N_1_before_0':n10,
        'p_2_before_4':str(Fraction(n,z)), 'p_1_before_0':str(Fraction(n10,z))}
    if enumerate_words:
        def gen(s,word):
            if s==w:
                yield word;return
            for i,r in edges(s):yield from gen(r,word+(i,))
        return result,gen(zero,())
    return result


def binary_words(m,t):
    n=m+t
    for pos in combinations(range(n),m):
        pp=set(pos);yield tuple('S' if i in pp else 'C' for i in range(n))


def rank(word,q):
    return [i+1 for i,s in enumerate(word) if s=='S'][q-1]


def check_fibers(u,t,v):
    result,words=oracle(u,t,v,True); actual=Counter();count=0
    for word in words:
        count+=1
        r=word.index(1)
        assert word[:r]==(0,)*r
        h=word.index(5)
        k=word[:h].count(6)
        assert word[h+1:]==(6,)*(v-k)
        middle=word[r+1:h]
        s=[x for x in middle if x in (2,3,6)]
        assert s[0]==2 and s.count(2)==s.count(3)==1
        q=s.index(3)+1
        assert 2<=q<=k+2
        base=tuple('C' if x==4 else 'S' for x in middle if x!=0)
        actual[(r,k,q,base)]+=1
    expected={}
    for r in range(u+1):
        a=u-r
        for k in range(v+1):
            m=k+2
            for q in range(2,m+1):
                for base in binary_words(m,t):
                    expected[r,k,q,base]=comb(a+rank(base,q)-1,a)
    assert actual==expected,(u,t,v,'fiber multiplicities differ')
    assert count==result['Z']
    return {'u':u,'t':t,'v':v,'extensions_enumerated':count,'fibers_with_base':len(actual)}


def check_binary_coupling():
    coupling_checks=0; weighted_checks=0
    for m,t in product(range(1,8),repeat=2):
        L=m+t-1; counts=Counter()
        for V in combinations(range(1,L+1),m):
            for deleted in range(m):
                W=V[:deleted]+V[deleted+1:];counts[W]+=1
                for q in range(1,m+1):
                    r_firstS=1 if q==1 else 1+W[q-2]
                    r_firstC=1+V[q-1]
                    assert r_firstS<=r_firstC
                    coupling_checks+=1
        assert set(counts.values())=={t}
        assert len(counts)==comb(L,m-1)
        for q in range(1,m+1):
            for a in range(0,8):
                z=n=0
                for word in binary_words(m,t):
                    wt=comb(a+rank(word,q)-1,a)
                    z+=wt;n+=wt*(word[0]=='S')
                assert n*(m+t)<=m*z,(m,t,q,a)
                weighted_checks+=1
    return {'pointwise_coupling_checks':coupling_checks,'weighted_binary_checks':weighted_checks}


def main():
    out={'status':'PASS','scope':'Four spine blocks 1,2,3,5 singleton; all u,t,v positive integers.'}
    out['coupling']=check_binary_coupling()
    fibers=[check_fibers(u,t,v) for u,t,v in product(range(1,4),repeat=3)]
    out['fiber_validation']={'vectors':len(fibers),'extensions_enumerated':sum(x['extensions_enumerated'] for x in fibers),
        'base_fibers_checked':sum(x['fibers_with_base'] for x in fibers),'details':fibers}
    checked=0; equality=[]
    for u,t,v in product(range(1,13),repeat=3):
        r=oracle(u,t,v);checked+=1
        assert (v+t+2)*r['N_2_before_4'] <= (v+2)*r['Z'],r
        if (v+t+2)*r['N_2_before_4']==(v+2)*r['Z']:equality.append(r)
    out['independent_DP']={'positive_box':'1 <= u,t,v <= 12','vectors':checked,'bound_equality_vectors':equality}
    out['small_exceptions']=[oracle(u,t,v) for u,t,v in ((2,1,2),(2,2,2),(3,2,3))]
    for r in out['small_exceptions']:
        n=r['N_1_before_0'] if r['t']==1 else r['N_2_before_4']
        assert r['Z']<=3*n<=2*r['Z']
    ray_checks=0
    for t in range(1,101):
        rays={(t+1,t+1),(t,t),(t,t-1),(t-1,t)}
        for u,v in product(range(2,t+3),repeat=2):
            cone=(2*u<t+v+2 and 2*v<u+t+2 and 2*t<u+v+2)
            assert cone==((u,v) in rays)
            if cone and t>=3:
                assert 3*(v+2)<=2*(v+t+2)
            ray_checks+=1
    out['cone_check']={'t_range':'1..100','pairs_tested':ray_checks}
    out['method_warning']='Finite checks audit implementation and conditioning; general conclusions are proved in AUDIT.md.'
    (ROOT/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
