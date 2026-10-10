import search,runpy,json
from pathlib import Path
from fractions import Fraction
OUT=Path(__file__).parent
orig=search.analyze;best=None;count=0

def wrapped(model,detail=False):
 global best,count
 o=orig(model,detail);E=o['E'];a,c,b,d,p=o['K']
 if not detail and o['premise'] and (3*p>2*E or 3*p<E):
  count+=1
  gap=Fraction(2*b-a,E) if 3*p>2*E else Fraction(2*d-c,E)
  if best is None or gap<best[0]:best=gap,orig(model,True)
  if gap<0:(OUT/'STRONGER_COUNTEREXAMPLE.json').write_text(json.dumps(orig(model,True),indent=2))
 return o
search.analyze=wrapped
search.main()
runpy.run_path(str(OUT/'targeted.py'),run_name='__main__')
(OUT/'stronger_summary.json').write_text(json.dumps({'replay_only':True,'eligible_evaluations':count,'minimum_2b_minus_a':str(best[0]) if best else None,'best_certificate':best[1] if best else None},indent=2))
