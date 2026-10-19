#!/usr/bin/env python3
from pathlib import Path
import json,gzip,time
from fractions import Fraction
from hashlib import sha256
from test_actual import *


def outside_closure(case):
    labels,edges=explicit(case,1)
    n=len(labels); idx={x:i for i,x in enumerate(labels)}; reach=[0]*n
    for a,b in edges: reach[idx[a]]|=1<<idx[b]
    for k in range(n):
        for i in range(n):
            if reach[i]>>k&1: reach[i]|=reach[k]
    outside=[x for x in labels if not x.startswith('c')]
    pairs=[[x,y] for x in outside for y in outside if reach[idx[x]]>>idx[y]&1]
    return outside,pairs

start=time.time(); full_manifest=[]; smallest=None; equal_labels={}; comparisons=0
controls2=0
for schema in (2,3,4,6):
    for kind in range(4):
        c=make_case(schema,kind,3,2,1); H,G,ids=central_arrays(c,3)
        assert length_counts(c,2,H,G,ids)==full_ideal_counts(c,2)
        controls2+=1
print('CLONE_MULTIPLICITY_CONTROLS',controls2,flush=True)
with gzip.open(ROOT/'all_exact_counts.jsonl.gz','wt') as out:
    for cid,case in enumerate(json.loads((ROOT/'manifest.json').read_text())):
        labels,rels=outside_closure(case)
        item={'case_id':cid,'parameters':case,'outside_labels':labels,'all_strict_outside_relations':rels,'central_chain_relations':'D < c_1 < ... < c_m < U; every x_j incomparable with every c_i'}
        full_manifest.append(item)
        fingerprint=json.dumps([labels,rels],sort_keys=True)
        equal_labels.setdefault(fingerprint,[]).append(cid)
        H,G,ids=central_arrays(case,max(MS)+1)
        for m in MS:
            z,N=length_counts(case,m,H,G,ids); zz,NN=length_counts(case,m+1,H,G,ids)
            out.write(json.dumps({'case_id':cid,'m':m,'total_m':str(z),'total_m1':str(zz),'numerators_m':[[str(x) for x in row] for row in N],'numerators_m1':[[str(x) for x in row] for row in NN]},separators=(',',':'))+'\n')
            d=None; witness=None
            for i in range(m):
                for x in range(case['t']):
                    aa=NN[i][x]*z-N[i][x]*zz; bb=N[i][x]*zz-NN[i+1][x]*z
                    if d is None or min(aa,bb)<d: d=min(aa,bb); witness=(i+1,x,'left' if aa<=bb else 'right')
            f=Fraction(d,z*zz)
            if smallest is None or f<smallest[0]:
                i,x,which=witness
                smallest=(f,{'case_id':cid,'parameters':case,'m':m,'i':i,'x':x,'which_gap':which,'gap':str(f),'gap_decimal':float(f),'total_m':str(z),'total_m1':str(zz),'numerator_i_m':str(N[i-1][x]),'numerator_i_m1':str(NN[i-1][x]),'numerator_ip1_m1':str(NN[i][x]),'cross_difference':str(d)})
            comparisons+=1
(ROOT/'all_actual_relations.json').write_text(json.dumps(full_manifest,indent=2))
(ROOT/'minimum_gap_certificate.json').write_text(json.dumps(smallest[1],indent=2))
summary=json.loads((ROOT/'summary.json').read_text()); summary['clone_multiplicity_independent_controls']=controls2; summary['literal_labeled_relation_distinct_instances']=len(equal_labels); summary['outside_parameter_instances']=summary.pop('actual_posets'); summary['certificate_write_seconds']=time.time()-start
(ROOT/'summary.json').write_text(json.dumps(summary,indent=2))
checks={p.name:sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.iterdir()) if p.is_file() and p.name not in ('SHA256SUMS.json',)}
(ROOT/'SHA256SUMS.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(summary),flush=True); print('MINIMUM_GAP',json.dumps(smallest[1]),flush=True)
