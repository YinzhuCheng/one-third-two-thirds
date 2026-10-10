#!/usr/bin/env python3
"""Exact naturally labelled prime-core catalogue. Python 3.10+, standard library only.
All algorithms here are original for this catalogue, independently checking earlier
module experiments in ../minimal-counterexample-reductions (read-only reference).
A relation is represented by strict upper-set bit masks; vertices are 0,...,n-1.
"""
import argparse, hashlib, json, time
from collections import Counter
from itertools import combinations
from pathlib import Path


def vertices(mask):
    while mask:
        bit=mask&-mask; yield bit.bit_length()-1; mask-=bit


def dual(up):
    return tuple(sum(1<<i for i in range(len(up)) if up[i]>>j&1) for j in range(len(up)))


def naturally_labelled(n):
    """Append largest label n-1 with an arbitrary ideal as its down-set.
    Induction gives each transitive subset of i<j exactly once; no quotienting.
    """
    if n==0: yield (); return
    for old in naturally_labelled(n-1):
        down=dual(old)
        for mask in range(1<<(n-1)):
            if all(down[x]&~mask==0 for x in vertices(mask)):
                yield tuple(r|((1<<(n-1)) if mask>>x&1 else 0) for x,r in enumerate(old))+(0,)


def autonomous_module(up,mask,down=None):
    if down is None: down=dual(up)
    outside=((1<<len(up))-1)^mask
    return all((up[x]&mask) in (0,mask) and (down[x]&mask) in (0,mask) for x in vertices(outside))


def proper_module(up):
    down=dual(up); n=len(up)
    for mask in range(1,(1<<n)-1):
        if mask.bit_count()>1 and autonomous_module(up,mask,down): return mask
    return None


def is_chain(up,mask,down=None):
    if down is None: down=dual(up)
    return all(mask&~(up[x]|down[x]|(1<<x))==0 for x in vertices(mask))


def width(up):
    return max(mask.bit_count() for mask in range(1<<len(up))
               if all(up[x]&mask==0 for x in vertices(mask)))


def very_good_pairs(up):
    """Zaguia Definition 5 in the supplied orientation, not automatically dual."""
    down=dual(up)
    return [(a,b) for a,b in combinations(range(len(up)),2)
            if down[a]==down[b] and is_chain(up,up[a]&~up[b],down)
            and is_chain(up,up[b]&~up[a],down)]


def forced_good_edges(up):
    """Structural Definition 1(i) edges, lifted to BOTTOM ports of this order.
    Counterexample assumption forces their probability >2/3 by Theorem 2.
    On dual(up), the bottom ports are TOP ports of the original order.
    """
    down=dual(up)
    return [(a,b) for a in range(len(up)) for b in range(len(up))
            if a!=b and not ((up[a]|down[a])>>b&1)
            and down[a]&~down[b]==0 and is_chain(up,up[b]&~up[a],down)]


def forced_graph(up):
    out=list(up)
    for a,b in forced_good_edges(up): out[a]|=1<<b
    return tuple(out)


def directed_cycle(graph):
    n=len(graph); state=[0]*n; stack=[]
    def dfs(x):
        state[x]=1; stack.append(x)
        for y in vertices(graph[x]):
            if state[y]==1:return stack[stack.index(y):]+[y]
            if state[y]==0:
                c=dfs(y)
                if c:return c
        stack.pop();state[x]=2
        return None
    for x in range(n):
        if state[x]==0:
            c=dfs(x)
            if c:return c
    return None


def two_port_graph(up):
    """All-weight graph: vertices 2i=B_i, 2i+1=T_i, never identified.
    Internal B_i->T_i is weak when weight=1; all interblock arcs are strict.
    A directed cycle must contain an interblock arc, so any cycle rejects.
    """
    n=len(up); graph=[0]*(2*n)
    for i in range(n): graph[2*i]|=1<<(2*i+1)
    for a in range(n):
        for b in vertices(up[a]):
            for x in (2*a,2*a+1):graph[x]|=(1<<(2*b))|(1<<(2*b+1))
    for a,b in forced_good_edges(up):graph[2*a]|=1<<(2*b)
    for a,b in forced_good_edges(dual(up)):graph[2*b+1]|=1<<(2*a+1)
    return tuple(graph)


def cover_edges(up):
    down=dual(up)
    return [(a,b) for a in range(len(up)) for b in vertices(up[a]) if not(up[a]&down[b])]


def height(up):
    # Natural labels are a topological ordering; only called for natural inputs.
    h=[1]*len(up)
    for a in range(len(up)):
        for b in vertices(up[a]):h[b]=max(h[b],h[a]+1)
    return max(h,default=0)


def describe(up):
    down=dual(up); bottom=forced_graph(up); top_dual=forced_graph(down)
    return {'n':len(up),'strict_up_masks':list(up),'cover_edges':cover_edges(up),
            'width':width(up),'height':height(up),
            'very_good_bottom_pairs':very_good_pairs(up),'very_good_top_pairs':very_good_pairs(down),
            'forced_good_bottom_edges':forced_good_edges(up),
            'forced_good_top_edges_dual_orientation':forced_good_edges(down),
            'bottom_cycle':directed_cycle(bottom),'top_cycle_dual_orientation':directed_cycle(top_dual),
            'two_port_cycle':directed_cycle(two_port_graph(up))}


def enumerate_catalogue(max_n,out):
    start=time.monotonic(); reports=[]; survivors=[]; cycle_extra=[]; two_port_extra=[]
    for n in range(1,max_n+1):
        t=time.monotonic(); c=Counter(); by_width=Counter(); by_height=Counter()
        for up in naturally_labelled(n):
            c['naturally_labelled_posets']+=1
            if proper_module(up) is not None: continue
            c['prime_cores']+=1
            w=width(up)
            if w<3:continue
            c['prime_width_at_least_3']+=1
            vg_b=very_good_pairs(up); down=dual(up); vg_t=very_good_pairs(down)
            if vg_b:c['excluded_very_good_bottom']+=1
            if vg_t:c['excluded_very_good_top']+=1
            if vg_b or vg_t:continue
            c['after_very_good_both_sides']+=1
            cyc_b=directed_cycle(forced_graph(up));cyc_t=directed_cycle(forced_graph(down))
            if cyc_b:c['excluded_bottom_cycle_after_very_good']+=1
            if cyc_t:c['excluded_top_cycle_after_very_good']+=1
            if cyc_b or cyc_t:
                c['excluded_either_cycle_after_very_good']+=1
                cycle_extra.append(describe(up));continue
            c['after_separate_port_cycles']+=1
            if directed_cycle(two_port_graph(up)):
                c['excluded_two_port_cycle_after_separate']+=1
                two_port_extra.append(describe(up));continue
            c['after_all_uniform_filters']+=1;by_width[w]+=1;by_height[height(up)]+=1
            survivors.append(describe(up))
        keys=['naturally_labelled_posets','prime_cores','prime_width_at_least_3','excluded_very_good_bottom','excluded_very_good_top','after_very_good_both_sides','excluded_bottom_cycle_after_very_good','excluded_top_cycle_after_very_good','excluded_either_cycle_after_very_good','after_separate_port_cycles','excluded_two_port_cycle_after_separate','after_all_uniform_filters']
        r={'n':n,**{k:c[k] for k in keys},'survivors_by_width':dict(sorted(by_width.items())),'survivors_by_height':dict(sorted(by_height.items())),'elapsed_seconds':round(time.monotonic()-t,3)}
        reports.append(r);print(json.dumps(r),flush=True)
    survivors.sort(key=lambda d:(d['n'],d['width'],len(d['cover_edges']),sum(x.bit_count() for x in d['strict_up_masks']),d['strict_up_masks']))
    cycle_extra.sort(key=lambda d:(d['n'],d['width'],len(d['cover_edges']),d['strict_up_masks']))
    result={'scope':'Naturally labelled strict partial orders on 0,...,n-1; not unlabelled counts. All weights are positive integers and are universally quantified by each structural filter. No weighted probability cutoff was used.','max_n':max_n,'counts':reports,'total_elapsed_seconds':round(time.monotonic()-start,3),'cycle_beyond_very_good_count':len(cycle_extra),'two_port_beyond_separate_count':len(two_port_extra),'survivor_count':len(survivors),'limitations':['Survivors are only candidates for further analysis, not counterexamples.','The finite enumeration implies no universal bound on core order or chain weights.','No unweighted automorphism or height-two exclusion is applied.','Bottom and top ports are never merged.']}
    out.mkdir(parents=True,exist_ok=True)
    for name,data in [('summary.json',result),('survivors.json',survivors),('cycle_beyond_very_good.json',cycle_extra),('two_port_beyond_separate.json',two_port_extra)]:
        (out/name).write_text(json.dumps(data,indent=2)+'\n')
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--max-n',type=int,default=7);ap.add_argument('--out',type=Path,default=Path(__file__).parent/'results')
    args=ap.parse_args();enumerate_catalogue(args.max_n,args.out)
