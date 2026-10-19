"""24 frozen actual t=2 structures. Exact integer window counts, no length scan."""
from itertools import product
from pathlib import Path
from math import factorial
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parent))
from interval_solver import threshold_polynomials,positive_intervals,intersect,binomial_kernel_coefficients
OUT=Path(__file__).resolve().parent
SCALES=[((3,7,23),(2,5,17)),((3,11,61),(2,3,5)),((2,3,5),(3,11,61)),((5,13,47),(4,17,41))]
def ceildiv(a,b):return (a+b-1)//b
def bridges(sz,kind):
 p,q,r=sz
 if kind==1:return [((0,1),(2,ceildiv(r,2))),((1,1),(2,ceildiv(r,2)))]
 if kind==2:return [((0,1),(1,ceildiv(q,2))),((1,1),(2,ceildiv(r,2)))]
 if kind==3:return [((0,ceildiv(p,2)),(2,ceildiv(r,3))),((1,ceildiv(q,2)),(2,ceildiv(2*r,3)))]
 raise ValueError(kind)
def closure(sz,edges):
 nodes=[(i,j) for i,n in enumerate(sz) for j in range(1,n+1)];pred={x:set() for x in nodes}
 for i,n in enumerate(sz):
  for j in range(2,n+1):pred[i,j].add((i,j-1))
 for a,b in edges:pred[tuple(b)].add(tuple(a))
 for k in nodes:
  for x in nodes:
   if k in pred[x]:pred[x]|=pred[k]
 # arbitrary bridge labels may not be a topological node ordering
 changed=True
 while changed:
  changed=False
  for x in nodes:
   old=len(pred[x]);pred[x]|=set().union(*(pred[y] for y in list(pred[x]))) if pred[x] else set()
   changed|=len(pred[x])!=old
 return nodes,pred

def gate_info(sz,edges,gs,order):
 nodes,pred=closure(sz,edges)
 sets=[]
 for g in gs:
  s={(i,j) for i,n in enumerate(g) for j in range(1,n+1)}
  s|=set().union(*(pred[x] for x in list(s))) if s else set();sets.append(s)
 if order:
  first,second=order;sets[second]|=sets[first]
 out=[]
 for s in sets:
  maxs=[x for x in sorted(s) if not any(x in pred[t] for t in s)]
  out.append(dict(prefix=[max([j for a,j in s if a==i],default=0) for i in range(3)],maximal_generators=maxs,nonprincipal=len(maxs)>=2))
 return out

def freeze():
 cases=[]
 for scale,(ds,us) in enumerate(SCALES,1):
  for topo in range(1,4):
   for chain in [False,True]:
    dg=[[ds[0],1,ceildiv(ds[2],4)],[1,ds[1],ceildiv(3*ds[2],4)]]
    ug=[[1,us[1],ceildiv(3*us[2],4)],[us[0],1,ceildiv(us[2],4)]]
    de,ue=bridges(ds,topo),bridges(us,topo)
    di=gate_info(ds,de,dg,(0,1) if chain else None);ui=gate_info(us,ue,ug,(1,0) if chain else None)
    assert all(x['nonprincipal'] for x in di+ui)
    pairs=[]
    for side,sz in [('D',ds),('Ureverse',us)]:
     for a,b in [((0,sz[0]),(1,sz[1])),((0,sz[0]),(2,ceildiv(sz[2],2))),((1,sz[1]),(2,ceildiv(3*sz[2],4)))]:
      pairs.append(dict(kind=side,source=list(a),target=list(b)))
    for i in range(2):
     pairs.append(dict(kind='DI',source=[2,ds[2]],target=i))
     pairs.append(dict(kind='IU',source=i,target=[2,us[2]]))
    pairs.append(dict(kind='II',source=0,target=1,skip=chain,skip_reason='comparable in I' if chain else None))
    cap=4*((ds[0]+1)*(ds[1]+1)*(ds[2]+1)+(us[0]+1)*(us[1]+1)*(us[2]+1))
    cases.append(dict(case_index=len(cases)+1,label=f'scale{scale}-bridge{topo}-I'+('chain' if chain else 'antichain'),scale=scale,bridge_type=topo,I_chain=chain,D_sizes=ds,U_reverse_sizes=us,D_bridges=de,U_reverse_bridges=ue,D_gate_raw=dg,U_reverse_gate_raw=ug,D_gates=di,U_reverse_gates=ui,n=sum(ds)+sum(us)+2,side_DP_state_cap=cap,pairs=pairs))
 assert len(cases)==24
 return cases

def count_side(sz,edges,gates,order=None,dd=None,di=None):
 """Count insertions before last side node, by subset of I already placed."""
 sz=tuple(sz);edges=[(tuple(a),tuple(b)) for a,b in edges]
 dp={};full=sz
 dp[(0,0,0)]=[1,0,0,0]
 visits=0
 for state in product(*(range(n+1) for n in sz)):
  vals=dp.get(state)
  if vals is None:continue
  visits+=4
  if state==full:continue
  for mask in range(4):
   v=vals[mask]
   if not v:continue
   for ch,n in enumerate(sz):
    if state[ch]>=n:continue
    x=(ch,state[ch]+1)
    if any(x==b and state[a[0]]<a[1] for a,b in edges):continue
    if dd is not None:
     a,b=dd
     if x==tuple(b) and state[a[0]]<a[1]:continue
    nxt=list(state);nxt[ch]+=1;nxt=tuple(nxt)
    dp.setdefault(nxt,[0,0,0,0])[mask]+=v
   for i in range(2):
    if mask&(1<<i) or any(state[ch]<gates[i][ch] for ch in range(3)):continue
    if order and i==order[1] and not(mask&(1<<order[0])):continue
    if di is not None and i==di[1] and state[di[0][0]]<di[0][1]:continue
    vals[mask|(1<<i)]+=v
 return dp.get(full,[0]*4),visits

def combine(left,right,chain):
 out=[0,0,0]
 for l in range(4):
  for r in range(4):
   if l&r:continue
   k=2-(l|r).bit_count()
   out[k]+=left[l]*right[r]*(1 if chain else factorial(k))
 return tuple(out)

def coeffs(case,pair=None):
 chain=case['I_chain'] or (pair is not None and pair['kind']=='II')
 dl={'order':(0,1) if chain else None};ul={'order':(1,0) if chain else None}
 if pair:
  kind=pair['kind']
  if kind=='D':dl['dd']=(pair['source'],pair['target'])
  if kind=='Ureverse':ul['dd']=(pair['source'],pair['target'])
  if kind=='DI':dl['di']=(pair['source'],pair['target'])
  if kind=='IU':ul['di']=(pair['target'],pair['source'])
 left,lv=count_side(case['D_sizes'],case['D_bridges'],case['D_gate_raw'],**dl)
 right,rv=count_side(case['U_reverse_sizes'],case['U_reverse_bridges'],case['U_reverse_gate_raw'],**ul)
 return combine(left,right,chain),dict(left=left,right=right,visited_side_states=lv+rv)

def variation(vals):
 vals=[1 if a>0 else -1 for a in vals if a]
 return sum(a!=b for a,b in zip(vals,vals[1:]))
def excursion(F):
 A,B,C=F
 f=lambda z:2*A+2*B*z+C*z*(z+1)
 if C>=0:return dict(concave=False,passes=False,failure='nonconcave')
 g=-C;zs=max(2,B//g);f2=f(2);fv=f(zs)
 failure='middle_budget' if B<=3*g else 'initial_bad' if f2>0 else 'vertex_amplitude' if fv<=0 else None
 return dict(concave=True,g=g,middle=B,middle_margin=B-3*g,z_star=zs,F2_twice=f2,Fmax_twice=fv,passes=f2<=0<fv,failure=failure)

def analyze(total,event):
 low,high=threshold_polynomials(total,event)
 nonpos=lambda f:positive_intervals(-f[0],-f[1],1-f[2])
 bal=intersect(nonpos(low),nonpos(high))
 FL=[a-3*b for a,b in zip(total,event)];FH=[3*b-2*a for a,b in zip(total,event)]
 checks={key:excursion(F) for key,F in [('low',FL),('high',FH)]}
 assert (len(bal)==2)==any(d['passes'] for d in checks.values())
 A,B,C=binomial_kernel_coefficients(*total);a,b,c=binomial_kernel_coefficients(*event)
 d2=a*B-b*A;d1=d2+2*(a*C-c*A);d0=(a+b)*C-c*(A+B)
 pos=positive_intervals(d2,d1,d0);neg=positive_intervals(-d2,-d1,-d0)
 return dict(event=event,balanced=bal,threshold_low=low,threshold_high=high,window_low=FL,window_high=FH,excursions=checks,threshold_variations=[variation(FL),variation(FH)],discrete_difference=[d2,d1,d0],nonmonotone=bool(pos and neg),difference_positive=pos,difference_negative=neg)

def main():
 cases=json.loads((OUT/'frozen_cases.json').read_text());results=[];start=time.monotonic()
 for case in cases:
  total,fib=coeffs(case);M=fib['left'][0]*fib['right'][0]
  assert total[2]==M*(1 if case['I_chain'] else 2)
  entries=[]
  for pi,pair in enumerate(case['pairs'],1):
   if pair.get('skip'):continue
   event,efib=coeffs(case,pair)
   assert all(0<=e<=t for e,t in zip(event,total))
   entry=dict(pair_index=pi,**pair,**analyze(total,event),fibers=efib)
   entries.append(entry)
  row=dict(**case,total=total,total_fibers=fib,counts=entries);results.append(row)
  print(case['case_index'],case['label'],'pairs',len(entries),'nonmonotone',sum(x['nonmonotone'] for x in entries),'two_components',sum(len(x['balanced'])==2 for x in entries),flush=True)
  (OUT/'all_counts.json').write_text(json.dumps(results,indent=2)+'\n')
 summary=dict(structures=len(results),candidate_slots=sum(len(c['pairs']) for c in cases),counted_pairs=sum(len(c['counts']) for c in results),n_range=[min(c['n'] for c in cases),max(c['n'] for c in cases)],max_side_DP_state_cap=max(c['side_DP_state_cap'] for c in cases),elapsed_seconds=time.monotonic()-start)
 hist={};fail={};novel=[];nonmono=[];witness=[]
 for c in results:
  for e in c['counts']:
   hist[str(len(e['balanced']))]=hist.get(str(len(e['balanced'])),0)+1
   tag=dict(case_index=c['case_index'],label=c['label'],total=c['total'],pair_index=e['pair_index'],kind=e['kind'],source=e['source'],target=e['target'])
   if e['nonmonotone']:nonmono.append(dict(**tag,**{k:e[k] for k in ['event','balanced','discrete_difference','difference_positive','difference_negative']}))
   if len(e['balanced'])==2:witness.append(dict(**tag,analysis=e))
   for side,d in e['excursions'].items():
    if d['concave']:
     k=d['failure'] or 'passes';fail[k]=fail.get(k,0)+1
     if d['middle_margin']>0:novel.append(dict(**tag,side=side,**d,event=e['event'],balanced=e['balanced']))
 summary.update(balance_component_histogram=hist,concave_threshold_failure_histogram=fail,strict_middle_budget_thresholds=novel,nonmonotone_pairs=nonmono,two_component_witnesses=witness)
 (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k not in ['strict_middle_budget_thresholds','nonmonotone_pairs','two_component_witnesses']},indent=2),flush=True)
if __name__=='__main__':
 if '--freeze' in sys.argv:
  cases=freeze();(OUT/'frozen_cases.json').write_text(json.dumps(cases,indent=2)+'\n');print('Frozen',len(cases),'structures; cap',max(c['side_DP_state_cap'] for c in cases));print('all four effective gates nonprincipal in every case')
 else:main()
