#!/usr/bin/env python3
from funnel_check import *
from completions import add_tails,continuations

def counts(pred):
 n=len(pred);full=(1<<n)-1
 @lru_cache(None)
 def e(rem,x=-1,y=-1):
  if not rem:return 1
  return sum(e(rem^(1<<i),x,y) for i in range(n) if rem>>i&1 and not(pred[i]&rem) and not(i==y and rem>>x&1))
 E=e(full);up=dual(pred)
 pp=[dict(pair=[x,y],numerator=e(full,x,y),denominator=E,probability=str(Q(e(full,x,y),E))) for x,y in itertools.combinations(range(n),2) if not((pred[x]|up[x])>>y&1)]
 return E,pp

def main():
 r=next(r for r in json.loads((OUT/'initial_profiles.json').read_text()) if r['id']=='n8c15-primal');p=r['profile']
 pred=add_tails(p['pred'],p['maxima'],[15,0]);up=dual(pred);inv=graph_invariants(up);E,pp=counts(pred)
 degs=[[p.bit_count(),u.bit_count()] for p,u in zip(pred,up)]
 rigid=len(set(map(tuple,degs)))==len(pred)
 B=continuations(pred,8,[4,7]);pi=[Q(f*b,E) for f,b in zip(p['F'],B)]
 result=dict(name='P15 guarded chain witness',source_profile_id=r['id'],core_pred=p['pred'],tail_definition='15-chain z1<...<z15, each zi above exactly core C minus {4}, and incomparable with core 4',pred=pred,strict_up_masks=list(up),extension_count=E,rank7_states=p['ideals'],F=p['F'],B=B,mu=list(map(str,pi)),selected_pairs=[p['pairs'][j] for j in r['selected']],selected_pair_probabilities=[next(x['probability'] for x in pp if x['pair']==p['pairs'][j]) for j in r['selected']],all_incomparable_pair_probabilities=pp,degree_pairs=degs,all_degree_pairs_distinct=rigid,automorphism_order=1 if rigid else None,full_forced_graph=full_graph(up),lower_forced_edges=forced_good_edges(up),upper_forced_edges=[(b,a) for a,b in forced_good_edges(dual(up))],invariants=inv)
 if not rigid:raise ValueError('rigidity claim failed')
 if E!=841 or pi!=[Q(768,841),Q(73,841)]:raise ValueError('count check failed')
 if inv['forced_cycle'] or inv['vgp_bottom'] or inv['vgp_top'] or not inv['all_proper_modules_chains'] or not inv['comparability_connected'] or not inv['incomparability_connected']:raise ValueError('funnel failed')
 (OUT/'exact_23_vertex_witness.json').write_text(json.dumps(result,indent=2)+'\n')
 # Nine-vertex quotient with the tail contracted to a singleton.
 qpred=add_tails(p['pred'],p['maxima'],[1,0]);qup=dual(qpred);qi=graph_invariants(qup)
 qdegs=[[p.bit_count(),u.bit_count()] for p,u in zip(qpred,qup)]
 q=dict(pred=qpred,strict_up_masks=list(qup),invariants=qi,degree_pairs=qdegs,automorphism_order=1 if len(set(map(tuple,qdegs)))==len(qdegs) else None,two_port_graph_acyclic=directed_cycle(__import__('catalogue').two_port_graph(qup)) is None)
 (OUT/'nine_vertex_tail_quotient.json').write_text(json.dumps(q,indent=2)+'\n')
 print('Frozen P15: E=',E,'mu=',pi,'selected probabilities=',result['selected_pair_probabilities'],'rigid=',rigid,'balanced pair count=',sum(Q(1,3)<=Q(x['probability'])<=Q(2,3) for x in pp))
if __name__=='__main__':main()
