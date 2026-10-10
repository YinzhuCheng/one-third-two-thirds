#!/usr/bin/env python3
from research import *

def vs(mask):
 while mask:
  bit=mask&-mask;yield bit.bit_length()-1;mask-=bit

def connected(graph):
 n=len(graph);seen=1;front=1
 while front:
  nxt=0
  for a in vs(front):nxt|=graph[a]
  front=nxt&~seen;seen|=front
 return seen==(1<<n)-1

def modules(up):
 n=len(up);down=dual(up);full=(1<<n)-1
 def kind(x,y):return 1 if up[x]>>y&1 else -1 if down[x]>>y&1 else 0
 proper_nonchain=[];proper=[]
 for a,b in itertools.combinations(range(n),2):
  s=(1<<a)|(1<<b)
  while True:
   old=s
   for x in vs(full^s):
    if len({kind(x,y) for y in vs(s)})>1:s|=1<<x
   if old==s:break
  if s!=full:
   proper.append(s)
   if not((up[a]|down[a])>>b&1):proper_nonchain.append(s)
 return sorted(set(proper)),sorted(set(proper_nonchain))

def graph_invariants(up):
 n=len(up);down=dual(up);full=(1<<n)-1
 comp=[u|d for u,d in zip(up,down)];inc=[full^(u|d|(1<<i)) for i,(u,d) in enumerate(zip(up,down))]
 proper,nonchain=modules(up)
 # Height valid for arbitrary labels.
 @lru_cache(None)
 def ht(i):return 1+max((ht(j) for j in vs(down[i])),default=0)
 # Width via bipartite maximum matching.
 match={}
 def aug(i,seen):
  for j in vs(up[i]):
   if j in seen:continue
   seen.add(j)
   if j not in match or aug(match[j],seen):match[j]=i;return True
  return False
 width=n-sum(aug(i,set()) for i in range(n))
 covers=cover_edges(up);coverund=[0]*n
 for a,b in covers:coverund[a]|=1<<b;coverund[b]|=1<<a
 return dict(n=n,width=width,height=max(ht(i) for i in range(n)),comparability_connected=connected(comp),incomparability_connected=connected(inc),proper_pair_generated_modules=[list(vs(s)) for s in proper],proper_nonchain_module_witnesses=[list(vs(s)) for s in nonchain],all_proper_modules_chains=not nonchain,cover_edges=[list(x) for x in covers],cover_graph_forest=len(covers)==n-1 if connected(coverund) else None,forced_cycle=directed_cycle(full_graph(up)),vgp_bottom=very_good_pairs(up),vgp_top=very_good_pairs(down))

if __name__=='__main__':
 data=json.loads((OUT/'adaptive_fixed_pair_failures.json').read_text());res=[]
 for d in data:
  r=graph_invariants(dual(d['pred']));r.update(source='adaptive_fixed_pair_failures.json',lengths=d['lengths']);res.append(r)
  print(r)
 (OUT/'adaptive_funnel_checks.json').write_text(json.dumps(res,indent=2)+'\n')
