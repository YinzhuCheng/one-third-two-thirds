#!/usr/bin/env python3
from independent_labeled_extensions import audit, ROOT
from fractions import Fraction
import json

out=[]
for a,b in [(3,2),(5,4),(7,6),(9,8),(8,4)]:
    row={'before':audit([], [a,b]),'children':[audit([], [a-1,b]),audit([], [a,b-1])]}
    expected=Fraction(b,a+b) if a==b+1 else Fraction(14,33)
    assert Fraction(row['before']['delta'])==expected
    assert all(Fraction(s['delta'])>expected for s in row['children'])
    if a==b+1: assert all(s['delta']=='1/2' for s in row['children'])
    else: assert [s['delta'] for s in row['children']]==['31/66','27/55']
    out.append(row)
    print((a,b),row['before']['extensions'],row['before']['delta'],[(s['lengths'],s['extensions'],s['delta']) for s in row['children']],flush=True)
(ROOT/'requested_cases_full_labeled_counts.json').write_text(json.dumps(out,indent=2)+'\n')
