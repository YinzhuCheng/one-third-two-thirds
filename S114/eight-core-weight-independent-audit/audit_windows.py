#!/usr/bin/env python3
"""Direct outside-extension mixture audit for the insertion lemma.

For each core and each distinguished block, all other weights are 1 and the
distinguished weight takes values 1,2,4. Enumerate the outside extensions
literally and use the exact conditional binomial event count. Compare with
independent occupancy DP, explicitly observing the after-window case.
"""
from collections import Counter
from fractions import Fraction
from math import comb
import json
from audit import ROOT,read,structure,all_pair_counts

def extensions(vertices,D):
    def f(word,left):
        if not left:
            yield word
        for v in sorted(left):
            if not D[v]&left:
                yield from f(word+(v,),left-{v})
    return f((),set(vertices))

def main():
    counts=Counter();examples={}
    for q in read('input_cores.json'):
        up=q['strict_up_masks'];U,D,I,chain=structure(up)
        for i in range(8):
            outside=list(extensions(set(range(8))-{i},D))
            for length in (1,2,4):
                w=[1]*8;w[i]=length
                V,Z,N,states=all_pair_counts(up,w);idx={v:k for k,v in enumerate(V)}
                denominator=0;numerator={j:0 for j in I[i] if D[i]<=D[j]}
                naive={j:Fraction() for j in numerator};ways_seen=set()
                for sigma in outside:
                    pos={v:k for k,v in enumerate(sigma)}
                    L=max((pos[k] for k in D[i]),default=-1)
                    R=min((pos[k] for k in U[i]),default=7)
                    assert L<R
                    h=R-L-1;ways=comb(h+length,length)
                    assert h<=sum(w[k] for k in I[i])
                    denominator+=ways;ways_seen.add(ways)
                    counts['outside_extension_fibers']+=1
                    for j in numerator:
                        assert pos[j]>L
                        if pos[j]>=R:
                            good=ways;case='after_window'
                        else:
                            rank=pos[j]-L
                            good=ways-comb(length+h-rank,length);case='inside_window'
                        assert good*(length+h)>=length*ways
                        numerator[j]+=good;naive[j]+=Fraction(good,ways)
                        counts[case]+=1
                        if case not in examples:
                            examples[case]=dict(class_id=q['class_id'],weights=w,target=i,witness=j,
                                outside_extension=sigma,left_boundary=L,right_boundary=R,window_size=h,
                                conditional_numerator=good,conditional_denominator=ways)
                assert denominator==Z
                for j,num in numerator.items():
                    assert num==N[idx[i,0]][idx[j,0]]
                    counts['exact_mixture_comparisons']+=1
                    uniform=naive[j]/len(outside);actual=Fraction(num,Z)
                    if uniform!=actual and 'nonuniform_outside_law' not in examples:
                        examples['nonuniform_outside_law']=dict(class_id=q['class_id'],weights=w,target=i,witness=j,
                            outside_extension_count=len(outside),insertion_multiplicities=sorted(ways_seen),
                            incorrect_uniform_outside_probability=[uniform.numerator,uniform.denominator],
                            actual_reweighted_probability=[actual.numerator,actual.denominator])
                counts['inflations']+=1
    assert set(examples)=={'after_window','inside_window','nonuniform_outside_law'}
    result=dict(status='PASS',counts=dict(counts),examples=examples)
    (ROOT/'window_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
