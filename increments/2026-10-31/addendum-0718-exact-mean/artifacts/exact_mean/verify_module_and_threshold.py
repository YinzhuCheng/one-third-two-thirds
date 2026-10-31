from pathlib import Path
import runpy,contextlib,io,json
from fractions import Fraction as F
with contextlib.redirect_stdout(io.StringIO()):j=runpy.run_path(str(Path(__file__).resolve().parent/'independent_mean_separation_check.py'))
V=j['V'];E=j['E'];S={'d','e'}
assert all(len({-1 if(x,y)in E else 1 if(y,x)in E else 0 for y in S})==1 for x in set(V)-S)
mean=F(1)-F(2,3)+F(1,5)
assert mean==F(8,15) and 1/mean-1==F(7,8)<1
print(json.dumps({'proper_module':sorted(S),'two_chains_mean':str(mean),'exact_kappa':str(1/mean-1),'sum_component_exact_kappa':'1'},indent=2))
