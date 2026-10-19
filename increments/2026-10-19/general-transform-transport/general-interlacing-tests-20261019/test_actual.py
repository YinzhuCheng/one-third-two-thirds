#!/usr/bin/env python3
"""Own exact actual-poset test. No external mathematical code is executed."""
from itertools import product
from functools import lru_cache
from fractions import Fraction
from math import factorial
import json, time, hashlib
from pathlib import Path
ROOT=Path(__file__).parent
MS=(1,3,11,47,191,767)
RATIOS=((3,3),(23,1),(1,23))

def order_edges(t,kind):
    if kind==0: return []
    if kind==1: return [(x,x+1) for x in range(t-1)]
    if kind==2: return [(x,x+1) if x%2==0 else (x+1,x) for x in range(t-1)]
    return [(x,x+2) for x in range(t-2)]

def make_case(schema,kind,t,a,b):
    I=order_edges(t,kind)
    # Each side group is a chain or a labeled antichain of exchangeable clones.
    if schema in (0,5): dg=[('chain',a),('chain',b)]; ug=dg.copy(); de=[]; ue=[]
    elif schema==1: dg=[('anti',a),('anti',b)]; ug=dg.copy(); de=[(0,1)]; ue=de.copy()
    elif schema==2: dg=[('anti',a),('anti',b)]; ug=dg.copy(); de=[]; ue=[]
    elif schema==3: dg=[('chain',a),('anti',b)]; ug=dg.copy(); de=[]; ue=[]
    elif schema==4: dg=[('anti',a),('chain',1),('anti',b)]; ug=dg.copy(); de=[(0,1),(1,2)]; ue=de.copy()
    else: dg=[('anti',a),('chain',1)]; ug=[('anti',b),('chain',1)]; de=[]; ue=[]
    dc=[]; uc=[]
    for x in range(t):
        if schema==0:
            dc.append([a*x//max(1,t-1), b*((2*x+1)%t)//max(1,t-1)])
            uc.append([a*((x+1)%t)//max(1,t-1), b*(t-1-x)//max(1,t-1)])
        elif schema==1:
            lev=x%3; levu=(2*x+1)%3
            dc.append([a if lev>=1 else 0,b if lev>=2 else 0])
            uc.append([a if levu>=1 else 0,b if levu>=2 else 0])
        elif schema==2:
            pat=((0,0),(1,0),(0,1),(1,1))[x%4]
            patu=((1,1),(0,1),(1,0),(0,0))[(2*x+1)%4]
            dc.append([a*pat[0],b*pat[1]])
            uc.append([a*patu[0],b*patu[1]])
        elif schema==3:
            dc.append([a*x//max(1,t-1),b*(x%2)])
            uc.append([a*((2*x+1)%t)//max(1,t-1),b*((x+1)%2)])
        elif schema==4:
            lev=x%4; levu=(2*x+1)%4
            dc.append([a if lev>=1 else 0,1 if lev>=2 else 0,b if lev>=3 else 0])
            uc.append([a if levu>=1 else 0,1 if levu>=2 else 0,b if levu>=3 else 0])
        elif schema==5:
            dc.append([a*x//max(1,t-1),b*(t-1-x)//max(1,t-1)])
            uc.append([a*((x+1)%t)//max(1,t-1),b*((t-x)%t)//max(1,t-1)])
        else:
            dp=((0,0),(0,1),(1,0),(1,1),(0,1),(1,0))[x]
            up=((1,1),(0,1),(1,0),(0,0),(1,0),(0,1))[x]
            dc.append([a*dp[0],dp[1]])
            uc.append([b*up[0],up[1]])
    return {'schema':schema,'I_kind':kind,'t':t,'ratio':[a,b], 'D_groups':dg,'U_groups':ug,'D_edges':de,'U_edges':ue,'I_edges':I,'D_cuts':dc,'U_cuts':uc}

def ideal_data(case):
    t=case['t']; preds=[0]*t
    for a,b in case['I_edges']: preds[b]|=1<<a
    for _ in range(t):
        for b in range(t):
            for a in range(t):
                if preds[b]>>a&1: preds[b]|=preds[a]
    ideals=[s for s in range(1<<t) if all(not(s>>x&1) or preds[x]&s==preds[x] for x in range(t))]
    lowers={s:[s^(1<<x) for x in range(t) if s>>x&1 and (s^(1<<x)) in ideals] for s in ideals}
    uppers={s:[s|(1<<x) for x in range(t) if not(s>>x&1) and preds[x]&s==preds[x]] for s in ideals}
    return preds,ideals,lowers,uppers

def side_counts(case, left, preds):
    t=case['t']; groups=case['D_groups' if left else 'U_groups']; edges=case['D_edges' if left else 'U_edges']; cuts=case['D_cuts' if left else 'U_cuts']
    sizes=tuple(g[1] for g in groups); ng=len(groups); full=(1<<t)-1
    gp=[[] for _ in groups]
    for a,b in edges: gp[b].append(a)
    states=list(product(*(range(n+1) for n in sizes)))
    valid=lambda cc: all(not cc[g] or all(cc[h]==sizes[h] for h in gp[g]) for g in range(ng))
    states=[cc for cc in states if valid(cc)]
    if left:
        dp={(tuple(0 for _ in groups),0):1}
        for cc in states:
            for mask in range(1<<t):
                val=dp.get((cc,mask),0)
                if not val: continue
                for x in range(t):
                    if not(mask>>x&1) and preds[x]&mask==preds[x] and all(cc[g]>=cuts[x][g] for g in range(ng)):
                        key=(cc,mask|(1<<x)); dp[key]=dp.get(key,0)+val
                for g,(typ,n) in enumerate(groups):
                    if cc[g]<n and all(cc[h]==sizes[h] for h in gp[g]):
                        nn=list(cc); nn[g]+=1; key=(tuple(nn),mask)
                        mult=n-cc[g] if typ=='anti' else 1
                        dp[key]=dp.get(key,0)+val*mult
        return [dp.get((sizes,s),0) for s in range(1<<t)]
    @lru_cache(None)
    def rec(cc,mask):
        if cc==sizes and mask==full: return 1
        ans=0
        for x in range(t):
            if not(mask>>x&1) and preds[x]&mask==preds[x]: ans+=rec(cc,mask|(1<<x))
        for g,(typ,n) in enumerate(groups):
            if cc[g]<n and all(cc[h]==sizes[h] for h in gp[g]) and all(cc[g]<cuts[x][g] or mask>>x&1 for x in range(t)):
                nn=list(cc); nn[g]+=1
                ans+=(n-cc[g] if typ=='anti' else 1)*rec(tuple(nn),mask)
        return ans
    return [rec(tuple(0 for _ in groups),s) if all(not(s>>x&1) or preds[x]&s==preds[x] for x in range(t)) else 0 for s in range(1<<t)]

def central_arrays(case, maxm):
    preds,ids,low,up=ideal_data(case)
    A=side_counts(case,True,preds); B=side_counts(case,False,preds)
    H=[A]; G=[B]
    for j in range(1,maxm):
        hh=H[-1].copy(); gg=G[-1].copy()
        for s in ids: hh[s]+=sum(hh[p] for p in low[s])
        for s in reversed(ids): gg[s]+=sum(gg[p] for p in up[s])
        H.append(hh); G.append(gg)
    return H,G,ids

def length_counts(case,m,H,G,ids):
    t=case['t']; total=sum(H[m-1][s]*G[0][s] for s in ids)
    nums=[]
    for i in range(1,m+1):
        row=[0]*t
        for s in ids:
            w=H[i-1][s]*G[m-i][s]
            for x in range(t):
                if not(s>>x&1): row[x]+=w
        nums.append(row)
    return total,nums

def explicit(case,m):
    labels=[]; D=[]; U=[]; edges=[]
    for side in ('D','U'):
        out=D if side=='D' else U
        for g,(typ,n) in enumerate(case[side+'_groups']):
            group=[f'{side}{g}_{k+1}' for k in range(n)]; labels+=group; out.append(group)
            if typ=='chain': edges+=list(zip(group,group[1:]))
        for a,b in case[side+'_edges']: edges += [(x,y) for x in out[a] for y in out[b]]
    II=[f'x{x}' for x in range(case['t'])]; CC=[f'c{i}' for i in range(1,m+1)]; labels+=II+CC
    edges += [(II[a],II[b]) for a,b in case['I_edges']]
    edges += [(d,c) for gg in D for d in gg for c in CC]
    edges += [(c,u) for gg in U for u in gg for c in CC]
    edges += list(zip(CC,CC[1:]))
    for x in range(case['t']):
        for g,cut in enumerate(case['D_cuts'][x]): edges += [(d,II[x]) for d in D[g][:cut]]
        for g,cut in enumerate(case['U_cuts'][x]): edges += [(II[x],u) for u in U[g][cut:]]
    return labels,edges

def full_ideal_counts(case,m):
    labels,edges=explicit(case,m); n=len(labels); idx={x:i for i,x in enumerate(labels)}; pred=[0]*n
    for a,b in edges: pred[idx[b]] |= 1<<idx[a]
    @lru_cache(None)
    def suffix(s):
        if s==(1<<n)-1: return 1
        return sum(suffix(s|(1<<v)) for v in range(n) if not(s>>v&1) and pred[v]&s==pred[v])
    total=suffix(0)
    nums=[]
    for i in range(1,m+1):
        row=[]
        c=idx[f'c{i}']
        for x in range(case['t']):
            xx=idx[f'x{x}']
            @lru_cache(None)
            def win(s):
                if s>>c&1: return suffix(s)
                if s>>xx&1: return 0
                return sum(win(s|(1<<v)) for v in range(n) if not(s>>v&1) and pred[v]&s==pred[v])
            row.append(win(0))
        nums.append(row)
    return total,nums

def controls():
    checks=0
    for schema in range(7):
        for kind in range(4):
            case=make_case(schema,kind,3,1,1); H,G,ids=central_arrays(case,4)
            for m in (1,2,4):
                assert length_counts(case,m,H,G,ids)==full_ideal_counts(case,m),(schema,kind,m)
                checks+=1
    return checks

def run():
    started=time.time(); manifest=[]; results=[]; checked=0; inequalities=0; mindata=None
    checkn=controls(); print('INDEPENDENT_TINY_CONTROLS',checkn,flush=True)
    for schema in range(7):
        for kind in range(4):
            for t in range(3,7):
                for a,b in RATIOS:
                    case=make_case(schema,kind,t,a,b); manifest.append(case)
                    H,G,ids=central_arrays(case,max(MS)+1)
                    familymins=[]
                    for m in MS:
                        z,N=length_counts(case,m,H,G,ids); zz,NN=length_counts(case,m+1,H,G,ids)
                        local=None
                        for i in range(m):
                            for x in range(t):
                                d1=NN[i][x]*z-N[i][x]*zz
                                d2=N[i][x]*zz-NN[i+1][x]*z
                                inequalities+=2
                                if d1<=0 or d2<=0:
                                    fail={'case':case,'m':m,'i':i+1,'x':x,'total_m':str(z),'total_m1':str(zz),'numerator_i_m':str(N[i][x]),'numerator_i_m1':str(NN[i][x]),'numerator_ip1_m1':str(NN[i+1][x]),'cross_difference_left':str(d1),'cross_difference_right':str(d2),'relations_m':explicit(case,m),'relations_m1':explicit(case,m+1)}
                                    (ROOT/'FAILURE.json').write_text(json.dumps(fail,indent=2)); print('FAILURE',json.dumps({k:v for k,v in fail.items() if not k.startswith('relations')}),flush=True)
                                    return
                                ff=min(Fraction(d1,z*zz),Fraction(d2,z*zz))
                                if local is None or ff<local: local=ff
                        checked+=1
                        familymins.append({'m':m,'min_gap':str(local)})
                    results.append({'schema':schema,'I_kind':kind,'t':t,'ratio':[a,b],'lengths':familymins})
            print('FAMILY_PASS',schema,kind,'comparisons',checked,'seconds',round(time.time()-started,1),flush=True)
            (ROOT/'progress.json').write_text(json.dumps({'comparisons':checked,'inequalities':inequalities,'families_completed':len(results)//12,'elapsed':time.time()-started}))
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)); (ROOT/'results.json').write_text(json.dumps(results,indent=2))
    summary={'status':'NO_FAILURE_IN_FROZEN_BUDGET','outer_families':28,'actual_posets':len(manifest),'adjacent_length_comparisons':checked,'strict_inequalities':inequalities,'tiny_independent_controls':checkn,'elapsed_seconds':time.time()-started,'m_values':MS,'ratios':RATIOS}
    (ROOT/'summary.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary),flush=True)
if __name__=='__main__': run()
