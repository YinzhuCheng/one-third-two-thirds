import random,json,time,math,itertools
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
OUT=Path(__file__).parent

def build(d,a,b,r,extra):
 chains=[list(range(d+a+1)),list(range(d+a+1,d+a+b+2)),list(range(d+a+b+2,d+a+b+r+2))]
 n=sum(map(len,chains)); u=chains[0][d]; y=chains[1][0]
 edges=[(x,z) for c in chains for x,z in zip(c,c[1:])]+[(chains[0][d-1],y)]+extra
 pred=[0]*n
 for x,z in edges:pred[z]|=1<<x
 for k in range(n):
  for z in range(n):
   if pred[z]>>k&1:pred[z]|=pred[k]
 if any(pred[z]>>z&1 for z in range(n)):return None
 if pred[u]!=pred[y]:return None
 # Require entire third chain neutral, so backend consists of A/B arms.
 if any((pred[z]>>u&1)or(pred[z]>>y&1) for z in chains[2]):return None
 return chains,pred,u,y,edges

def analyze(model,detail=False):
 chains,pred,u,y,edges=model; lens=tuple(map(len,chains)); loc={v:(c,i) for c,ch in enumerate(chains) for i,v in enumerate(ch)}
 req=[]
 for z in range(len(pred)):
  req.append(tuple(max([i+1 for i,x in enumerate(ch) if pred[z]>>x&1],default=0) for ch in chains))
 def moves(s):
  for c in range(3):
   if s[c]<lens[c]:
    z=chains[c][s[c]]
    if all(s[k]>=req[z][k] for k in range(3)):
     t=list(s);t[c]+=1;yield z,tuple(t)
 @lru_cache(None)
 def F(s):
  if s==lens:return 1
  return sum(F(t) for z,t in moves(s))
 E=F((0,0,0));d=loc[u][1];r=sum(not ((pred[z]>>u&1) or (pred[z]>>y&1)) for z in chains[2])
 @lru_cache(None)
 def pre(i,j):
  if i==j==0:return 1
  ans=0
  if i:
   z=chains[0][i-1]
   if req[z][2]<=j:ans+=pre(i-1,j)
  if j:
   z=chains[2][j-1]
   if req[z][0]<=i:ans+=pre(i,j-1)
  return ans
 aa=[pre(d,j) for j in range(r+1)]; cc=[aa[0]]+[aa[j]-aa[j-1] for j in range(1,r+1)]
 ff=list(itertools.accumulate(aa)); es=[];cs=[];vs=[]
 for j in range(r+1):
  s=(d,0,j);su=(d+1,0,j);sy=(d,1,j)
  es.append(F(s));cs.append([F(su),F(sy)])
  ru=sum(F(t) for z,t in moves(su) if pred[z]>>u&1)
  ry=sum(F(t) for z,t in moves(sy) if pred[z]>>y&1)
  vs.append([ru,F((d+1,1,j)),ry])
 Ru,H,Ry=[sum(ff[j]*vs[j][k] for j in range(r+1)) for k in range(3)]
 assert E==2*H+Ru+Ry==sum(cc[j]*es[j] for j in range(r+1))
 det=H*H-Ru*Ry;gap=Fraction(det,E*E);ratio=Fraction(H*H,Ru*Ry) if Ru*Ry else Fraction(10**100)
 qs=[Fraction(sum(cs[k][0] for k in range(j,r+1)),es[j]) for j in range(r+1)]
 p=Fraction(H+Ru,E)
 energy=sum(ff[j]*es[j]*(qs[j]-qs[j+1])**2 for j in range(r))
 var=sum(cc[j]*es[j]*(qs[j]-p)**2 for j in range(r+1))
 ev=(energy-var)/E
 out={'n':len(pred),'shape':[d,lens[0]-d-1,lens[1]-1,r],'E':E,'Ru':Ru,'H':H,'Ry':Ry,'det':det,'gap':str(gap),'ratio':str(ratio),'energy_minus_variance':str(ev),'q_monotone':all(qs[j]<=qs[j+1] for j in range(r)) or all(qs[j]>=qs[j+1] for j in range(r))}
 if detail:out.update(chains=chains,edges=edges,pred=pred,a=aa,c=cc,f=ff,E_j=es,C_j=cs,V_j=vs,q_j=list(map(str,qs)),p=str(p),energy=str(energy),variance=str(var),states=F.cache_info().currsize)
 return out,(gap,ratio,ev)

def extras_for(shape,rng,density):
 d,a,b,r=shape; model=build(*shape,[]);ch,pr,u,y,ed=model
 # Global random interleaving of the arm successors and neutral chain; u,y and D remain before arm successors.
 tails=[c[d+1:] for c in [ch[0]]]+[ch[1][1:],ch[2][:]]
 order=[]
 while any(tails):
  c=rng.choice([i for i in range(3) if tails[i]]);order.append(tails[c].pop(0))
 rank={z:i for i,z in enumerate(order)};extra=[]
 for x in ch[0][:d]:
  for z in ch[2]:
   if rng.random()<density*.25:extra.append((x,z))
 for x in order:
  for z in order:
   if rank[x]>=rank[z] or rng.random()>=density:continue
   # A/B may receive neutral requirements and cross-arm dependencies, but may not precede neutral points.
   if z in ch[2]:continue
   if any(x in c and z in c for c in ch):continue
   extra.append((x,z))
 # Selective entry prerequisites for opposite arm.
 for z in ch[1][1:]:
  if rng.random()<density:extra.append((u,z))
 for z in ch[0][d+1:]:
  if rng.random()<density:extra.append((y,z))
 return extra

def main():
 rng=random.Random(10320261010);start=time.time();best=[None,None,None];records=[];num=0;nonmono=0;negative_ev=0
 stages=[('grid_single_gate',None),('random_selective',800),('larger_selective',150)]
 for stage,budget in stages:
  t=time.time();count=0
  if budget is None:
   params=((d,a,b,r,gu,gy) for d in [1,2,4] for a,b in [(1,1),(2,2),(4,4),(8,8),(3,8),(8,3)] for r in [2,4,8,16] for gu in range(r+1) for gy in range(r+1))
  else:params=range(budget)
  for param in params:
   if budget is None:
    d,a,b,r,gu,gy=param;shape=[d,a,b,r];model=build(*shape,[]);ch=model[0];extra=[]
    if gu:extra.append((ch[2][gu-1],ch[0][d+1]))
    if gy:extra.append((ch[2][gy-1],ch[1][1]))
   else:
    hi=13 if stage=='random_selective' else 27
    shape=[rng.choice([1,2,3,5]),rng.randrange(1,hi),rng.randrange(1,hi),rng.randrange(2,hi+5)]
    extra=extras_for(shape,rng,rng.choice([.015,.04,.1,.2,.4]))
   model=build(*shape,extra)
   if model is None:continue
   out,scores=analyze(model);count+=1;num+=1;nonmono+=not out['q_monotone'];negative_ev+=scores[2]<0
   for k,key in enumerate(['gap','ratio','energy_minus_variance']):
    if best[k] is None or scores[k]<best[k][0]:
     best[k]=(scores[k],analyze(model,True)[0]);(OUT/('best_'+key+'.json')).write_text(json.dumps(best[k][1],indent=2))
   if scores[0]<0:
    (OUT/'TARGET_COUNTEREXAMPLE.json').write_text(json.dumps(analyze(model,True)[0],indent=2));raise RuntimeError('TARGET COUNTEREXAMPLE')
   if scores[2]<0 and negative_ev==1:(OUT/'first_real_negative_energy.json').write_text(json.dumps(analyze(model,True)[0],indent=2))
   if not out['q_monotone'] and nonmono==1:(OUT/'first_nonmonotone.json').write_text(json.dumps(analyze(model,True)[0],indent=2))
  rec={'stage':stage,'count':count,'elapsed':time.time()-t,'total':num,'nonmonotone_q':nonmono,'negative_real_energy':negative_ev,'best_scores':[str(b[0]) for b in best]};records.append(rec);print(json.dumps(rec),flush=True)
  (OUT/'summary.json').write_text(json.dumps(records,indent=2))
 print('DONE',time.time()-start,flush=True)
if __name__=='__main__':main()
