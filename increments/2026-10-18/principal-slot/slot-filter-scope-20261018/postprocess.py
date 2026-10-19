#!/usr/bin/env python3
"""Read saved exact moments; classify filters; do not recount any LE or rerun DP."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json
P=Path('/workspace/shared/large-slot-moment-stress-20261018')
O=Path(__file__).resolve().parent
objects={o['name']:o for o in json.loads((P/'objects.json').read_text())['objects']}
rows=[json.loads(s) for s in (P/'raw_results.jsonl').read_text().splitlines()]
cases={r['name']:r for r in rows if r['type']=='case'}
pairs=[r for r in rows if r['type']=='pair']
labels=['empty_filters','both_principal','only_smaller_mean_side_principal','only_larger_mean_side_principal','both_nonprincipal']

def structure(obj, case):
    lengths=obj['lengths'];offs=[];n=0
    for length in lengths:offs.append(n);n+=length
    edges=[(o+i,o+i+1) for o,L in zip(offs,lengths) for i in range(L-1)]
    edges += [(offs[a]+p,offs[b]+q) for a,p,b,q in obj['cross']]
    reach=[0]*n
    for a,b in edges:reach[a]|=1<<b
    for z in range(n):
        for a in range(n):
            if reach[a]>>z&1:reach[a]|=reach[z]
    assert all(not(reach[v]>>v&1) for v in range(n))
    result=[]
    for saved,threshold in zip(case['filters'],obj['filters']):
        assert saved['threshold']==threshold
        mask=sum(((1<<L)-(1<<t))<<off for t,L,off in zip(threshold,lengths,offs))
        members=[v for v in range(n) if mask>>v&1]
        assert all(not(reach[v]&~mask) for v in members) # actual upset
        mins=[v for v in members if all(not(reach[u]>>v&1) for u in members)]
        principal=len(mins)==1
        assert principal==any((reach[v]|(1<<v))==mask for v in members)
        coords=[[a,v-offs[a]] for v in mins for a,L in enumerate(lengths) if offs[a]<=v<offs[a]+L]
        result.append(dict(threshold=threshold,empty=not mask,principal=principal,minima=coords,minimum_count=len(mins)))
    assert len(result)==len(case['filters'])==len(obj['filters'])
    return result

filters={name:structure(objects[name],case) for name,case in cases.items()}
stats={label:Counter() for label in labels};by_object=defaultdict(Counter)
extrema={};pair_labels=[];equal_mean_one_principal=[]

def record(row,label):
    case=cases[row['case']];obj=objects[row['case']];K=int(case['le'])
    a,b,c,d=(int(row[k]) for k in ('sum_Ry','sum_Rz','sum_product','sum_min'));m=min(a,b)
    rec=dict(case=row['case'],n=case['n'],pair_indices=[row['i'],row['j']],source_pair_class=row['class'],structure_label=label,lengths=obj['lengths'],cross=obj['cross'],le=str(K),Sy=filters[row['case']][row['i']],Sz=filters[row['case']][row['j']],sum_Ry=str(a),sum_Rz=str(b),sum_product=str(c),sum_min=str(d),sum_Ry2=row['sum_Ry2'],sum_Rz2=row['sum_Rz2'],target_gap_num=row['target_gap_num'],covariance_gap_num=row['covariance_gap_num'],r=str(Q(a,K)),s=str(Q(b,K)),N=str(Q(c+d,K)),covariance=str(Q(c*K-a*b,K*K)),target_gap=str(Q(int(row['target_gap_num']),K*K)),covariance_gap=str(Q(int(row['covariance_gap_num']),K*K)))
    if m:
        rec.update(mean_ratio=str(Q(max(a,b),m)),target_pressure=str(Q((c+d)*K-a*b,m*m+2*m*K)),target_relative_gap=str(Q(int(row['target_gap_num']),m*m+2*m*K)),covariance_pressure=str(Q(c*K-a*b,m*m+m*K)),covariance_relative_gap=str(Q(int(row['covariance_gap_num']),m*m+m*K)))
    return rec

def consider(key,value,row,label,maximize=False):
    if key not in extrema or (value>extrema[key][0] if maximize else value<extrema[key][0]):
        extrema[key]=(value,record(row,label),1)
    elif value==extrema[key][0]:
        old=extrema[key];extrema[key]=(old[0],old[1],old[2]+1)

for row in pairs:
    name=row['case'];y,z=(filters[name][row[k]] for k in ('i','j'))
    a,b,c,d=(int(row[k]) for k in ('sum_Ry','sum_Rz','sum_product','sum_min'))
    K=int(cases[name]['le']);m=min(a,b)
    assert a==int(cases[name]['filters'][row['i']]['sum_R']) and b==int(cases[name]['filters'][row['j']]['sum_R'])
    tn=int(row['target_gap_num']);cn=int(row['covariance_gap_num'])
    assert tn==a*b+m*m+2*m*K-(c+d)*K
    assert cn==a*b+m*m+m*K-c*K
    assert tn>=0 and cn>=0
    covered=(y['principal'] and z['principal']) or (y['principal'] and a<=b) or (z['principal'] and b<=a)
    if y['empty'] or z['empty']:label='empty_filters'
    elif y['principal'] and z['principal']:label='both_principal'
    elif (y['principal'] and a<=b) or (z['principal'] and b<=a):label='only_smaller_mean_side_principal'
    elif y['principal'] or z['principal']:label='only_larger_mean_side_principal'
    else:label='both_nonprincipal'
    s=stats[label];s['pairs']+=1;s['positive_means' if m else 'zero_mean']+=1
    s['matches_pending_T_proof_hypothesis']+=covered
    s['same_filter_pairs']+=(row['i']==row['j'])
    s['distinct_nonempty_pairs']+=(row['i']!=row['j'] and not(y['empty'] or z['empty']))
    s['positive_distinct_nonempty_pairs']+=(bool(m) and row['i']!=row['j'] and not(y['empty'] or z['empty']))
    if not m and max(a,b):s['one_zero_mean_infinite_ratio']+=1
    if not m and not max(a,b):s['both_zero_mean_undefined_ratio']+=1
    if a==b:s['equal_means']+=1
    if a==b and y['principal']!=z['principal']:
        s['equal_means_exactly_one_principal']+=1
        equal_mean_one_principal.append(record(row,label))
    by_object[name][label]+=1
    pair_labels.append([name,row['i'],row['j'],label,covered])
    if not m:continue
    scopes=[label,'all']
    if not(y['empty'] or z['empty']) and row['i']!=row['j']:scopes.append('distinct_nonempty')
    if not(y['empty'] or z['empty']) and not covered:
        scopes.append('outside_pending_T_proof_nonempty')
        if row['i']!=row['j']:scopes.append('outside_pending_T_proof_distinct_nonempty')
    if label=='both_nonprincipal' and row['i']!=row['j']:scopes.append('both_nonprincipal_distinct')
    for scope in scopes:
        for kind,val in [('target_relative_gap',Q(tn,m*m+2*m*K)),('covariance_relative_gap',Q(cn,m*m+m*K)),('target_absolute_gap',Q(tn,K*K)),('covariance_absolute_gap',Q(cn,K*K))]:
            consider(scope+'/'+kind,val,row,label)
        consider(scope+'/mean_ratio',Q(max(a,b),m),row,label,True)

small=json.loads(Path('/workspace/shared/actual-slot-covariance-20261018/results.json').read_text())
small_selected={}
for key,row in small['closest'].items():
    n=row['n'];reach=[0]*n
    for a,b in row['covers']:reach[a]|=1<<b
    for v in range(n):
        for a in range(n):
            if reach[a]>>v&1:reach[a]|=reach[v]
    mins=[[v for v in row[side] if all(not(reach[u]>>v&1) for u in row[side])] for side in ['Sy','Sz']]
    py,pz=[len(x)==1 for x in mins];a=int(row['sum_Ry']);b=int(row['sum_Rz']);m=min(a,b);K=int(row['le'])
    label=('empty_filters' if not row['Sy'] or not row['Sz'] else 'both_principal' if py and pz else 'only_smaller_mean_side_principal' if (py and a<=b) or (pz and b<=a) else 'only_larger_mean_side_principal' if py or pz else 'both_nonprincipal')
    small_selected[key]=dict(source_key=key,name=row['name'],structure_label=label,minima=mins,Sy=row['Sy'],Sz=row['Sz'],covers=row['covers'],r=row['r'],s=row['s'],target_relative_gap=str(Q(int(row['target_gap_num']),m*m+2*m*K)) if m else None,covariance_relative_gap=str(Q(int(row['covariance_gap_num']),m*m+m*K)) if m else None)
summary=dict(status='Structural postprocessing only; pending T proof not independently reviewed; no proof claim for stronger covariance candidate.',source=str(P),pair_count=len(pairs),objects_started=len(cases),n_range=[min(c['n'] for c in cases.values()),max(c['n'] for c in cases.values())],classification_precedence=labels,by_structure={k:dict(v) for k,v in stats.items()},by_object={k:dict(v) for k,v in by_object.items()},equal_mean_exactly_one_principal=equal_mean_one_principal,pending_T_hypothesis_matches=sum(x['matches_pending_T_proof_hypothesis'] for x in stats.values()),small_batch_missing='results.json stores case totals and selected extrema, but no complete tested filter pools, pairwise exact means, or moment matrices; its 280123 pairs cannot be structurally reclassified without forbidden recounting.',small_batch_pairs=small['pair_count'],small_batch_saved_selected_extrema=small_selected,extrema={k:dict(value=str(v[0]),ties=v[2],record=v[1]) for k,v in extrema.items()})
(O/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
(O/'pair_labels.json').write_text(json.dumps(dict(columns=['case','i','j','structure_label','matches_pending_T_hypothesis'],rows=pair_labels),ensure_ascii=False,separators=(',',':'))+'\n')
print(json.dumps({k:summary[k] for k in ['pair_count','objects_started','by_structure','pending_T_hypothesis_matches']},ensure_ascii=False,indent=2))
for scope in labels+['distinct_nonempty','outside_pending_T_proof_nonempty']:
    print('\n'+scope)
    for kind in ['target_relative_gap','covariance_relative_gap','mean_ratio']:
        x=summary['extrema'].get(scope+'/'+kind)
        if x:
            r=x['record'];print(kind,x['value'],float(Q(x['value'])),r['case'],r['pair_indices'],r['Sy']['threshold'],r['Sz']['threshold'],r['Sy']['minima'],r['Sz']['minima'],'ties',x['ties'])
