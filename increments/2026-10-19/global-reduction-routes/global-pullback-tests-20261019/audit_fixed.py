#!/usr/bin/env python3
"""Independent fixed-data checks; does not generate or scan any new posets."""
import json,gzip
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from collections import Counter
OUT=Path(__file__).resolve().parent
cases={c['id']:c for c in json.loads((OUT/'frozen_cases.json').read_text())}
counts={}
with gzip.open(OUT/'all_exact_counts.jsonl.gz','rt') as f:
    for line in f:
        c=json.loads(line);counts[(c['case'],c['m'])]=c
records=[]
with gzip.open(OUT/'control_records.jsonl.gz','rt') as f:
    for line in f:
        r=json.loads(line)
        if r['premise']:records.append(r)

def raw_data(case,m):
    C=[f'c{i+1}' for i in range(m)]; names=case['names']+C;ix={v:i for i,v in enumerate(names)}
    rel=case['strict_relations']+list(zip(C,C[1:]))+[(d,c) for d in case['D'] for c in C]+[(c,u) for c in C for u in case['U']]
    pred=[0]*len(names)
    for a,b in rel:pred[ix[b]]|=1<<ix[a]
    return names,pred

def extensions_count(pred,extra=None):
    pred=list(pred);n=len(pred);full=(1<<n)-1
    if extra is not None:a,b=extra;pred[b]|=1<<a
    # Independent bottom-up prefix count, not the production suffix numerator rule.
    layer={0:1}
    for depth in range(n):
        nxt={}
        for mask,num in layer.items():
            for i in range(n):
                bit=1<<i
                if not mask&bit and pred[i]&mask==pred[i]:nxt[mask|bit]=nxt.get(mask|bit,0)+num
        layer=nxt
    return layer.get(full,0)

def direct_all_pairs(pred):
    n=len(pred);full=(1<<n)-1;total=0;nums=[[0]*n for _ in range(n)]
    def visit(mask,order):
        nonlocal total
        if mask==full:
            total+=1
            for k,a in enumerate(order):
                for b in order[k+1:]:nums[a][b]+=1
            return
        for i in range(n):
            bit=1<<i
            if not mask&bit and pred[i]&mask==pred[i]:visit(mask|bit,order+[i])
    visit(0,[])
    return total,nums

selected=sorted({(r['case'],r['m']-d) for r in records for d in (0,1)})
audit={'distinct_fixed_models':len(selected),'all_pair_added_relation_checks':0,'direct_extension_models':[],'controls':[],'analytic_identity_checks':[]}
for cid,m in selected:
    c=counts[(cid,m)];names,pred=raw_data(cases[cid],m);assert names==c['names'];assert extensions_count(pred)==c['total']
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            n=extensions_count(pred,(i,j));assert n==c['numerators'][i][j],(cid,m,names[i],names[j],n,c['numerators'][i][j]);audit['all_pair_added_relation_checks']+=1
    if cid in ('F1-s4','F3-s4'):
        T,N=direct_all_pairs(pred);assert T==c['total'] and N==c['numerators'];audit['direct_extension_models'].append({'case':cid,'m':m,'total':T})

def p(c,a,b):return Fraction(c['numerators'][c['names'].index(a)][c['names'].index(b)],c['total'])
def side_eps(c,x,side):
    case=cases[c['case']]
    if x in case['D'] or x in case['U']:return Fraction(0)
    return p(c,'c1',x) if side=='L' else p(c,x,'c'+str(c['m']))

def topo_block(c,case,sides):
    names=c['names'];idx={x:i for i,x in enumerate(names)}
    L=set(case['D'])|{x for x,s in sides.items() if s=='L'};R=set(case['U'])|{x for x,s in sides.items() if s=='R'};C=set(c['C']);rank={x:0 if x in L else 1 if x in C else 2 for x in names}
    edges={x:set() for x in names};ind={x:0 for x in names}
    for a in names:
        for b in names:
            if a==b:continue
            if 3*c['numerators'][idx[a]][idx[b]]>2*c['total']:
                assert rank[a]<=rank[b],('backward strong edge',a,b)
                edges[a].add(b);ind[b]+=1
    order=[]
    while len(order)<len(names):
        avail=[x for x in names if ind[x]==0 and x not in order]
        if not avail:return None
        x=min(avail,key=lambda x:(rank[x],idx[x]));order.append(x)
        for y in edges[x]:ind[y]-=1
    assert [rank[x] for x in order]==sorted(rank.values())
    return order

for r in records:
    c=counts[(r['case'],r['m'])];q=counts[(r['case'],r['m']-1)];case=cases[r['case']]
    diag={'case':r['case'],'m':r['m'],'sides':r['sides'],'cross':[],'parent_balanced_blocks':dict(Counter(x[-1] for x in r['parent_balanced'])),'parent_balanced':r['parent_balanced'],'contiguous_strong_graph_extension':topo_block(c,case,r['sides'])}
    for a,b,N,T,n,t in r['eligible_cross']:
        ep=side_eps(c,a,'L')+side_eps(c,b,'R');eq=side_eps(q,a,'L')+side_eps(q,b,'R')
        assert 1-p(c,a,b)<=ep and 1-p(q,a,b)<=eq and eq<ep
        diag['cross'].append({'pair':[a,b],'parent':str(Fraction(N,T)),'short':str(Fraction(n,t)),'epsilon_sum_parent':str(ep),'epsilon_sum_short':str(eq),'short_budget_le_1_over_3':eq<=Fraction(1,3)})
    assert diag['contiguous_strong_graph_extension'] is not None
    audit['controls'].append(diag)

# Exact bivariate polynomial identities, monomials (power of m,power of s).
def add(a,b,coef=1):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,0)+coef*v
    return {k:v for k,v in out.items() if v}
def mul(a,b):
    out={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),0)+u*v
    return {k:v for k,v in out.items() if v}
def scale(a,k):return {i:v*k for i,v in a.items() if v*k}
m={(1,0):1};s={(0,1):1};one={(0,0):1};mp1=add(m,one);mp2=add(m,scale(one,2));sm1=add(add(s,m),one)
T=add(mul(sm1,sm1),mp1);Tm1=add(mul(add(s,m),add(s,m)),m)
minor=mul(mp1,mp2);minprev=mul(m,mp1)
delta=add(mul(minor,Tm1),mul(minprev,T),-1)
expected=scale(mul(mul(s,mp1),add(s,m)),2)
assert delta==expected
audit['analytic_identity_checks'].append('minority difference numerator = 2*s*(m+1)*(m+s)')
sidepoly=add(T,scale(mul(m,add(add(s,m),scale(one,2))),3),-1)
expected_side={(0,2):1,(1,1):-1,(0,1):2,(2,0):-2,(1,0):-3,(0,0):2};assert sidepoly==expected_side
audit['analytic_identity_checks'].append('T-3*m*(s+m+2)=s^2+(2-m)*s-2*m^2-3*m+2')
# Verify the displayed formulas against all already-frozen F1 counts, no new model.
for (cid,k),c in counts.items():
    if cases[cid]['family']!=1:continue
    z=cases[cid]['s'];den=(z+k+1)**2+k+1;assert c['total']==den
    assert p(c,'a','b')==1-Fraction((k+1)*(k+2),2*den)
    for j in range(1,k+1):
        assert p(c,f'c{j}','a')==Fraction((k-j+1)*(z+k+2),den)
        assert p(c,f'c{j}','b')==1-Fraction(j*(z+k+2),den)
audit['analytic_identity_checks'].append('full-gate closed formulas agree with all 96 already-frozen F1 exact models')
(OUT/'independent_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps({k:v for k,v in audit.items() if k!='controls'},indent=2))
