#!/usr/bin/env python3
"""Exact finite checks of domain boundary and threshold arithmetic.
Universal monotonicity arguments are in THEOREM.md; these checks supplement them.
"""
from math import comb,prod
from pathlib import Path
import json
P=Path(__file__).parent

def check(x,*why):
 if not x:raise RuntimeError(why)

def main():
 count=0;thresholds=[];bounds=[]
 for a,U,M in ((1,3,3),(2,9,19),(3,29,90)):
  at=3*prod(M+i for i in range(a+1));rhs=prod(M+U+i for i in range(a+1))
  bad=3*prod(M+1+i for i in range(a+1));brhs=prod(M+1+U+i for i in range(a+1))
  check(at<rhs and bad>=brhs,'inner_cap',a)
  bounds.append({'outer':a,'port_cap':U,'inner_cap':M,'allowed_boundary':[at,rhs],'disallowed_boundary':[bad,brhs]})
  for u in range(2,U+1):
   first=None
   for s in range(349):
    num=prod(s+r for r in range(1,a+1));den=prod(s+u+r for r in range(1,a+1))
    bn=comb(s+u,u);bd=comb(a+s+u,u)
    check(num*bd==den*bn,'product_binomial_identity',a,u,s)
    passing=3*bn>2*bd
    if passing and first is None:first=s
    if first is not None:check(passing,'threshold_monotonicity',a,u,s)
    count+=1
   check(first is not None,'threshold_exists',a,u)
   thresholds.append([a,u,first])
 result={'status':'PASS','product_binomial_identities':count,'inner_cap_boundaries':bounds,'upper_thresholds':thresholds,'largest_inner_product_argument':123,'integer_domain_maximum_order':348}
 (P/'bounds_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
