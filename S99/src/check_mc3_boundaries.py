#!/usr/bin/env python3
"""Exact targeted diagnostics for the two MC3 boundary arguments.
No finite diagnostic is a proof of MC3. Standard library only.
"""
from functools import lru_cache
from itertools import permutations
from fractions import Fraction as F
from pathlib import Path
import json


def closure(n,edges):
 p=[0]*n
 for a,b in edges:p[b]|=1<<a
 for a in range(n):
  for b in range(n):
   if p[b]>>a&1:p[b]|=p[a]
 assert all(not(p[v]>>v&1)for v in range(n))
 return tuple(p)


def counter(p):
 full=(1<<len(p))-1
 @lru_cache(None)
 def f(mask):
  if mask==full:return 1
  return sum(f(mask|1<<v) for v in range(len(p))if not(mask>>v&1)and not(p[v]&~mask))
 return f


def extensions(p,removed=0):
 full=(1<<len(p))-1
 def visit(mask,seq):
  if mask==full:yield tuple(seq);return
  for v in range(len(p)):
   if not(mask>>v&1)and not(p[v]&~mask):yield from visit(mask|1<<v,seq+[v])
 yield from visit(removed,[])


def pair_count(p,x,y):
 edges=[(a,b)for b in range(len(p))for a in range(len(p))if p[b]>>a&1]
 return counter(closure(len(p),edges+[(x,y)]))(0)


def brute(p,qs):
 count=0;out=[0]*len(qs)
 for seq in permutations(range(len(p))):
  mask=0
  for v in seq:
   if p[v]&~mask:break
   mask|=1<<v
  else:
   count+=1;loc={v:i for i,v in enumerate(seq)}
   out=[t+int(loc[a]<loc[b])for t,(a,b)in zip(out,qs)]
 return count,out


def r1_example(edges):
 # a=0, x=1, y=4. All non-a points belong to these two root chains.
 p=closure(7,[(1,2),(2,3),(4,5),(5,6)]+edges)
 a,x,y=0,1,4;f=counter(p);E=f(0);rows=list(extensions(p,1<<a));n=len(rows)
 assert n==f(1<<a)
 sf=sum(tau[0]==x for tau in rows);rf=sum(set(tau[:2])=={x,y}for tau in rows)
 U=V=W=0;E0=X0=Y0=0
 for tau in rows:
  ff=next((i+1 for i,v in enumerate(tau)if v not in(x,y)),len(tau)+1)
  hh=next((i+1 for i,v in enumerate(tau)if p[v]>>a&1),len(tau)+1)
  assert ff in (2,3)and hh>=ff
  px=tau.index(x);py=tau.index(y)
  for slot in range(ff):
   E0+=1;X0+=int(slot<=px);Y0+=int(slot<=py)
  for slot in range(ff,hh):
   bx=slot<=px;by=slot<=py
   assert not(bx and by)
   if bx:U+=1
   elif by:V+=1
   else:W+=1
 X=pair_count(p,a,x);Y=pair_count(p,a,y)
 assert E0==2*n+rf and X0==2*n-sf and Y0==n+sf
 assert E==E0+U+V+W and X==X0+U and Y==Y0+V
 assert rf*n>=2*sf*(n-sf)
 assert 3*min(X,Y)<2*E
 assert 2*X+Y-2*E==n-sf-2*rf-V-2*W
 assert X+2*Y-2*E==sf-2*rf-U-2*W
 B,dirs=brute(p,[(a,x),(a,y)])
 assert B==E and dirs==[X,Y]
 return dict(p=list(p),E=E,n=n,s=str(F(sf,n)),r=str(F(rf,n)),extra=[U,V,W],directions=[str(F(X,E)),str(F(Y,E))],brute_extensions=B)


def family(m):
 # a=0,b=1,x=2,u=3..m+2,y=m+3,v=m+4.
 n=m+5;a,b,x,y,v=0,1,2,m+3,m+4
 ed=[(a,b),(b,3),(x,3),(a,v),(y,v)]+list(zip(range(3,m+2),range(4,m+3)))
 p=closure(n,ed);f=counter(p);E=f(0)
 expected=(3*m*m+27*m+50)//2
 assert E==expected
 qs=[(a,x),(b,x),(a,y),(b,y),(x,y)]
 nums=[pair_count(p,*q)for q in qs]
 expected_nums=[2*(E+2)//3,(E+2)//3,E-4*m-10,E-8*m-20,E-6*m-16]
 assert nums==expected_nums
 masks=[0,1<<a,(1<<a)|(1<<b)]
 Es=[f(mask)for mask in masks]
 Cx=[f(mask|1<<x)for mask in masks];Cy=[f(mask|1<<y)for mask in masks]
 D=[f(mask|1<<x|1<<y)for mask in masks]
 assert Es==[E,(m+3)*(m+4),(m+2)*(m+3)//2]
 assert Cx==[(m+3)*(m+4)//2-1,(m+2)*(m+3)//2,(m+1)*(m+2)//2]
 assert Cy==[3*m+8,2*m+6,m+2]and D==[m+2,m+2,m+1]
 rx=[Cx[j]-(Cx[j+1]if j<2 else 0)-D[j]for j in range(3)]
 ry=[Cy[j]-(Cy[j+1]if j<2 else 0)-D[j]for j in range(3)]
 assert rx==[0,0,m*(m+1)//2]and ry==[0,2,1]
 H=sum((j+1)*D[j]for j in range(3));Rx=sum((j+1)*rx[j]for j in range(3));Ry=sum((j+1)*ry[j]for j in range(3))
 assert H==6*m+9 and Rx==3*m*(m+1)//2 and Ry==7 and E==2*H+Rx+Ry
 q=[F(sum(Cx[j:]),Es[j])for j in range(3)]
 assert q==[1-F(6*m+16,E),F((m+2)**2,(m+3)*(m+4)),F(m+1,m+3)]
 delta=F(H,E)-q[0]*(1-q[0]);delta_formula=F(51*m*m+195*m+162,2*E*E)
 assert delta==delta_formula
 energy=F(1,2)*(q[1]-q[0])**2+F(Es[2],2*E)*(q[2]-q[1])**2
 assert energy<=delta
 assert 9*Es[1]>4*E and 3*Es[2]<E
 if m>=10:
  assert all(3*nums[i]>2*E for i in (0,2,3,4))
  assert E<3*nums[1]<2*E
 out=dict(m=m,n=n,E=E,pair_numerators=nums,pairs=qs,T=[str(F(e,E))for e in Es],Cx=Cx,Cy=Cy,D=D,H=H,Rx=Rx,Ry=Ry,delta=str(delta),energy=str(energy),q=[str(v)for v in q],states=f.cache_info().currsize)
 if m==10:
  sy=pair_count(p,3,y)
  assert E==310 and sy==165 and F(sy,E)==F(33,62)
  assert 3*sy>=E and 3*sy<=2*E
  assert F(sy,E)==q[0]**2-delta
  assert q[0]>F(2,3) and q[0]**2<=F(2,3)
  out['singleton_successor_rescue']=dict(s=3,y=y,numerator=sy,probability=str(F(sy,E)),entry_probability=str(q[0]))
 if m in(1,3):
  B,dirs=brute(p,qs);assert B==E and dirs==nums
  out['brute_extensions']=B
 return out


def main():
 r1=[r1_example(ed)for ed in [[],[(0,2),(0,5)],[(0,3),(0,6)],[(0,2),(0,6)]]]
 assert all(v>0 for v in r1[0]['extra'])
 fs=[family(m)for m in [1,2,3,5,6,9,10,12,20,50,100]]
 out=dict(status='PASSED',R1_examples=r1,family_examples=fs,scope='Targeted exact diagnostics of proved formulas; not a search certificate or MC3 proof.')
 path=Path(__file__).resolve().parent.parent/'evidence'/'mc3_boundaries.json'
 path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(dict(status='PASSED',R1_examples=len(r1),family_parameters=[r['m']for r in fs],brute_examples=sum('brute_extensions'in r for r in r1+fs),output=str(path)),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
