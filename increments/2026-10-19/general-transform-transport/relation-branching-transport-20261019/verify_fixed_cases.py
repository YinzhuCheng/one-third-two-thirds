from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def chain(V):return list(zip(V,V[1:]))
def make_ch(label,n):return [f'{label}{i}' for i in range(1,n+1)]
A=make_ch('A',19); B=make_ch('B',19); C=make_ch('C',10); D=make_ch('D',2)
cases=[
 dict(id='common_witness',V=['x','y','z'],arcs=[],edit=('x','y'),targets=[('x','z'),('y','z')]),
 dict(id='both_selected_witnesses_lost_low',V=['x','y','z','u','v'],arcs=chain(['z','u','v']),edit=('x','y'),targets=[('x','z'),('y','z')]),
 dict(id='both_selected_witnesses_lost_high',V=['x','y','z','u','v'],arcs=chain(['u','v','z']),edit=('x','y'),targets=[('x','z'),('y','z')]),
 dict(id='rare_branch_double_loss',V=['x','a2','a3','b1','b2','y','z'],arcs=chain(['x','a2','a3'])+chain(['b1','b2','y']),edit=('x','y'),targets=[('x','z'),('y','z')]),
 dict(id='ordered_distinct_target_overlap',V=A+C+D,arcs=chain(A)+chain(C)+chain(D),edit=('A10','D1'),targets=[('A10','C5'),('A10','C6')]),
 dict(id='dominant_branch_double_endpoint',V=A+B+['z'],arcs=chain(A)+chain(B),edit=('A10','B8'),targets=[('A10','z'),('B8','z')]),
 dict(id='reversed_target_order_boundary',V=['x','y','w','z'],arcs=[('w','z')],edit=('x','y'),targets=[('x','w'),('x','z')]),
]
A99=make_ch('H',99)
cases.append(dict(id='ordered_overlap_concentrated',V=A99+C+D,arcs=chain(A99)+chain(C)+chain(D),edit=('H50','D1'),targets=[('H50','C5'),('H50','C6')]))
assert len(cases)==8 and max(len(c['V']) for c in cases)==111

def count(V,arcs):
 ix={v:i for i,v in enumerate(V)};n=len(V);full=(1<<n)-1;pred=[0]*n
 for a,b in arcs:pred[ix[b]]|=1<<ix[a]
 @lru_cache(None)
 def f(mask):
  if mask==full:return 1
  ans=0
  for i in range(n):
   bit=1<<i
   if not mask&bit and pred[i]&mask==pred[i]:ans+=f(mask|bit)
  return ans
 ans=f(0)
 return ans,f.cache_info().currsize

def bal(q):return F(1,3)<=q<=F(2,3)
def dump(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:dump(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [dump(v) for v in x]
 return x
out=[]
for c in cases:
 V,arcs=c['V'],c['arcs'];x,y=c['edit']
 N,states=count(V,arcs);Np,_=count(V,arcs+[(x,y)]);Nm,_=count(V,arcs+[(y,x)])
 assert N==Np+Nm and Np and Nm
 p=F(Np,N)
 def q(a,b,branch='P'):
  extra=[] if branch=='P' else ([(x,y)] if branch=='plus' else [(y,x)])
  den={'P':N,'plus':Np,'minus':Nm}[branch]
  return F(count(V,arcs+extra+[(a,b)])[0],den)
 vals={a+'<'+b:{branch:q(a,b,branch) for branch in ['P','plus','minus']} for a,b in c['targets']}
 for a,b in c['targets']:
  vs=vals[a+'<'+b]
  assert vs['P']==p*vs['plus']+(1-p)*vs['minus']
  if a==x:assert vs['plus']>=vs['P']>=vs['minus']
  if a==y:assert vs['plus']<=vs['P']<=vs['minus']
 if c['id']=='ordered_distinct_target_overlap':
  w,z='C5','C6'
  assert p<F(1,3)
  print('BT1 planned hypothesis check:', dump(vals), flush=True)
  # This control is retained even if the planned sufficient hypotheses fail.
  if bal(q(x,z,'plus')) and bal(q(x,w,'minus')):
   assert F(1,3)<=q(x,w)<=q(x,z)<=F(2,3)
 if c['id']=='ordered_overlap_concentrated':
  w,z='C5','C6'
  assert p<F(1,3)
  assert bal(q(x,z,'plus')) and bal(q(x,w,'minus'))
  assert F(1,3)<=q(x,w)<=q(x,z)<=F(2,3)
 if c['id']=='dominant_branch_double_endpoint':
  assert p<F(1,3)
  assert bal(q(x,'z','minus')) and bal(q(y,'z','minus'))
  assert bal(q(x,'z')) or bal(q(y,'z'))
 if c['id']=='both_selected_witnesses_lost_low':
  assert bal(q(x,'z','plus')) and bal(q(y,'z','minus'))
  assert q(x,'z')<F(1,3) and q(y,'z')<F(1,3)
 if c['id']=='both_selected_witnesses_lost_high':
  assert bal(q(y,'z','plus')) and bal(q(x,'z','minus'))
  assert q(x,'z')>F(2,3) and q(y,'z')>F(2,3)
 if c['id']=='rare_branch_double_loss':
  assert p>F(2,3)
  assert bal(q(x,'z','minus')) and bal(q(y,'z','minus'))
  assert q(x,'z')>F(2,3) and q(y,'z')<F(1,3)
 row=dict(id=c['id'],n=len(V),N=N,Nplus=Np,Nminus=Nm,p=p,original_ideal_states=states,targets=vals)
 out.append(row)
 print(json.dumps(dump(row),ensure_ascii=False))
(ROOT/'verification.json').write_text(json.dumps(dump(dict(budget_objects=8,max_n=111,results=out)),indent=2)+'\n')
print('Eight actual controls completed. The planned BT1 hypothesis in control 5 failed and was retained; the valid-certificate, exact-mixture and Shepp assertions all passed.')
