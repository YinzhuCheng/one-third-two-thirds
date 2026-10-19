"""Independent fixed controls for two already frozen cases; never invokes producer DP."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
from math import comb
import json

ROOT=Path(__file__).parent
SRC=Path(__file__).resolve().parent.parent / 'actual-excursion-targets-20261019'
rows=json.loads((SRC/'all_counts.json').read_text())
frozen=json.loads((SRC/'frozen_cases.json').read_text())
assert len(rows)==len(frozen)==24
assert sum(len(r['counts']) for r in rows)==252
assert sum(len(r['pairs']) for r in frozen)==264
assert all([r[k] for k in f]==list(f.values()) for r,f in zip(rows,frozen))

# Independently rederive each threshold's concavity and integer positive-island criterion.
fail=Counter(); passing=[]; strict=[]; B_hist=Counter()
for row in rows:
    a,b,c=row['total']; assert c>0
    for e in row['counts']:
        aa,bb,cc=e['event']; assert 0<=aa<=a and 0<=bb<=b and 0<=cc<=c
        actual_pass=False
        for side,(A,B,C) in [('low',(a-3*aa,b-3*bb,c-3*cc)),('high',(3*aa-2*a,3*bb-2*b,3*cc-2*c))]:
            if C>=0: continue
            g=-C; z=max(2,B//g)
            f2=2*A+4*B-6*g
            fz=2*A+2*B*z-g*z*(z+1)
            name='middle_budget' if B<=3*g else 'initial_bad' if f2>0 else 'vertex_amplitude' if fz<=0 else 'passes'
            fail[name]+=1
            old=e['excursions'][side]
            assert (g,z,f2,fz,name)==(old['g'],old['z_star'],old['F2_twice'],old['Fmax_twice'],old['failure'] or 'passes')
            if B>3*g:
                strict.append((row['case_index'],e['pair_index'],side,A,z,f2,fz))
                assert fz>f2>0 and A>0
            if f2<=0<fz:
                passing.append((row['case_index'],e['pair_index'],side));actual_pass=True
        assert actual_pass==(len(e['balanced'])==2)
        B_hist[len(e['balanced'])]+=1
assert fail=={'middle_budget':290,'initial_bad':18}
assert len(strict)==18 and min(x[4] for x in strict)==6 and max(x[4] for x in strict)==17
assert not passing

# Full predecessor-mask ideal DP on the complete P_1. Uses actual unweighted LE.
# Distinct from the producer's two-side stopping/window gluing algorithm.
def build(case,m,event=None):
    ds,us=case['D_sizes'],case['U_reverse_sizes']
    D=[('D',a,j) for a,n in enumerate(ds) for j in range(1,n+1)]
    U=[('U',a,j) for a,n in enumerate(us) for j in range(1,n+1)]
    I=[('I',i) for i in range(2)]; C=[('C',j) for j in range(m)]
    names=D+I+C+U; pos={x:i for i,x in enumerate(names)}; pred=[0]*len(names)
    def edge(x,y): pred[pos[y]]|=1<<pos[x]
    for a,n in enumerate(ds):
        for j in range(1,n):edge(('D',a,j),('D',a,j+1))
    for a,n in enumerate(us):
        for j in range(1,n):edge(('U',a,j+1),('U',a,j))
    for s,t in case['D_bridges']:edge(('D',*s),('D',*t))
    for s,t in case['U_reverse_bridges']:edge(('U',*t),('U',*s))
    for d in D:
        for u in U:edge(d,u)
        for c in C:edge(d,c)
    for c in C:
        for u in U:edge(c,u)
    for j in range(m-1):edge(C[j],C[j+1])
    for i,g in enumerate(case['D_gate_raw']):
        for a,n in enumerate(g):
            for j in range(1,n+1):edge(('D',a,j),('I',i))
    for i,g in enumerate(case['U_reverse_gate_raw']):
        for a,n in enumerate(g):
            for j in range(1,n+1):edge(('I',i),('U',a,j))
    if case['I_chain']:edge(I[0],I[1])
    if event:
        kind=event['kind']; s,t=event['source'],event['target']
        if kind=='II':edge(('I',s),('I',t))
        elif kind=='DI':edge(('D',*s),('I',t))
        else:raise ValueError(kind)
    full=(1<<len(names))-1
    @lru_cache(None)
    def count(done):
        if done==full:return 1
        total=0
        for i,p in enumerate(pred):
            if not(done>>i&1) and p&done==p: total+=count(done|(1<<i))
        return total
    v=count(0)
    return v,count.cache_info().currsize

def evalpoly(abc,m):return sum(v*comb(m+j,j) for j,v in enumerate(abc))
control=[]
for ci,pi in [(1,11),(2,7)]:
    row=rows[ci-1];e=next(x for x in row['counts'] if x['pair_index']==pi)
    T,states=build(row,1)
    N,estates=build(row,1,e)
    assert T==evalpoly(row['total'],1)
    assert N==evalpoly(e['event'],1)
    control.append(dict(case_index=ci,pair_index=pi,m=1,total=T,event=N,total_states=states,event_states=estates,window_total=row['total'],window_event=e['event']))

# Exact reported onset of the case1 II interval; tails are covered by the concave-island exclusion.
r=rows[0];e=next(x for x in r['counts'] if x['kind']=='II')
for m,expected_balanced in [(1,False),(5,False),(17,False),(18,True),(19,True)]:
    T=evalpoly(r['total'],m);N=evalpoly(e['event'],m)
    assert (T<=3*N<=2*T)==expected_balanced

out={'checks':'PASS','structures':24,'counted_pairs':252,'concave_failures':dict(fail),'strict_middle_count':18,'strict_middle_vertices':[min(x[4] for x in strict),max(x[4] for x in strict)],'balanced_component_histogram_from_saved_intervals':dict(B_hist),'actual_uniform_full_poset_controls':control}
(ROOT/'actual_controls.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
