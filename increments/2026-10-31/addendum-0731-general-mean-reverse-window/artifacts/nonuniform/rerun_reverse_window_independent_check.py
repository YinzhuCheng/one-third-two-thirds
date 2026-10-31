#!/usr/bin/env python3
"""Independent raw-relation closure, induced-poset and integer-count checks."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from collections import Counter
import json,itertools,math,hashlib
basepath=(Path(__file__).resolve().parent/'BASE_EXAMPLE.json')
gappath=(Path(__file__).resolve().parent/'LOWER_GAP_WITNESS.json')
base=json.loads(basepath.read_text());rawgap=json.loads(gappath.read_text())
def closure(V,relations):
    U={x:set() for x in V}
    for edge in relations:
        a,b=edge.split('<');U[a].add(b)
    for k in V:
        for x in V:
            if k in U[x]:U[x]|=U[k]
    assert not any(x in U[x] for x in V)
    return U
def restrict(U,W):return {x:U[x]&set(W) for x in W}
def pred(U):return {x:{y for y in U if x in U[y]} for x in U}
def count(U,extra=()):
    V=list(U);D=pred(U);pre=[sum(1<<j for j,y in enumerate(V) if y in D[x]) for x in V]
    for a,b in extra:pre[V.index(b)]|=1<<V.index(a)
    full=(1<<len(V))-1
    @lru_cache(None)
    def f(mask):
        if mask==full:return 1
        return sum(f(mask|1<<i) for i in range(len(V)) if not mask>>i&1 and not pre[i]&~mask)
    return f(0)
def enumerate_words(U):
    V=list(U);D=pred(U)
    def dfs(word,remaining):
        if not remaining:yield word;return
        for x in V:
            if x in remaining and not D[x]&remaining:yield from dfs(word+[x],remaining-{x})
    yield from dfs([],set(V))
V=base['V'];U=closure(V,base['relations']);D=pred(U)
Q=restrict(U,[x for x in V if x not in {'v','b','c1','c2'}]);DQ=pred(Q)
A=(U['v']&U['c1'])-U['c2'];F=U['c2'];L=A&U['b'];M=F-U['b'];C=F&U['b']
assert L=={'a1','a2','a4'} and M=={'f0'} and C=={'f1','f2','f3'}
assert DQ['a1']=={'d'} and DQ['f0']=={'d','e'}
assert Q['a1']=={'a4','f2','f3'} and Q['f0']=={'f2','f3'}
R=restrict(Q,[x for x in Q if x not in {'a1','f0'}])
expected_gap_edges=[a+'<'+b for a in R for b in R[a]]+['d<gap1','gap1<gap2','gap2<e','e<mcopy','mcopy<f2']
G=closure(rawgap['vertices'],rawgap['relations'])
G_expected=closure(list(R)+['gap1','gap2','mcopy'],expected_gap_edges)
assert G==G_expected, 'witness lacks or adds inherited relations'
assert all(b in R[a] for a,b in [('d','e'),('e','a4'),('e','f1'),('f1','f2')])
# Count via independent deletion DP from the complete original closure.
N=count(U);R0=count(restrict(U,[x for x in V if x!='c1']));R1=count(restrict(U,[x for x in V if x not in {'v','c1'}]));B=count(restrict(U,[x for x in V if x not in {'v','b','c1'}]));Z=count(restrict(U,[x for x in V if x not in {'c1','c2'}]));K=count(U,[('c1','d')])
gap=count(G);early=count(G,[('s','e')]);late=count(G,[('e','s')])
# Fully separate LE(Q) sum check.
words=list(enumerate_words(Q));SB=sum(min(w.index(x)+1 for x in M|C) for w in words);SZ=sum(min(w.index(x)+1 for x in L|C) for w in words)
# Six-point suffix rank distribution independently enumerated from G.
T=restrict(G,['a3','a4','f1','f2','f3','mcopy']);hist=Counter(w.index('f1')+1 for w in enumerate_words(T))
slots={j:math.comb(8,2)-math.comb(8-j,2) for j in hist}
assert gap==699 and early==420 and late==279 and hist=={2:3,3:6,4:6}
assert sum(hist[j]*slots[j] for j in hist)==late
assert SB==B and SZ==Z and B-Z==3790 and R0==R1+Z and K==2*R0+B-Z
allowance=Fraction(2*N,3)-2*R0
assert allowance==568 and gap>allowance and 3*R0<N and 3*K>2*N
out={'base_source':str(basepath),'base_sha256':hashlib.sha256(basepath.read_bytes()).hexdigest(),'gap_source':str(gappath),'gap_source_sha256':hashlib.sha256(gappath.read_bytes()).hexdigest(),'Q_vertices':list(Q),'R_vertices':list(R),'L':sorted(L),'M':sorted(M),'C':sorted(C),'critical_profiles':{x:{'D_Q':sorted(DQ[x]),'U_Q':sorted(Q[x])} for x in ['a1','f0']},'gap_matches_full_inherited_R_plus_exact_five_edges':True,'counts':{'N':N,'R0':R0,'R1':R1,'B':B,'Z':Z,'K_c1d':K,'eQ':len(words),'sum_first_M_C':SB,'sum_first_L_C':SZ,'B_minus_Z':B-Z,'gap':gap,'gap_s_before_e':early,'gap_e_before_s':late,'suffix_six':sum(hist.values())},'suffix_f1_rank_histogram':dict(hist),'insert_s_a2_counts_by_rank':slots,'allowance':str(allowance),'lower_certificate_surplus':str(gap-allowance),'q0':str(Fraction(R0,N)),'pd':str(Fraction(K,N)),'N_minus_3R0':N-3*R0,'3K_minus_2N':3*K-2*N,'quantitative_K_lower_bound':2*R0+gap,'quantitative_K_excess_above_2N_over_3':str(2*R0+gap-Fraction(2*N,3)),'integer_factor_identity':{'n':len(Q),'gap_n':len(G),'factor':(len(Q)+1)*math.factorial(len(Q)),'gap_factorial':math.factorial(len(G))}}
(Path(__file__).resolve().parent/'reverse_window_independent_validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
