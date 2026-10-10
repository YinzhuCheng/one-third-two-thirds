from search import *
for n in range(5,8):
 for ps in gen_posets(n):
  if sum(not any(p>>i&1 for p in ps) for i in range(n))!=3 or width(ps)!=3:continue
  p=profile(ps)
  if not p:continue
  if not all(any(f<=3*a[j]<=2*f for a in p['A']) for j,f in enumerate(p['F'])):continue
  if cover(p):continue
  print(json.dumps(p));(OUT/'genuine_vertex_negative.json').write_text(json.dumps(p,indent=2));raise SystemExit
print('none')
