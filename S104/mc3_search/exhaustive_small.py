import json,time,itertools
from pathlib import Path
from functools import lru_cache
OUT=Path(__file__).parent
start=time.time();stats=[]
def gen(n):
 if n==0:yield ();return
 for pr in gen(n-1):
  for s in range(1<<(n-1)):
   if all(not(s>>j&1) or (s&pr[j])==pr[j] for j in range(n-1)):yield pr+(s,)
def analyze(pr,pairs):
 n=len(pr);full=(1<<n)-1
 @lru_cache(None)
 def F(s):
  if s==full:return 1
  return sum(F(s|1<<z) for z in range(n) if not(s>>z&1) and pr[z]&s==pr[z])
 E=F(0);K=[0]*len(pairs);H={0:1}
 for s in range(full):
  if s not in H:continue
  for z in range(n):
   if s>>z&1 or pr[z]&s!=pr[z]:continue
   t=s|1<<z;H[t]=H.get(t,0)+H[s]
   for j,(a,b) in enumerate(pairs):
    if z==a and not(s>>b&1):K[j]+=H[s]*F(t)
 assert H[full]==E
 return E,K
for n in range(4,8):
 count=0;eligible=0;premise=0;hist={}
 for pr in gen(n):
  count+=1;mins=[z for z in range(n) if not pr[z]]
  if len(mins)!=3:continue
  # A 4-antichain check is exact for width <= 3.
  if any(all(not(pr[b]>>a&1) for a,b in itertools.combinations(ss,2)) for ss in itertools.combinations(range(n),4)):continue
  for x,y in itertools.combinations(mins,2):
   B=[z for z in range(n) if z not in [x,y] and not(pr[z]>>x&1 or pr[z]>>y&1)]
   if len(B)!=2 or not(pr[B[1]]>>B[0]&1):continue
   eligible+=1;b1,b2=B;pairs=[(b1,x),(b1,y),(b2,x),(b2,y),(x,y)];E,K=analyze(pr,pairs)
   if 3*K[0]<=2*E or 3*K[1]<=2*E:continue
   premise+=1;good=[j for j,k in enumerate(K) if E<=3*k<=2*E];hist[str(good)]=hist.get(str(good),0)+1
   if not good:
    (OUT/'EXHAUSTIVE_COUNTEREXAMPLE.json').write_text(json.dumps({'pred':pr,'pairs':pairs,'E':E,'K':K}));raise RuntimeError('COUNTEREXAMPLE')
 rec={'n':n,'naturally_labeled_posets':count,'eligible_pair_instances':eligible,'premise_instances':premise,'good_histogram':hist};stats.append(rec);print(json.dumps(rec),flush=True)
(OUT/'exhaustive_summary.json').write_text(json.dumps({'n_max':7,'results':stats,'seconds':time.time()-start},indent=2))
