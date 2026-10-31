from pathlib import Path
from functools import lru_cache
from fractions import Fraction
import runpy,json,hashlib
p=Path(__file__).resolve().parent;ns=runpy.run_path(str(p/'verify_e16_structure.py'));V=ns['V'];D=ns['D'];U=ns['U'];inc=ns['incomp'];chain=ns['chain'];idx={x:i for i,x in enumerate(V)};base=[sum(1<<idx[a]for a in D[b])for b in V];full=(1<<len(V))-1
arcs=[]
for a in V:
 for b in V:
  if not (inc(a,b)and ((D[a]<=D[b]and chain(U[b]-U[a]))or(U[b]<=U[a]and chain(D[a]-D[b])))):continue
  pp=base.copy();pp[idx[b]]|=1<<idx[a]
  @lru_cache(None)
  def count(mask):
   if mask==full:return 1
   return sum(count(mask|1<<i)for i in range(len(V))if not mask>>i&1 and pp[i]&mask==pp[i])
  numerator=count(0);assert 2*numerator>136953
  arcs.append({'a':a,'b':b,'numerator':numerator,'probability':str(Fraction(numerator,136953))})
assert len(arcs)==39
(p/'E16_GOOD_PAIR_VALIDATION.json').write_text(json.dumps({'N':136953,'union_primal_dual_good_pair_candidate_count':len(arcs),'all_probabilities_strictly_above_half':True,'arcs':arcs},indent=2));print('All 39 primal/dual union good-pair candidate probabilities independently exceed 1/2')
manifest={x.name:hashlib.sha256(x.read_bytes()).hexdigest()for x in sorted(p.iterdir())if x.is_file()and x.name!='MANIFEST.json'};(p/'MANIFEST.json').write_text(json.dumps({'created_utc':'2026-10-31','files':manifest},indent=2))
