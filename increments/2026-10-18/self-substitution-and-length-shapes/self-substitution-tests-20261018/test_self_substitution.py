#!/usr/bin/env python3
from itertools import permutations, combinations
from collections import defaultdict
from fractions import Fraction
from math import factorial
import json
from pathlib import Path
OUT=Path(__file__).parent

def transitive(n,edges):
    rel=set(edges)
    for k in range(n):
      for i in range(n):
       for j in range(n):
        if (i,k) in rel and (k,j) in rel: rel.add((i,j))
    assert not any((i,i) in rel for i in range(n))
    return rel

def small_le(n,rel):
    les=[]
    for perm in permutations(range(n)):
      rank=[0]*n
      for i,a in enumerate(perm):rank[a]=i
      if all(rank[a]<rank[b] for a,b in rel):les.append(perm)
    M=[[0]*n for _ in range(n)]
    pairs={}
    for L in les:
      rank=[0]*n
      for i,a in enumerate(L):rank[a]=i;M[a][i]+=1
      for a,b in combinations(range(n),2):pairs[a,b]=pairs.get((a,b),0)+(rank[a]<rank[b])
    return les,M,pairs

def kernels(n,rel,m):
    pred=[{a for a,b in rel if b==p} for p in range(n)]
    start=(0,)*n;finish=(m,)*n
    bydepth=[[start]];F={start:1};edges={}
    for d in range(n*m):
      nxt=set()
      for c in bydepth[d]:
        ed=[]
        for p in range(n):
          if c[p]<m and all(c[a]==m for a in pred[p]):
            cc=list(c);cc[p]+=1;cc=tuple(cc)
            ed.append((p,cc));F[cc]=F.get(cc,0)+F[c];nxt.add(cc)
        edges[c]=ed
      bydepth.append(sorted(nxt))
    B={finish:1}
    for layer in reversed(bydepth[:-1]):
      for c in layer:B[c]=sum(B[cc] for p,cc in edges[c])
    assert B[start]==F[finish]
    inc=[(p,r) for p,r in combinations(range(n),2) if (p,r) not in rel and (r,p) not in rel]
    K={}
    for p,r in inc:
      mat=[[0]*m for _ in range(m)]
      for layer in bydepth[:-1]:
        for c in layer:
          for q,cc in edges[c]:
            if q==p:
              i=c[p]; w=F[c]*B[cc]
              for j in range(c[r],m):mat[i][j]+=w
      K[p,r]=mat
    return F[finish],K,len(F),sum(len(v) for v in edges.values())

def direct_big_le(n,rel):
    # Independent direct recursive generation of labeled P[P], no core word use.
    N=n*n;pred=[0]*N
    for p,a in [(p,a) for p in range(n) for a in range(n)]:
      v=p*n+a
      for r,b in [(r,b) for r in range(n) for b in range(n)]:
        if (r,p) in rel or (r==p and (b,a) in rel):pred[v]|=1<<(r*n+b)
    pairs=[(u,v) for u,v in combinations(range(N),2) if not(pred[v]>>u&1) and not(pred[u]>>v&1)]
    counts={pair:0 for pair in pairs};total=0
    def go(mask,order):
      nonlocal total
      if len(order)==N:
        total+=1
        rank=[0]*N
        for i,v in enumerate(order):rank[v]=i
        for u,v in pairs:counts[u,v]+=rank[u]<rank[v]
        return
      for v in range(N):
        if not(mask>>v&1) and pred[v]&~mask==0:go(mask|1<<v,order+[v])
    go(0,[])
    return total,counts

EXAMPLES=[
 ('C1_disjoint_C2',['X','A','B'],[(1,2)]),
 ('C2_disjoint_C3',['A1','A2','B1','B2','B3'],[(0,1),(2,3),(3,4)]),
 ('N',['A','B','C','D'],[(0,2),(0,3),(1,3)]),
 # Rigid asymmetric 4-point core: a<b<c and a<d. d and b,c have different roles.
 ('Asymmetric4',['a','b','c','d'],[(0,1),(1,2),(0,3)]),
]

allresults=[]
for name,names,eds in EXAMPLES:
 n=len(names);rel=transitive(n,eds);les,M,basecounts=small_le(n,rel);e=len(les)
 inc=[(a,b) for a,b in combinations(range(n),2) if (a,b) not in rel and (b,a) not in rel]
 base_delta=max((min(Fraction(basecounts[a,b],e),1-Fraction(basecounts[a,b],e)) for a,b in inc),default=Fraction(0))
 er,K,states,transitions=kernels(n,rel,n);E=er*e**n
 records=[]
 for p,r in inc:
  for a in range(n):
   for b in range(n):
    k=sum(M[a][i]*M[b][j]*K[p,r][i][j] for i in range(n) for j in range(n))
    num=k*e**(n-2);prob=Fraction(num,E);bal=min(prob,1-prob)
    records.append({'core':[p,r],'inner':[a,b],'count':num,'prob':str(prob),'balance':str(bal)})
 cross_delta=max((Fraction(t['balance']) for t in records),default=Fraction(0));delta=max(base_delta,cross_delta)
 maxima=[t for t in records if Fraction(t['balance'])==cross_delta]
 out={'name':name,'names':names,'n':n,'edges':sorted(rel),'eP':e,'base_delta':str(base_delta),'base_pair_counts':{f'{a},{b}':basecounts[a,b] for a,b in inc},'rank_counts':M,'eR':er,'states':states,'transitions':transitions,'E':E,'kernels':{f'{a},{b}':K[a,b] for a,b in inc},'cross_records':records,'cross_delta':str(cross_delta),'deltaPP':str(delta),'maxima':maxima}
 if n==3:
  DE,DC=direct_big_le(n,rel);assert DE==E
  for t in records:
   p,r=t['core'];a,b=t['inner'];assert DC[p*n+a,r*n+b]==t['count']
  for p in range(n):
   for a,b in inc:assert DC[p*n+a,p*n+b]==basecounts[a,b]*E//e
  out['direct_LE_check']={'E':DE,'incomparable_pairs':len(DC),'all_pair_counts_agree':True,'method':'recursive labeled topological order generation'}
 allresults.append(out)
 print(name,'n=',n,'eP=',e,'eR=',er,'E=',E,'deltaP=',base_delta,'deltaPP=',delta,'maxima=',maxima,flush=True)
(OUT/'counts.json').write_text(json.dumps(allresults,ensure_ascii=False,indent=2)+'\n')
