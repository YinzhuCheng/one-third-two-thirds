from itertools import permutations
from fractions import Fraction as F
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def chain(a): return list(zip(a,a[1:]))
cases=[
 dict(id='antichain3',V=['x','y','z'],arcs=[],edit=['x','y']),
 dict(id='antichain4',V=['x','y','z','w'],arcs=[],edit=['x','y'],target=['z','w']),
 dict(id='external_witness_loss',V=['x','y','z','w'],arcs=[['y','z']],edit=['x','y'],target=['z','w']),
 dict(id='external_positive',V=['x','y','z','w'],arcs=[['x','z']],edit=['x','y'],target=['z','w']),
 dict(id='external_negative',V=['x','y','z','w'],arcs=[['x','w']],edit=['x','y'],target=['z','w']),
 dict(id='ordinal_A2_block',V=['d1','d2','x','y','u1','u2'],arcs=[[d,m] for d in ['d1','d2'] for m in ['x','y']]+[[m,u] for m in ['x','y'] for u in ['u1','u2']],edit=['x','y']),
 dict(id='two_disjoint_chains',V=['a1','a2','b1','b2','b3'],arcs=chain(['a1','a2'])+chain(['b1','b2','b3']),edit=['a1','b2'],chains=[['a1','a2'],['b1','b2','b3']]),
 dict(id='two_chains_cross_constraints',V=['a1','a2','a3','b1','b2','b3'],arcs=chain(['a1','a2','a3'])+chain(['b1','b2','b3'])+[['a1','b2'],['b1','a3']],edit=['a2','b2'],chains=[['a1','a2','a3'],['b1','b2','b3']]),
 dict(id='balanced_improvement',V=['a1','a2','b'],arcs=[['a1','a2']],edit=['a1','b'],target=['a2','b'],chains=[['a1','a2'],['b']]),
]
assert len(cases)==9 and all(len(c['V'])<=6 for c in cases)

def dump(v):
 if isinstance(v,F): return str(v)
 if isinstance(v,dict): return {str(k):dump(w) for k,w in v.items()}
 if isinstance(v,(list,tuple)): return [dump(w) for w in v]
 return v

def cov(rows,A,B):
 return F(sum(a*b for a,b in zip(A,B)),len(rows))-F(sum(A),len(rows))*F(sum(B),len(rows))

out=[]
for c in cases:
 V=c['V']; x,y=c['edit']
 rows=[{v:i for i,v in enumerate(L)} for L in permutations(V) if all(L.index(a)<L.index(b) for a,b in c['arcs'])]
 plus=[r for r in rows if r[x]<r[y]]; minus=[r for r in rows if r[y]<r[x]]
 assert plus and minus
 p=F(len(plus),len(rows))
 pairs=[(a,b) for i,a in enumerate(V) for b in V[i+1:]]
 def q(rs,a,b): return F(sum(r[a]<r[b] for r in rs),len(rs))
 def delta(a,b): return q(plus,a,b)-q(rows,a,b)
 pair_results={a+'<'+b:dict(original=q(rows,a,b),plus=q(plus,a,b),minus=q(minus,a,b),drift=delta(a,b),cov_edit=cov(rows,[int(r[x]<r[y]) for r in rows],[int(r[a]<r[b]) for r in rows])) for a,b in pairs}
 between={}
 for z in V:
  if z in (x,y):continue
  r=F(sum(row[x]<row[z]<row[y] for row in rows),len(rows))
  s=F(sum(row[y]<row[z]<row[x] for row in rows),len(rows))
  lhs=delta(x,z)-delta(y,z); rhs=(1-p)*r/p+s
  assert lhs==rhs
  assert delta(x,z)>=0 and delta(y,z)<=0
  between[z]=dict(r=r,s=s,difference=lhs)
 global_preservation=all(delta(a,b)==0 for a,b in pairs if {a,b}!={x,y})
 no_between=all(v['r']==v['s']==0 for v in between.values())
 assert global_preservation==no_between
 # Matrix law of total covariance, exactly over every ordered pair of pair coordinates.
 for a,b in pairs:
  A=[int(r[a]<r[b]) for r in rows]; Ap=[int(r[a]<r[b]) for r in plus]; Am=[int(r[a]<r[b]) for r in minus]
  for u,v in pairs:
   B=[int(r[u]<r[v]) for r in rows]; Bp=[int(r[u]<r[v]) for r in plus]; Bm=[int(r[u]<r[v]) for r in minus]
   dA=q(plus,a,b)-q(minus,a,b);dB=q(plus,u,v)-q(minus,u,v)
   assert cov(rows,A,B)==p*cov(plus,Ap,Bp)+(1-p)*cov(minus,Am,Bm)+p*(1-p)*dA*dB
 if 'chains' in c:
  A,B=c['chains']
  assert all(delta(a,b)>=0 for a in A for b in B)
 target=None
 if 'target' in c:
  a,b=c['target']; target=dict(pair=c['target'],original=q(rows,a,b),plus=q(plus,a,b),drift=delta(a,b),cov_edit=p*delta(a,b))
 result=dict(id=c['id'],n=len(V),N=len(rows),Nplus=len(plus),Nminus=len(minus),p=p,global_other_pairs_preserved=global_preservation,between=between,pairs=pair_results,target=target)
 out.append(result)
 print(json.dumps(dump({k:v for k,v in result.items() if k in ['id','n','N','Nplus','Nminus','p','global_other_pairs_preserved','target']}),ensure_ascii=False))
(ROOT/'verification.json').write_text(json.dumps(dump(dict(budget_objects=9,max_n=6,results=out)),indent=2,ensure_ascii=False)+'\n')
print('All exact assertions passed.')
