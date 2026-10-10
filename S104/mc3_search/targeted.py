from search import *
import math
rng=random.Random(1042026);start=time.time();best=(-1,None);seen=0;prem=0

def score(o):
 E=o['E'];a,c,b,d,p=o['K'];return max(min(a/E-2/3,c/E-2/3,p/E-2/3,1/3-b/E),min(a/E-2/3,c/E-2/3,1-p/E-2/3,1/3-d/E))
seed=json.loads((OUT/'closest_menu_boundary.json').read_text())
for restart in range(40):
 if restart%4==0:
  lens=tuple(seed['shape']);ch=seed['chains'];base=[(a,b) for c in ch for a,b in zip(c,c[1:])];extra=[tuple(e) for e in seed['edges'] if tuple(e) not in base]
 else:
  lens=(rng.randrange(1,12),rng.randrange(1,12),rng.randrange(2,16));extra=generate(lens,rng,rng.choice([.01,.04,.1,.25]));model=build(lens,extra);ch=model[0]
 model=build(lens,extra);o=analyze(model);s=score(o);x,y,b1,b2=ch[0][0],ch[1][0],ch[2][0],ch[2][1];n=sum(lens);chain={z:c for c,ls in enumerate(ch) for z in ls}
 for step in range(500):
  candidate=extra[:]
  if candidate and rng.random()<.52:candidate.pop(rng.randrange(len(candidate)))
  else:
   a,b=rng.sample(range(n),2)
   if chain[a]==chain[b] or b in [x,y,b1,b2]:continue
   if (a,b) not in candidate:candidate.append((a,b))
  m=build(lens,candidate)
  if m is None:continue
  v=analyze(m);seen+=1;prem+=v['premise'];t=score(v)
  if t>best[0]:
   best=(t,analyze(m,True));(OUT/'targeted_best.json').write_text(json.dumps(dict(best[1],target_score=t),indent=2))
  if v['premise'] and not v['good']:
   (OUT/'COUNTEREXAMPLE.json').write_text(json.dumps(analyze(m,True),indent=2));raise RuntimeError('MC3 COUNTEREXAMPLE')
  if t>0:
   (OUT/'EXTREME_COUNTEREXAMPLE.json').write_text(json.dumps(analyze(m,True),indent=2));raise RuntimeError('EXTREME COUNTEREXAMPLE')
  temperature=.003*(1-step/500)+.0001
  if t>=s or rng.random()<math.exp(max(-700,(t-s)/temperature)):extra,o,s=candidate,v,t
 print(json.dumps({'restart':restart,'seen':seen,'premise':prem,'best_score':best[0],'seconds':time.time()-start}),flush=True)
(OUT/'targeted_summary.json').write_text(json.dumps({'attempt_budget':20000,'valid_evaluations':seen,'premise_evaluations':prem,'best_score':best[0],'seconds':time.time()-start},indent=2))
