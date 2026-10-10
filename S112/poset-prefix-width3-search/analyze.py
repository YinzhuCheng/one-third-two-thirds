from search import *
d=json.loads((OUT/'candidates.json').read_text())
for p in d['candidates']:
 for k in range(1,len(p['A'])+1):
  good=[]
  for ss in combinations(range(len(p['A'])),k):
   pp=dict(p,A=[p['A'][i] for i in ss])
   if cover(pp):good.append(ss)
  if good:break
 p['minimum_cover_size']=k;p['minimum_covers']=good
 print(p['n'],p['pred'],'min',k,good,'F',p['F'],'A',p['A'])
(OUT/'analyzed.json').write_text(json.dumps(d,indent=2))
