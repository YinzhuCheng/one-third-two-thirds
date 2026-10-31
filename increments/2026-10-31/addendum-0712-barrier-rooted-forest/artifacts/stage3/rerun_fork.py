#!/usr/bin/env python3
"""Raw-edge independent fork witness audit, no producer imports."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
import json, itertools, hashlib
p=(Path(__file__).resolve().parent/'fork_candidate.json')
data=json.loads(p.read_text()); V=data['V']; n=len(V); idx={x:i for i,x in enumerate(V)}
# Floyd-Warshall closure built only from supplied generating relations.
lt=[[False]*n for _ in V]
for edge in data['relations']:
    a,b=edge.split('<');lt[idx[a]][idx[b]]=True
for k in range(n):
    for i in range(n):
        for j in range(n):
            lt[i][j]=lt[i][j] or (lt[i][k] and lt[k][j])
assert not any(lt[i][i] for i in range(n))
D={a:{b for b in V if lt[idx[b]][idx[a]]} for a in V}
U={a:{b for b in V if lt[idx[a]][idx[b]]} for a in V}
I={a:set(V)-D[a]-U[a]-{a} for a in V}
def ordered(S):return [x for x in V if x in S]
def chain(S):return all(y in U[x] or x in U[y] for x,y in itertools.combinations(S,2))
def antichain(S):return all(y in I[x] for x,y in itertools.combinations(S,2))
vg=[];dvg=[];graph={x:set(U[x]) for x in V}; primal=[];dual=[]
for x,y in itertools.permutations(V,2):
    if y not in I[x]:continue
    if D[x]<=D[y] and chain(U[y]-U[x]):graph[x].add(y);primal.append([x,y])
    if U[y]<=U[x] and chain(D[x]-D[y]):graph[x].add(y);dual.append([x,y])
for x,y in itertools.combinations(V,2):
    if y not in I[x]:continue
    if D[x]==D[y] and chain(U[x]-U[y]) and chain(U[y]-U[x]):vg.append([x,y])
    if U[x]==U[y] and chain(D[x]-D[y]) and chain(D[y]-D[x]):dvg.append([x,y])
# Deterministic independent topological elimination.
todo=set(V);topo=[]
while todo:
    available=[x for x in V if x in todo and not any(x in graph[y] for y in todo)]
    if not available:break
    x=available[0];todo.remove(x);topo.append(x)
# Exhaustive module checks (65518 proper nonsingletons).
modules=[]
for mask in range(1,(1<<n)-1):
    if mask.bit_count()<2:continue
    S={V[i] for i in range(n) if mask>>i&1}
    if all(S<=D[x] or S<=U[x] or S<=I[x] for x in set(V)-S):modules.append(ordered(S))
# Independent deletion DP; all predecessor masks from original full closure.
def extension_count(removed=(),extra=()):
    W=[x for x in V if x not in removed];full=(1<<len(W))-1
    pre=[sum(1<<j for j,y in enumerate(W) if y in D[x]) for x in W]
    for x,y in extra:pre[W.index(y)]|=1<<W.index(x)
    @lru_cache(None)
    def tails(used):
        if used==full:return 1
        return sum(tails(used|1<<i) for i in range(len(W)) if not used>>i&1 and not pre[i]&~used)
    return tails(0)
A=(U['v']&U['c1'])-U['c2'];F=U['c2'];T=U['v']-U['c1'];Q=set(V)-{'v','b','c1','c2'}
L=A&U['b'];M=F-U['b'];C=F&U['b'];H={'e'};K=H|L;R=Q-K-M
inter=lambda sets:set.intersection(*sets)
dunion=set.union(*(D[x]&R for x in M));dcommon=inter([D[x]&R for x in K])
uunion=set.union(*(U[x]&R for x in K));ucommon=inter([U[x]&R for x in M])
N=extension_count();R0=extension_count({'c1'});R1=extension_count({'v','c1'});B=extension_count({'v','b','c1'});Z=extension_count({'c1','c2'});num=extension_count(extra=[('c1','d')])
# Enumerate LE(Q) separately to audit the two first-position counting identities.
W=ordered(Q);first_sums=[0,0];eq=0
pre={x:D[x]&Q for x in W}
def enumerate_q(prefix,remaining):
    global eq
    if not remaining:
        eq+=1
        for k,S in enumerate([M|C,L|C]):
            first_sums[k]+=next((j+1 for j,x in enumerate(prefix) if x in S),len(W)+1)
        return
    for x in W:
        if x in remaining and not(pre[x]&remaining):enumerate_q(prefix+[x],remaining-{x})
enumerate_q([],set(W))
old=[[x,y] for x in ordered(L) for y in ordered(M) if D[y]&Q <= D[x]&Q and U[x]&Q <= U[y]&Q]
nonmodule=[{'external':x,'below':ordered(U[x]&K),'above':ordered(D[x]&K),'incomparable':ordered(I[x]&K)} for x in ordered(R) if not(K<=D[x] or K<=U[x] or K<=I[x])]
out={'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'vertices':V,'generating_relations':data['relations'],'D':{x:ordered(D[x]) for x in V},'U':{x:ordered(U[x]) for x in V},'I_v':ordered(I['v']),'T':ordered(T),'A':ordered(A),'F':ordered(F),'L':ordered(L),'M':ordered(M),'C':ordered(C),'Q':ordered(Q),'K':ordered(K),'R':ordered(R),'L_antichain':antichain(L),'K_nonchain':not chain(K),'barrier_H_below_L':all(L<=U[x] for x in H),'K_cross_M':all(M<=I[x] for x in K),'profiles':{x:{'D_R':ordered(D[x]&R),'U_R':ordered(U[x]&R)} for x in ordered(K|M)},'D_R_union_M':ordered(dunion),'D_R_common_K':ordered(dcommon),'U_R_union_K':ordered(uunion),'U_R_common_M':ordered(ucommon),'external_lower_inclusion':dunion<=dcommon,'external_upper_inclusion':uunion<=ucommon,'budget':{'q':len(H),'l':len(L),'m':len(M),'holds':len(L)<=len(M)*(len(H)+1)},'nonautonomous_K_witnesses':nonmodule,'degrees':{x:len(I[x]) for x in V},'max_inc':max(map(len,I.values())),'very_good':vg,'dual_very_good':dvg,'mixed_arc_count':sum(map(len,graph.values())),'mixed_acyclic':not todo,'mixed_topological_order':topo,'modules':modules,'old_point_matching_edges':old,'counts':{'N':N,'R0':R0,'R1':R1,'B':B,'Z':Z,'K_c1d':num,'eQ':eq,'sum_first_M_C':first_sums[0],'sum_first_L_C':first_sums[1]},'q0':str(Fraction(R0,N)),'pd':str(Fraction(num,N)),'q0_closed_balanced':N<=3*R0<=2*N,'q0_lower_slack':3*R0-N,'pd_closed_balanced':N<=3*num<=2*N,'B_minus_Z':B-Z}
assert I['v']=={'c1','c2'} and 'c2' in U['c1'] and not D['v']
assert T=={'b','d','e'} and 'e' in U['d'] and {'d','e'}<=I['b']
assert A=={'a6','a7','a8','a9','a10'} and F=={'f11','f12','f13','f14','f15'}
assert L=={'a8','a10'} and M=={'f11'} and C=={'f12','f13','f14','f15'}
assert antichain(L) and L<=U['e'] and all(M<=I[x] for x in K)
assert dunion<=dcommon and uunion<=ucommon and len(L)<=len(M)*(len(H)+1)
assert out['max_inc']==9 and not vg and not dvg and not todo and not modules
assert R0==R1+Z and num==R0+R1+B and B<=Z and first_sums==[B,Z]
(Path(__file__).resolve().parent/'fork_independent_validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['D','U','generating_relations']},ensure_ascii=False,indent=2))
