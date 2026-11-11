#!/usr/bin/env python3
from pathlib import Path
from functools import lru_cache
import json,time

def close(pred):
 p=list(pred)
 for j in range(len(p)):
  old=-1
  while old!=p[j]:
   old=p[j]
   for i in range(len(p)):
    if p[j]>>i&1:p[j]|=p[i]
 return tuple(p)

def all_natural(n):
 pairs=[(i,j) for j in range(n) for i in range(j)]
 seen=set()
 for bits in range(1<<len(pairs)):
  p=[0]*n
  for z,(i,j) in enumerate(pairs):
   if bits>>z&1:p[j]|=1<<i
  p=close(p)
  if p not in seen:seen.add(p);yield p

def isideal(p,C):return all(not(C>>i&1) or p[i]&C==p[i] for i in range(len(p)))
def stats(p,C):
 n=len(p);full=(1<<n)-1;B=full^C
 @lru_cache(None)
 def count(S):
  if S==full:return 1
  return sum(count(S|1<<i) for i in range(n) if not S>>i&1 and p[i]&S==p[i])
 @lru_cache(None)
 def jsum(S):
  if S&B:return 0
  # J=sum_{t>=0} 1[J>t], starting at current private prefix.
  return count(S)+sum(jsum(S|1<<i) for i in range(n) if C>>i&1 and not S>>i&1 and p[i]&S==p[i])
 return count(0),jsum(0)

def full_Q(p,C):
 # a,b,u,v then H. u under every H; b under common H.
 q=[0,0,1,1]
 for i,m in enumerate(p):q.append(1|4|(2 if not C>>i&1 else 0)|(m<<4))
 return close(q)

def count_events(p,events):
 n=len(p);full=(1<<n)-1
 def cnt(extra=None):
  pp=list(p)
  if extra:
   x,y=extra;pp[y]|=1<<x;pp=close(pp)
   if any(pp[i]>>i&1 for i in range(n)):return 0
  @lru_cache(None)
  def dp(S):
   if S==full:return 1
   return sum(dp(S|1<<i) for i in range(n) if not S>>i&1 and pp[i]&S==pp[i])
  return dp(0)
 return [cnt()]+[cnt(e) for e in events]


def matching_size(left,right,pred):
 partner={}
 def aug(y,seen):
  for x in right:
   if not pred[y]>>x&1 or x in seen:continue
   seen.add(x)
   if x not in partner or aug(partner[x],seen):partner[x]=y;return True
  return False
 return sum(aug(y,set()) for y in left)

def select_H(p,Cmask):
 n=len(p);full=(1<<n)-1;C=[i for i in range(n) if Cmask>>i&1];B=[i for i in range(n) if not Cmask>>i&1]
 valid=[]
 for S in range(1<<n):
  if S&~Cmask or not isideal(p,S):continue
  a=S.bit_count();B0=[i for i in B if p[i]&S!=S];s=len(B0)
  deficit=s-matching_size(B0,C,p)
  F=n*(a-s-1)+4*a+2*s+2
  if deficit<=2 and F>=0:valid.append(dict(S=S,a=a,s=s,F=F,deficit=deficit))
 return valid

def roots_to_H(q):
 return tuple(m>>4 for m in q[4:]),sum(1<<i for i,m in enumerate(q[4:]) if not m&2)

def compare(q):
 p,C=roots_to_H(q);H=list(range(4,len(q)));n=len(H)
 choices=select_H(p,C);common=[i for i in range(len(p)) if not C>>i&1];private=[i for i in range(len(p)) if C>>i&1];B0=[i for i in common if p[i]&C!=C];sc=len(B0);cc=len(private);Fc=n*(cc-sc-1)+4*cc+2*sc+2;old={'qualifies':sc-matching_size(B0,private,p)<=2 and Fc>=0,'old_D':all(p[i] for i in common),'old_M':len(common)-matching_size(common,private,p)<=2};old_DH=[]
 for i in H:
  if q[i]&2 or any(q[i]>>j&1 for j in H):continue
  R=[j for j in H if j!=i and not q[j]>>i&1]
  old_DH.append(dict(p=i,r=len(R),qualifies=len(R)<=2 and len(R)*(n-2)<=6))
 N,A,D=count_events(q,[(2,1),(3,2)])
 degree=max(sum(not((q[i]>>j&1)or(q[j]>>i&1)) for j in range(len(q)) if i!=j) for i in range(len(q)))
 return dict(pred=q,degree=degree,N=N,K_ub=A,K_vu=D,margin=2*A+D-N,choices=choices,whole_C_shield=old['qualifies'],old_FG_D=old['old_D'],old_FG_M=old['old_M'],old_DH=old_DH)

def main():
 start=time.time();rank_tests=0;equals=0;posets=0;Cs=0;contracts=0;gate_tests=0
 for n in range(7):
  for p in all_natural(n):
   posets+=1
   for C in range(1<<n):
    if not isideal(p,C):continue
    Cs+=1;N,J=stats(p,C)
    sub=C
    while True:
     a=sub.bit_count();s=sum(1 for i in range(n) if not C>>i&1 and p[i]&sub!=sub)
     margin=(s+1)*J-(a+s+1)*N
     assert margin>=0,(p,C,sub,N,J,s,margin)
     rank_tests+=1;equals+=margin==0
     if sub==0:break
     sub=(sub-1)&C
    choices=select_H(p,C)
    if choices:
     contracts+=1
     # The full-H raw root margin must pay for each accepted shield.
     m=(n+4)*J-2*(n+1)*N
     assert m>=0,(p,C,choices,m)
     gate_tests+=len(choices)
 ex=[compare((0,0,1,1,5,5,37,7,151,407,919)),compare((0,0,1,1,5,5,7,87,215,471,983))]
 for x in ex:
  assert x['choices'] and x['margin']>=0 and not x['whole_C_shield'] and not x['old_FG_D'] and not x['old_FG_M'] and not any(t['qualifies'] for t in x['old_DH'])
 out=dict(status='PASS',scope='all natural-label posets through six labels, every private ideal and every private subset; every ideal-shield gate accepted in full H; two full original-Q controls',natural_posets=posets,private_ideals=Cs,rank_tests=rank_tests,rank_equalities=equals,gate_contracts=contracts,gate_choices=gate_tests,examples=ex)
 target=Path(__file__).with_name('PRIVATE_SHIELD_SELECTION_CHECK.json');target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
