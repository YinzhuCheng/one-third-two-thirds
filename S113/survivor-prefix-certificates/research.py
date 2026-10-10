#!/usr/bin/env python3
from pathlib import Path
import json,sys,itertools
from functools import lru_cache
from fractions import Fraction as Q
sys.path.insert(0,'/workspace/shared/poset-prefix-width3-search')
from certify import lp,verify_cells,verify_profile
sys.path.insert(0,'/workspace/shared/prime-core-catalogue')
from catalogue import dual, cover_edges, forced_good_edges, directed_cycle, very_good_pairs
OUT=Path(__file__).resolve().parent

def profile(up):
 n=len(up); pred=list(dual(up)); full=(1<<n)-1
 maxima=[i for i,u in enumerate(up) if not u]
 ideals=[full^(1<<v) for v in maxima]; common=full
 for s in ideals:common&=s
 pairs=[list(p) for p in itertools.combinations(range(n),2) if all(common>>v&1 for v in p) and not ((up[p[0]]|pred[p[0]])>>p[1]&1)]
 @lru_cache(None)
 def e(rem,x=-1,y=-1):
  if not rem:return 1
  return sum(e(rem^(1<<v),x,y) for v in range(n) if rem>>v&1 and not(pred[v]&rem) and not(v==y and rem>>x&1))
 F=[e(s) for s in ideals]; A=[[e(s,x,y) for s in ideals] for x,y in pairs]
 p=dict(n=n,r=n-1,pred=pred,covers_edges=[list(e) for e in cover_edges(up)],maxima=maxima,ideals=ideals,pairs=pairs,F=F,A=A,covers=True)
 if pairs:verify_profile(p)
 return p

def full_graph(up):
 g=list(up)
 for a,b in forced_good_edges(up):g[a]|=1<<b
 for b,a in forced_good_edges(dual(up)):g[a]|=1<<b
 return g

def test(p):
 F,A=p['F'],p['A']
 fixed=[i for i,row in enumerate(A) if all(f<=3*a<=2*f for f,a in zip(F,row))]
 if fixed:
  selected=[fixed[0]];cells=[lp(F,[A[selected[0]]],x) for x in ('L','H')]
  return dict(covered=True,selected=selected,fixed_pairs=fixed,cells=cells)
 for k in (2,3):
  for selected in itertools.combinations(range(len(A)),k):
   cells=[]
   for x in itertools.product('LH',repeat=k):
    c=lp(F,[A[i] for i in selected],x);cells.append(c)
    if Q(c['optimum'])>0:break
   else:return dict(covered=True,selected=list(selected),fixed_pairs=[],cells=cells)
 return dict(covered=False,fixed_pairs=[])

def main():
 data=json.loads(Path('/workspace/shared/prime-core-catalogue-independent-audit/orbit_and_singleton_audit.json').read_text())
 result=[]
 for i,c in enumerate(data['classes']):
  for direction in ('primal','dual'):
   up=tuple(c['representative_masks']);up=up if direction=='primal' else dual(up)
   p=profile(up);r=test(p)
   r.update(id=f'n{len(up)}c{i:02d}-{direction}',class_index=i,direction=direction,strict_up_masks=list(up),profile=p,core_cycle=directed_cycle(full_graph(up)),core_vgp_bottom=very_good_pairs(up),core_vgp_top=very_good_pairs(dual(up)))
   result.append(r)
   print(r['id'],'max',p['maxima'],'pairs',len(p['pairs']),'covered',r['covered'],'selected',[p['pairs'][j] for j in r.get('selected',[])],'fixed',r['fixed_pairs'],'cycle',r['core_cycle'],flush=True)
   (OUT/'initial_profiles.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
