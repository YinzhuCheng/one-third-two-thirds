#!/usr/bin/env python3
"""Exact independent audit of the c=d=1 seven-core integral exclusion.
No author code or counting formulas are imported. Checks remain active under -O.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
def require(ok, context):
    if not ok: raise RuntimeError(str(context))
def graph(w):
    labels=tuple((i,r) for i,n in enumerate(w) for r in range(1,n+1))
    ix={x:i for i,x in enumerate(labels)}; pred=[0]*len(labels)
    for i,n in enumerate(w):
        for r in range(2,n+1): pred[ix[i,r]]|=1<<ix[i,r-1]
    for i,j in COVERS: pred[ix[j,1]]|=1<<ix[i,w[i]]
    return pred,ix

def check_structural(pred,ix,w):
    down=pred.copy()
    # All original edges respect the block/rank label order in this topological labelling.
    for i in range(len(pred)):
        mask=down[i]
        for j in range(i):
            if mask>>j&1:down[i]|=down[j]
    up=[0]*len(pred)
    for j in range(len(pred)):
        for i in range(len(pred)):
            if down[j]>>i&1:up[i]|=1<<j
    x=ix[3,1];z=ix[5,1];f=ix[6,w[6]]
    A=sum(1<<ix[0,k] for k in range(1,w[0]+1))
    Fminus=sum(1<<ix[6,k] for k in range(1,w[6]))
    require(up[f]==0 and up[z]==0 and up[x]==1<<z,('upsets',w))
    require(down[x]&~down[f]==A,('first downset difference',w))
    require(down[f]&~down[z]==Fminus,('second downset difference',w))
    require(not(down[x]>>f&1 or down[f]>>x&1),('x incomparable F',w))
    require(not(down[z]>>f&1 or down[f]>>z&1),('z incomparable F',w))
    if w[6]==1:
        require(down[f]&~down[x]==0 and up[x]&~up[f]==1<<z,('v1 lower reverse edge',w))

def count(pred):
    full=(1<<len(pred))-1
    @lru_cache(None)
    def dp(done):
        if done==full:return 1
        answer=0; remain=full^done
        while remain:
            bit=remain&-remain;remain^=bit;i=bit.bit_length()-1
            if pred[i]&done==pred[i]:answer+=dp(done|bit)
        return answer
    return dp(0),dp.cache_info().currsize

def edge_count(pred,ix,left,right):
    p=pred.copy();p[ix[right]]|=1<<ix[left]
    return count(p)[0]

def mono_int(p,q,h,k):
    # Integral over 0<s<r<x<z<1 of s^p r^q x^h z^k.
    return F(1,(p+1)*(p+q+2)*(p+q+h+3)*(p+q+h+k+4))

def poly_volume(w,kind):
    # Integrate A=T0 first, then all interior chain coordinates.
    # Base density s^(a-1)(r-s)^(b-1)x^u(z-s)^t(1-r)^v.
    # For F<x or F<z, replace last factor with (x-r)^v or (z-r)^v.
    u,a,b,c,t,d,v=w; require(c==d==1,w)
    raw=F(0)
    for i,j,k in product(range(b),range(t+1),range(v+1)):
        coefficient=(-1)**(i+j+k)*comb(b-1,i)*comb(t,j)*comb(v,k)
        p=a-1+i+j;q=b-1-i+k;h=u;zz=t-j
        if kind=='F<x':h+=v-k
        elif kind=='F<z':zz+=v-k
        else:require(kind=='all',kind)
        raw+=coefficient*mono_int(p,q,h,zz)
    denominator=factorial(a-1)*factorial(b-1)*factorial(u)*factorial(t)*factorial(v)
    return raw/denominator

def J(n,alpha):return (1-alpha**(n+1))/F(n+1)
def conditional(t,v,alpha,delta):
    # Exact polynomial integrals of the proposed two-coordinate conditional law.
    D=Ez=Ex=F(0)
    for j in range(t+1):
        co=comb(t,j)*delta**(t-j)
        D+=co*(J(j+1,alpha)-alpha*J(j,alpha))
        Ez+=co*(J(j+v+1,alpha)-alpha*J(j+v,alpha))
        Ex+=co*(J(j+v+1,alpha)-alpha**(v+1)*J(j,alpha))/F(v+1)
    require(D>0,('positive volume',t,v,alpha,delta))
    return D,Ez,Ex

def check_conditional():
    alphas=[F(0),F(1,1000),F(1,5),F(1,2),F(4,5),F(999,1000)]
    deltas=[F(0),F(1,1000),F(1,7),F(1),F(10),F(10000)]
    checks=equality=strict=0
    for t in range(1,9):
        for v in range(t+1,t+7):
            for a,d in product(alphas,deltas):
                D,Ez,Ex=conditional(t,v,a,d);slack=D-2*Ez+Ex
                require(slack>=0,(t,v,a,d,slack))
                require((slack==0)==(v==t+1 and d==0),('equality',t,v,a,d,slack))
                checks+=1;equality+=slack==0;strict+=slack>0
    # Reference h=g' has exponent v-1, delta=0; its integral is identically zero.
    identities=0
    for v in range(1,21):
        for a in alphas:
            D,Ez,Ex=conditional(v-1,v,a,F(0))
            require(D-2*Ez+Ex==0,('zero reference',v,a));identities+=1
    # Outside the theorem's exponent range the proposed bound can fail, even delta>0.
    D,Ez,Ex=conditional(2,2,F(0),F(1,1000))
    require(2*Ez-Ex>D,'outside-range test unexpectedly satisfied')
    return {'parameter_grid_checks':checks,'strict_checks':strict,'equality_checks':equality,
            'reference_identity_checks':identities,
            'alpha_grid':[str(x) for x in alphas],'delta_grid':[str(x) for x in deltas],
            'outside_range_example':{'t':2,'v':2,'alpha':'0','delta':'1/1000','2Ez_minus_Ex_over_D':str((2*Ez-Ex)/D)}}

def check_weights(w,integrate=True):
    u,a,b,c,t,d,v=w;pred,ix=graph(w);check_structural(pred,ix,w);Z,states=count(pred)
    Q=edge_count(pred,ix,(3,1),(6,v))
    R=edge_count(pred,ix,(6,v),(5,1))
    require(Q+2*R<2*Z,('strict inequality',w,Z,Q,R))
    require(not(3*Q>2*Z and 3*R>2*Z),('forced arrows coexist',w))
    if integrate:
        allv=poly_volume(w,'all');fx=poly_volume(w,'F<x');fz=poly_volume(w,'F<z')
        require(allv*factorial(sum(w))==Z,('order polytope volume',w,allv,Z))
        require((allv-fx)/allv==F(Q,Z),('q integration',w,Q,Z,(allv-fx)/allv))
        require(fz/allv==F(R,Z),('r integration',w,R,Z,fz/allv))
    # Reverse actual labelled extensions, reidentify blocks, and check dual events.
    dw=(v,d,c,b,t,a,u);dp,di=graph(dw);DZ,_=count(dp)
    DQ=edge_count(dp,di,(0,1),(2,dw[2]))
    DR=edge_count(dp,di,(1,1),(0,1))
    require((DZ,DQ,DR)==(Z,Q,R),('dual events',w,Z,Q,R,DZ,DQ,DR))
    return {'weights':list(w),'extensions':Z,'q_numerator':Q,'r_numerator':R,
            'strict_slack_numerator':2*Z-Q-2*R,'states':states}

def check_full():
    rows=[];n=0;maxstates=0
    for u,a,b,t,k in product(range(1,5),repeat=5):
        w=(u,a,b,1,t,1,t+k);r=check_weights(w)
        n+=1;maxstates=max(maxstates,r['states'])
        if w in ((1,1,1,1,1,1,2),(2,1,1,1,1,1,2),(2,1,4,1,3,1,4),(4,4,4,1,4,1,8)):rows.append(r)
    extras=[(8,1,1,1,1,1,2),(1,9,1,1,3,1,4),(2,3,12,1,5,1,6),
            (11,7,3,1,4,1,9),(3,2,5,1,12,1,13),(5,11,9,1,8,1,9)]
    return {'grid':'u,a,b,t,k in {1,2,3,4}; v=t+k; c=d=1','grid_vectors':n,
            'dp_counts_per_vector':6,'polynomial_volume_integrals_per_vector':3,
            'max_ideal_states':maxstates,'examples':rows,'asymmetric_extras':[check_weights(w) for w in extras]}

def check_four_nonsingleton_logic():
    checked=0
    for flags in product((1,2),repeat=7):
        if sum(x>1 for x in flags)>3:continue
        u,a,b,c,t,d,v=flags
        reasons=[]
        if u==1 or v==1:reasons.append('singleton port')
        if b==c==1:reasons.append('both inner spine blocks singleton')
        if c==d==1 and t==1 and v>=2:reasons.append('integral theorem')
        if a==b==1 and t==1 and u>=2:reasons.append('dual integral theorem')
        require(reasons,('uncovered support pattern',flags));checked+=1
    singleton=0
    for u,a,b,t in product(range(1,5),repeat=4):
        w=(u,a,b,1,t,1,1);pred,ix=graph(w);check_structural(pred,ix,w);singleton+=1
    # t<=b follows exactly from v<=t and 2t<b+1+v, checked as arithmetic, not proof.
    implications=0
    for b,t,v in product(range(1,51),repeat=3):
        if 2<=v<=t and 2*t<b+1+v:
            require(2<=v<=t<=b,(b,t,v));implications+=1
    return {'support_patterns_with_at_most_three_nonsingletons':checked,'bounded_corollary_implications':implications,'v1_structural_cycles':singleton,
            'scope':'logical coverage only; port and both-inner-singleton theorems are independent dependencies'}

def main():
    result={'status':'PASS','conditional_integrals':check_conditional(),'actual_full_extensions':check_full(),
            'corollary_logic':check_four_nonsingleton_logic()}
    (ROOT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
