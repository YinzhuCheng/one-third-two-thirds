#!/usr/bin/env python3
from research import *

def add_tails(pred,maxima,lengths,ordinal=0):
 n=len(pred);out=list(pred);full=(1<<n)-1
 for omit,length in zip(maxima,lengths):
  gate=full^(1<<omit)
  for k in range(length):
   out.append(gate);gate|=1<<(len(out)-1)
 gate=full
 for k in range(ordinal):
  out.append(gate);gate|=1<<(len(out)-1)
 return out

def continuations(pred,n,maxima):
 N=len(pred)
 @lru_cache(None)
 def e(rem):
  if not rem:return 1
  return sum(e(rem^(1<<i)) for i in range(N) if rem>>i&1 and not(pred[i]&rem))
 full=(1<<N)-1;core=(1<<n)-1
 return [e(full^(core^(1<<i))) for i in maxima]

def main():
 data=json.loads((OUT/'initial_profiles.json').read_text());audit=[]
 for r in data:
  p=r['profile'];n=p['n'];up=tuple(r['strict_up_masks']);maxima=p['maxima'];nonmax=((1<<n)-1)^sum(1<<v for v in maxima)
  g=full_graph(up)
  persistent=[row&nonmax if nonmax>>i&1 else 0 for i,row in enumerate(g)]
  cyc=directed_cycle(persistent)
  rr=dict(id=r['id'],nonmax_persistent_cycle=cyc,acyclic_completion=None)
  if not cyc:
   for lens,ordinal in [(tuple(0 for _ in maxima),1)]+[(lens,0) for lens in itertools.product(range(3),repeat=len(maxima)) if any(lens)]:
    pred=add_tails(p['pred'],maxima,lens,ordinal);pu=dual(pred);fg=full_graph(pu)
    if not directed_cycle(fg):
     B=continuations(pred,n,maxima);den=sum(f*b for f,b in zip(p['F'],B));probs=[Q(sum(a*b for a,b in zip(row,B)),den) for row in p['A']]
     vg=[very_good_pairs(pu),very_good_pairs(dual(pu))]
     if any(vg):raise ValueError('cycle checker mismatch')
     rr['acyclic_completion']=dict(tail_lengths=list(lens),ordinal_tail_length=ordinal,pred=pred,B=B,pair_probabilities=list(map(str,probs)),forced_graph=fg,very_good_pairs=vg)
     break
  audit.append(rr)
  print(rr['id'],'persistent',cyc,'completion',None if not rr['acyclic_completion'] else (rr['acyclic_completion']['tail_lengths'],rr['acyclic_completion']['ordinal_tail_length']),flush=True)
 (OUT/'completion_checks.json').write_text(json.dumps(audit,indent=2)+'\n')
 # Fixed-pair failure witnesses for adaptive class, arbitrary chain lengths
 for r in data:
  if r['id']!='n8c15-primal':continue
  p=r['profile'];rr=[]
  for pairindex in r['selected']:
   found=[]
   for length in range(1,31):
    for j in range(len(p['maxima'])):
     lens=[0]*len(p['maxima']);lens[j]=length
     pred=add_tails(p['pred'],p['maxima'],lens);pu=dual(pred)
     B=continuations(pred,p['n'],p['maxima']);den=sum(f*b for f,b in zip(p['F'],B));pr=Q(sum(a*b for a,b in zip(p['A'][pairindex],B)),den)
     if not Q(1,3)<=pr<=Q(2,3):
      found.append(dict(pair=p['pairs'][pairindex],lengths=lens,pred=pred,B=B,probability=str(pr),cycle=directed_cycle(full_graph(pu)),vgp=[very_good_pairs(pu),very_good_pairs(dual(pu))]))
    if found:break
   rr.extend(found)
  (OUT/'adaptive_fixed_pair_failures.json').write_text(json.dumps(rr,indent=2)+'\n')
  print('ADAPTIVE FIXED FAILURES',rr)
if __name__=='__main__':main()
