#!/usr/bin/env python3
"""Audit proposal's grid kernel against enumerated categorical iid uniform samples.
For grid size Q each sample is assigned one of Q equal-probability bins.
Thresholds i/Q are bin boundaries. Ranks m+1 denote the deterministic endpoint 1.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import importlib.util,json
BASE=Path(__file__).resolve().parent
proposal=BASE.parent/'actual_fiber/test_exact_fiber_mtp2.py'
spec=importlib.util.spec_from_file_location('proposal',proposal);M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
Q=4;cases=0
for m in range(0,7):
    expected=Counter()
    for sample in product(range(Q),repeat=m):
        ranks=sorted(sample)+[Q]
        for p in range(1,m+2):
            for q in range(1,m+2):
                for i in range(Q+1):
                    for j in range(Q+1):
                        if ranks[p-1]>=i and ranks[q-1]>=j:expected[p,q,i,j]+=1
    for p in range(1,m+2):
        for q in range(1,m+2):
            for i in range(Q+1):
                for j in range(Q+1):
                    assert M.kernel(m,p,q,i,j,Q)==expected[p,q,i,j],(m,p,q,i,j)
                    cases+=1
result={'status':'PASS','m_range':[0,6],'all_rank_pairs':True,'grid_denominator':Q,'comparisons':cases,'method':'Enumerated Q^m iid uniform-bin tuples, with rank m+1 represented by deterministic endpoint 1. Includes thresholds 0,1 and rank coincidences.'}
(BASE/'kernel_boundary_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
