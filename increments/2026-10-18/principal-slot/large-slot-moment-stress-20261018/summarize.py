#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
P=Path(__file__).resolve().parent
objects={c['name']:c for c in json.loads((P/'objects.json').read_text())['objects']}
rows=[json.loads(x) for x in (P/'raw_results.jsonl').read_text().splitlines()]
cases={r['name']:r for r in rows if r['type']=='case'}
pairs=[r for r in rows if r['type']=='pair'];stop=[r for r in rows if r['type']=='stop'][-1]
seen=Counter(r['case'] for r in pairs)
byclass=Counter(r['class'] for r in pairs)
by_n=Counter(cases[r['case']]['n'] for r in pairs)
best={};counts=Counter();bad=[]

def make_record(r):
 c=cases[r['case']];obj=objects[r['case']];K=int(c['le']);a,b,z,d=[int(r[t]) for t in ['sum_Ry','sum_Rz','sum_product','sum_min']];m=min(a,b)
 rec=dict(r)
 rec.update(n=c['n'],lengths=obj['lengths'],cross=obj['cross'],legal_ideal_count=c['states'],le=c['le'],Sy_threshold=c['filters'][r['i']]['threshold'],Sz_threshold=c['filters'][r['j']]['threshold'])
 rec.update(r=str(Fraction(a,K)),s=str(Fraction(b,K)),N=str(Fraction(z+d,K)),covariance=str(Fraction(z*K-a*b,K*K)),target_gap=str(Fraction(int(r['target_gap_num']),K*K)),covariance_gap=str(Fraction(int(r['covariance_gap_num']),K*K)))
 if m:
  rec.update(mean_ratio=str(Fraction(max(a,b),m)),target_pressure=str(Fraction((z+d)*K-a*b,m*m+2*m*K)),covariance_pressure=str(Fraction(z*K-a*b,m*m+m*K)),target_relative_gap=str(Fraction(int(r['target_gap_num']),m*m+2*m*K)),covariance_relative_gap=str(Fraction(int(r['covariance_gap_num']),m*m+m*K)))
 return rec
for r in pairs:
 c=cases[r['case']];K=int(c['le']);a,b,z,d=[int(r[t]) for t in ['sum_Ry','sum_Rz','sum_product','sum_min']];m=min(a,b)
 tn=int(r['target_gap_num']);cn=int(r['covariance_gap_num'])
 assert tn==a*b+m*m+2*m*K-(z+d)*K
 assert cn==a*b+m*m+m*K-z*K
 assert a==int(c['filters'][r['i']]['sum_R']) and b==int(c['filters'][r['j']]['sum_R'])
 assert tn-cn==(m-d)*K and 0<=d<=m
 assert int(r['sum_Ry2'])*K>=a*a and int(r['sum_Rz2'])*K>=b*b
 assert (z*K-a*b)**2 <= (int(r['sum_Ry2'])*K-a*a)*(int(r['sum_Rz2'])*K-b*b)
 if tn<0 or cn<0:bad.append(make_record(r))
 if not m:counts['zero_mean']+=1;continue
 counts['positive_means']+=1
 ratio=Fraction(max(a,b),m)
 if ratio>=10:counts['mean_ratio_at_least_10']+=1
 if ratio>=100:counts['mean_ratio_at_least_100']+=1
 if ratio>=1000:counts['mean_ratio_at_least_1000']+=1
 if r['class']!='empty_filter':
  for threshold in (10,100,1000):
   if ratio>=threshold:counts[f'nonempty_mean_ratio_at_least_{threshold}']+=1
 scores={'target_relative_gap':Fraction(tn,m*m+2*m*K),'covariance_relative_gap':Fraction(cn,m*m+m*K),'target_absolute_gap':Fraction(tn,K*K),'covariance_absolute_gap':Fraction(cn,K*K),'negative_mean_ratio':-ratio}
 for typ,score in scores.items():
  keys=[typ,typ+'_'+r['class']]
  if r['class'] not in ('same','empty_filter'):keys.append(typ+'_distinct_nonempty')
  if ratio>=10 and r['class']!='empty_filter':keys.append(typ+'_asymmetric10_nonempty')
  for key in keys:
   if key not in best or score<best[key][0]:best[key]=(score,make_record(r))
summary=dict(status='finite sampled exact stress test only; both candidates remain unproved',stop=stop,planned_objects=len(objects),objects_started=len(cases),objects_completed=sum(seen[n]==c['planned_pairs'] for n,c in cases.items()),pairs=len(pairs),n_range=[min(cases[r['case']]['n'] for r in pairs),max(cases[r['case']]['n'] for r in pairs)],filter_pairs_by_class=dict(byclass),pairs_by_n=dict(by_n),positive_mean_statistics=dict(counts),max_ideal_count=max(c['states'] for c in cases.values()),largest_complete_LE_count=max((int(c['le']) for c in cases.values())),counterexamples=bad,case_progress=[dict(name=n,n=c['n'],states=c['states'],le=c['le'],filters=c['filter_count'],planned_pairs=c['planned_pairs'],tested_pairs=seen[n]) for n,c in cases.items()],unstarted_objects=[n for n in objects if n not in cases],extrema={k:dict(score=str(v[0]),record=v[1]) for k,v in best.items()})
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ('extrema','case_progress')},indent=2))
for key in ['target_relative_gap','covariance_relative_gap','target_relative_gap_distinct_nonempty','covariance_relative_gap_distinct_nonempty','covariance_relative_gap_asymmetric10_nonempty','negative_mean_ratio']:
 x=summary['extrema'][key];r=x['record'];print(key,x['score'],float(Fraction(x['score'])),r['case'],r['class'],r['Sy_threshold'],r['Sz_threshold'],'r,s=',r['r'],r['s'],'pressures',r['target_pressure'],r['covariance_pressure'])
