#!/usr/bin/env python3
"""Exact chain-inflation pilot; standard Python only.

Expanded elements are (base label, 1-based chain index). Every cross-block
pair is recorded, including base-comparable pairs. No witnesses are selected
before the complete pair-probability table is built.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def closure(n, edges):
    rel = set(edges)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i,k) in rel and (k,j) in rel:
                    rel.add((i,j))
    assert not any((i,i) in rel for i in range(n))
    return rel

def update(n, edges, lengths):
    rel = closure(n, edges)
    x,y = next((x,y) for x in range(n) for y in range(x+1,n)
               if (x,y) not in rel and (y,x) not in rel)
    out = list(lengths)
    out[x] *= 2
    out[y] *= 3
    return tuple(out), (x,y)

def exact(n, edges, lengths):
    lengths=tuple(lengths)
    rel=closure(n,edges)
    pred=[tuple(x for x in range(n) if (x,y) in rel) for y in range(n)]
    zero=(0,)*n
    def children(s):
        for v in range(n):
            if s[v]<lengths[v] and all(s[u]==lengths[u] for u in pred[v]):
                t=list(s); t[v]+=1
                yield v,tuple(t)
    @lru_cache(None)
    def suffix(s):
        if s==lengths: return 1
        return sum(suffix(t) for _,t in children(s))
    denominator=suffix(zero)
    prefix={zero:1}
    all_states=sorted(product(*(range(m+1) for m in lengths)),key=sum)
    for s in all_states:
        if s not in prefix: continue
        for _,t in children(s):
            prefix[t]=prefix.get(t,0)+prefix[s]
    assert prefix[lengths]==denominator
    # Count an extension exactly once, when its first element of the pair is placed.
    nums={ (u,i,v,j):0
          for u in range(n) for v in range(u+1,n)
          for i in range(1,lengths[u]+1) for j in range(1,lengths[v]+1)}
    for s, pref in prefix.items():
        for v,t in children(s):
            i=s[v]+1
            weight=pref*suffix(t)
            for w in range(v+1,n):
                for j in range(s[w]+1,lengths[w]+1):
                    nums[v,i,w,j]+=weight
    all_pairs=[]
    delta=Fraction(0)
    witnesses=[]
    for (u,i,v,j),numerator in nums.items():
        comparable=((u,v) in rel or (v,u) in rel)
        p=Fraction(numerator,denominator)
        row={'u':[u,i],'v':[v,j], 'numerator':numerator,
             'denominator':denominator,'reduced':str(p),'comparable':comparable}
        if not comparable:
            balance=min(p,1-p)
            row['balance']=str(balance)
            if balance>delta: delta=balance; witnesses=[]
            if balance==delta: witnesses.append({'u':[u,i],'v':[v,j],
                                               'p':str(p),'balance':str(balance)})
        else:
            assert p==(1 if (u,v) in rel else 0)
        all_pairs.append(row)
    return {'lengths':lengths,'extensions':denominator,
            'reachable_states':len(prefix),'delta':str(delta),
            'witnesses':witnesses,'all_cross_block_pairs':all_pairs}

def two_chain_formula(a,b,i,j):
    # A_i precedes B_j iff at least i A's occur in the first i+j-1 positions.
    t=i+j-1
    numerator=sum(comb(t,r)*comb(a+b-t,a-r)
                  for r in range(max(i,t-b),min(a,t)+1)
                  if 0<=a-r<=a+b-t)
    return Fraction(numerator,comb(a+b,a))

def main():
    specs=[]
    for lengths in [(1,1),(1,2),(1,3),(1,4),(1,10),(1,20),(2,1),(20,1),(2,3),(3,2)]:
        specs.append(('two_independent_chains',2,[],lengths))
    specs += [
        ('asymmetric_three_block',3,[(0,2)],(1,2,1)),
        ('asymmetric_three_block_extreme',3,[(0,2)],(1,10,2)),
        ('four_block_N',4,[(0,2),(0,3),(1,3)],(1,2,1,1)),
        ('four_block_N_unequal',4,[(0,2),(0,3),(1,3)],(2,1,3,2)),
    ]
    results=[]
    for name,n,edges,lengths in specs:
        new,selected=update(n,edges,lengths)
        before=exact(n,edges,lengths)
        after=exact(n,edges,new)
        if n==2:
            for table in [before,after]:
                a,b=table['lengths']
                assert table['extensions']==comb(a+b,a)
                for row in table['all_cross_block_pairs']:
                    assert Fraction(row['numerator'],row['denominator']) == two_chain_formula(a,b,row['u'][1],row['v'][1])
        item={'name':name,'base_n':n,'base_relations':sorted(closure(n,edges)),
              'selected_blocks':selected,'before':before,'after':after,
              'monotonicity_holds':Fraction(after['delta'])<=Fraction(before['delta'])}
        results.append(item)
        print(name, lengths,'->',new,'E',before['extensions'],'->',after['extensions'],
              'delta',before['delta'],'->',after['delta'],'holds',item['monotonicity_holds'])
    output=ROOT/'exact_results.json'
    output.write_text(json.dumps(results,indent=2)+'\n')
    # Full first counterexample table, with unreduced extension counts.
    case=next(x for x in results if x['name']=='two_independent_chains' and x['before']['lengths']==(1,2))
    lines=['pair,count(A_i < B_j),extensions,probability,balance']
    for row in case['after']['all_cross_block_pairs']:
        lines.append(f"A{row['u'][1]}:B{row['v'][1]},{row['numerator']},{row['denominator']},{row['reduced']},{row['balance']}")
    (ROOT/'counterexample_all_pairs.csv').write_text('\n'.join(lines)+'\n')
    n_case=next(x for x in results if x['name']=='four_block_N')
    for stage in ['before','after']:
        lines=['u_block,u_index,v_block,v_index,numerator,denominator,probability,balance,comparable']
        for row in n_case[stage]['all_cross_block_pairs']:
            lines.append(','.join(map(str,[*row['u'],*row['v'],row['numerator'],row['denominator'],row['reduced'],row.get('balance',''),row['comparable']])))
        (ROOT/f'N_{stage}_all_pairs.csv').write_text('\n'.join(lines)+'\n')
    print('Wrote',output)

if __name__=='__main__': main()
