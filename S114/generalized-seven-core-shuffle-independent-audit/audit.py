#!/usr/bin/env python3
"""Independent labelled ideal-DP audit; no author implementation imports.
All arithmetic is integral. DP uses actual element labels and direct predecessor
masks; a comparison probability is computed by adding its edge to the DAG.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib, json, sys, time
from math import comb

ROOT=Path(__file__).resolve().parent
COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))

def require(condition,context):
    """Checks remain active under python -O."""
    if not condition:raise RuntimeError(str(context))

def labelled_graph(lengths, cross=()):
    labels=tuple((i,r) for i,n in enumerate(lengths) for r in range(1,n+1))
    index={x:i for i,x in enumerate(labels)}
    pred=[0]*len(labels)
    for i,n in enumerate(lengths):
        for r in range(2,n+1):
            pred[index[i,r]]|=1<<index[i,r-1]
    for left,right in cross:
        pred[index[right]]|=1<<index[left]
    return labels,pred,index

def core_graph(w):
    return labelled_graph(w,[((i,w[i]),(j,1)) for i,j in COVERS])

def count(pred):
    full=(1<<len(pred))-1
    @lru_cache(None)
    def dp(done):
        if done==full:return 1
        answer=0
        remaining=full^done
        while remaining:
            bit=remaining&-remaining;remaining^=bit
            x=bit.bit_length()-1
            if pred[x]&done==pred[x]:answer+=dp(done|bit)
        return answer
    return dp(0),dp.cache_info().currsize

def comparison(pred,index,left,right):
    p=pred.copy();p[index[right]]|=1<<index[left]
    return count(p)

def words(pred):
    full=(1<<len(pred))-1
    def recurse(done,word):
        if done==full:
            yield tuple(word);return
        remaining=full^done
        while remaining:
            bit=remaining&-remaining;remaining^=bit
            x=bit.bit_length()-1
            if pred[x]&done==pred[x]:
                word.append(x);yield from recurse(done|bit,word);word.pop()
    yield from recurse(0,[])

def lemma_counts(r,k,t,q):
    require(1<=q<=k and min(k,t)>=1 and r>=0, '1<=q<=k and min(k,t)>=1 and r>=0')
    cross=[] if r==0 else [((0,r),(1,q))]
    labels,pred,index=labelled_graph((r,k,t),cross)
    z,_=count(pred)
    n,_=comparison(pred,index,(1,1),(2,1))
    return z,n

def check_lemma():
    cases=0;equal=0;strict=0;endpoints={1:0,'k':0}
    for r,k,t in product(range(6),range(1,7),range(1,7)):
        for q in range(1,k+1):
            z,n=lemma_counts(r,k,t,q)
            slack=k*z-(k+t)*n
            require(slack>=0, (r,k,t,q,z,n))
            require((slack==0)==(r==0), (r,k,t,q,z,n))
            cases+=1;equal+=slack==0;strict+=slack>0
            endpoints[1]+=q==1;endpoints['k']+=q==k
    return {'cases':cases,'equal_exactly_r_zero':equal,'strict_r_positive':strict,
            'q_1_cases':endpoints[1],'q_k_cases':endpoints['k']}

def proposed_closed_counts(w):
    # Transcription of the claimed mathematical formula, compared only against
    # our independent actual-label ideal DP. No author code is imported.
    u,a,b,c,t,d,v=w
    z=n=0
    for i in range(u+1):
        for j in range(t+1):
            f=comb(a+b+i+j-1,i)
            g=comb(u-i+c+t-j,t-j)*comb(u-i+c+t-j+d+v,v)
            z+=comb(b+j-1,j)*f*g
            h=1 if j==0 else (0 if b==1 else comb(b+j-2,j))
            n+=h*f*g
    return z,n

def check_core(w):
    u,a,b,c,t,d,v=w
    labels,pred,index=core_graph(w)
    z,states=count(pred)
    n,ns=comparison(pred,index,(2,1),(4,1))
    m,ms=comparison(pred,index,(4,t),(3,c))
    # Both strict bounds, without converting to floating point.
    require(n*(b+c+v+t)<z*(b+c+v), (w,z,n))
    require(m*(u+b+c+t)<z*(u+b+c), (w,z,m))
    dw=(v,d,c,b,t,a,u)
    dl,dp,di=core_graph(dw)
    dz,ds=count(dp)
    dn,dns=comparison(dp,di,(2,1),(4,1))
    require(z==dz and m==dn, (w,z,m,dz,dn))
    require(proposed_closed_counts(w)==(z,n), 'proposed_closed_counts(w)==(z,n)')
    require(proposed_closed_counts(dw)==(z,m), 'proposed_closed_counts(dw)==(z,m)')
    # If either new linear inequality fails, its corresponding arrow fails.
    if 2*t>=b+c+v:require(3*n<2*z, '3*n<2*z')
    if 2*t>=u+b+c:require(3*m<2*z, '3*m<2*z')
    return {'weights':list(w),'extensions':z,'forward_numerator':n,
            'dual_numerator':m,'labelled_ideal_states':states,
            'comparison_states':ns+ms+dns,'dual_ideal_states':ds}

def check_box():
    count_=0;maxstates=0;totalstates=0;critical=[]
    for w in product(range(1,4),repeat=7):
        r=check_core(w);count_+=1
        maxstates=max(maxstates,r['labelled_ideal_states'])
        totalstates+=r['labelled_ideal_states']+r['comparison_states']+r['dual_ideal_states']
        if w in ((2,1,1,1,1,1,2),(2,1,1,1,2,1,2),(3,1,1,1,2,1,3),(2,2,2,2,2,2,2)):
            critical.append(r)
    extras=[(1,9,1,1,1,11,1),(3,7,2,4,6,9,5),(8,2,3,2,8,6,9),
            (4,5,6,7,8,9,10),(10,9,8,7,6,5,4),(1,12,1,5,9,2,13),
            (7,1,2,1,9,13,1),(20,2,1,1,8,3,15),(1,1,1,1,30,1,1)]
    return {'box_cases':count_,'box_oracle_calls':5*count_,'closed_formula_comparisons':2*count_,'max_ideal_states':maxstates,
            'total_oracle_states':totalstates,'critical_examples':critical,
            'asymmetric_extras':[check_core(w) for w in extras]}

def check_fibers(w):
    u,a,b,c,t,d,v=w
    labels,pred,index=core_graph(w)
    groups={};total=0
    for word in words(pred):
        total+=1
        l=word.index(index[1,a]);h=word.index(index[5,1])
        prefix=word[:l+1];suffix=word[h:];mid=word[l+1:h]
        s=tuple(x for x in mid if labels[x][0] in (2,3,6))
        key=(prefix,suffix,s)
        if key not in groups:
            i=sum(labels[x][0]==0 for x in prefix)
            f=sum(labels[x][0]==6 for x in mid)
            q=s.index(index[3,1])+1;k=len(s)
            require(k==b+c+f and b+1<=q<=b+f+1<=k, 'k==b+c+f and b+1<=q<=b+f+1<=k')
            require(set(mid)==set(s)|{index[0,j] for j in range(i+1,u+1)}|{index[4,j] for j in range(1,t+1)}, 'set(mid)==set(s)|{index[0,j] for j in range(i+1,u+1)}|{index[4,j] for j in range(1,t+1)}')
            groups[key]=[u-i,k,t,q,f,0,0]
        g=groups[key];g[-2]+=1;g[-1]+=word.index(index[2,1])<word.index(index[4,1])
    f0=0;r0=0;maxq=0;minq=10**9
    for r,k,t,q,f,z,n in groups.values():
        expected=lemma_counts(r,k,t,q)
        require((z,n)==expected, (w,r,k,t,q,z,n,expected))
        require((k+t)*n<=k*z, '(k+t)*n<=k*z')
        f0+=f==0;r0+=r==0;maxq=max(maxq,q);minq=min(minq,q)
    require(f0>0 and r0>0, 'f0>0 and r0>0')
    return {'weights':list(w),'complete_labelled_extensions':total,'fibers':len(groups),
            'f_zero_fibers':f0,'remaining_A_zero_fibers':r0,'q_min':minq,'q_max':maxq}

def check_integer_cone():
    # Algebra is proved in AUDIT.md; these are independent finite integer checks.
    cases=0;survivors=0
    for a,b,c,d in product(range(1,5),repeat=4):
        for u,v,t in product(range(1,31),repeat=3):
            cases+=1
            if not(2*u<a+b+t+v and 2*v<u+c+t+d and 2*t<b+c+min(u,v)):continue
            survivors+=1
            require(2*t<=a+d+3*b+3*c-4, '2*t<=a+d+3*b+3*c-4')
            require(3*t<=2*a+d+5*b+4*c-6, '3*t<=2*a+d+5*b+4*c-6')
            require(3*t<=a+2*d+4*b+5*c-6, '3*t<=a+2*d+4*b+5*c-6')
            require(u<=(2*(a+b+t)+(c+d+t)-3)//3, 'u<=(2*(a+b+t)+(c+d+t)-3)//3')
            require(v<=((a+b+t)+2*(c+d+t)-3)//3, 'v<=((a+b+t)+2*(c+d+t)-3)//3')
    return {'spine_box':[1,4],'pendant_box':[1,30],
            'integer_candidates_checked':cases,'cone_survivors_checked':survivors}

def check_sharp_cap():
    examples=[]
    for a,b,c,d in product(range(1,21),repeat=4):
        alpha=a+b-1;beta=c+d-1;s=b+c
        U=(2*alpha+beta)//3;V=(alpha+2*beta)//3
        T=s-1+min(U,V)
        require(2*U-V<=alpha and 2*V-U<=beta, '2*U-V<=alpha and 2*V-U<=beta')
        require(T==min((2*a+d+5*b+4*c-6)//3,(a+2*d+4*b+5*c-6)//3), 'T==min((2*a+d+5*b+4*c-6)//3,(a+2*d+4*b+5*c-6)//3)')
        u=T+U;v=T+V;t=T
        require(min(u,v)>=2, 'min(u,v)>=2')
        require(2*u<a+b+t+v and 2*v<u+c+t+d and 2*t<b+c+min(u,v), '2*u<a+b+t+v and 2*v<u+c+t+d and 2*t<b+c+min(u,v)')
        require(2*(T+1)>=s+(T+1)+min(U,V), '2*(T+1)>=s+(T+1)+min(U,V)')
        if (a,b,c,d) in ((1,1,1,1),(1,1,1,2),(2,2,2,2),(1,1,1,20)):
            examples.append({'spine':[a,b,c,d],'U':U,'V':V,'T':T,'witness':[u,a,b,c,t,d,v]})
    return {'spine_box':[1,20],'cases':20**4,'examples':examples}

def main():
    start=time.time()
    result={'status':'PASS','implementation':'independent labelled predecessor-mask ideal DP',
            'uses_author_code':False,'lemma':check_lemma()}
    print('lemma PASS',flush=True)
    result['general_bound']=check_box();print('general bound PASS',flush=True)
    result['fibers']=[check_fibers(w) for w in (
        (1,1,1,1,1,1,1),(2,2,1,1,2,2,2),
        (2,1,2,2,2,1,2),(2,2,2,1,1,2,2),(1,3,1,2,2,3,2))]
    print('fiber bijections PASS',flush=True)
    result['integer_cone']=check_integer_cone();print('integer cone PASS',flush=True)
    result['sharp_cap']=check_sharp_cap();print('sharp integer cap PASS',flush=True)
    print('Elapsed seconds:',round(time.time()-start,3),flush=True)
    (ROOT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
