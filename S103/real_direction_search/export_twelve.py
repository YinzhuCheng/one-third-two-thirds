from search import *
o=json.loads((OUT/'minimal_single_gate_negative_energy.json').read_text());keep=[z for z in range(o['n']) if z!=4];mp={z:i for i,z in enumerate(keep)};ch=[[mp[z] for z in c if z in mp] for c in o['chains']];pred=[sum(1<<mp[x] for x in keep if o['pred'][z]>>x&1) for z in keep];ed=[(mp[x],mp[z]) for z in keep for x in keep if o['pred'][z]>>x&1];oo,s=analyze((ch,pred,mp[3],mp[5],ed),True);(OUT/'induced_minimal_twelve.json').write_text(json.dumps(oo,indent=2))
n=oo['n'];u=mp[3];y=mp[5];counts=[0,0,0,0]
def dfs(seq,mask):
 if len(seq)==n:
  pos={z:i for i,z in enumerate(seq)};counts[0]+=1;counts[1]+=any(pos[z]<pos[y] for z in range(n) if pred[z]>>u&1);counts[2]+=any(pos[z]<pos[u] for z in range(n) if pred[z]>>y&1);counts[3]+=pos[u]<pos[y];return
 for z in range(n):
  if not mask>>z&1 and pred[z]&mask==pred[z]:dfs(seq+[z],mask|1<<z)
dfs([],0);assert counts==[oo['E'],oo['Ru'],oo['Ry'],oo['H']+oo['Ru']];print(counts)
(OUT/'twelve_enumeration.json').write_text(json.dumps(dict(zip(['E','Ru','Ry','u_before_y'],counts)),indent=2))
