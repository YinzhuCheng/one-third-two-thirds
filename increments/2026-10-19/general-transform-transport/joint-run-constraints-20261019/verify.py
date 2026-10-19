#!/usr/bin/env python3
"""Exact checks on 12 fixed original posets + 3 marker augmentations + 1 nonactual contrast.
No random generation or exhaustive enumeration of poset classes.
"""
from fractions import Fraction as F
from math import comb
from collections import Counter
import json
from pathlib import Path
from explore import models
OUT=Path(__file__).resolve().parent

def C(n,k):return comb(n,k) if n>=k>=0 else 0

def extensions(n,edges):
 pred=[0]*n
 for a,b in edges:pred[b]|=1<<a
 for k in range(n):
  for i in range(n):
   if pred[i]>>k&1:pred[i]|=pred[k]
 out=[]
 def rec(w,used):
  if len(w)==n:out.append(tuple(w));return
  for i in range(n):
   if not used>>i&1 and pred[i]&used==pred[i]:rec(w+[i],used|1<<i)
 rec([],0)
 ideals=[m for m in range(1<<n) if all(not m>>i&1 or pred[i]&m==pred[i] for i in range(n))]
 return out,ideals

def run(w,mask):
 for r,x in enumerate(w):
  if not mask>>x&1:return r
 return len(w)

def lc(v):return all(v[i]*v[i]>=v[i-1]*v[i+1] for i in range(1,len(v)-1))
def E(joint,fn):return sum(p*fn(x,y) for (x,y),p in joint.items())
def aseq(joint,h):return [E(joint,lambda x,y:(y-i+1) if x>=i else 0) for i in range(h+1)]
def bseq(joint,g):return [E(joint,lambda x,y:min(x,j)+1 if y>=j else 0) for j in range(g+1)]
def wm(x,y):return (x+1)*(y+1)-C(x+1,2)
def um(x,y):return y*C(x+1,2)-2*C(x+1,3)
def dm(x,y):return C(y+2,3)-C(y-x+1,3)
def vm(x,y):return C(y,2)*C(x+1,2)-2*(y-1)*C(x+1,3)+3*C(x+1,4)
def stats(joint,h,g):
 r=E(joint,lambda x,y:x);s=E(joint,lambda x,y:y)
 a=aseq(joint,h);b=bseq(joint,g)
 assert lc(a) and lc(b)
 A=[s+1]+[E(joint,lambda x,y:(y+1)*C(x,k)-k*C(x+1,k+1)) for k in range(1,h+1)]
 B=[F(1)]+[E(joint,lambda x,y:(x+1)*C(y,k)-C(x,k+1)) for k in range(1,g+1)]
 assert lc(A) and lc(B)
 for k in range(1,h+1):assert A[k]==sum(C(i-1,k-1)*a[i] for i in range(k,h+1))
 for k in range(1,g+1):assert B[k]==sum(C(j-1,k-1)*b[j] for j in range(k,g+1))
 ts=[]
 for m in range(4):
  Z=E(joint,lambda x,y:C(y+m,m))
  t=[E(joint,lambda x,y:C(y-i+m,m) if x>=i else 0) for i in range(h+1)]
  assert t[0]==Z and lc(t)
  T=[Z]+[sum(C(i-1,k-1)*t[i] for i in range(k,h+1)) for k in range(1,h+1)]
  assert lc(T)
  ts.append({'m':m,'Z':Z,'tail_numerators':t,'moment_numerators':T})
 ew,eu,ed,ev=[E(joint,z) for z in (wm,um,dm,vm)]
 for x,y in joint:
  assert wm(x,y)==sum(y-i+1 for i in range(x+1))
  assert um(x,y)==sum(i*(y-i+1) for i in range(x+1))
  assert dm(x,y)==sum(C(y-i+1,2) for i in range(x+1))
  assert vm(x,y)==sum(i*C(y-i+1,2) for i in range(x+1))
 assert ew*ev<=eu*ed
 cov=E(joint,lambda x,y:x*y)-r*s;var=E(joint,lambda x,y:x*x)-r*r
 return {'r':r,'s':s,'a':a,'b':b,'A':A,'B':B,'m_markers':ts,'marker_covariance_slack':eu*ed-ew*ev,'cov':cov,'varX':var,'T_slack':r*r+2*r-(cov+r)}

report={'scope':'12 fixed original posets; all nested ideals; 3 direct marker augmentations; 1 nonactual algebraic contrast','originals':[]}
pairs=0
for n,edges,name in models:
 le,ideals=extensions(n,edges);runs={k:[run(w,k) for w in le]for k in ideals}
 checks=[]
 for k in ideals:
  for l in ideals:
   if k&l!=k:continue
   joint={xy:F(z,len(le)) for xy,z in Counter(zip(runs[k],runs[l])).items()}
   st=stats(joint,k.bit_count(),l.bit_count());pairs+=1
   checks.append({'K':k,'L':l,'joint':[(x,y,p)for(x,y),p in joint.items()],'stats':st})
 report['originals'].append({'name':name,'n':n,'edges':edges,'e':len(le),'nested_pairs':checks})
 print(name,'e=',len(le),'nested pairs=',len(checks),'PASS')

# Three additional fixed actual structures. No marker-augmented class search.
n,edges=4,[(0,1),(2,3)];K,L=5,7
le,_=extensions(n,edges);joint={xy:F(z,len(le))for xy,z in Counter((run(w,K),run(w,L))for w in le).items()}
a=aseq(joint,2);b=bseq(joint,3)
Qedges=edges+[(4,5),(4,1),(4,3),(5,3)]
ql,_=extensions(6,Qedges)
rankjoint=Counter((w.index(4)-0,w.index(5)-1)for w in ql)
# Zero-based index(u)=i and index(v)=j+1.
for i in range(3):
 for j in range(i,4):assert F(rankjoint[i,j],len(le))==E(joint,lambda x,y:int(x>=i and y>=j))
for i,z in enumerate(a):assert sum(w.index(4)==i for w in ql)==len(le)*z
for j,z in enumerate(b):assert sum(w.index(5)==j+1 for w in ql)==len(le)*z
assert len(ql)==len(le)*E(joint,wm)
report['direct_two_markers']={'base':'C2+C2','K':K,'L':L,'e_base':len(le),'e_augmented':len(ql),'rank_counts':[(i,j,z)for(i,j),z in rankjoint.items()]}
for m in (1,2):
 me=edges+[(v,v+1)for v in range(n,n+m-1)]+[(v,3)for v in range(n,n+m)]
 ml,_=extensions(n+m,me)
 Z=E(joint,lambda x,y:C(y+m,m))
 assert len(ml)==len(le)*Z
 qq=[F(sum(run(w,K)>=i for w in ml),len(ml))for i in range(3)]
 t=[E(joint,lambda x,y:C(y-i+m,m) if x>=i else 0)/Z for i in range(3)]
 assert qq==t
 report[f'direct_m_{m}']={'e_augmented':len(ml),'tail':qq}

# Two different nested K,L on the SAME already-counted three-point model.
le,_=extensions(3,[(0,1)])
positive=Counter((run(w,1),run(w,3))for w in le)
negative=Counter((run(w,1),run(w,5))for w in le)
for tag,co in [('positive_cov_gap',positive),('nonMTP2_tail',negative)]:
 jj={xy:F(z,len(le))for xy,z in co.items()};report[tag]={'joint':[(x,y,p)for(x,y),p in jj.items()],'stats':stats(jj,1,2)}
# Survival MTP2 minor on i=0,1 and j=1,2.
jj={xy:F(z,len(le))for xy,z in negative.items()}
q=lambda i,j:E(jj,lambda x,y:int(x>=i and y>=j))
minor=q(0,1)*q(1,2)-q(0,2)*q(1,1)
assert minor==F(-1,9)
report['nonMTP2_tail']['minor']=minor

# One nonactual law, with strict h=2<g=3 and all triangular q_ij positive.
fake={(0,2):F(3,8),(0,3):F(1,8),(1,1):F(1,4),(2,2):F(1,8),(2,3):F(1,8)}
qx=[E(fake,lambda x,y:int(x>=i))for i in range(3)]
qy=[E(fake,lambda x,y:int(y>=j))for j in range(4)]
MX=[E(fake,lambda x,y:C(x,r))for r in range(3)]
MY=[E(fake,lambda x,y:C(y,r))for r in range(4)]
fa=aseq(fake,2);fb=bseq(fake,3)
rr=E(fake,lambda x,y:x);ss=E(fake,lambda x,y:y)
N=E(fake,lambda x,y:x*y+x);Tgap=rr*ss+rr*rr+2*rr-N
assert lc(qx) and lc(qy) and lc(MX) and lc(MY) and Tgap>=0
assert fa[1]**2-fa[0]*fa[2]==F(-23,64)
assert all(E(fake,lambda x,y:int(x>=i and y>=j))>0 for i in range(3) for j in range(i,4))
report['nonactual_contrast']={'joint':[(x,y,p)for(x,y),p in fake.items()],'qX':qx,'qY':qy,'MX':MX,'MY':MY,'a':fa,'b':fb,'a_LC_gap':fa[1]**2-fa[0]*fa[2],'r':rr,'s':ss,'N':N,'T_slack':Tgap}
report['summary']={'actual_original_structures':12,'direct_augmented_structures':3,'nonactual_contrast':1,'nested_pairs_checked':pairs,'all_actual_checks':'PASS'}

def conv(z):
 if isinstance(z,F):return str(z)
 if isinstance(z,dict):return {str(k):conv(v)for k,v in z.items()}
 if isinstance(z,(list,tuple)):return [conv(v)for v in z]
 return z
(OUT/'verification.json').write_text(json.dumps(conv(report),ensure_ascii=False,indent=2))
print(report['summary']);print('direct counts',len(ql));print('fake',conv(report['nonactual_contrast']))
