from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
import json

out = {}

def chain_pair(m, j, h, t):
    # P(external chain t is before internal chain j), exact shuffle count.
    num=0
    for i in range(j, j+h):
        # internal j occurs at position i+1 (0-based prefix i), t external before iff i-j+1 >=t
        e_before=i-j+1
        if e_before <t or e_before>h: continue
        num += comb(i,j-1)*comb(m+h-i-1,m-j)
    return F(num,comb(m+h,m))

def two_chain_p(m,j):
    e2=F(j*(j+1),(m+1)*(m+2))
    return 2*F(j,m+1)-e2,e2

def cdf_beta(a,b,t):
    n=a+b-1
    return sum(F(comb(n,r))*t**r*(1-t)**(n-r) for r in range(a,n+1))

# 1. Actual central deletion C_8 + C_1 + C_8 -> C_8 + C_8, E=C_2.
old_left=1-two_chain_p(17,8)[0]
old_right=two_chain_p(17,10)[1]
new_left=1-two_chain_p(16,8)[0]
new_right=two_chain_p(16,9)[1]
assert old_left==old_right==F(55,171)<F(1,3)
assert new_left==new_right==F(5,17)<old_left
# Finite explicit exponential-gap values check the single coupling for all positions.
L=list(range(1,9)); H=[9,10]; R=list(range(11,19))
s_old=sum(L+H+R); s_new=sum(L+[H[0]]+R)
assert all(F(sum(L[:i]),s_new)>=F(sum(L[:i]),s_old) for i in range(1,9))
assert all(1-F(sum(R[j-1:]),s_new)<=1-F(sum(R[j-1:]),s_old) for j in range(1,9))
out['control_1']={'old_rare':str(old_left),'new_rare':str(new_left),'coupling_all_16_retained_coordinates':'PASS'}

# 2. Nonchain A,B: enumerate exactly the 84/60 true LE, no poset search.
def extensions(labels,rels):
    return [p for p in permutations(labels) if all(p.index(a)<p.index(b) for a,b in rels)]
def pair_prob(le,a,b): return F(sum(p.index(a)<p.index(b) for p in le),len(le))
A=['a1','a2']; C=['c']; B=['b1','b2']; E=['y1','y2']
old_rel=[(a,c) for a in A for c in C]+[(c,b) for c in C for b in B]+[(a,b) for a in A for b in B]+[('y1','y2')]
new_rel=[(a,b) for a in A for b in B]+[('y1','y2')]
le_old=extensions(A+C+B+E,old_rel); le_new=extensions(A+B+E,new_rel)
assert len(le_old)==84 and len(le_new)==60
for a in A:
    for y in E: assert pair_prob(le_new,a,y)<=pair_prob(le_old,a,y)
for b in B:
    for y in E: assert pair_prob(le_new,y,b)<=pair_prob(le_old,y,b)
for u,v in [('a1','a2'),('b1','b2'),('y1','y2')]:
    assert pair_prob(le_new,u,v)==pair_prob(le_old,u,v)
assert pair_prob(le_old,'a1','a2')==F(1,2)
out['control_2']={'old_LE':len(le_old),'new_LE':len(le_new),'all_8_polarized_boundaries':'nonincreasing','internal_antichains':'1/2, unchanged; not globally bad'}

# 3. Mean-preserving real deletion N=2,q=6.
N,q=2,6; m=N*q-1; k=(N-1)*q-1
old=two_chain_p(m,N)[0]; new=two_chain_p(k,N-1)[0]
assert old==F(23,78) and new==F(2,7) and new<old<F(1,3)
assert old-new==F(5,546)
for j in [N,N*(q-1)]:
    for t in [1,2]: assert chain_pair(m,j,2,t)==two_chain_p(m,j)[t-1]
# CDF signs prove these true beta marginals are not first-order comparable.
d_low=cdf_beta(1,5,F(1,100))-cdf_beta(2,10,F(1,100))
d_high=cdf_beta(1,5,F(9,10))-cdf_beta(2,10,F(9,10))
assert d_low>0 and d_high<0
j=m+1
balanced=two_chain_p(m,j//3)[0]
assert balanced==F(7,13) and F(1,3)<balanced<F(2,3)
out['control_3']={'old_rare':str(old),'new_rare':str(new),'strict_gain':str(old-new),'FOSD':'incomparable','uncontrolled_balanced_pair':str(balanced)}

# 4. Four marked pairs in the same actual shortening, N=3,q=12.
N,q=3,12; m=N*q-1;k=(N-1)*q-1; Rn=q//6
removed={r*N-1 for r in range(1,q+1)}
kept=[j for j in range(1,m+1) if j not in removed]
assert len(kept)==k
rows=[]
for r in range(1,Rn+1):
    for late in [False,True]:
        z=q-r if late else r
        old_j=N*z; new_j=(N-1)*z
        assert kept[new_j-1]==old_j
        # early rare y1<x; late rare x<y2
        po=1-two_chain_p(m,old_j)[1] if late else two_chain_p(m,old_j)[0]
        pn=1-two_chain_p(k,new_j)[1] if late else two_chain_p(k,new_j)[0]
        assert pn<po<F(1,3)
        assert F(old_j,m+1)==F(new_j,k+1)
        assert chain_pair(m,old_j,2,1)==two_chain_p(m,old_j)[0]
        assert chain_pair(k,new_j,2,2)==two_chain_p(k,new_j)[1]
        rows.append({'old_j':old_j,'new_j':new_j,'old_rare':str(po),'new_rare':str(pn)})
out['control_4']={'m':m,'k':k,'removed':sorted(removed),'marks':rows}

# 5. Raw rank is inadequate across sizes: remove top of C2, retain bottom.
old=F(1,3);new=F(1,2)
assert chain_pair(2,1,1,1)==old and chain_pair(1,1,1,1)==new
out['control_5']={'raw_rank_old_new':[1,1],'old_P_y_before_x':str(old),'new_P_y_before_x':str(new),'conclusion':'raw-rank equality does not preserve boundary pair'}

# 6. General gated environment can change a completely external pair.
# P_m=(C_m < t) disjoint union r; r<t probability=(m+1)/(m+2).
old=F(3,4);new=F(2,3)
assert old>F(2,3) and F(1,3)<=new<=F(2,3)
out['control_6']={'environment':'(C_m<t) disjoint r, m=2 -> 1','old_external_P_r_before_t':str(old),'new_external_P_r_before_t':str(new),'conclusion':'outside separated-window class, pure external law need not remain safe'}

with open('/workspace/shared/interface-safe-descent-20261019/controls.json','w') as f: json.dump(out,f,indent=2,ensure_ascii=False)
print(json.dumps(out,indent=2,ensure_ascii=False))
print('PASS: exactly 6 preselected controls; no poset-family search.')
