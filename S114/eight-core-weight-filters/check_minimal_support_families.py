#!/usr/bin/env python3
"""Infinite-family exclusions via exact linear upper bounds, then finite ideal DP.
Only the port-forced blocks may vary; every other block is fixed to weight 1.
Uses no LP/float and no uniform quotient law.
"""
from fractions import Fraction as F
from pathlib import Path
import itertools,json
from validate_inflations import oracle
HERE=Path(__file__).parent

def inverse(M):
 n=len(M);A=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
 for k in range(n):
  p=next(i for i in range(k,n) if A[i][k]);A[k],A[p]=A[p],A[k]
  v=A[k][k];A[k]=[x/v for x in A[k]]
  for i in range(n):
   if i!=k:
    v=A[i][k];A[i]=[a-v*b for a,b in zip(A[i],A[k])]
 return [row[n:] for row in A]
def encoded(x):return [x.numerator,x.denominator]
def main():
 D=json.loads((HERE/'weight_filter_catalogue.json').read_text())['cores'];out=[]
 for q in D:
  Fidx=q['port_forced_nonsingleton_indices'];S=set(Fidx);rules={r['target']:r for r in q['rules']}
  A=[[2 if i==j else -1 if j in rules[i]['incomparable_indices'] else 0 for j in Fidx] for i in Fidx]
  b=[sum(j not in S for j in rules[i]['incomparable_indices'])-1 for i in Fidx]
  inv=inverse(A);assert all(x>=0 for row in inv for x in row)
  upper=[sum(a*c for a,c in zip(row,b)) for row in inv];floors=[x.numerator//x.denominator for x in upper]
  cases=[];cartesian=0
  R={(i,j) for i in range(8) for j in range(8) if q['strict_up_masks'][i]>>j&1}
  for vals in itertools.product(*(range(2,u+1) for u in floors)):
   cartesian+=1;w=[1]*8
   for i,v in zip(Fidx,vals):w[i]=v
   if not all(2*w[r['target']]<sum(w[j] for j in r['incomparable_indices']) for r in q['rules']):continue
   V,P,Z,N,states=oracle(R,w)
   balanced=[(a,b) for a in range(len(V)) for b in range(a+1,len(V)) if (a,b) not in P and (b,a) not in P and Z<=3*N[a][b]<=2*Z]
   assert balanced,(q['class_id'],w)
   a,c=balanced[0]
   cases.append({'weights':w,'extension_count':Z,'balanced_pair_zero_based_ranks':[V[a],V[c]],'numerator':N[a][c],'denominator':Z})
  row={'class_id':q['class_id'],'variable_indices':Fidx,'all_other_weights':1,'variable_lower_bound':2,'matrix':A,'rhs':b,'inverse_rational':[[encoded(x) for x in row] for row in inv],'upper_bounds_rational':[encoded(x) for x in upper],'upper_bounds_integer':floors,'cartesian_vectors':cartesian,'filter_feasible_vectors':len(cases),'balanced_certificates':cases,'additional_nonsingleton_clause':[i for i in range(8) if i not in S],'necessary_nonsingleton_count':len(S)+1}
  out.append(row);print(q['class_id'],Fidx,'upper',floors,'cases',len(cases),flush=True)
 result={'status':'PASS','theorem':'For every class C02-C18, a counterexample needs at least one nonsingleton block outside its port-forced set. This excludes an unbounded original weight family using exact finite bounds, not a finite-box extrapolation.','certificate_method':'Inverse matrices are exact and entrywise nonnegative; multiplying A*w<=b gives certified upper bounds. Every integer vector in the bounds passing all linear filters has an independently counted balanced pair.','total_filter_feasible_vectors':sum(q['filter_feasible_vectors'] for q in out),'maximum_checked_inflation_order':max(sum(c['weights']) for q in out for c in q['balanced_certificates']),'cores':out}
 (HERE/'minimal_support_family_certificates.json').write_text(json.dumps(result,indent=2)+'\n');print('TOTAL',result['total_filter_feasible_vectors'],'MAX_ORDER',result['maximum_checked_inflation_order'])
if __name__=='__main__':main()
