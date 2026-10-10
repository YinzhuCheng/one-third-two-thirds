#!/usr/bin/env python3
"""Second exact verifier: different extension oracle, by adding one edge.
No import of the generator or the all-pair forward/backward ideal oracle.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import itertools,json
HERE=Path(__file__).parent

def counts(up,w,pair=None):
 V=[(i,r) for i in range(8) for r in range(w[i])];index={v:i for i,v in enumerate(V)}
 pred=[sum(1<<a for a,(i,r) in enumerate(V) if up[i]>>j&1 or i==j and r<s) for j,s in V]
 if pair:
  a,b=[index[tuple(v)] for v in pair];pred[b]|=1<<a
 end=(1<<len(V))-1
 @lru_cache(None)
 def f(S):
  if S==end:return 1
  return sum(f(S|1<<v) for v,p in enumerate(pred) if not S>>v&1 and not p&~S)
 return f(0)

def main():
 G={q['class_id']:q for q in json.loads((HERE/'weight_filter_catalogue.json').read_text())['cores']};D=json.loads((HERE/'minimal_support_family_certificates.json').read_text());num=0;counts_n=0
 for c in D['cores']:
  q=G[c['class_id']];S=c['variable_indices'];assert S==q['port_forced_nonsingleton_indices'];m=len(S)
  A=c['matrix'];b=c['rhs'];H=[[F(*v) for v in row] for row in c['inverse_rational']]
  rules={r['target']:r for r in q['rules']}
  assert A==[[2 if i==j else -1 if j in rules[i]['incomparable_indices'] else 0 for j in S] for i in S]
  assert b==[sum(j not in S for j in rules[i]['incomparable_indices'])-1 for i in S]
  assert all(v>=0 for row in H for v in row)
  assert all(sum(H[i][k]*A[k][j] for k in range(m))==int(i==j) for i in range(m) for j in range(m))
  upper=[sum(a*x for a,x in zip(row,b)) for row in H]
  assert upper==[F(*v) for v in c['upper_bounds_rational']]
  bound=[int(v//1) for v in upper];assert bound==c['upper_bounds_integer']
  expected=[]
  for values in itertools.product(*(range(2,u+1) for u in bound)):
   w=[1]*8
   for i,v in zip(S,values):w[i]=v
   if all(sum(a*v for a,v in zip(r['coefficients'],w))<=-1 for r in q['rules']):expected.append(w)
  assert expected==[r['weights'] for r in c['balanced_certificates']]
  assert len(expected)==c['filter_feasible_vectors']
  for r in c['balanced_certificates']:
   w=r['weights'];pair=r['balanced_pair_zero_based_ranks'];Z=counts(q['strict_up_masks'],w);N=counts(q['strict_up_masks'],w,pair)
   assert Z==r['extension_count']==r['denominator'] and N==r['numerator'] and Z<=3*N<=2*Z
   (i,a),(j,b)=pair;assert i!=j and not q['strict_up_masks'][i]>>j&1 and not q['strict_up_masks'][j]>>i&1
   num+=1;counts_n+=2
 assert num==D['total_filter_feasible_vectors']==22
 result={'status':'PASS','family_count':len(D['cores']),'balanced_pair_certificates':num,'independent_precedence_edge_counts':counts_n,'method':'Fraction matrix identities and complete bounded-grid reconstruction, followed by independent recursive linear-extension counts with one added precedence edge.'}
 (HERE/'family_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
