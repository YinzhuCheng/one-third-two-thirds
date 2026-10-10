"""Independent exact verifier for the four-element terminal chain certificate.
Python standard library only. All checks remain active with python -O.
"""
from functools import lru_cache
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json

COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
def require(ok,info):
    if not ok:raise RuntimeError(repr(info))

def actual_poset(w):
    blocks=[];off=0
    for wi in w:blocks.append(tuple(range(off,off+wi)));off+=wi
    pred=[0]*off
    for block in blocks:
        for x,y in zip(block,block[1:]):pred[y]|=1<<x
    for i,j in COVERS:pred[blocks[j][0]]|=1<<blocks[i][-1]
    down=pred[:]
    for y in range(off):
        for x in range(off):
            if down[y]>>x&1:down[y]|=down[x]
    up=[sum(1<<y for y in range(off) if down[y]>>x&1)for x in range(off)]
    return blocks,pred,down,up

def is_chain(mask,down):
    return all((down[x]>>y&1)or(down[y]>>x&1)for x in range(len(down))if mask>>x&1 for y in range(x+1,len(down))if mask>>y&1)

def count_and_hist(w):
    blocks,pred,down,up=actual_poset(w);N=len(pred);full=(1<<N)-1
    x=blocks[3][0];z=blocks[5][0];Fs=blocks[6];fm=sum(1<<f for f in Fs)
    require(down[Fs[0]]&~down[x]==0 and is_chain(up[x]&~up[Fs[0]],down),('lower force',w))
    require(up[Fs[-1]]&~up[x]==0 and is_chain(down[x]&~down[Fs[-1]],down),('upper force',w))
    require(up[z]&~up[Fs[-1]]==0 and is_chain(down[Fs[-1]]&~down[z],down),('terminal force',w))
    @lru_cache(None)
    def suffix(mask):
        if mask==full:return 1
        return sum(suffix(mask|1<<j)for j in range(N)if not(mask>>j&1)and pred[j]&mask==pred[j])
    E=suffix(0);hist=[0]*5;f_before_z=0;states={0:1}
    for depth in range(N):
        nxt={}
        for mask,prefix in states.items():
            for j in range(N):
                if mask>>j&1 or pred[j]&mask!=pred[j]:continue
                child=mask|1<<j;ways=prefix*suffix(child)
                if j==x:hist[(mask&fm).bit_count()]+=ways
                if j==z and mask>>Fs[-1]&1:f_before_z+=ways
                nxt[child]=nxt.get(child,0)+prefix
        states=nxt
    require(states[full]==E and sum(hist)==E,('counts partition',w))
    return E,hist,f_before_z

def polynomial(k,n):
    return 17*k*k*n*n+19*k*k*n+102*k*k-27*k*n*n-657*k*n-18*k+52*n*n+524*n+3480

def shifted(d,l):
    return 17*d**4+34*d**3*l+332*d**3+17*d*d*l*l+475*d*d*l+1927*d*d+143*d*l*l+1647*d*l+3376*d+342*l*l+1134*l+3060

def main():
    vectors=0;crossings=0;largest=Q(0);minmargin=None
    for u,a,b,t in product(range(1,6),repeat=4):
        w=(u,a,b,1,t,1,4);E,h,C=count_and_hist(w)
        require(15*h[1]<=4*E and 35*h[2]<=9*E,('rank bounds',w,E,h))
        lhs=3*(12*sum(h[3:])+15*sum(h[:4])+C)
        require(lhs<56*E,('certificate',w,E,h,C))
        margin=Q(56*E-lhs,3*E)
        if minmargin is None or margin<minmargin:minmargin=margin
        largest=max(largest,Q(h[3],E))
        balanced=[i for i in range(1,5)if E<=3*sum(h[:i])<=2*E]
        if 3*(E-h[0])>2*E and 3*(E-h[4])>2*E and 3*C>2*E:
            require(bool(balanced),('forced endpoints crossing',w,h,C));crossings+=1
        vectors+=1
    monomials=0
    small=[lambda l:4*(13*l*l+131*l+870),lambda l:6*(7*l*l-5*l+582),lambda l:6*(11*l*l-75*l+448),lambda l:4*(31*l*l-133*l+408),lambda l:72*(3*l*l-l+18)]
    for k,l in product(range(101),repeat=2):
        n=k+l;M3=Q(k+1,k+4)*Q(n+2,n+5);M4=Q(k+1,k+5)*Q(n+2,n+6);C=Q(n+2,n+6)
        gap=Q(11,3)-48*M3+51*M4-C
        denom=3*(k+4)*(k+5)*(n+5)*(n+6)
        require(gap*denom==polynomial(k,n)>0,('polynomial identity',k,l))
        require(polynomial(k,n)==(small[k](l)if k<5 else shifted(k-5,l)),('positive expansion',k,l))
        monomials+=1
    atomchecks=0
    for m in range(1001):
        for j,bound in ((1,Q(4,15)),(2,Q(9,35))):
            p=Q((5-j)*comb(m+j,j),comb(m+6,4))
            require(p<=bound<Q(1,3),('beta rank',m,j,p));atomchecks+=1
    require(Q(2*comb(8,3),comb(11,4))>Q(1,3),('rank3 bound deliberately fails',))
    out={'status':'PASS','actual_labelled_vectors':vectors,'weight_scope':'u,a,b,t each 1..5; c=d=1; v=4','forced_endpoint_crossing_vectors':crossings,'largest_rank3_atom_in_box':str(largest),'smallest_certificate_margin_in_box':str(minmargin),'exact_triangle_monomials':monomials,'exact_beta_binomial_checks':atomchecks,'structural_actual_vertex_checks':3*vectors,'scope':'Unbounded v=4 theorem; bounded checks validate implementation only.'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
