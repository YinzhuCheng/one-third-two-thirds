#!/usr/bin/env python3
"""Self-contained exact ideal DP for the pre-frozen 28 structural families."""
from functools import lru_cache
from collections import defaultdict, Counter
from fractions import Fraction
from pathlib import Path
import gzip, json, hashlib, time
OUT=Path(__file__).resolve().parent

def closure(names,edges):
    n=len(names); ix={x:i for i,x in enumerate(names)}; suc=[0]*n
    for a,b in edges: suc[ix[a]]|=1<<ix[b]
    for k in range(n):
        for i in range(n):
            if suc[i]>>k&1: suc[i]|=suc[k]
    assert all(not(suc[i]>>i&1) for i in range(n))
    pred=[sum(1<<i for i in range(n) if suc[i]>>j&1) for j in range(n)]
    return suc,pred

def shape_edges(labels,shape,dual=False):
    s=len(labels)
    if shape=='chain': e=list(zip(labels,labels[1:]))
    elif shape=='antichain': e=[]
    elif shape=='fork': e=[(x,labels[-1]) for x in labels[:-1]]
    elif shape=='twochain':
        cut=(s+1)//2; e=list(zip(labels[:cut],labels[1:cut]))+list(zip(labels[cut:],labels[cut+1:]))
    else: raise ValueError(shape)
    return [(b,a) for a,b in e] if dual else e

def build_cases():
    cases=[]
    for family in range(1,8):
        for s in (2,3,4,6):
            D=[f'd{i+1}' for i in range(s)]; U=[f'u{i+1}' for i in range(s)]
            I=['a','b'] if family<=5 else ['a','a2','b2','b']
            shape={1:'chain',2:'antichain',3:'fork',4:'twochain',5:'chain',6:'chain',7:'twochain'}[family]
            e=shape_edges(D,shape)+shape_edges(U,shape,dual=family==3)
            e += [(d,u) for d in D for u in U]
            if family<=4: e += [('a',u) for u in U]+[(d,'b') for d in D]
            elif family==5:
                e += [('a',u) for u in U[1:]]+[(d,'b') for d in D[:-1]]+[(D[0],'a'),('b',U[-1])]
            else:
                e += [(a,u) for a in ('a','a2') for u in U]+[(d,b) for d in D for b in ('b','b2')]
                e += [('a','a2'),('b2','b')] if family==6 else [(D[0],'a2'),('b2',U[-1])]
            names=D+I+U; suc,pred=closure(names,e)
            cases.append({'id':f'F{family}-s{s}','family':family,'s':s,'D':D,'I':I,'U':U,'names':names,'generating_edges':e,'strict_relations':[[x,names[j]] for i,x in enumerate(names) for j in range(len(names)) if suc[i]>>j&1]})
    return cases

def count(names,edges):
    n=len(names); full=(1<<n)-1; suc,pred=closure(names,edges)
    @lru_cache(None)
    def Z(mask):
        if mask==full:return 1
        ans=0; rem=full^mask
        while rem:
            bit=rem&-rem; rem-=bit; i=bit.bit_length()-1
            if pred[i]&mask==pred[i]:ans+=Z(mask|bit)
        return ans
    total=Z(0); states=sorted(Zstates(Z,full,pred),key=int.bit_count)
    A={0:1}; nums=[[0]*n for _ in range(n)]
    for mask in states:
        pref=A.get(mask,0)
        if not pref: continue
        rem=full^mask
        while rem:
            bit=rem&-rem; rem-=bit; i=bit.bit_length()-1
            if pred[i]&mask!=pred[i]:continue
            nxt=mask|bit; A[nxt]=A.get(nxt,0)+pref
            w=pref*Z(nxt); other=full^nxt
            while other:
                b=other&-other; other-=b; j=b.bit_length()-1; nums[i][j]+=w
    assert A[full]==total
    assert all(nums[i][j]+nums[j][i]==total for i in range(n) for j in range(i+1,n))
    return {'names':names,'total':total,'numerators':nums,'states':len(states)},suc

def Zstates(Z,full,pred):
    # Reachable-ideal traversal, separately checked against suffix recurrence.
    todo=[0]; seen={0}; n=len(pred)
    while todo:
        mask=todo.pop()
        for i in range(n):
            bit=1<<i
            if not mask&bit and pred[i]&mask==pred[i]:
                nxt=mask|bit
                if nxt not in seen:seen.add(nxt);todo.append(nxt)
    return seen

def model(case,m):
    C=[f'c{i+1}' for i in range(m)]; names=case['names']+C
    edges=case['generating_edges']+list(zip(C,C[1:]))+[(d,c) for d in case['D'] for c in C]+[(c,u) for c in C for u in case['U']]
    result,suc=count(names,edges); result.update({'m':m,'C':C})
    return result,suc

def bal(n,t):return t<=3*n<=2*t

def frac(n,t):return str(Fraction(n,t))

def main():
    cases=build_cases(); frozen=OUT/'frozen_cases.json'
    if frozen.exists():assert json.loads(frozen.read_text())==json.loads(json.dumps(cases))
    else:frozen.write_text(json.dumps(cases,indent=2)+'\n')
    digest=hashlib.sha256(frozen.read_bytes()).hexdigest()
    summary={'frozen_cases_sha256':digest,'families':28,'lengths':[2,24],'planned_controls':644,'completed_controls':0,'same_side_premise_controls':0,'premise_m_ge_2t_controls':0,'split_side_premise_controls':0,'eligible_cross_pair_instances':0,'cross_parent_balanced_instances':0,'cross_short_balanced_instances':0,'cross_new_balanced_instances':0,'all_external_new_balanced_under_premise':0,'same_side_new_balanced_under_premise':0,'cases':[],'counterexample':None}
    start=time.time()
    with gzip.open(OUT/'all_exact_counts.jsonl.gz','wt') as counts,gzip.open(OUT/'control_records.jsonl.gz','wt') as records:
        for case in cases:
            print('START',case['id'],flush=True); prev=None; cs=Counter(); best=None
            for m in range(1,25):
                cur,suc=model(case,m); counts.write(json.dumps({'case':case['id'],**cur})+'\n')
                if prev is None:prev=cur;continue
                names=cur['names']; ix={x:i for i,x in enumerate(names)}; ni=cur['numerators']; T=cur['total']; six={x:i for i,x in enumerate(prev['names'])}; sn=prev['numerators']; S=prev['total']
                sides={}; columns={}
                for x in case['I']:
                    col=[ni[ix[c]][ix[x]] for c in cur['C']]; columns[x]=col
                    if all(3*v<T for v in col):sides[x]='L'
                    elif all(3*v>2*T for v in col):sides[x]='R'
                    else:sides[x]='X'
                premise=all(s!='X' for s in sides.values())
                rec={'case':case['id'],'m':m,'parent_total':T,'short_total':S,'sides':sides,'columns':columns,'premise':premise,'external_new':[],'eligible_cross':[],'parent_balanced':[]}
                summary['completed_controls']+=1;cs['controls']+=1
                if premise:
                    cs['premise']+=1;summary['same_side_premise_controls']+=1
                    if m>=2*len(case['I']):summary['premise_m_ge_2t_controls']+=1
                    L=set(case['D'])|{x for x,s in sides.items() if s=='L'}; R=set(case['U'])|{x for x,s in sides.items() if s=='R'}
                    if any(s=='L' for s in sides.values()) and any(s=='R' for s in sides.values()):cs['split']+=1;summary['split_side_premise_controls']+=1
                    for i,a in enumerate(names):
                        for j in range(i+1,len(names)):
                            b=names[j]
                            if not(suc[i]>>j&1 or suc[j]>>i&1) and bal(ni[i][j],T):
                                block='C' if a in cur['C'] or b in cur['C'] else ('L' if a in L and b in L else 'R' if a in R and b in R else 'cross')
                                rec['parent_balanced'].append([a,b,ni[i][j],T,block])
                    for i,a in enumerate(case['names']):
                        for b in case['names'][i+1:]:
                            ai=ix[a];bi=ix[b]
                            if suc[ai]>>bi&1 or suc[bi]>>ai&1:continue
                            pnum=ni[ai][bi];snum=sn[six[a]][six[b]]
                            cross=(a in L and b in R) or (a in R and b in L)
                            if bal(snum,S) and not bal(pnum,T):
                                rec['external_new'].append([a,b,pnum,T,snum,S,'cross' if cross else 'same_side'])
                                summary['all_external_new_balanced_under_premise']+=1
                                if not cross:summary['same_side_new_balanced_under_premise']+=1
                            if cross:
                                left,right=(a,b) if a in L else (b,a)
                                pnum=ni[ix[left]][ix[right]];snum=sn[six[left]][six[right]]
                                entry=[left,right,pnum,T,snum,S]
                                rec['eligible_cross'].append(entry);summary['eligible_cross_pair_instances']+=1;cs['cross']+=1
                                if bal(pnum,T):summary['cross_parent_balanced_instances']+=1
                                if bal(snum,S):summary['cross_short_balanced_instances']+=1
                                if bal(snum,S) and not bal(pnum,T):summary['cross_new_balanced_instances']+=1;summary['counterexample']=rec
                                # Record smallest exact parent p(a<b), with orientation L->R.
                                if best is None or Fraction(pnum,T)<Fraction(best['num'],best['total']):best={'m':m,'pair':[left,right],'num':pnum,'total':T,'short_num':snum,'short_total':S}
                    assert all(p[-1]!='C' for p in rec['parent_balanced'])
                records.write(json.dumps(rec)+'\n')
                if summary['counterexample'] is not None:
                    (OUT/'counterexample.json').write_text(json.dumps({'case':case,'record':rec,'parent':cur,'short':prev},indent=2)+'\n')
                    break
                prev=cur
            summary['cases'].append({'id':case['id'],'stats':dict(cs),'minimum_cross_parent':best})
            (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
            print('DONE',case['id'],dict(cs),'best',best,'elapsed',round(time.time()-start,2),flush=True)
            if summary['counterexample'] is not None:break
    summary['elapsed_seconds']=time.time()-start
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
