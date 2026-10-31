#!/usr/bin/env python3
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
import json,itertools
src=(Path(__file__).resolve().parent/'BASE_EXAMPLE.json');raw=json.loads(src.read_text());V=raw['V'];U={x:set() for x in V}
for edge in raw['relations']:
    a,b=edge.split('<');U[a].add(b)
for k in V:
    for a in V:
        if k in U[a]:U[a]|=U[k]
assert not any(x in U[x] for x in V)
D={x:{y for y in V if x in U[y]} for x in V}
Q=[x for x in V if x not in {'v','b','c1','c2'}];L={'a1','a2','a4'};M={'f0'};C={'f1','f2','f3'}
FB={x for x in M|C if not(D[x]&(M|C))};FZ={x for x in L|C if not(D[x]&(L|C))}
assert FB=={'f0','f1'} and FZ=={'a1','a2','f1'}
def count(V,extra=()):
    pre=[sum(1<<j for j,y in enumerate(V) if y in D[x]) for x in V];full=(1<<len(V))-1
    for a,b in extra:pre[V.index(b)]|=1<<V.index(a)
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|1<<i) for i in range(len(V)) if not mask>>i&1 and not pre[i]&~mask)
    return f(0)
N=count(V);A=count(V,[('a1','f0')]);Kmotif=count(V,[('a2','f1')]);EQ=count(Q);AQ=count(Q,[('a1','f0')])
# All Q extensions verify exact frontier targets, and quantify moving f1 out of C.
sums={'B':0,'Z':0,'B_front':0,'Z_front':0,'Z_after_move_f1_to_M':0};seen_first_B=set();seen_first_Z=set();example=None
sets=[M|C,L|C,FB,FZ,L|(C-{'f1'})]
def dfs(word,left):
    global example
    if not left:
        vals=[]
        for key,S in zip(sums,sets):
            k=next(i for i,x in enumerate(word) if x in S);sums[key]+=k+1;vals.append(k+1)
        assert vals[0]==vals[2] and vals[1]==vals[3]
        seen_first_B.add(word[vals[0]-1]);seen_first_Z.add(word[vals[1]-1])
        if vals[4]>vals[1] and example is None:example=word
        return
    for x in Q:
        if x in left and not(D[x]&left):dfs(word+[x],left-{x})
dfs([],set(Q))
assert seen_first_B==FB and seen_first_Z==FZ and sums['Z_after_move_f1_to_M']>sums['Z']
assert N==201453 and A==144124 and 3*A>2*N
out={'Q':Q,'B_minimal_frontier':sorted(FB),'Z_minimal_frontier':sorted(FZ),'common_minimal_frontier':sorted(FB&FZ),'frontier_disjoint_decomposition':{'M_front':sorted(FB-FZ),'C_front':sorted(FB&FZ),'L_front':sorted(FZ-FB)},'all_Q_extensions_frontier_identity':True,'first_target_sums':sums,'moving_f1_strict_increase':sums['Z_after_move_f1_to_M']-sums['Z'],'moving_f1_counterexample_word':example,'P_profiles':{x:{'D':sorted(D[x]),'U':sorted(U[x])} for x in ['a1','f0']},'counts':{'N':N,'a1_before_f0':A,'a2_before_f1':Kmotif,'eQ':EQ,'Q_a1_before_f0':AQ},'pP_a1_f0':str(Fraction(A,N)),'pQ_a1_f0':str(Fraction(AQ,EQ)),'pP_a2_f1':str(Fraction(Kmotif,N)),'3A_minus_2N':3*A-2*N,'pP_a1_f0_balanced':N<=3*A<=2*N}
(Path(__file__).resolve().parent/'frontier_independent_validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
