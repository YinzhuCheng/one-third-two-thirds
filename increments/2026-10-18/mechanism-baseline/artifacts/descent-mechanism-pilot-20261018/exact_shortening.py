#!/usr/bin/env python3
"""Exact, original-label one-block shortening on Q = the two-point antichain.

No floating point and no sampling. Every incomparable pair is counted.
The shortened poset deletes the LAST label in its selected chain; all remaining
labels keep their names. Within-chain pairs are deterministic and excluded from
delta. This script does not search for counterexamples to the 1/3--2/3 conjecture.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, isqrt
import csv
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

@lru_cache(None)
def pair_counts(a,b):
    assert a>=1 and b>=1
    E=comb(a+b,a)
    # At A_r, exactly k B labels have already appeared. Prefix and suffix counts.
    C=tuple(tuple(sum(comb(r+k-1,k)*comb(a+b-r-k,a-r)
                          for k in range(s))
                  for s in range(1,b+1)) for r in range(1,a+1))
    assert all(0 < n < E for row in C for n in row)
    return E,C

@lru_cache(None)
def delta(a,b):
    E,C=pair_counts(a,b)
    M=max(min(n,E-n) for row in C for n in row)
    return Fraction(M,E)

def record(a,b,full=True):
    E,C=pair_counts(a,b)
    d=delta(a,b)
    best=[{'A':r,'B':s,'count_A_before_B':n,'denominator':E}
          for r,row in enumerate(C,1) for s,n in enumerate(row,1)
          if Fraction(min(n,E-n),E)==d]
    out={'quotient':'two-point antichain','lengths':[a,b],
         'extension_count':E,'delta':str(d),'maximizing_pairs':best,
         'label_convention':'A1<...<Aa and B1<...<Bb; delete the last label of the selected chain'}
    if full:out['all_incomparable_pair_counts_A_before_B']=[list(x) for x in C]
    return out

def hypergeometric_check(a,b):
    E,C=pair_counts(a,b)
    for r,row in enumerate(C,1):
      for s,n in enumerate(row,1):
        t=r+s-1
        p=Fraction(sum(comb(a,k)*comb(b,t-k)
                       for k in range(max(r,t-b),min(a,t)+1)),comb(a+b,t))
        assert p==Fraction(n,E),(a,b,r,s,p,n,E)

def word_check(a,b):
    E,C=pair_counts(a,b)
    observed=[[0]*b for _ in range(a)]
    count=0
    for AA in combinations(range(a+b),a):
      count+=1
      aset=set(AA)
      BB=[i for i in range(a+b) if i not in aset]
      for r,x in enumerate(AA):
        for s,y in enumerate(BB):observed[r][s]+=x<y
    assert count==E and tuple(map(tuple,observed))==C,(a,b)

def b2_delta_formula(a):
    D=(a+1)*(a+2)
    h=min(abs(2*t*(t+1)-D) for t in range(1,a+1))
    return Fraction(1,2)-Fraction(h,2*D),h

def pell_solutions(last_power=7):
    # (x+u sqrt(8)) = (3+sqrt(8))^j, a=(x-3)/2.
    x,u=1,0
    for j in range(1,last_power+1):
      x,u=3*x+8*u,x+3*u
      a=(x-3)//2
      if a>=2:yield j,a,u

def main():
    word_cases=0
    for a in range(1,14):
      for b in range(1,a+1):
        if a+b<=14:
          word_check(a,b);word_cases+=1
    for a in range(1,31):
      for b in range(1,a+1):hypergeometric_check(a,b)
    for a in range(2,2001):
      assert b2_delta_formula(a)[0]==delta(a,2)
    rows=[]
    for a in range(2,31):
      for b in range(2,a+1):
        d,da,db=delta(a,b),delta(a-1,b),delta(a,b-1)
        if da>d and db>d:
          rows.append({'a':a,'b':b,'delta':str(d),'after_shrink_A':str(da),
                       'after_shrink_B':str(db),
                       'witness_after_A':record(a-1,b,False)['maximizing_pairs'],
                       'witness_after_B':record(a,b-1,False)['maximizing_pairs']})
    with (ROOT/'local_minima_A2_lengths_2_to_30.json').open('w') as f:json.dump(rows,f,indent=2)
    with (ROOT/'local_minima_A2_lengths_2_to_30.csv').open('w') as f:
      w=csv.DictWriter(f,fieldnames=['a','b','delta','after_shrink_A','after_shrink_B'])
      w.writeheader();w.writerows({k:r[k] for k in w.fieldnames} for r in rows)
    cases=[(3,2),(2,2),(3,1),(8,4),(7,4),(8,3),(7,2),(6,2),(7,1),
           (48,2),(47,2),(48,1),(287,2),(286,2),(287,1),
           (1680,2),(1679,2),(1680,1)]
    with (ROOT/'exact_pair_certificates.json').open('w') as f:
      json.dump([record(a,b) for a,b in cases],f,indent=2)
    pell=[]
    # Large cases are certified by the closed formulas, not populated in the
    # quadratic all-pair cache. Small cases are checked directly above.
    for j,a,u in pell_solutions(9):
      D=(a+1)*(a+2)
      assert D==2*u*u and u<a+1
      d=Fraction(u-1,2*u)
      da=1-Fraction(u*(u-1),a*(a+1))
      db=Fraction((a+1)//2,a+1)
      assert da-d==Fraction(a+1-u,u*a)>0
      assert db>d
      pell.append({'power':j,'a':a,'b':2,'u':u,'E':u*u,'delta':str(d),
                   'E_after_A':a*(a+1)//2,'delta_after_A':str(da),
                   'E_after_B':a+1,'delta_after_B':str(db)})
    with (ROOT/'pell_family_certificates.json').open('w') as f:json.dump(pell,f,indent=2)
    summary={'word_enumeration_verified_cases':word_cases,
             'hypergeometric_verified_cases':465,
             'b2_formula_verified_a_range':[2,2000],
             'finite_scan_quotient':'two-point antichain',
             'finite_scan_domain':'2 <= b <= a <= 30',
             'finite_scan_objects':435,'strict_local_minima':len(rows),
             'even_even_strict_local_minima':sum(r['a']%2==r['b']%2==0 for r in rows),
             'note':'These are finite exact local-mechanism data, not evidence about a delta<1/3 condition.'}
    with (ROOT/'verification_summary.json').open('w') as f:json.dump(summary,f,indent=2)
    print(json.dumps(summary,indent=2))
    print('Wrote exact all-label certificates, local-minimum list, Pell family.')

if __name__=='__main__':main()
