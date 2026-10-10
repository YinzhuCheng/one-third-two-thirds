#!/usr/bin/env python3
"""Bounded analytic-filter diagnostic, separate from exact endpoint rejection.
Every inequality comparison is an exact integer comparison. Proof status is
recorded in cone_audit.json; finite arithmetic is not a universal proof.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
from collections import Counter
import hashlib,json,time

NAMES=('rank_upper_T1_B0','rank_upper_T6_B5','top_lower_T0_T2','bottom_lower_B3_B6')

def filters(w):
    u,a,b,c,t,d,v=w
    topden=comb(a+b+t+v+u,u);bottomden=comb(d+c+t+u+v,v)
    bounds=((comb(b+t+v+u,u),topden),(comb(c+t+u+v,v),bottomden),
            (comb(a+b+u-1,u),topden),(comb(d+c+v-1,v),bottomden))
    passing=tuple(3*n>2*z if j<2 else 3*n<z for j,(n,z) in enumerate(bounds))
    return bounds,passing

def main():
    root=Path(__file__).resolve().parent;start=time.monotonic()
    p=json.loads((root/'census.json').read_text());v=json.loads((root/'verification.json').read_text())
    byweights={tuple(r['weights']):r for r in v['per_vector']}
    survivors=[];summaries=[];old=set(p['old_four_arrow_indices'])
    for r in p['records']:
        bounds,passing=filters(r['weights'])
        if all(passing):
            q=byweights[tuple(r['weights'])]
            survivors.append({'weights':r['weights'],'spine':r['spine'],'order':r['order'],
              'analytic_bounds':{name:{'numerator':n,'denominator':z,'reduced':str(Fraction(n,z))}
                                for name,(n,z) in zip(NAMES,bounds)},
              'failed_exact_forced_arrows':[p['arrows'][i] for i in r['failed_forced_arrow_indices']],
              'survives_old_four_exact':not old.intersection(r['failed_forced_arrow_indices']),
              'actual_delta':q['delta_reduced'],'actual_maximizing_pairs':q['maximizing_pairs'],
              'actual_balanced_pair_count':q['balanced_pair_count']})
    for m in range(1,p['scope_max_spine']+1):
        records=[r for r in p['records'] if max(r['spine'])<=m];alive=list(records);seq=[]
        standalone={name:sum(filters(r['weights'])[1][i] for r in records) for i,name in enumerate(NAMES)}
        for i,name in enumerate(NAMES):
            alive=[r for r in alive if filters(r['weights'])[1][i]]
            seq.append({'added_filter':name,'remaining':len(alive)})
        sub=[r for r in survivors if max(r['spine'])<=m]
        summaries.append({'max_spine':m,'starting_cone_vectors':len(records),'standalone_passes':standalone,
          'cumulative_passes':seq,'analytic_survivor_count':len(sub),
          'analytic_survivors_then_old_four_exact':[r['weights'] for r in sub if r['survives_old_four_exact']],
          'analytic_survivors_then_full_18_exact':[r['weights'] for r in sub if not r['failed_exact_forced_arrows']],
          'minimal_analytic_survivor':sub[0]['weights'] if sub else None,
          'survivors_grouped_by_spine':dict(Counter(','.join(map(str,r['spine'])) for r in sub))})
    out={'status':'EXACT_ARITHMETIC_PASS_PROOF_DEPENDENCIES_SEPARATE',
      'scope':'Same entire necessary cone with spine a,b,c,d in {1,2,3}; no larger search.',
      'base_census_sha256':hashlib.sha256((root/'census.json').read_bytes()).hexdigest(),
      'filter_order':NAMES,'summaries':summaries,'analytic_survivors':survivors,
      'elapsed_seconds':round(time.monotonic()-start,6),
      'interpretation':'Analytic survival establishes neither a counterexample nor an unresolved balance case. All these finite vectors already have actual labelled-DP balanced pairs and fail the full endpoint menu. The diagnostic identifies limitations of these particular universal inequalities.'}
    (root/'analytic_filters.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='analytic_survivors'},indent=2))
if __name__=='__main__':main()
