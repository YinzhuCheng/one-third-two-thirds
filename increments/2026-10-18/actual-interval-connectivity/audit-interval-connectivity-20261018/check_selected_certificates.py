"""Independent, bounded audit. Reads frozen results; recounts only three existing objects."""
import json
from math import comb
from itertools import combinations, permutations
from pathlib import Path
from collections import Counter
BASE=Path('/workspace/shared')
OUT=BASE/'audit-interval-connectivity-20261018'
B=BASE/'disconnected-balance-interval-test-20261018'
frozen=json.loads((B/'frozen_cases.json').read_text())
rows=json.loads((B/'all_counts.json').read_text())
certs=json.loads((B/'two_variation_certificates.json').read_text())
lengths=[(3,5),(4,7),(5,9),(7,10),(8,13),(10,15),(12,17),(14,20),(17,23),(20,27),(24,30),(27,31)]
ceil=lambda a,b:(a+b-1)//b

def gates(p,q):
    return [([ceil(p,5),ceil(4*q,5)],[ceil(4*p,5),ceil(q,5)]),
            ([0,ceil(3*q,4)],[ceil(3*p,4),0]),
            ([ceil(p,3),q],[p,ceil(q,3)]),
            ([1,q-1],[p-1,1]),([ceil(p,2),q],[p,0]),
            ([0,q],[p,ceil(q,2)]),
            ([ceil(p,4),ceil(3*q,4)],[ceil(3*p,4),ceil(q,4)]),
            ([ceil(p,3),ceil(2*q,3)],[ceil(2*p,3),ceil(q,3)])]

def expected_pairs(p,q):
    total=comb(p+q,p)
    candidates=[]
    for r in range(1,p+1):
      for s in range(1,q+1):
       if r!=s:
        k=r+s-1
        e=sum(comb(k,h)*comb(p+q-k,p-h) for h in range(max(r,k-q),min(p,k)+1))
        zone=0 if 3*(r+s)<=p+q else 1 if 3*(r+s)<=2*(p+q) else 2
        candidates.append((r,s,e,zone))
    used=[]
    for h in (1,2):
      key=lambda x:(abs(3*x[2]-h*total),x[0],x[1])
      for zone in range(3):
        pool=sorted((x for x in candidates if x[3]==zone and x[:2] not in used),key=key)
        take=pool[:2]
        if len(take)<2:
          take+=sorted((x for x in candidates if x[:2] not in used and x not in take),key=key)[:2-len(take)]
        used.extend(x[:2] for x in take)
    return used

assert len(frozen)==len(rows)==96
for i,((p,q),(y,z)) in enumerate(((pq,g) for pq in lengths for g in gates(*pq)),1):
    f=frozen[i-1]; r=rows[i-1]
    assert (f['case_index'],f['p'],f['q'],f['y'],f['z'])==(i,p,q,y,z)
    assert {k:r[k] for k in f}==f
    assert [(x['r'],x['s']) for x in f['pairs']]==expected_pairs(p,q)
    assert len({(x['r'],x['s']) for x in f['pairs']})==12
    assert y[0]<z[0] and y[1]>z[1]
assert len({(r['p'],r['q'],tuple(r['y']),tuple(r['z'])) for r in frozen})==96

# Check certificate algebra from saved coefficients, without recounting structures.
cert_out=[]
for c in certs:
    r=rows[c['case_index']-1]
    e=next(e for e in r['counts'] if [e['r'],e['s']]==c['pair'])
    t=r['total']; n=e['event']
    basis=([3*x-2*y for x,y in zip(n,t)] if c['side']=='H' else [y-3*x for x,y in zip(n,t)])
    a,b,d=basis
    poly=[d,2*b+3*d,2*(a+b+d)]
    A,B,C=poly; delta=B*B-4*A*C
    other=e['low' if c['side']=='H' else 'high']
    assert poly==c['polynomial']==e['high' if c['side']=='H' else 'low']
    assert delta==c['discriminant']<0
    assert all(x<0 for x in other)
    assert e['balanced']==c['balanced']
    assert e['balanced']==([[1,None]] if A<0 else [])
    cert_out.append(dict(case=c['case_index'],pair=c['pair'],side=c['side'],polynomial=poly,discriminant=delta,other_threshold_coefficients=other))
assert len(certs)==9

# Independently enumerate D words of the one previously counted case 28.
r=rows[27]; p,q=r['p'],r['q']; d=p+q
key=(7,9); total=[0,0,0]; event=[0,0,0]
for apos in combinations(range(d),p):
    aset=set(apos); bpos=[i for i in range(d) if i not in aset]
    ls=[]
    for a,b in (r['y'],r['z']):
        release=max(apos[a-1] if a else -1,bpos[b-1] if b else -1)
        ls.append(d-1-release)
    ly,lz=ls; v=(ly*lz+min(ly,lz),ly+lz,2)
    for i,x in enumerate(v): total[i]+=x
    if apos[key[0]-1]<bpos[key[1]-1]:
        for i,x in enumerate(v): event[i]+=x
saved=next(x for x in r['counts'] if (x['r'],x['s'])==key)
assert total==r['total'] and event==saved['event']
word_control=dict(case=28,D_words=comb(d,p),total=total,pair=key,event=event)

# Independent direct LE enumeration of the frozen smallest P_1, not window DP.
r=rows[0];p,q=r['p'],r['q']; names=[f'A{i}' for i in range(1,p+1)]+[f'B{i}' for i in range(1,q+1)]+['y','z','C']
pre={x:set() for x in names}
for prefix,n in [('A',p),('B',q)]:
    for i in range(2,n+1):pre[f'{prefix}{i}'].add(f'{prefix}{i-1}')
for x,gate in [('y',r['y']),('z',r['z'])]:
    for prefix,k in zip(['A','B'],gate):
        if k:pre[x].add(f'{prefix}{k}')
pre['C']={f'A{p}',f'B{q}'}
nt=0; ec=[0]*12; cols=[0,0]
def visit(w,remaining):
    global nt
    if not remaining:
        nt+=1; pos={x:i for i,x in enumerate(w)}
        for k,e in enumerate(r['counts']):ec[k]+=pos[f"A{e['r']}"]<pos[f"B{e['s']}"]
        cols[0]+=pos['C']<pos['y'];cols[1]+=pos['C']<pos['z']
        return
    placed=set(w)
    for x in remaining:
        if pre[x]<=placed:visit(w+[x],[y for y in remaining if y!=x])
visit([],names)
assert nt==r['total'][0]+2*r['total'][1]+3*r['total'][2]==812
for k,e in enumerate(r['counts']):assert ec[k]==e['event'][0]+2*e['event'][1]+3*e['event'][2]
assert cols==[237,275]
direct_control=dict(case=1,m=1,total=nt,event_counts=ec,C_before_y=cols[0],C_before_z=cols[1])

# Independent 5! enumeration of old case 8, using relations, not stored masks.
old=json.loads((BASE/'actual-external-pair-shapes-20261018/all_counts.json').read_text())[7]
names=old['names'];D=set(names[:old['d']]);I=set(names[old['d']:old['d']+2]);
t=[0,0,0]; events={('d0','d1'):[0,0,0],('d1','y'):[0,0,0],('y','z'):[0,0,0]}
for w in permutations(names):
    pos={x:i for i,x in enumerate(w)}
    if any(pos[x]>=pos[y] for x,y in old['relations']):continue
    last=max(pos[x] for x in D);K=sum(pos[x]>last for x in I)
    t[K]+=1
    for (x,y),v in events.items():v[K]+=pos[x]<pos[y]
assert t==old['total']==[5,8,12]
for pair,v in events.items():assert v==next(e['event'] for e in old['pairs'] if tuple(e['pair'])==pair)
old_control=dict(case=8,total=t,events={','.join(k):v for k,v in events.items()})

hist=Counter();baltypes=Counter();v2=[];nonmono=0
for r in rows:
    for e in r['counts']:
        hist[tuple(e['threshold_variations'])]+=1
        b=e['balanced']
        baltypes['empty' if not b else 'all' if b==[[1,None]] else 'tail' if b[-1][1] is None else 'bounded']+=1
        nonmono+=bool(e['difference_positive'] and e['difference_negative'])
        if max(e['threshold_variations'])==2:v2.append((r['case_index'],[e['r'],e['s']]))
assert len(v2)==9 and nonmono==69
assert baltypes==dict(empty=426,all=497,tail=135,bounded=94)
result=dict(frozen_structure_and_pair_selection='PASS; no actual-R recount of 96-case batch',certificates=cert_out,word_control=word_control,direct_control=direct_control,old_actual_control=old_control,saved_statistics=dict(variation_histogram={str(k):v for k,v in hist.items()},balance_types=dict(baltypes),nonmonotone=nonmono))
(OUT/'selected_certificate_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
print('PASS: bounded independent audit; no new structures or full-batch rerun')
# Recompute only algebraic diagnostics of the saved old 120-case records.
old_rows=json.loads((BASE/'actual-external-pair-shapes-20261018/all_counts.json').read_text())
def variation(v):
    s=[(x>0)-(x<0) for x in v if x]
    return sum(x!=y for x,y in zip(s,s[1:]))
old_hist=Counter();old_basis_two=[];nold=0
for r in old_rows:
    t=r['total']
    for e in r['pairs']:
        nold+=1;n=e['event']
        bs=([x-3*y for x,y in zip(t,n)],[3*y-2*x for x,y in zip(t,n)])
        shifted=[]
        for side,(A,B,C) in zip(['L','H'],bs):
            q=[C,2*B+5*C,2*A+4*B+6*C]
            shifted.append(variation(q))
            if variation([A,B,C])==2:
                delta=q[1]*q[1]-4*q[0]*q[2]
                assert variation(q)==0 and delta<0
                old_basis_two.append(dict(case=r['case_index'],pair=e['pair'],side=side,basis=[A,B,C],shifted=q,discriminant=delta))
        old_hist[tuple(shifted)]+=1
assert len(old_rows)==120 and nold==2255 and len(old_basis_two)==11
assert old_hist==Counter({(0,0):2113,(0,1):124,(1,0):16,(1,1):2})
result['old_saved_statistics']=dict(structures=120,pairs=nold,basis_V2_thresholds=len(old_basis_two),shifted_variation_histogram={str(k):v for k,v in old_hist.items()},V2_certificates=old_basis_two)
(OUT/'selected_certificate_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: old 120 records algebraic diagnostics; 11 basis-V2, all shifted-V0 and discriminant negative')
