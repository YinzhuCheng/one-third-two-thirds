import json,collections
src='/workspace/shared/actual-external-pair-shapes-20261018/all_counts.json'
x=json.load(open(src))
def V(q):
 s=[(v>0)-(v<0) for v in q if v];return sum(a!=b for a,b in zip(s,s[1:]))
cnt=collections.Counter();unc=[];nonmono=[];alltypes=collections.Counter();dican=collections.Counter()
for case in x:
 n=case['n'];d=case['d'];u=case['u'];a,b,c=case['total']
 typ=['D']*d+['I']*2+['U']*u
 assert len(typ)==n
 for p in case['pairs']:
  i,j=p['indices'];tp=typ[i]+typ[j];alltypes[tp]+=1
  ae,be,ce=p['event'];lv=(a-3*ae,b-3*be,c-3*ce);hv=(3*ae-2*a,3*be-2*b,3*ce-2*c)
  vl,vh=V(lv),V(hv);cnt[tp,vl,vh]+=1
  rec={'case':case['case_index'],'pair':p['pair'],'type':tp,'total':[a,b,c],'event':[ae,be,ce],'v_low':vl,'v_high':vh,'low_basis':lv,'high_basis':hv,'balanced':p['balanced']}
  if max(vl,vh)>=2:unc.append(rec)
  if p['difference_positive'] and p['difference_negative']:nonmono.append(rec)
  if tp in ('DI','IU'):
   # Normalize event D<I or I<U; both cE=c.
   assert ce==c
   A=a-ae;B=b-be
   h=(b+3*c)*A+(3*c-a)*B
   dic=(a*be-b*ae)
   dican[tp,'hneg' if h<0 else 'hnonneg']+=1
   dican[tp,'dneg' if dic<0 else 'dnonneg']+=1
out={'source':src,'pairs':sum(alltypes.values()),'alltypes':dict(alltypes),'stratification':[{'type':t,'v_low':vl,'v_high':vh,'count':v} for (t,vl,vh),v in sorted(cnt.items())],'uncovered_count':len(unc),'uncovered':unc,'nonmonotone':nonmono,'cross_diagnostics':[{'type':t,'condition':c,'count':v} for (t,c),v in sorted(dican.items())]}
json.dump(out,open('/workspace/shared/actual-interval-connectivity-20261018/old120_variation_strata.json','w'),ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in out.items() if k!='uncovered'},ensure_ascii=False,indent=2))
print('uncovered first',json.dumps(unc[:8],ensure_ascii=False,indent=2))
