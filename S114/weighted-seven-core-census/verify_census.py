#!/usr/bin/env python3
"""Independent-representation arithmetic checks, not an independent peer audit.

Reads census.py only for the separate actual-label DP and data conventions.
Every cone vector receives all-actual-pair counts, independently of the chain
prefix DP that generated its 18 endpoint numerators.
"""
from pathlib import Path
from itertools import product
from math import comb
from fractions import Fraction
import hashlib, json, time
import census


def middle_count(w):
    u,a,b,c,t,d,v=w;n=0
    for i in range(u+1):
        for j in range(t+1):
            h=1 if j==0 else (comb(b+j-2,j) if b>=2 else 0)
            n+=h*comb(a+b+i+j-1,i)*comb(u-i+c+t-j,t-j)*comb(u-i+c+t-j+d+v,v)
    return n


def brute_cone(spine):
    a,b,c,d=spine
    # A deliberately different, weaker bounding box from algebraic elimination:
    # 2t <= a+d+3b+3c-4. Independent direct loops impose all four conditions.
    T=(a+d+3*b+3*c-4)//2
    out=set()
    for t in range(1,T+1):
        A=a+b+t;B=c+d+t
        for u in range(2,(2*A+B-3)//3+1):
            for v in range(2,(A+2*B-3)//3+1):
                if 2*u<A+v and 2*v<B+u and 2*t<b+c+u and 2*t<b+c+v:
                    out.add((u,a,b,c,t,d,v))
    return out


def main():
    root=Path(__file__).resolve().parent
    inp=root/'census.json';data=json.loads(inp.read_text());start=time.monotonic()
    expected=set();maxsp=data['scope_max_spine']
    for spine in product(range(1,maxsp+1),repeat=4):
        expected |= brute_cone(spine)
    observed={tuple(r['weights']) for r in data['records']}
    assert len(observed)==len(data['records']) and expected==observed
    rows=[];min_delta=Fraction(1,1);minimizers=[];totalpairs=balancedpairs=0;middlechecks=0
    for k,r in enumerate(data['records']):
        w=tuple(r['weights']);q=census.actual_label_dp(w);z=q['extensions']
        assert z==r['extensions']
        assert list(q['forced_endpoint_numerators'].values())==r['forced_endpoint_numerators']
        assert middle_count(w)==q['forced_endpoint_numerators']['B2<B4']
        assert middle_count(census.dual_weights(w))==q['forced_endpoint_numerators']['T4<T3']
        middlechecks+=2
        delta=Fraction(q['delta_numerator'],z)
        assert delta>=Fraction(1,3)
        totalpairs+=len(q['incomparable_pairs']);balancedpairs+=len(q['balanced_pairs'])
        row={'weights':w,'extensions':z,'delta_reduced':str(delta),'incomparable_pair_count':len(q['incomparable_pairs']),
             'balanced_pair_count':len(q['balanced_pairs']),'maximizing_pairs':q['maximizing_pairs']}
        rows.append(row)
        if delta<min_delta:min_delta=delta;minimizers=[row]
        elif delta==min_delta:minimizers.append(row)
        if k%250==0:print('verified',k,'elapsed',round(time.monotonic()-start,3),flush=True)
    out={'status':'PASS','independent_peer_audit':False,
      'description':'Full-scope independent state-representation DP and direct cone enumeration; this is author verification, not external peer audit.',
      'source_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'spine_max':maxsp,
      'cone_vectors':len(observed),'cone_enumeration_set_equality':True,
      'actual_label_denominator_comparisons':len(rows),'actual_label_endpoint_comparisons':18*len(rows),
      'middle_binomial_formula_comparisons':middlechecks,'actual_label_incomparable_pair_counts':totalpairs,
      'actual_balanced_pairs_counted':balancedpairs,'minimum_delta':str(min_delta),'minimum_delta_cases':minimizers,
      'elapsed_seconds':round(time.monotonic()-start,6),'per_vector':rows,
      'cone_proof_status':'See cone_audit.json; not supplied by arithmetic checks.'}
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='per_vector'},indent=2))

if __name__=='__main__':main()
