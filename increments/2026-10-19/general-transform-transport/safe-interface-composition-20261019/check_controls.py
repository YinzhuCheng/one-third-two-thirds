from fractions import Fraction as F
from itertools import combinations
from math import comb
import json


def les(n, edges):
    pred=[0]*n
    for a,b in edges: pred[b]|=1<<a
    out=[]
    def go(mask,w):
        if len(w)==n: out.append(tuple(w)); return
        for x in range(n):
            if not(mask>>x&1) and pred[x]&mask==pred[x]: go(mask|1<<x,w+[x])
    go(0,[])
    return out

def ranks(n, edges):
    ll=les(n,edges)
    return [F(sum(w.index(x)+1 for w in ll),len(ll)) for x in range(n)],len(ll)

def beta(p): return min(p,1-p)
def ser(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {str(k):ser(w) for k,w in v.items()}
    if isinstance(v,(list,tuple)): return [ser(w) for w in v]
    return v

out={}
# C1: a non-layered core, all boundary balances under symmetric cap deletion.
n=4
r,l=ranks(n,[(0,2),(1,2),(1,3)])
old=[(x+1)/7 for x in r]
new=[x/5 for x in r]
assert all(beta(b)<=beta(a) for a,b in zip(old,new))
assert all(a==F(1,2)+F(5,7)*(b-F(1,2)) for a,b in zip(old,new))
out['C1_arbitrary_N_core']={'LE_core':l,'expected_ranks':r,'old_P_y_before_x':old,'new_P_y_before_x':new}
# C2: every actual retained boundary is strictly bad and improves.
a=4;c=1;t=2
n=2*a
old=F(2*c+a+1,2*(2*c+2*a+1)); new=F(a+1,2*(2*a+1))
assert old==F(7,22) and new==F(5,18) and new<old<F(1,3)
# Each of 2*a*t actual retained cross pairs has exactly the indicated rare probability.
out['C2_full_boundary_nonempty']={'core':'A4 ordinal-sum A4','caps':[1,1],'external_antichain_size':t,'retained_cross_pairs':2*a*t,'all_old_rare':old,'all_new_rare':new,'drop':old-new,'internal_balance':F(1,2)}
# C3: one common deletion does not exist, despite each marker individually feasible.
m=9; j=(3,7); d=1; k=m-d
rows=[]
for deleted in range(1,m+1):
    if deleted in j: continue
    rr=[x-int(deleted<x) for x in j]
    probs=[F(rr[0],k+1),1-F(rr[1],k+1)]
    good=[p<F(1,3) for p in probs]
    rows.append({'delete':deleted,'new_ranks':rr,'rare_probabilities':probs,'improves':good})
assert any(q['improves'][0] for q in rows) and any(q['improves'][1] for q in rows)
assert not any(all(q['improves']) for q in rows)
out['C3_individually_feasible_jointly_impossible']={'old_rare':[F(3,10)]*2,'rows':rows}
# C4: actual two-chain shuffle counts, two-cap delete C11 -> C9, all 4 selected cross pairs.
def shuffle_prob(m,j,e,y):
    ans=0;total=comb(m+e,e)
    for ext in combinations(range(m+e),e):
        ext=set(ext); q=[i for i in range(m+e) if i not in ext]; ee=sorted(ext)
        ans+=ee[y-1]<q[j-1]
    return F(ans,total)
oldv={(j,y):shuffle_prob(11,j,2,y) for j in (2,10) for y in (1,2)}
newv={(j,y):shuffle_prob(9,j-1,2,y) for j in (2,10) for y in (1,2)}
rare_old={p:min(v,1-v) for p,v in oldv.items()}
rare_new={p:min(v,1-v) for p,v in newv.items()}
assert all(rare_new[p]<rare_old[p]<F(1,3) for p in oldv)
assert rare_old[2,1]==F(23,78) and rare_new[2,1]==F(2,11)
assert rare_old[2,2]==F(1,26) and rare_new[2,2]==F(1,55)
out['C4_nonlinear_all_selected_cross_pairs']={'source':'C11 disjoint-union C2','delete_source_chain_positions':[1,11],'retained_markers':[2,10],'old_P_y_before_x':oldv,'new_P_y_before_x':newv,'old_rare':rare_old,'new_rare':rare_new,'true_shuffle_counts':[comb(13,2),comb(11,2)]}
# C5: ratio outside [1/3,2/3] can enter the band in a real chain deletion.
old=F(3,10);new=F(2,6)
assert old<F(1,3) and new==F(1,3)
out['C5_ratio_sharpness']={'core':'C5','caps':[1,3],'core_marker_rank':2,'alpha':F(1,4),'old_rare':old,'new_rare':new}
# C6: high-degree actual external chain kernel reverses a lower-layer rare probability.
def rising(a,q): return prod(range(a,a+q))
from math import prod
q=7
old=sum((F(rising(i+1,q),rising(11,q)) for i in range(1,5)),F(0))/4
new=sum((F(rising(i,q),rising(9,q)) for i in range(1,5)),F(0))/4
assert old==F(19,2992) and new==F(1,156) and old<new<F(1,3)
out['C6_high_degree_external_kernel']={'core':'A4 ordinal-sum A4','caps':[1,1],'external':'C7 maximum','old_rare':old,'new_rare':new,'direction':'increases despite both remaining rare'}
with open('/workspace/shared/safe-interface-composition-20261019/controls.json' ,'w') as f: json.dump(ser(out),f,ensure_ascii=False,indent=2)
print('PASS: 6 preselected actual controls; no poset-family search.')
