#!/usr/bin/env python3
"""Checks the one author-proposed chain-tail family; no broad poset search."""
from check import *

def main():
 rows=json.loads((ROOT/'author_snapshot/initial_profiles.json').read_text());r=next(x for x in rows if x['id']=='n8c15-primal');base=r['profile']['pred'];qpred=base+[239];d,u,covers=from_pred(qpred)
 proper_modules=[]
 for bits in range(1,1<<9):
  s=set(members(bits,9))
  if not 2<=len(s)<9:continue
  if all(len({1 if x in u[v] else -1 if x in d[v] else 0 for x in s})==1 for v in set(range(9))-s):proper_modules.append(sorted(s))
 need(not proper_modules,'9-point quotient not prime')
 quotient=structure(d,u);need(quotient['automorphism_count']==1,'quotient not rigid');need(quotient['full_forced_topological_order'] is not None,'quotient graph cyclic')
 degree_pairs=[(len(d[v]),len(u[v])) for v in range(9)];need(len(set(degree_pairs))==9,'distinct degree-pair rigidity proof unavailable')
 tests=[]
 for k in (1,2,3,4,15,31):
  pred=base+[239|sum(1<<j for j in range(8,8+i)) for i in range(k)]
  w=dict(pred=pred,B=[k+1,1]);a=completion_check(r,w);s=a['structural'];d,u,_=from_pred(pred);g=graph(d,u)[0]
  rankorder=[1,0,3,6,2,5,4,7]+list(range(8,8+k));rank={v:i for i,v in enumerate(rankorder)}
  need(all(rank[x]<rank[y] for x in range(8+k) for y in g[x]),'symbolic topological ordering fails')
  need(s['maximum_incomparability_degree']==max(5,k+3) and s['height']==k+4 and s['width']==3,'dimension formula')
  need(s['comparability_connected'] and s['incomparability_connected'] and not s['proper_nonchain_module_witnesses'] and s['automorphism_count']==1,'family structural claim')
  need(s['very_good_pairs']==[[],[]],'family VGP')
  need(a['extensions']==48*k+121,'extension count formula')
  need(rat(a['pair_probabilities'][4])==Q(23*k+79,48*k+121),'first probability formula')
  need(rat(a['pair_probabilities'][5])==Q(15*k+55,48*k+121),'second probability formula')
  need(s['passes_requested_structural_funnel']==(k>=4),'funnel threshold')
  tests.append(a)
 # Explicitly match the two adaptive profiles by relabeling the full directed order.
 other=next(x for x in rows if x['id']=='n8c13-dual');d0,u0,_=from_pred(base);d1,u1,_=from_pred(other['profile']['pred']);isos=[]
 for perm in permutations(range(8)):
  if all(len(d0[i])==len(d1[perm[i]]) and len(u0[i])==len(u1[perm[i]]) for i in range(8)) and all({perm[j] for j in u0[i]}==u1[perm[i]] for i in range(8)):isos.append(list(perm))
 need(len(isos)==1,'adaptive profile isomorphism')
 out=dict(verdict='PASS',quotient_pred=qpred,quotient_covers=covers,quotient_structure=quotient,quotient_degree_pairs=degree_pairs,exhaustive_quotient_proper_modules=proper_modules,adaptive_isomorphism_from_n8c15_primal_to_n8c13_dual=isos[0],family_tests=tests,formulas=dict(vertices='k+8',extension_count='48k+121',B=['k+1','1'],p_2_before_5='(23k+79)/(48k+121)',p_2_before_6='(15k+55)/(48k+121)',height='k+4',width='3',pi='max(5,k+3)',passes_requested_funnel='k>=4',second_selected_pair_unbalanced='k>=15'))
 (ROOT/('family_results_optimized.json' if sys.flags.optimize else 'family_results.json')).write_text(json.dumps(out,indent=2)+'\n')
 print('PASS quotient exhaustive modules, unique degree pairs, adaptive isomorphism:',isos[0]);print('PASS finite family controls:',[1,2,3,4,15,31]);print(json.dumps(out['formulas'],indent=2))
if __name__=='__main__':main()
