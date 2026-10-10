#!/usr/bin/env python3
from check import *

def check_invariants(pred,a):
 d,u,covers=from_pred(pred);s=structure(d,u);g=graph(d,u)[0];n=len(d)
 for key in ('width','height','comparability_connected','incomparability_connected','cover_graph_forest'):need(a[key]==s[key],'author invariant '+key)
 need(a['n']==n,'invariant size');need(a['all_proper_modules_chains']==(not s['proper_nonchain_module_witnesses']),'module assertion')
 modules=sorted({tuple(sorted(module_closure(x,y,d,u))) for x,y in combinations(range(n),2) if len(module_closure(x,y,d,u))<n})
 need(sorted(map(tuple,a['proper_pair_generated_modules']))==modules,'complete proper pair modules')
 need(sorted(map(tuple,a['proper_nonchain_module_witnesses']))==s['proper_nonchain_module_witnesses'],'module nonchain witnesses')
 need(a['cover_edges']==covers,'covers');need(a['vgp_bottom']==s['very_good_pairs'][0] and a['vgp_top']==s['very_good_pairs'][1],'invariant VGP')
 need((a['forced_cycle'] is None)==(topo(g) is not None),'invariant graph')
 if a['forced_cycle'] is not None:need(cycle_valid(a['forced_cycle'],g),'invariant cycle')
 return s

def main():
 src=ROOT/'author_snapshot';w=json.loads((src/'exact_23_vertex_witness.json').read_text());pred=w['pred'];d,u,covers=from_pred(pred);n=len(d);orders=list(extensions(d));rows=[]
 for x,y in combinations(range(n),2):
  if not incompar(x,y,u):continue
  numerator=sum(o.index(x)<o.index(y) for o in orders);rows.append(dict(pair=[x,y],numerator=numerator,denominator=len(orders),probability=str(Q(numerator,len(orders)))))
 need(rows==w['all_incomparable_pair_probabilities'],'complete full-poset pair table');need(w['extension_count']==len(orders),'full witness extensions')
 need(w['strict_up_masks']==list(map(mask,u)),'full upset table');degree=[[len(d[x]),len(u[x])] for x in range(n)];need(degree==w['degree_pairs'] and len(set(map(tuple,degree)))==n,'degree rigidity')
 need(w['all_degree_pairs_distinct'] is True and w['automorphism_order']==1,'rigidity flags')
 g,lo,hi=graph(d,u);need(list(map(mask,g))==w['full_forced_graph'],'full actual graph');need(sorted(lo)==sorted(w['lower_forced_edges']) and sorted(hi)==sorted(w['upper_forced_edges']),'all structural rule edges')
 inv=check_invariants(pred,w['invariants'])
 ref=json.loads((ROOT/'results.json').read_text())['adaptive_fixed_pair_failures'][1]
 need(w['core_pred']==pred[:8] and w['rank7_states']==[239,127] and w['F']==[48,73] and w['B']==[16,1],'cut export')
 need(list(map(rat,w['mu']))==[Q(768,841),Q(73,841)],'mu export')
 need(w['selected_pairs']==[[2,5],[2,6]] and w['selected_pair_probabilities']==['424/841','280/841'],'selected export')
 f=json.loads((src/'family_invariants.json').read_text());degs=[n-1-len(d[i])-len(u[i]) for i in range(n)]
 need(degs==f['incomparability_degrees'] and f['pi']==max(degs)==18 and f['maximizers']==[4],'pi export')
 quotient=json.loads((src/'nine_vertex_tail_quotient.json').read_text());qd,qu,_=from_pred(quotient['pred']);qs=check_invariants(quotient['pred'],quotient['invariants']);need(quotient['strict_up_masks']==list(map(mask,qu)),'quotient up masks')
 need(quotient['degree_pairs']==[[len(qd[i]),len(qu[i])] for i in range(9)] and quotient['automorphism_order']==qs['automorphism_count']==1,'quotient rigidity')
 ports=[set() for _ in range(18)]
 for i in range(9):ports[2*i].add(2*i+1)
 for i in range(9):
  for j in qu[i]:ports[2*i+1].add(2*j)
 _,ql,qh=graph(qd,qu)
 for i,j in ql:ports[2*i].add(2*j)
 for i,j in qh:ports[2*i+1].add(2*j+1)
 need(topo(ports) is not None and quotient['two_port_graph_acyclic'] is True,'two-port graph')
 balanced=[r for r in rows if Q(1,3)<=rat(r['probability'])<=Q(2,3)];need(len(balanced)==8,'balanced pair number')
 out=dict(verdict='PASS',all_incomparable_pair_probabilities=rows,balanced_pairs=balanced,invariants=inv,quotient_two_port_topological_order=topo(ports),checked_final_author_files=['exact_23_vertex_witness.json','nine_vertex_tail_quotient.json','family_invariants.json'])
 (ROOT/('final_witness_results_optimized.json' if sys.flags.optimize else 'final_witness_results.json')).write_text(json.dumps(out,indent=2)+'\n')
 print('PASS all 27 incomparable pair counts, 8 balanced pairs, complete rule graphs, modules, rigidity, quotient two-port DAG, pi=18')
if __name__=='__main__':main()
