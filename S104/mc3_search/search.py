import random,json,time,itertools
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
OUT=Path(__file__).parent

def build(lens,extra):
 ch=[];n=0
 for m in lens:ch.append(list(range(n,n+m)));n+=m
 x,y,b1,b2=ch[0][0],ch[1][0],ch[2][0],ch[2][1]
 edges=[(a,b) for c in ch for a,b in zip(c,c[1:])]+extra
 pred=[0]*n
 for a,b in edges:pred[b]|=1<<a
 for k in range(n):
  for b in range(n):
   if pred[b]>>k&1:pred[b]|=pred[k]
 if any(pred[b]>>b&1 for b in range(n)):return
 if pred[x] or pred[y] or pred[b1] or pred[b2]!=(1<<b1):return
 B=[b for b in range(n) if b not in [x,y] and not(pred[b]>>x&1 or pred[b]>>y&1)]
 if B!=[b1,b2]:return
 return ch,pred,edges

def analyze(model,detail=False):
 ch,pred,edges=model;lens=tuple(map(len,ch));n=len(pred);loc={v:(c,i) for c,chain in enumerate(ch) for i,v in enumerate(chain)}
 x,y,b1,b2=ch[0][0],ch[1][0],ch[2][0],ch[2][1]
 pairs=[(b1,x),(b1,y),(b2,x),(b2,y),(x,y)]
 req=[tuple(max([i+1 for i,v in enumerate(c) if pred[z]>>v&1],default=0) for c in ch) for z in range(n)]
 @lru_cache(None)
 def moves(s):
  ans=[]
  for c in range(3):
   if s[c]<lens[c]:
    z=ch[c][s[c]]
    if all(s[k]>=req[z][k] for k in range(3)):
     t=list(s);t[c]+=1;ans.append((z,tuple(t)))
  return ans
 @lru_cache(None)
 def F(s):return 1 if s==lens else sum(F(t) for z,t in moves(s))
 E=F((0,0,0));K=[0]*5;layer={(0,0,0):1}
 for _ in range(n):
  nxt={}
  for s,H in layer.items():
   for z,t in moves(s):
    nxt[t]=nxt.get(t,0)+H
    for j,(a,b) in enumerate(pairs):
     if z==a and s[loc[b][0]]<=loc[b][1]:K[j]+=H*F(t)
  layer=nxt
 assert layer[lens]==E
 premise=3*K[0]>2*E and 3*K[1]>2*E
 good=[j for j,k in enumerate(K) if E<=3*k<=2*E]
 # MC3 counterexample exactly premise and no good.
 out={'n':n,'shape':lens,'E':E,'K':K,'probabilities':[str(Fraction(k,E)) for k in K],'premise':premise,'good':good,'states':F.cache_info().currsize}
 if detail:out.update(chains=ch,pred=pred,edges=edges,pairs=pairs)
 return out

def generate(lens,rng,density):
 base=build(lens,[])
 ch=[];n=0
 for m in lens:ch.append(list(range(n,n+m)));n+=m
 x,y,b1,b2=ch[0][0],ch[1][0],ch[2][0],ch[2][1]
 # Root x,y,b1 precede every tail in this chosen topological order.
 tails=[c[1:] for c in ch[:2]]+[ch[2][1:]];order=[x,y,b1]
 while any(tails):
  c=rng.choice([c for c in range(3) if tails[c]]);order.append(tails[c].pop(0))
 rank={z:i for i,z in enumerate(order)};chain={z:c for c,ls in enumerate(ch) for z in ls};extra=[]
 if len(ch[2])>2:extra.append((rng.choice([x,y]),ch[2][2]))
 for i,a in enumerate(order):
  for b in order[i+1:]:
   if chain[a]==chain[b] or b in [x,y,b1,b2]:continue
   if rng.random()<density:extra.append((a,b))
 return extra

def main():
 rng=random.Random(10410071);start=time.time();stats=[];best=None;closest=None
 for stage,budget,hi in [('small_random',3000,7),('medium_random',1500,15),('large_random',300,28)]:
  premise=0;valid=0;hist={};t=time.time()
  for rep in range(budget):
   lens=(rng.randrange(1,hi),rng.randrange(1,hi),rng.randrange(2,hi+1));extra=generate(lens,rng,rng.choice([0,.01,.03,.07,.15,.3,.6]));model=build(lens,extra)
   if model is None:continue
   a=analyze(model);valid+=1
   if a['premise']:
    premise+=1;hist[str(a['good'])]=hist.get(str(a['good']),0)+1
    score=max(min(3*k-a['E'],2*a['E']-3*k) for k in a['K'])/a['E']
    if best is None or score<best[0]:
     best=(score,analyze(model,True));(OUT/'closest_menu_boundary.json').write_text(json.dumps(best[1],indent=2))
    if not a['good']:
     (OUT/'COUNTEREXAMPLE.json').write_text(json.dumps(analyze(model,True),indent=2));print('COUNTEREXAMPLE',flush=True);return
  rec={'stage':stage,'budget':budget,'valid':valid,'premise':premise,'good_histogram':hist,'seconds':time.time()-t};stats.append(rec);print(json.dumps(rec),flush=True);(OUT/'summary.json').write_text(json.dumps(stats,indent=2))
 print('DONE',time.time()-start,flush=True)
if __name__=='__main__':main()
