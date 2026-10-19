#!/usr/bin/env python3
"""Label only saved pairs, exact saved moments, and finite saved poset relations.
No new poset/filter/pair enumeration; no linear extension count or DP; no hashes.
"""
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction as Q
import json
P=Path('/workspace/shared/large-slot-moment-stress-20261018')
S=Path('/workspace/shared/slot-filter-scope-20261018')
O=Path(__file__).resolve().parent
objects={x['name']:x for x in json.loads((P/'objects.json').read_text())['objects']}
raw=[json.loads(x) for x in (P/'raw_results.jsonl').read_text().splitlines()]
cases={x['name']:x for x in raw if x['type']=='case'}
pairs=[x for x in raw if x['type']=='pair']
old=json.loads((S/'pair_labels.json').read_text())
oldlabels={(x[0],x[1],x[2]):dict(zip(old['columns'],x)) for x in old['rows']}
assert len(oldlabels)==len(pairs)==5073

meta={}
for name,case in cases.items():
    obj=objects[name]; lengths=obj['lengths'];offs=[];n=0
    for L in lengths:offs.append(n);n+=L
    edges=[(off+i,off+i+1) for off,L in zip(offs,lengths) for i in range(L-1)]
    edges += [(offs[a]+p,offs[b]+q) for a,p,b,q in obj['cross']]
    reach=[0]*n
    for a,b in edges:reach[a]|=1<<b
    for v in range(n):
        for a in range(n):
            if reach[a]>>v&1:reach[a]|=reach[v]
    # Connected components of the saved defining relations equal comparability components.
    parent=list(range(n))
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    for v,w in edges:
        rv,rw=find(v),find(w)
        if rv!=rw:parent[rw]=rv
    components=defaultdict(list)
    for v in range(n):components[find(v)].append(v)
    chain_components=[]
    for comp in components.values():
        if all(v==w or (reach[v]>>w&1) or (reach[w]>>v&1) for v in comp for w in comp):
            order=sorted(comp,key=lambda v:sum(bool(reach[w]>>v&1) for w in comp))
            assert all(reach[v]>>w&1 for pos,v in enumerate(order) for w in order[pos+1:])
            cm=sum(1<<v for v in comp)
            chain_components.append(dict(size=len(comp),mask=str(cm),order_flat_indices=order,order_coordinates=[[a,v-offs[a]] for v in order for a,L in enumerate(lengths) if offs[a]<=v<offs[a]+L]))
    filters=[]
    for idx,(threshold,saved) in enumerate(zip(obj['filters'],case['filters'])):
        assert threshold==saved['threshold']
        mask=sum(((1<<L)-(1<<t))<<off for t,L,off in zip(threshold,lengths,offs))
        members=[v for v in range(n) if mask>>v&1]
        assert all(not(reach[v]&~mask) for v in members)
        mins=[v for v in members if all(not(reach[u]>>v&1) for u in members)]
        coords=lambda vs:[[a,v-offs[a]] for v in vs for a,L in enumerate(lengths) if offs[a]<=v<offs[a]+L]
        # Independence needs only all saved defining edges; closure gives a second check.
        independent=all(bool(mask>>a&1)==bool(mask>>b&1) for a,b in edges)
        independent_closure=all(not(reach[a]&~mask) if mask>>a&1 else not(reach[a]&mask) for a in range(n))
        assert independent==independent_closure
        filters.append(dict(index=idx,threshold=threshold,mask=str(mask),size=len(members),empty=not mask,principal=len(mins)==1,minima=coords(mins),independent_block=independent,complement_size=n-len(members)))
    meta[name]=dict(n=n,lengths=lengths,cross=obj['cross'],le=case['le'],chain_components=chain_components,filters=filters)

counts=Counter(); overlaps=Counter();by_case=defaultdict(Counter);out=[];extrema={}
flag_names=['principal_T_reviewed','independent_block_nested_reviewed_TC','diagonal_nonempty_TC','empty_filter_TC','zero_mean_TC','chain_component_suffix_reviewed_TC']

def actual_filter(name,i):
    f=meta[name]['filters'][i]
    # Threshold and full chain lengths specify every actual member; expand coordinates for extrema.
    f=dict(f);f['members']=[[a,p] for a,(t,L) in enumerate(zip(f['threshold'],meta[name]['lengths'])) for p in range(t,L)]
    return f

def record(row,labels):
    name=row['case'];K=int(cases[name]['le']);a,b,c,d=[int(row[x]) for x in ['sum_Ry','sum_Rz','sum_product','sum_min']];m=min(a,b)
    return dict(case=name,pair_indices=[row['i'],row['j']],source_pair_class=row['class'],labels=labels,lengths=meta[name]['lengths'],cross=meta[name]['cross'],le=str(K),Sy=actual_filter(name,row['i']),Sz=actual_filter(name,row['j']),sum_Ry=str(a),sum_Rz=str(b),sum_product=str(c),sum_min=str(d),sum_Ry2=row['sum_Ry2'],sum_Rz2=row['sum_Rz2'],r=str(Q(a,K)),s=str(Q(b,K)),N=str(Q(c+d,K)),covariance=str(Q(c*K-a*b,K*K)),T_gap_num=row['target_gap_num'],C_gap_num=row['covariance_gap_num'],T_gap=str(Q(int(row['target_gap_num']),K*K)),C_gap=str(Q(int(row['covariance_gap_num']),K*K)),T_pressure=str(Q((c+d)*K-a*b,m*m+2*m*K)) if m else None,T_relative_gap=str(Q(int(row['target_gap_num']),m*m+2*m*K)) if m else None,C_pressure=str(Q(c*K-a*b,m*m+m*K)) if m else None,C_relative_gap=str(Q(int(row['covariance_gap_num']),m*m+m*K)) if m else None)

def consider(scope,row,labels):
    name=row['case'];K=int(cases[name]['le']);a=int(row['sum_Ry']);b=int(row['sum_Rz']);m=min(a,b)
    if not m:return
    for kind,den in [('T',m*m+2*m*K),('C',m*m+m*K)]:
        val=Q(int(row['target_gap_num' if kind=='T' else 'covariance_gap_num']),den)
        key=scope+'/'+kind+'_relative_gap'
        if key not in extrema or val<Q(extrema[key]['value']):extrema[key]=dict(value=str(val),ties=1,records=[record(row,labels)])
        elif val==Q(extrema[key]['value']):extrema[key]['ties']+=1;extrema[key]['records'].append(record(row,labels))

for row in pairs:
    name=row['case']; i=row['i'];j=row['j'];K=int(cases[name]['le']);old=oldlabels[name,i,j]
    y,z=[meta[name]['filters'][idx] for idx in [i,j]];ym,zm=[int(f['mask']) for f in [y,z]]
    a,b,c,d=[int(row[x]) for x in ['sum_Ry','sum_Rz','sum_product','sum_min']];m=min(a,b)
    assert a==int(cases[name]['filters'][i]['sum_R']) and b==int(cases[name]['filters'][j]['sum_R'])
    assert int(row['target_gap_num'])==a*b+m*m+2*m*K-(c+d)*K
    assert int(row['covariance_gap_num'])==a*b+m*m+m*K-c*K
    ycontainsz=(ym&zm)==zm; zcontainsy=(ym&zm)==ym; same=ym==zm
    nonnested=not(ycontainsz or zcontainsy)
    # Sy=V and nonempty Sz subset V, or swapped. W is allowed to be empty.
    orientations=[]
    if zm and ycontainsz and y['independent_block']:
        orientations.append(dict(larger_filter_side='y',a=y['complement_size'],b=y['size'],smaller_filter_size=z['size']))
    if ym and zcontainsy and z['independent_block']:
        orientations.append(dict(larger_filter_side='z',a=z['complement_size'],b=z['size'],smaller_filter_size=y['size']))
    chain_suffix_witnesses=[]
    for ci,comp in enumerate(meta[name]['chain_components']):
        if comp['size']==meta[name]['n']:continue # audited actual theorem requires nonempty V
        cm=int(comp['mask']);outside=((1<<meta[name]['n'])-1)^cm
        if (ym&outside)!=outside or (zm&outside)!=outside:continue
        ky=comp['size']-(ym&cm).bit_count();kz=comp['size']-(zm&cm).bit_count()
        assert ym&cm==sum(1<<v for v in comp['order_flat_indices'][ky:])
        assert zm&cm==sum(1<<v for v in comp['order_flat_indices'][kz:])
        chain_suffix_witnesses.append(dict(chain_component_index=ci,a=comp['size'],V_size=meta[name]['n']-comp['size'],k_y=ky,k_z=kz,chain_order_coordinates=comp['order_coordinates']))
    flags=dict(principal_T_reviewed=bool(old['matches_pending_T_hypothesis']),independent_block_nested_reviewed_TC=bool(orientations),diagonal_nonempty_TC=bool(same and ym),empty_filter_TC=bool(not ym or not zm),zero_mean_TC=not m,chain_component_suffix_reviewed_TC=bool(chain_suffix_witnesses))
    assert flags['principal_T_reviewed']==((y['principal'] and z['principal']) or (y['principal'] and a<=b) or (z['principal'] and b<=a))
    if flags['zero_mean_TC']:assert c==d==0
    if not ym:assert a==meta[name]['n']*K and c==meta[name]['n']*b and d==b
    if not zm:assert b==meta[name]['n']*K and c==meta[name]['n']*a and d==a
    proved_TC=flags['diagonal_nonempty_TC'] or flags['empty_filter_TC'] or flags['zero_mean_TC']
    pre_NBU_T=proved_TC or flags['principal_T_reviewed'] or flags['independent_block_nested_reviewed_TC']
    pre_NBU_TC=proved_TC or flags['independent_block_nested_reviewed_TC']
    pending_TC=pre_NBU_TC or flags['chain_component_suffix_reviewed_TC']
    all_T=pre_NBU_T or flags['chain_component_suffix_reviewed_TC']
    reviewed_T=all_T
    labels=dict(**flags,independent_block_orientations=orientations,chain_suffix_witnesses=chain_suffix_witnesses,T_union_before_NBU=pre_NBU_T,TC_union_before_NBU=pre_NBU_TC,same_filter=same,nonempty=bool(ym and zm),positive_means=bool(m),nested=not nonnested,nonnested=nonnested,T_union_including_pending=all_T,TC_union_including_pending=pending_TC,T_reviewed_or_elementary=reviewed_T,TC_CP18_or_elementary=proved_TC,T_union_final=all_T,TC_union_final=pending_TC,TC_reviewed_or_elementary=pending_TC)
    out.append(dict(case=name,i=i,j=j,principal_structure_label=old['structure_label'],**labels))
    counts['all']+=1;counts['nonnested']+=nonnested;counts['nested']+=not nonnested
    for k,v in flags.items():counts[k]+=v
    for key in ['T_union_including_pending','TC_union_including_pending','T_reviewed_or_elementary','TC_CP18_or_elementary','T_union_before_NBU','TC_union_before_NBU','T_union_final','TC_union_final','TC_reviewed_or_elementary']:
        counts[key]+=labels[key];counts['outside_'+key]+=not labels[key]
    counts['independent_a0']+=any(x['a']==0 for x in orientations)
    counts['independent_a1']+=any(x['a']==1 for x in orientations)
    counts['independent_a_gt1']+=any(x['a']>1 for x in orientations)
    sig='|'.join(k for k in flag_names if flags[k]) or 'none'
    overlaps[sig]+=1
    for key in ['all','T_union_including_pending','TC_union_including_pending','T_union_before_NBU','TC_union_before_NBU','chain_component_suffix_reviewed_TC','T_union_final','TC_union_final']:
        by_case[name][key]+=key=='all' or labels[key]
    for scope,ok in [('all',True),('outside_T_union',not all_T),('outside_TC_union',not pending_TC),('outside_reviewed_T',not reviewed_T),('outside_T_union_nonnested',not all_T and nonnested),('outside_T_union_nested',not all_T and not nonnested),('outside_TC_union_nonnested',not pending_TC and nonnested)]:
        if ok:consider(scope,row,labels)
    if not all_T:
        counts['outside_T_union_nonnested' if nonnested else 'outside_T_union_nested']+=1
        counts['outside_T_union_positive_means']+=bool(m)
        counts['outside_T_union_nonempty']+=bool(ym and zm)
        counts['outside_T_union_distinct']+=not same
        by_case[name]['outside_T_union']+=1
        by_case[name]['outside_T_union_nonnested' if nonnested else 'outside_T_union_nested']+=1
    if not pending_TC:counts['outside_TC_union_nonnested' if nonnested else 'outside_TC_union_nested']+=1
    counts['new_T_coverage_by_independent_block']+=not (proved_TC or flags['principal_T_reviewed']) and flags['independent_block_nested_reviewed_TC']
    counts['new_TC_coverage_by_independent_block']+=not proved_TC and flags['independent_block_nested_reviewed_TC']
    counts['new_T_coverage_by_NBU']+=not pre_NBU_T and flags['chain_component_suffix_reviewed_TC']
    counts['new_TC_coverage_by_NBU']+=not pre_NBU_TC and flags['chain_component_suffix_reviewed_TC']
    by_case[name]['new_T_coverage_by_NBU']+=not pre_NBU_T and flags['chain_component_suffix_reviewed_TC']
    by_case[name]['new_TC_coverage_by_NBU']+=not pre_NBU_TC and flags['chain_component_suffix_reviewed_TC']

summary=dict(reviewed_independent_block_source='/workspace/shared/audit-slot-shortening-extensions-20261018/REVIEW.md section B PASS',NBU_status='Reviewed PASS in /workspace/shared/audit-nbu-prefix-20261018/REVIEW.md; final coverage stops after this mechanism',status='Saved-data labels only. Principal T is treated as reviewed per parent task. General independent-block nested mechanism is reviewed PASS per parent task; chain-component suffix NBU mechanism is reviewed PASS; CP1.8 diagonal and empty/zero-mean elementary degeneracies cover T and C. Never infer C from principal T.',pair_count=len(pairs),case_count=len(cases),source_files=[str(P/'objects.json'),str(P/'raw_results.jsonl'),str(S/'pair_labels.json')],counts=dict(counts),exclusive_flag_combinations=dict(overlaps),by_case={k:dict(v) for k,v in by_case.items()},extrema=extrema,proof_status=dict(principal_T_reviewed='T only, per parent task; source labels originally used pending wording',independent_block_nested_reviewed_TC='Reviewed PASS per parent task; arbitrary internal W/V posets',diagonal_nonempty_TC='CP1.8 previously proved; T and C',empty_filter_TC='Elementary exact deterministic-slot proof; T and C',zero_mean_TC='Elementary nonnegative-zero-expectation proof; T and C',chain_component_suffix_reviewed_TC='Reviewed PASS in audit-nbu-prefix-20261018/REVIEW.md; U=C_a disjoint union nonempty V; both filters are chain suffix union all V'),scope='Read saved defining relations, filters and exact pair moments; no new posets, filters, pairs, linear extensions or DP; no hash calculation.')
(O/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
# Small archival form: exact records retain full reconstructive thresholds/relations,
# but omit coordinate dumps and large decimal masks.
compact=json.loads(json.dumps(summary))
for item in compact['extrema'].values():
    for rec in item['records']:
        for side in ['Sy','Sz']:
            rec[side].pop('members',None);rec[side].pop('mask',None)
        for witness in rec['labels'].get('chain_suffix_witnesses',[]):
            witness.pop('chain_order_coordinates',None)
(O/'summary_compact.json').write_text(json.dumps(compact,ensure_ascii=False,indent=2)+'\n')

(O/'pair_labels.json').write_text(json.dumps(dict(schema_version=1,flag_names=flag_names,rows=out),ensure_ascii=False,separators=(',',':'))+'\n')
(O/'filter_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,separators=(',',':'))+'\n')
print(json.dumps(summary['counts'],ensure_ascii=False,indent=2))
for key,val in extrema.items():
    if key.startswith('outside'):
        row=val['records'][0]
        print(key, val['value'], float(Q(val['value'])), 'ties',val['ties'],row['case'],row['pair_indices'],row['Sy']['threshold'],row['Sz']['threshold'],'nonnested',row['labels']['nonnested'])
