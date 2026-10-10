from search import *
def strong(o):
 es=o['E_j'];qs=list(map(Fraction,o['q_j']));ff=o['f'];extra=Fraction(0)
 for j in range(len(es)-2):
  delta=es[j+1]**2-es[j]*es[j+2];v=es[j]*(qs[j]-qs[j+1])-es[j+1]*(qs[j+1]-qs[j+2]);assert delta>=0
  if not delta:assert v==0
  else:extra+=Fraction(ff[j]*es[j+2],delta)*v*v
 return Fraction(o['energy_minus_variance'])+extra/o['E']

def generate(rng):
 d=rng.choice([1,2,3,5,8]);a=rng.randrange(1,20);b=rng.randrange(1,20);r=rng.randrange(2,25);t=rng.randrange(1,12)
 ch,pr,u,y,edges=build(d,a,b,r,[]);n=len(pr);ch[2]+=list(range(n,n+t));edges+=[(ch[2][i],ch[2][i+1]) for i in range(r-1,r+t-1)]
 edges.append((rng.choice([u,y]),ch[2][r]));n+=t
 tails=[ch[0][d+1:],ch[1][1:],ch[2][:]];order=[]
 while any(tails):
  c=rng.choice([k for k in range(3) if tails[k]]);order.append(tails[c].pop(0))
 density=rng.choice([.01,.03,.07,.15,.3]);neutral=set(ch[2][:r])
 for i,x in enumerate(order):
  for z in order[i+1:]:
   if z not in neutral and not any(x in c and z in c for c in ch) and rng.random()<density:edges.append((x,z))
 for z in order:
  if z not in neutral:
   if rng.random()<density:edges.append((u,z))
   if rng.random()<density:edges.append((y,z))
 for x in ch[0][:d]:
  for z in neutral:
   if rng.random()<density/4:edges.append((x,z))
 pred=[0]*n
 for x,z in edges:pred[z]|=1<<x
 for k in range(n):
  for z in range(n):
   if pred[z]>>k&1:pred[z]|=pred[k]
 assert pred[u]==pred[y] and not any(pred[z]>>z&1 for z in range(n))
 assert all(not(pred[z]>>u&1 or pred[z]>>y&1) for z in neutral)
 return ch,pred,u,y,edges
rng=random.Random(103731);best=None;neg=0;targetneg=0;nmin=10000;nmax=0;start=time.time()
for i in range(2000):
 m=generate(rng);o,s=analyze(m,True);v=strong(o);nmin=min(nmin,o['n']);nmax=max(nmax,o['n']);targetneg+=s[0]<0
 if s[0]<0:(OUT/'TARGET_COUNTEREXAMPLE_THREE_ARMS.json').write_text(json.dumps(o,indent=2));raise RuntimeError('target negative')
 if v<0:neg+=1
 if best is None or v<best:
  best=v;o['strengthened']=str(v);o['actual_neutral_length']=len(o['E_j'])-1;(OUT/'best_strengthened.json').write_text(json.dumps(o,indent=2))
 if (i+1)%250==0:print(i+1,'negative strengthened',neg,'best',float(best),flush=True)
res={'samples':2000,'seed':103731,'n_range':[nmin,nmax],'negative_target':targetneg,'negative_strengthened':neg,'best_strengthened':str(best),'elapsed':time.time()-start}
(OUT/'strong_summary.json').write_text(json.dumps(res,indent=2));print(res,flush=True)
