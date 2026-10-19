"""Independent full-poset sparse ideal DP for existing case1, m=0,1,2,5.
Does not use the producer's side DP, window stitching, or interval solver.
"""
from pathlib import Path
from math import comb
import json,time
OUT=Path(__file__).resolve().parent

def graph(case,m):
 nodes=[];edges=[]
 for side,sz in [('D',case['D_sizes']),('U',case['U_reverse_sizes'])]:
  for ch,n in enumerate(sz):
   nodes.extend((side,ch,j) for j in range(1,n+1))
   for j in range(1,n):
    edges.append(((side,ch,j),(side,ch,j+1)) if side=='D' else ((side,ch,j+1),(side,ch,j)))
 nodes += [('I',0),('I',1)]+[('C',j) for j in range(1,m+1)]
 for side in ['D','U']:
  for a,b in case[side+'_bridges' if side=='D' else 'U_reverse_bridges']:
   x=(side,*a);y=(side,*b);edges.append((x,y) if side=='D' else (y,x))
 for ch,n in enumerate(case['D_sizes']):
  for uh,un in enumerate(case['U_reverse_sizes']):edges.append((('D',ch,n),('U',uh,un)))
 if m:
  for ch,n in enumerate(case['D_sizes']):edges.append((('D',ch,n),('C',1)))
  for j in range(1,m):edges.append((('C',j),('C',j+1)))
  for ch,n in enumerate(case['U_reverse_sizes']):edges.append((('C',m),('U',ch,n)))
 for i in range(2):
  for ch,j in enumerate(case['D_gate_raw'][i]):
   if j:edges.append((('D',ch,j),('I',i)))
  for ch,j in enumerate(case['U_reverse_gate_raw'][i]):
   if j:edges.append((('I',i),('U',ch,j)))
 if case['I_chain']:edges.append((('I',0),('I',1)))
 ids={x:i for i,x in enumerate(nodes)};pred=[0]*len(nodes)
 for a,b in edges:pred[ids[b]]|=1<<ids[a]
 events=[]
 for p in case['pairs']:
  if p.get('skip'):continue
  k=p['kind']
  if k=='D':a=('D',*p['source']);b=('D',*p['target'])
  if k=='Ureverse':a=('U',*p['target']);b=('U',*p['source'])
  if k=='DI':a=('D',*p['source']);b=('I',p['target'])
  if k=='IU':a=('I',p['source']);b=('U',*p['target'])
  if k=='II':a=('I',p['source']);b=('I',p['target'])
  events.append((ids[a],ids[b]))
 return nodes,pred,events

def direct_counts(case,m):
 nodes,pred,events=graph(case,m);n=len(nodes);dim=len(events)+1
 dp={0:[1]*dim};states=1;maxlayer=1
 for rank in range(n):
  nxt={}
  for mask,vs in dp.items():
   for x in range(n):
    bit=1<<x
    if mask&bit or pred[x]&~mask:continue
    vals=nxt.setdefault(mask|bit,[0]*dim);vals[0]+=vs[0]
    for k,(a,b) in enumerate(events,1):
     if x!=b or mask&(1<<a):vals[k]+=vs[k]
  dp=nxt;states+=len(dp);maxlayer=max(maxlayer,len(dp))
 assert set(dp)=={(1<<n)-1}
 return dp[(1<<n)-1],states,maxlayer

def main():
 case=json.loads((OUT/'frozen_cases.json').read_text())[0]
 row=json.loads((OUT/'all_counts.json').read_text())[0]
 polys=[row['total']]+[e['event'] for e in row['counts']]
 results=[];start=time.monotonic()
 for m in [0,1,2,5]:
  observed,states,layer=direct_counts(case,m)
  expected=[a+b*(m+1)+c*comb(m+2,2) for a,b,c in polys]
  assert observed==expected,(m,observed,expected)
  results.append(dict(m=m,n=case['n']+m,total=observed[0],event_counts=observed[1:],visited_ideals=states,max_layer_ideals=layer,all_match=True))
  print('PASS',m,'ideals',states,'total',observed[0],flush=True)
 out=dict(case_index=1,method='independent sparse full-poset ideal DP; no window formula',checks=results,elapsed_seconds=time.monotonic()-start,pass_all=True)
 (OUT/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
