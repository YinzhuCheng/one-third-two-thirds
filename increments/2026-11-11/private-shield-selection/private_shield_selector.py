#!/usr/bin/env python3
"""Exact structural selector, not source completeness or original-ideal evidence.

Input is the complete original ideal Q=P minus U_P(v), with root labels
(a0,b,u,v)=(0,1,2,3), and optional full reference. Full original completion
and all-exterior-above-v must be certified independently by the caller.
"""
from fractions import Fraction

def _matching(left,right,pred):
 partner={}
 def aug(y,seen):
  for x in right:
   if not pred[y]>>x&1 or x in seen:continue
   seen.add(x)
   if x not in partner or aug(partner[x],seen):partner[x]=y;return True
  return False
 return sum(aug(y,set()) for y in left)

def select_private_shield(pred,reference=None):
 p=tuple(pred);N=len(p);full=(1<<N)-1
 out={'qualifies':False,'requires_external_evidence':'exact original ideal and all actual exterior above v; no complete source census is asserted'}
 if N<4 or any(not isinstance(m,int) or m<0 or m&~full for m in p):return out|{'reason':'invalid predecessor array'}
 if any(p[i]>>i&1 for i in range(N)):return out|{'reason':'cycle or reflexive mask'}
 if any(p[j]>>i&1 and p[i]&~p[j] for i in range(N) for j in range(N)):return out|{'reason':'masks are not transitively closed'}
 if p[:4]!=(0,0,1,1):return out|{'reason':'root full downsets are not exact'}
 H=list(range(4,N));Hmask=sum(1<<i for i in H);n=len(H)
 if any(not p[y]&4 or p[y]&8 for y in H):return out|{'reason':'tail is not wholly above u and incomparable with v'}
 if reference is not None:
  if sorted(reference)!=list(range(N)):return out|{'reason':'invalid reference permutation'}
  where={x:i for i,x in enumerate(reference)}
  if any(p[j]>>i&1 and where[i]>where[j] for i in range(N) for j in range(N)):return out|{'reason':'reference is not an extension'}
  if not where[1]<where[2]<where[3]:return out|{'reason':'the two fixed bank events do not both reverse reference'}
 C=[i for i in H if not p[i]&2];Cmask=sum(1<<i for i in C);B=[i for i in H if p[i]&2]
 choices=[];S=Cmask
 while True:
  # S is a private ideal in H, not necessarily an original P ideal by itself.
  if all(not(S>>i&1) or p[i]&Hmask&~S==0 for i in H):
   a=S.bit_count();B0=[y for y in B if p[y]&S!=S];s=len(B0);deficit=s-_matching(B0,C,p)
   F=n*(a-s-1)+4*a+2*s+2
   if deficit<=2 and F>=0:choices.append({'S':[x for x in C if S>>x&1],'S_mask':S,'a':a,'s':s,'B0':B0,'matching_deficiency':deficit,'F':F})
  if S==0:break
  S=(S-1)&Cmask
 choices.sort(key=lambda x:(-Fraction(x['F'],x['s']+1),-x['a'],x['s'],x['S_mask']))
 return out|{'qualifies':bool(choices),'choices':choices,'private':C,'common':B,'bank':[(2,2,1),(1,3,2)],'threshold':1,'reference_checked':reference is not None}

if __name__=='__main__':
 import json,sys
 q=json.load(sys.stdin);print(json.dumps(select_private_shield(q['pred'],q.get('reference')),indent=2))
