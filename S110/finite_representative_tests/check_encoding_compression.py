#!/usr/bin/env python3
"""Exact finite checks of finite_epsilon_representative.md; no decay assertion.
All label arithmetic here is zero-based. No external dependencies.
"""
from collections import defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json, random
from pathlib import Path

RNG=random.Random(20261010)

def decode(word,R):
    n=len(word); pred=[0]*n; inc=[]
    for j in range(n):
        for i in range(j):
            if j-i<=R and (word[j]>>(j-i-1))&1: inc.append((i,j))
            else: pred[j]|=1<<i
    return pred,inc

def lawful(word,R,D):
    pred,inc=decode(word,R); deg=[0]*len(word)
    for i,j in inc: deg[i]+=1; deg[j]+=1
    assert max(deg,default=0)<=D
    for j,p in enumerate(pred):
        for i in range(j):
            if p>>i&1: assert pred[i]&~p==0
    for j,b in enumerate(word): assert b>>min(j,R)==0
    return pred,inc

def encode_pred(pred,R):
    return tuple(sum((not(pred[j]>>(j-t)&1))<<(t-1)
                     for t in range(1,min(j,R)+1)) for j in range(len(pred)))

def probabilities(pred,inc):
    n=len(pred); full=(1<<n)-1; transitions={}
    @lru_cache(None)
    def back(s):
        if s==full: transitions[s]=[]; return 1
        opts=[j for j in range(n) if not(s>>j&1) and pred[j]&~s==0]
        transitions[s]=opts
        return sum(back(s|(1<<j)) for j in opts)
    total=back(0); f={0:1}; counts={p:0 for p in inc}; bylater=defaultdict(list)
    for i,j in inc: bylater[j].append(i)
    for s in sorted(transitions,key=int.bit_count):
        for j in transitions[s]:
            t=s|(1<<j); ways=f[s]*back(t)
            for i in bylater[j]:
                if s>>i&1: counts[i,j]+=ways
            f[t]=f.get(t,0)+f[s]
    assert f[full]==total
    return {p:Fraction(c,total) for p,c in counts.items()},total,len(transitions)

def compress(w,q,markstart=None):
    if len(w)<q: return w,None,0
    g=defaultdict(list)
    for k in range(len(w)-q+1):
        edge=(w[k+1:k+q],w[k+q-1],k)
        if edge[:2] not in [(v,a) for v,a,_ in g[w[k:k+q-1]]]:
            g[w[k:k+q-1]].append(edge)
        g[w[k+1:k+q]]
    def path(a,b):
        dq=deque([a]); prev={a:None}
        while dq:
            u=dq.popleft()
            if u==b: break
            for v,letter,k in g[u]:
                if v not in prev: prev[v]=(u,letter,k); dq.append(v)
        assert b in prev
        out=[]; u=b
        while prev[u] is not None:
            v,letter,k=prev[u]; out.append((letter,k)); u=v
        return out[::-1]
    s=w[:q-1]; t=w[-q+1:]
    if markstart is None:
        walk=path(s,t); markout=None
    else:
        k=markstart; pre=path(s,w[k:k+q-1]); post=path(w[k+1:k+q],t)
        walk=pre+[(w[k+q-1],k)]+post; markout=len(pre)
    out=s+tuple(letter for letter,k in walk)
    assert len(out)<=len(w)
    assert out[:q-1]==s and out[-q+1:]==t
    original={w[k:k+q] for k in range(len(w)-q+1)}
    assert all(out[k:k+q] in original for k in range(len(out)-q+1))
    assert len(out)<=q+2*len(g)-2 if markstart is not None else len(out)<=q+len(g)-2
    return out,markout,len(g)

def containing(n,q,a,b):
    """Inclusive interval [a,b], return start of q-gram containing it."""
    k=max(0,b-q+1)
    assert k<=a and k+q<=n
    return k

def local_signature(w,R,B,i,j):
    a=max(0,i-B); b=min(len(w)-1,j+B)
    pred,inc=decode(w,R)
    pattern=tuple(tuple(bool(pred[v]>>u&1) for u in range(a,v)) for v in range(a,b+1))
    return (i-a,j-a,b-a+1,a==0,b==len(w)-1,pattern)

def final_witness(w,v,R,B,q,i,j):
    n=len(w); m=len(v)
    if i<=B: return i,j,'left'
    if j>=m-1-B: return i+n-m,j+n-m,'right'
    if m==q-1: return i,j,'zero_path_interior'
    k=containing(m,q,i-B-1,j+B+1)
    z=next(z for z in range(n-q+1) if w[z:z+q]==v[k:k+q])
    return i+z-k,j+z-k,'interior'

def retained_pair(w,v,R,B,q,x,y,k,markout):
    if x<=B: return x,y,'left'
    if y>=len(w)-1-B: return x+len(v)-len(w),y+len(v)-len(w),'right'
    return x+markout-k,y+markout-k,'marked_interior'

def ordinal_random(n,D):
    pred=[]
    while len(pred)<n:
        k=min(RNG.randrange(1,D+2),n-len(pred)); base=len(pred); core=(1<<base)-1
        p=[0]*k
        for j in range(k):
            for i in range(j):
                if RNG.randrange(3)==0: p[j]|=(1<<i)|p[i]
        pred.extend(core|(v<<base) for v in p)
    return pred

def gaps(n,S):
    return [sum(1<<i for i in range(j) if j-i not in S) for j in range(n)]

def run_case(pred,D,B,name,choose='maximum'):
    R=2*D-1; q=2*B+3*R+6; w=encode_pred(pred,R); pred,inc=lawful(w,R,D)
    if not inc or len(w)<q: return None
    probs,total,states=probabilities(pred,inc)
    if choose=='left':
        pair=inc[0]
    elif choose=='interior':
        options=[p for p in inc if p[0]>B and p[1]<len(w)-1-B]
        if not options: return None
        pair=options[len(options)//2]
    else:
        pair=max(inc,key=lambda p:(min(probs[p],1-probs[p]),p[0]))
    x,y=pair; k=containing(len(w),q,max(0,x-B-1),min(len(w)-1,y+B+1))
    v,markout,ng=compress(w,q,k); vp,vi=lawful(v,R,D); assert vi
    vprobs,vtotal,vstates=probabilities(vp,vi)
    coverage=defaultdict(int); maxerr=Fraction(0)
    for i,j in vi:
        a,b,kind=final_witness(w,v,R,B,q,i,j); coverage[kind]+=1
        assert (a,b) in probs
        assert local_signature(v,R,B,i,j)==local_signature(w,R,B,a,b)
        maxerr=max(maxerr,abs(vprobs[i,j]-probs[a,b]))
    a,b,kind=retained_pair(w,v,R,B,q,x,y,k,markout)
    assert (a,b) in vprobs
    assert local_signature(w,R,B,x,y)==local_signature(v,R,B,a,b)
    delta=max(min(p,1-p) for p in probs.values())
    vdelta=max(min(p,1-p) for p in vprobs.values())
    return dict(name=name,D=D,B=B,q=q,n=len(w),n_final=len(v),graph_states=ng,
                original_ideal_states=states,final_ideal_states=vstates,
                final_pairs=len(vi),witness_cases=dict(coverage),retained_kind=kind,
                max_actual_witness_probability_error=str(maxerr),
                original_delta=str(delta),final_delta=str(vdelta),
                marked_pair_mode=choose)

def main():
    records=[]
    for D,S in [(2,{1}),(4,{1,3}),(6,{1,2,5})]:
        for B in [0,1,3,7]:
            for mode in ['maximum','interior']:
                r=run_case(gaps(110,S),D,B,f'gap_{sorted(S)}',mode)
                if r: records.append(r)
    for D in [1,2,3,4,6]:
        for B in [0,1,3]:
            for trial in range(3):
                r=run_case(ordinal_random(100,D),D,B,f'ordinal_random_{trial}')
                if r: records.append(r)
    records.append(run_case(gaps(110,{1}),2,7,'explicit_left_retained_pair','left'))
    # Exhaust all valid R=1 words of lengths up to 12 for small q=5.
    exhaustive=0; zeropath=0
    for n in range(5,13):
        for tail in product([0,1],repeat=n-1):
            w=(0,)+tail
            if any(w[j] and w[j+1] for j in range(n-1)): continue
            lawful(w,1,1)
            v,_,_=compress(w,5)
            lawful(v,1,1)
            if len(v)==4: zeropath+=1
            for i,j in decode(v,1)[1]:
                a,b,_=final_witness(w,v,1,0,5,i,j)
                assert local_signature(v,1,0,i,j)==local_signature(w,1,0,a,b)
            exhaustive+=1
    # Negative control: ordinary shortest path erases the sole nonchain block.
    w=(0,)*20+(1,)+(0,)*20; q=9
    unmarked,_,_=compress(w,q)
    marked,_,_=compress(w,q,containing(len(w),q,19,20))
    assert len(decode(w,1)[1])==1 and not decode(unmarked,1)[1]
    assert len(decode(marked,1)[1])==1
    result=dict(status='PASS',scope='Encoding, legality, marked and unmarked path shortening, exact local witnesses and endpoint flags. No probability-decay theorem asserted by these finite tests.',
                seed=20261010,actual_poset_cases=len(records),records=records,
                exhaustive_R1_words=exhaustive,zero_edge_path_cases=zeropath,
                erased_nonchain_negative_control=dict(original_n=len(w),unmarked_n=len(unmarked),marked_n=len(marked)))
    out=Path(__file__).with_name('exact_checks.json'); out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))

if __name__=='__main__': main()
