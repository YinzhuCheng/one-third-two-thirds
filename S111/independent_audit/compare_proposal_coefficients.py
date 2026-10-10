#!/usr/bin/env python3
import json
from pathlib import Path
B=Path(__file__).resolve().parent
A=json.loads((B.parent/'actual_fiber/all_small_mtp2_certificates.json').read_text())
C=json.loads((B/'small_minimality_full_coefficients.json').read_text())
def canonical(record,polynomials):
    h=tuple(sorted(tuple(x) for x in record['histogram']))
    transpose=tuple(sorted((q,p,k) for p,q,k in h))
    if h>transpose:polynomials=polynomials[::-1]
    return ((record['m'],min(h,transpose)),tuple(tuple(sorted(tuple(x) for x in poly)) for poly in polynomials))
def checked_dict(pairs):
    result={}
    for key,value in pairs:
        if key in result:assert result[key]==value
        result[key]=value
    return result
a=checked_dict(canonical(r,r['cross_polynomials']) for r in A)
c=checked_dict(canonical(r,[x['delta_terms'] for x in r['certificate']]) for r in C)
assert a==c
result={'status':'PASS','proposal_records':len(A),'independent_records':len(C),'canonical_histograms_up_to_transpose':len(a),'all_exact_cross_polynomial_coefficients_match':True}
(B/'proposal_coefficient_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
