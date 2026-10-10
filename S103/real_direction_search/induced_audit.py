from search import *
o=json.loads((OUT/'minimal_single_gate_negative_energy.json').read_text());n=o['n'];u=o['chains'][0][o['shape'][0]];y=o['chains'][1][0];optional=[z for z in range(n) if z not in [u,y]];cnt=neg=0;best=n
for mask in range(1<<len(optional)):
 keep=sorted([u,y]+[z for i,z in enumerate(optional) if mask>>i&1]);mp={z:i for i,z in enumerate(keep)}
 if not any(z in keep for z in o['chains'][0][:o['shape'][0]]):continue
 ch=[[mp[z] for z in c if z in mp] for c in o['chains']];pred=[sum(1<<mp[x] for x in keep if o['pred'][z]>>x&1) for z in keep];ed=[(mp[x],mp[z]) for z in keep for x in keep if o['pred'][z]>>x&1]
 oo,s=analyze((ch,pred,mp[u],mp[y],ed));cnt+=1
 if s[2]<0:
  neg+=1;best=min(best,len(keep));print('negative induced',keep,s[2],flush=True)
res={'checked_nonempty_D_induced_subsets':cnt,'negative_energy_subsets':neg,'minimum_vertices_in_negative_induced_subset':best,'original_n':n};print(res)
(OUT/'induced_audit.json').write_text(json.dumps(res,indent=2))
