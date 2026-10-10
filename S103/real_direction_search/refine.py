from search import *

def strengthened(out):
 es=out['E_j'];qs=list(map(Fraction,out['q_j']));ff=out['f'];extra=Fraction(0)
 for j in range(len(es)-2):
  delta=es[j+1]**2-es[j]*es[j+2]
  bracket=es[j]*(qs[j]-qs[j+1])-es[j+1]*(qs[j+1]-qs[j+2])
  assert delta>=0
  if not delta:assert bracket==0
  else:extra+=Fraction(ff[j]*es[j+2],delta)*bracket**2
 return Fraction(out['energy_minus_variance'])+extra/out['E']

count=0;found=None;strongnegative=0
for n in range(7,22):
 for d in range(1,min(7,n-5)):
  for a in range(1,5):
   for b in range(1,5):
    r=n-d-a-b-2
    if not 2<=r<=16:continue
    for gate in range(1,r+1):
     model=build(d,a,b,r,[]);ch=model[0];model=build(d,a,b,r,[(ch[2][gate-1],ch[1][1])])
     out,scores=analyze(model);count+=1
     if scores[2]<0:
      out=analyze(model,True)[0];out['strengthened']=str(strengthened(out));found=out;break
    if found:break
   if found:break
  if found:break
 if found:break
print('MIN SINGLE-GATE',count,n,found['shape'],found['energy_minus_variance'],found['strengthened'],flush=True)
(OUT/'minimal_single_gate_negative_energy.json').write_text(json.dumps(found,indent=2))
# Independent subset recurrence, without chain-state representations or weighted V summation.
def verify(out):
 n=out['n'];pred=out['pred'];ch=out['chains'];d=out['shape'][0];u=ch[0][d];y=ch[1][0];full=(1<<n)-1
 @lru_cache(None)
 def cnt(mask):
  if mask==full:return 1
  return sum(cnt(mask|1<<z) for z in range(n) if not mask>>z&1 and pred[z]&mask==pred[z])
 # First event that resolves each release count; each ordered valid prefix contributes suffix count.
 @lru_cache(None)
 def event(mask,typ):
  if typ==0 and mask>>y&1:return 0
  if typ==1 and mask>>u&1:return 0
  ans=0
  for z in range(n):
   if mask>>z&1 or pred[z]&mask!=pred[z]:continue
   t=mask|1<<z
   if (typ==0 and pred[z]>>u&1 and not mask>>y&1) or (typ==1 and pred[z]>>y&1 and not mask>>u&1):ans+=cnt(t)
   elif not (typ==0 and z==y or typ==1 and z==u):ans+=event(t,typ)
  return ans
 E=cnt(0);Ru=event(0,0);Ry=event(0,1);H=(E-Ru-Ry)//2
 assert [E,Ru,H,Ry]==[out[k] for k in ['E','Ru','H','Ry']]
 # Independent backend q_j: sum extensions whose first entry among u,y is u.
 D=pred[u]
 @lru_cache(None)
 def win(mask):
  ans=0
  for z in range(n):
   if mask>>z&1 or pred[z]&mask!=pred[z]:continue
   t=mask|1<<z
   if z==u:ans+=cnt(t)
   elif z!=y:ans+=win(t)
  return ans
 for j in range(len(ch[2])+1):
  mask=D|sum(1<<z for z in ch[2][:j]);assert cnt(mask)==out['E_j'][j];assert Fraction(win(mask),cnt(mask))==Fraction(out['q_j'][j])
 return {'E':E,'Ru':Ru,'H':H,'Ry':Ry,'subset_states':cnt.cache_info().currsize,'q_verified':True}
results={}
for name in ['minimal_single_gate_negative_energy','first_nonmonotone','best_gap','best_ratio']:
 out=json.loads((OUT/(name+'.json')).read_text());results[name]=verify(out);results[name]['strengthened']=str(strengthened(out));print(name,results[name],flush=True)
(OUT/'independent_checks.json').write_text(json.dumps(results,indent=2))
