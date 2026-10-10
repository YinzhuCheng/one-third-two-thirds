#!/usr/bin/env python3
from functools import lru_cache
from fractions import Fraction as Q
from pathlib import Path
from certify import permutation_profile
import json
OUT=Path(__file__).resolve().parent

def add_guarded_chain(pred,core_n,omitted,length):
 out=list(pred);gate=((1<<core_n)-1)^(1<<omitted)
 for _ in range(length):
  out.append(gate);gate|=1<<(len(out)-1)
 return out

def continuations(pred,core_n,maxima):
 @lru_cache(None)
 def count(rem):
  if not rem:return 1
  return sum(count(rem^(1<<v)) for v,p in enumerate(pred) if rem>>v&1 and not(p&rem))
 full=(1<<len(pred))-1;core=(1<<core_n)-1
 return [count(full^(core^(1<<v))) for v in maxima]

def probs(F,A,B):return [Q(sum(a*b for a,b in zip(row,B)),sum(f*b for f,b in zip(F,B))) for row in A]

result=[]
for pred,target,chainlen,ratio,expected_pair,expected_p in [
 ([0,0,1,3,5,7],3,1,[2,1,1],0,Q(21,31)),
 ([0,0,1,3,5,7],4,1,[1,2,1],1,Q(11,16)),
 ([0,0,1,2,5,7],3,5,[6,1,1],0,Q(41,61)),
 ([0,0,1,2,5,7],4,1,[1,2,1],1,Q(5,7)),
 ([0,0,0,1,2,5,11],4,10,[11,1,1],0,Q(380,569)),
 ([0,0,0,1,2,5,11],5,9,[1,10,1],1,Q(438,655)),
]:
 n=len(pred);maxima=[i for i in range(n) if not any(p>>i&1 for p in pred)]
 F,A=permutation_profile(pred,maxima,[[0,1],[1,2]])
 full=add_guarded_chain(pred,n,target,chainlen);B=continuations(full,n,maxima)
 assert B==ratio and all(p.bit_count()>=n-1 for p in full[n:])
 pp=probs(F,A,B);assert pp[expected_pair]==expected_p>Q(2,3)
 result.append(dict(core_pred=pred,omitted=target,chain_length=chainlen,completion_pred=full,B=B,probabilities=list(map(str,pp))))

# Genuine negative control: every simplex vertex is covered, actual guarded
# completion has both fully observed incomparable pairs above 2/3.
pred=[0,0,1,1,2,5];F,A=permutation_profile(pred,[3,4,5],[[0,1],[1,2]])
assert F==[10,15,20] and A==[[6,12,12],[7,7,16]]
assert all(any(Q(1,3)<=Q(row[j],F[j])<=Q(2,3) for row in A) for j in range(3))
full=add_guarded_chain(pred,6,4,5);full=add_guarded_chain(full,6,5,6)
B=continuations(full,6,[3,4,5]);pp=probs(F,A,B)
assert B==[462,792,924] and pp==[Q(177,265),Q(357,530)] and all(x>Q(2,3) for x in pp)
result.append(dict(name='genuine vertex-only negative control',core_pred=pred,completion_pred=full,B=B,probabilities=list(map(str,pp))))
(OUT/'completion_audit.json').write_text(json.dumps(result,indent=2))
print('PASS: six fixed-pair failure completions and one genuine vertex-only negative control; all exact.')
