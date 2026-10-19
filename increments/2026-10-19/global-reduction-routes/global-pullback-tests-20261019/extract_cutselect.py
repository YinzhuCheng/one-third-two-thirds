#!/usr/bin/env python3
"""Read fixed data only. No new LE counting, models, lengths, or side-pair scans."""
from pathlib import Path
from fractions import Fraction
import gzip,json
from math import factorial,comb
OUT=Path(__file__).resolve().parent
cases={c['id']:c for c in json.loads((OUT/'frozen_cases.json').read_text())}
res=[]
with gzip.open(OUT/'control_records.jsonl.gz','rt') as f:
    for line in f:
        r=json.loads(line)
        if not r['premise']:continue
        c=cases[r['case']];s=c['s'];family=c['family'];T=r['parent_total'];m=r['m']
        if family<=4:
            h={1:1,2:factorial(s)**2,3:factorial(s-1)**2,4:comb(s,(s+1)//2)**2}[family]
            B=h*(s+1)**2;kind='exact';reason='L=D disjoint {a}; Rside={b} disjoint U'
            assert T==h*((s+m+1)**2+m+1)
        elif family==7:
            assert s==6 and m==2
            ed=comb(s,(s+1)//2)
            B=(ed*(s+1)*(s+2))**2;kind='upper_bound';reason='Drop d1<a2 and b2<u_s inside sides; each side becomes size-s D/U plus two isolated markers'
        else:raise AssertionError('Unexpected fixed S control')
        fbound=Fraction(B,T);assert fbound<Fraction(2,3)
        res.append({'case':c['id'],'m':m,'parent_total':T,'cut_count_or_upper_bound':B,'kind':kind,'f_or_upper_bound':str(fbound),'reason':reason,'could_reach_f_gt_2_over_3':False})
out={'models_newly_counted':0,'new_pair_numerators':0,'fixed_S_controls':len(res),'cut_select_threshold_covered':0,'controls':res}
(OUT/'cutselect_extraction.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
