from pathlib import Path
from functools import lru_cache
import json
p=Path(__file__).resolve().parent;e=json.loads((p/'LOWER_GAP_WITNESS.json').read_text());V=e['vertices'];ix={v:i for i,v in enumerate(V)};pre=[0]*len(V)
for rel in e['relations']:
 a,b=rel.split('<');pre[ix[b]]|=1<<ix[a]
full=(1<<len(V))-1
@lru_cache(None)
def f(mask):
 if mask==full:return 1
 return sum(f(mask|1<<i)for i,p in enumerate(pre)if not mask>>i&1 and p&mask==p)
assert f(0)==699
print({'e_Q_gap':f(0),'paper_count':4*105+3*13+6*18+6*22,'old_menu_budget':568,'strictly_above_budget':f(0)>568})
