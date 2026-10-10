#!/usr/bin/env python3
"""Necessary weight restrictions for a fixed surviving core.
Formal ports B_i,T_i are identified ONLY for indices asserted to have weight 1.
Internal weak loops created by that identification are omitted. Interblock arcs
remain strict. Cyclicity excludes every weight vector obeying those equalities.
"""
import json,itertools
from pathlib import Path
import catalogue as c


def contracted_graph(up,singletons):
    n=len(up);full=c.two_port_graph(up)
    representative={v:(v-1 if v%2 and (v//2 in singletons) else v) for v in range(2*n)}
    nodes=sorted(set(representative.values()));lookup={v:i for i,v in enumerate(nodes)}
    graph=[0]*len(nodes)
    for a in range(2*n):
        for b in c.vertices(full[a]):
            x,y=lookup[representative[a]],lookup[representative[b]]
            if x==y:
                assert a//2==b//2 and a%2==0 and b==a+1
                continue
            graph[x]|=1<<y
    return tuple(graph),nodes


def analyze(up):
    n=len(up);forbidden=[];allowed=[]
    for k in range(n+1):
        for S in itertools.combinations(range(n),k):
            graph,nodes=contracted_graph(up,set(S));cy=c.directed_cycle(graph)
            if cy:
                if not any(set(d['singleton_vertices'])<=set(S) for d in forbidden):
                    forbidden.append({'singleton_vertices':list(S),'cycle_representative_ports':[nodes[a] for a in cy]})
            else:allowed.append(S)
    max_singletons=max(map(len,allowed));max_sets=[list(S) for S in allowed if len(S)==max_singletons]
    return {'strict_up_masks':list(up),'minimal_forbidden_singleton_subsets':forbidden,'max_number_of_singleton_blocks_passing_port_filter':max_singletons,'maximal_size_allowed_singleton_subsets':max_sets,'necessary_number_of_nonsingleton_blocks':n-max_singletons,'necessary_total_inflation_size_from_this_filter':n+(n-max_singletons),'interpretation':'For every listed forbidden subset S, a counterexample inflation must have at least one i in S with weight_i >= 2. This is a necessary constraint only, not a sufficiency claim.'}

if __name__=='__main__':
    base=Path(__file__).parent
    data=json.loads((base/'n7_survivor_isomorphism_classes.json').read_text())
    results=[analyze(d['representative_naturally_labelled']['strict_up_masks']) for d in data]
    (base/'n7_singleton_constraints.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
