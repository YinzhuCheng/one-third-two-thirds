#!/usr/bin/env python3
from fractions import Fraction as Q
from itertools import combinations, product, permutations
from pathlib import Path
import json
OUT=Path(__file__).resolve().parent

def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q())
def solve(A,b):
 n=len(b);M=[[Q(x) for x in a]+[Q(bb)] for a,bb in zip(A,b)]
 for k in range(n):
  j=next((j for j in range(k,n) if M[j][k]),None)
  if j is None:return None
  M[k],M[j]=M[j],M[k];d=M[k][k];M[k]=[v/d for v in M[k]]
  for j in range(n):
   if j!=k:
    d=M[j][k];M[j]=[v-d*w for v,w in zip(M[j],M[k])]
 return [row[-1] for row in M]

def lp(F,A,pattern):
 m=len(F);k=len(A);q=[[Q(a,f) for a,f in zip(row,F)] for row in A]
 h=[[Q(1,3)-x if side=='L' else x-Q(2,3) for x in row] for row,side in zip(q,pattern)]
 rows=[[-int(i==j) for j in range(m)]+[0] for i in range(m)] + [[-x for x in hh]+[1] for hh in h]
 eq=[Q(1)]*m+[Q(0)];best=None
 for active in combinations(range(len(rows)),m):
  x=solve([eq]+[rows[i] for i in active],[1]+[0]*m)
  if x is not None and all(dot(r,x)<=0 for r in rows):
   if best is None or x[-1]>best[-1]:best=x
 assert best is not None
 tight=[i for i,r in enumerate(rows) if dot(r,best)==0]
 for active in combinations(tight,m):
  basis=[rows[i] for i in active]+[eq]
  w=solve(list(map(list,zip(*basis))),[0]*m+[1])
  if w is None or any(t<0 for t in w[:-1]):continue
  weights=[Q(0)]*len(rows)
  for i,v in zip(active,w[:-1]):weights[i]=v
  assert w[-1]==best[-1]
  result=dict(pattern=''.join(pattern),optimum=str(best[-1]),mu=[str(x) for x in best[:-1]],lambda_pairs=[str(x) for x in weights[m:]],eta=[str(x) for x in weights[:m]],nu=str(w[-1]))
  verify(F,A,result)
  return result
 raise AssertionError('missing dual')

def verify(F,A,c):
 m=len(F);q=[[Q(a,f) for a,f in zip(row,F)] for row in A];p=c['pattern']
 h=[[Q(1,3)-x if side=='L' else x-Q(2,3) for x in row] for row,side in zip(q,p)]
 mu=list(map(Q,c['mu']));lam=list(map(Q,c['lambda_pairs']));eta=list(map(Q,c['eta']));nu=Q(c['nu']);opt=Q(c['optimum'])
 assert all(x>=0 for x in mu+lam+eta) and sum(mu)==sum(lam)==1
 assert all(dot(hh,mu)>=opt for hh in h)
 assert all(sum(l*hh[j] for l,hh in zip(lam,h))+eta[j]==nu for j in range(m))
 assert opt==nu

def permutation_profile(pred,maxima,pairs):
 n=len(pred);full=(1<<n)-1;F=[];A=[[] for _ in pairs]
 for omitted in maxima:
  vertices=[i for i in range(n) if i!=omitted];valid=[]
  for perm in permutations(vertices):
   where={v:i for i,v in enumerate(perm)}
   if all(where[x]<where[y] for y in vertices for x in vertices if pred[y]>>x&1):valid.append(where)
  F.append(len(valid))
  for row,(x,y) in zip(A,pairs):row.append(sum(v[x]<v[y] for v in valid))
 return F,A

def cert(prof,name,selected):
 prof=dict(prof);F=prof['F'];A=[prof['A'][i] for i in selected]
 assert permutation_profile(prof['pred'],prof['maxima'],prof['pairs'])==(F,prof['A'])
 cells=[lp(F,A,p) for p in product('LH',repeat=len(A))]
 assert all(Q(c['nu'])<=0 for c in cells)
 q=[[Q(a,f) for a,f in zip(row,F)] for row in prof['A']]
 assert all(any(x<Q(1,3) or x>Q(2,3) for x in row) for row in q)
 prof.update(name=name,selected_indices=selected,selected_pairs=[prof['pairs'][i] for i in selected],certificates=cells,covered=True,all_observed_pairs_nonfixed=True)
 print(name,'F',F,'A',A)
 for c in cells:print(c)
 return prof

if __name__=='__main__':
 data=json.loads((OUT/'candidates.json').read_text())
 specs=[('W3-six-boundary',[0,0,1,3,5,7],[0,1]),('W3-six-triangle',[0,0,1,2,5,7],[0,1]),('W3-seven-three-minima',[0,0,0,1,2,5,11],[0,2])]
 result=[]
 for name,pred,sel in specs:
  p=next(p for p in data['candidates'] if p['pred']==pred)
  result.append(cert(p,name,sel))
 (OUT/'exact_templates.json').write_text(json.dumps(result,indent=2))
