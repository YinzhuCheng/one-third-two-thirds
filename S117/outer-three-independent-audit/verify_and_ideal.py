#!/usr/bin/env python3
"""One independent full record comparison and selected actual-label ideal DP."""
import argparse,gzip,hashlib,json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from math import comb
ROOT=Path(__file__).parent
EDGES=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
def check(ok,*why):
 if not ok:raise RuntimeError(why)
def dual(w):return (w[6],w[5],w[3],w[2],w[4],w[1],w[0])
def load(p):
 rows={}
 stream=p.open() if p.exists() else gzip.open(str(p)+'.gz','rt')
 for line in stream:
  values=list(map(int,line.split()));check(len(values)==12,'row_width',p)
  w=tuple(values[:7]);check(w not in rows,'duplicate',p,w);rows[w]=values[7:]
 stream.close()
 return rows

def labelled_ideals(w):
 labels=[(b,r) for b in range(7) for r in range(1,w[b]+1)]
 ident={x:j for j,x in enumerate(labels)};n=len(labels)
 rel=set(EDGES)
 while True:
  nxt=rel|{(a,d) for a,b in rel for c,d in rel if b==c}
  if nxt==rel:break
  rel=nxt
 pred=[];blockmask=[]
 for b in range(7):blockmask.append(sum(1<<ident[b,r] for r in range(1,w[b]+1)))
 for b,r in labels:
  pred.append(sum(1<<ident[c,s] for c,s in labels if (c,b) in rel or c==b and s<r))
 eventlabels=[((1,1),(0,1)),((6,w[6]),(5,w[5])),((0,w[0]),(2,w[2])),((2,1),(4,1)),((3,1),(6,1)),((4,w[4]),(3,w[3])),((1,w[1]),(0,1)),((6,w[6]),(5,1))]
 events=[(ident[x],ident[y]) for x,y in eventlabels]
 # Each extra coordinate counts extensions satisfying one additional x<y.
 layer={0:[1]*(1+len(events))};states=1;maxwidth=1
 for lev in range(n):
  nxt={}
  for mask,counts in layer.items():
   for bm in blockmask:
    remaining=bm&~mask
    if not remaining:continue
    bit=remaining&-remaining;y=bit.bit_length()-1
    if pred[y]&~mask:continue
    nm=mask|bit
    target=nxt.get(nm)
    if target is None:target=[0]*len(counts);nxt[nm]=target
    target[0]+=counts[0]
    for k,(x,ey) in enumerate(events,1):
     if y!=ey or mask&(1<<x):target[k]+=counts[k]
  check(nxt,'dead_layer',w,lev)
  layer=nxt;states+=len(layer);maxwidth=max(maxwidth,len(layer))
 check(len(layer)==1 and (1<<n)-1 in layer,'terminal_ideal',w)
 return layer[(1<<n)-1],states,maxwidth,eventlabels

def main(source):
 independent=load(ROOT/'recurrence_counts.txt');author=load(source/'exact_counts.txt')
 survivors=[tuple(map(int,line.split())) for line in (ROOT/'survivors.txt').open()]
 check(len(survivors)==len(set(survivors)),'reconstructed_duplicates')
 check(set(independent)==set(author)==set(survivors),'complete_domain')
 check(independent==author,'independent_count_disagreement')
 sourcews=[tuple(w) for w in json.loads((source/'analytic_survivors.json').read_text())]
 check(set(sourcews)==set(survivors),'source_domain')
 check({dual(w) for w in survivors}==set(survivors),'duality_domain')
 minprob=None;minvectors=[];standalone=[0]*6;cumulative=[0]*6;eq=[0]*6
 for w,r in independent.items():
  z,n10,n65,n02,n24=r;dr=independent[dual(w)]
  check(z==dr[0] and n10==dr[2] and n65==dr[1],'dual_counts',w)
  nums=[n10,n65,z-n02,n24,z-dr[3],dr[4]]
  flags=[3*x>2*z for x in nums]
  for k in range(6):standalone[k]+=flags[k];cumulative[k]+=all(flags[:k+1]);eq[k]+=3*nums[k]==2*z
  check(2*n02>z and 2*dr[3]>z,'stronger_half_bound',w)
  p=Fraction(n02,z)
  if minprob is None or p<minprob:minprob=p;minvectors=[w]
  elif p==minprob:minvectors.append(w)
  u,a,b,c,t,d,v=w
  check(3*comb(b+t+v+u,u)>2*comb(a+b+t+v+u,u),'rank_left_binomial',w)
  check(3*comb(c+t+u+v,v)>2*comb(d+c+t+u+v,v),'rank_right_binomial',w)
  check(3*comb(a+b+u-1,u)<comb(a+b+t+v+u,u),'lower_left',w)
  check(3*comb(d+c+v-1,v)<comb(d+c+t+u+v,v),'lower_right',w)
 # Deterministic coverage: endpoint-probability extremizers, order extremes,
 # every coordinate extreme, each nonempty spine family, spread through domain.
 chosen=set(minvectors)
 ordered=sorted(survivors)
 for k in range(11):chosen.add(ordered[k*(len(ordered)-1)//10])
 for k in range(7):
  chosen.add(min(ordered,key=lambda w:(w[k],sum(w),w)))
  chosen.add(max(ordered,key=lambda w:(w[k],-sum(w),w)))
 chosen.add(min(ordered,key=lambda w:(sum(w),w)));chosen.add(max(ordered,key=lambda w:(sum(w),w)))
 for a,d in ((2,3),(3,2),(3,3)):
  family=[w for w in ordered if (w[1],w[5])==(a,d)]
  chosen.add(min(family,key=lambda w:(sum(w),w)));chosen.add(max(family,key=lambda w:(sum(w),w)))
 chosen|={dual(w) for w in tuple(chosen)}
 records=[];totalstates=0
 for w in sorted(chosen,key=lambda w:(sum(w),w)):
  vals,states,width,eventlabels=labelled_ideals(w)
  z,n10,n65,n02,n24=independent[w];dr=independent[dual(w)]
  expected=[z,n10,n65,n02,n24,dr[3],dr[4]]
  check(vals[:7]==expected,'actual_label_DP',w,vals[:7],expected)
  u,a,b,c,t,d,v=w
  boundpairs=[(comb(b+t+v+u,u),comb(a+b+t+v+u,u)),(comb(c+t+u+v,v),comb(d+c+t+u+v,v))]
  for actual,(num,den) in zip(vals[7:],boundpairs):check(actual*den<=num*z,'rank_bound_actual',w)
  records.append({'weights':w,'counts':vals,'ideal_states':states,'maximum_layer_size':width,'events':eventlabels})
  totalstates+=states
  print('labelled_DP',len(records),'of',len(chosen),'weights',w,'states',states,flush=True)
 report={'status':'INDEPENDENT_ARITHMETIC_AND_LABELLED_IDEAL_PASS','candidate_count':61785506,'survivors':len(survivors),'count_columns_matched':5*len(survivors),'standalone_six_passes':standalone,'cumulative_six_passes':cumulative,'six_equalities':eq,'exact_final_survivors':0,'stronger_half_bound_vectors':len(survivors),'minimum_p_T0_before_T2':str(minprob),'minimum_vectors':minvectors,'labelled_DP_vectors':len(records),'labelled_DP_total_states':totalstates,'labelled_DP_count_comparisons':7*len(records),'labelled_DP_rank_bound_comparisons':2*len(records),'labelled_DP_records':records}
 (ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='labelled_DP_records'},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=ROOT.parent/'outer-three-census');args=p.parse_args();main(args.source)
