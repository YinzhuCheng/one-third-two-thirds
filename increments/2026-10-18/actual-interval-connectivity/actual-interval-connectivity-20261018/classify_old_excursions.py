import json
from fractions import Fraction
from math import isqrt
p='/workspace/shared/actual-interval-connectivity-20261018/old120_variation_strata.json'
x=json.load(open(p));cases=json.load(open('/workspace/shared/actual-external-pair-shapes-20261018/all_counts.json'))
def V(q):
 q=[(s>0)-(s<0) for s in q if s];return sum(a!=b for a,b in zip(q,q[1:]))
y=[]
for rec in x['uncovered']:
 for side in ['low','high']:
  if rec['v_'+side]!=2:continue
  A,B,C=rec[side+'_basis'];q=[C,2*B+5*C,2*A+4*B+6*C];delta=q[1]**2-4*q[0]*q[2]
  # V descending == ascending
  out={**rec,'side':side,'twice_threshold_in_x_m_minus_1':q,'V_shifted':V(q),'discriminant':delta}
  if C<0:
   zs=max(2,B//(-C));val=2*A+2*B*zs+C*zs*(zs+1)
   out.update({'maximizer_z':zs,'twice_integer_max':val,'first_twice_threshold':q[2], 'possible_two_component_excursion':q[2]<=0 and val>0})
   if val<=0:out['reason']='凹阈值在所有整数m≥1非正'
   elif q[2]>0:out['reason']='首项已经处坏侧，凹正集接左端，不能分开两段平衡集'
  elif C>0:
   out['reason']='该坏侧阈值最终为正；凸阈值只能给两端坏侧，不能作两段平衡之间的有界坏间隙'
  else:out['reason']='退化一次，无有界正凸起'
  y.append(out)
json.dump(y,open('/workspace/shared/actual-interval-connectivity-20261018/old120_uncovered_excursion_checks.json','w'),ensure_ascii=False,indent=2)
for p in y:
 print(p['case'],p['pair'],p['type'],p['side'],p[p['side']+'_basis'],'qshift',p['twice_threshold_in_x_m_minus_1'],'V',p['V_shifted'],'disc',p['discriminant'],'max',p.get('twice_integer_max'),'why',p['reason'])
c=next(c for c in cases if c['case_index']==8)
print('case8',json.dumps({k:v for k,v in c.items() if k!='pairs'},ensure_ascii=False,indent=2))
