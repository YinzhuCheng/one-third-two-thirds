from search import *
count=0;found=None
for n in range(7,28):
 for a in range(1,7):
  for b in range(1,7):
   r=n-1-a-b-2
   if not 2<=r<=22:continue
   for gate in range(1,r+1):
    m=build(1,a,b,r,[]);ch=m[0];m=build(1,a,b,r,[(ch[2][gate-1],ch[1][1])]);o,s=analyze(m);count+=1
    if s[2]<0:found=analyze(m,True)[0];break
   if found:break
  if found:break
 if found:break
(OUT/'singleton_negative_energy.json').write_text(json.dumps(found,indent=2));print('singleton',count,n,found['shape'],found['energy_minus_variance'],flush=True)

def enumerate_check(o):
 n=o['n'];pred=o['pred'];ch=o['chains'];d=o['shape'][0];u=ch[0][d];y=ch[1][0];tot=ru=ry=pcount=0
 def dfs(seq,mask):
  nonlocal tot,ru,ry,pcount
  if len(seq)==n:
   tot+=1;pos={z:i for i,z in enumerate(seq)};pcount+=pos[u]<pos[y]
   ru+=any(pos[z]<pos[y] for z in range(n) if pred[z]>>u&1)
   ry+=any(pos[z]<pos[u] for z in range(n) if pred[z]>>y&1)
   return
  for z in range(n):
   if not mask>>z&1 and pred[z]&mask==pred[z]:dfs(seq+[z],mask|1<<z)
 dfs([],0)
 assert [tot,ru,(tot-ru-ry)//2,ry,pcount]==[o['E'],o['Ru'],o['H'],o['Ry'],o['H']+o['Ru']]
 return {'enumerated_extensions':tot,'Ru':ru,'Ry':ry,'H':(tot-ru-ry)//2,'u_before_y':pcount}
res={}
for name in ['minimal_single_gate_negative_energy','singleton_negative_energy','first_nonmonotone']:
 o=json.loads((OUT/(name+'.json')).read_text());res[name]=enumerate_check(o);print(name,res[name],flush=True)
(OUT/'complete_extension_enumeration.json').write_text(json.dumps(res,indent=2))
