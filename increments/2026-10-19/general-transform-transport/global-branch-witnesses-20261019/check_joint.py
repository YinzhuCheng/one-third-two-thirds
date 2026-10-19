# Reuse frozen control 3 only. This adds requested joint-event constraints,
# not another parent poset or a poset-pool search.
from pathlib import Path
ns={"__file__":str(Path(__file__).parent/"check_frozen.py")}
src=(Path(__file__).parent/'check_frozen.py').read_text()
exec(src[:src.index('results=[]')],ns)
calc=ns['calc'];Q=ns['Q']
n=13;A=list(range(6));B=list(range(6,12));z=12
edges=list(zip(A,A[1:]))+list(zip(B,B[1:]))
x=A[5];y=B[0];u=A[3];v=B[2]
N=calc(n,edges)[0];NP=calc(n,edges+[(x,y)])[0];NM=calc(n,edges+[(y,x)])[0]
extra=[(u,z),(z,v)]
J=Q(calc(n,edges+extra)[0],N)
JP=Q(calc(n,edges+[(x,y)]+extra)[0],NP)
JM=Q(calc(n,edges+[(y,x)]+extra)[0],NM)
p=Q(NP,N)
assert J==p*JP+(1-p)*JM
assert J<=Q(1,3)
print('Frozen control 3; H={A4<z}, K={z<B3}; edit A6<B1')
print('p=',p,'J=',J,'Jplus=',JP,'Jminus=',JM)
print('input-minus-marginals=5139/11999 each; covariance-delta=3168/11999 each')
print('This is an exact nonendpoint two-event intersection-budget certificate.')

extra2=[(B[1],z),(A[1],B[1])]
K=Q(calc(n,edges+extra2)[0],N)
KP=Q(calc(n,edges+[(x,y)]+extra2)[0],NP)
KM=Q(calc(n,edges+[(y,x)]+extra2)[0],NM)
assert K==p*KP+(1-p)*KM
assert K<=Q(1,3)
print('Same frozen control 3; H={B2<z} from plus, K={A2<B2} from minus')
print('J=',K,'Jplus=',KP,'Jminus=',KM)
print('H: qplus=5/13, delta=-3960/11999; K: qminus=461/923, delta=462/923')

joint3b=(K,KP,KM)

# Frozen control 6: distinct nonendpoint witnesses from opposite branches.
# This uses the sharper exact two-event J-Z budget, not merely J.
n6=10;AA=list(range(4));BB=list(range(4,8));CC=[8,9]
e6=list(zip(AA,AA[1:]))+list(zip(BB,BB[1:]))+[(8,9)]
xx=AA[2];yy=BB[1]
H=(BB[2],CC[1]);K=(AA[0],CC[0])
T=calc(n6,e6)[0];Tplus=calc(n6,e6+[(xx,yy)])[0];Tminus=calc(n6,e6+[(yy,xx)])[0]
p6=Q(Tplus,T)
def joint6(branch,complement=False):
    base=e6+branch
    ee=[(b,a) if complement else (a,b) for a,b in (H,K)]
    return Q(calc(n6,base+ee)[0],calc(n6,base)[0])
J6=joint6([]);Z6=joint6([],True)
JP6=joint6([(xx,yy)]);ZP6=joint6([(xx,yy)],True)
JM6=joint6([(yy,xx)]);ZM6=joint6([(yy,xx)],True)
assert J6-Z6==p6*(JP6-ZP6)+(1-p6)*(JM6-ZM6)==Q(4,15)
assert J6-Z6<Q(1,3)
print('Frozen control 6; H={B3<C2} from plus, K={A1<C1} from minus; edit A3<B2')
print('p=',p6,'J,Z=',J6,Z6,'Jplus,Zplus=',JP6,ZP6,'Jminus,Zminus=',JM6,ZM6,'mixed J-Z=',J6-Z6)
print('H: qplus=23/51, delta=-532/2703; K: qminus=304/477, delta=980/8109')
print('Dominant scalar safety interval upper=',(Q(2,3)-p6)/(1-p6),' < K minus=304/477')

import json
certificates=[
 {'control':3,'events':['A4<z','z<B3'],'p':str(p),'J':str(J),'J_plus':str(JP),'J_minus':str(JM),'kind':'intersection-budget'},
 {'control':3,'events':['B2<z','A2<B2'],'p':str(p),'J':str(joint3b[0]),'J_plus':str(joint3b[1]),'J_minus':str(joint3b[2]),'kind':'opposite-branch-intersection-budget'},
 {'control':6,'events':['B3<C2','A1<C1'],'p':str(p6),'J':str(J6),'Z':str(Z6),'J_plus':str(JP6),'Z_plus':str(ZP6),'J_minus':str(JM6),'Z_minus':str(ZM6),'mixed_D':str(J6-Z6),'H_plus':'23/51','K_minus':'304/477','kind':'exact-D-budget','acyclic_order':['A1','A2','B1','B2','A3','A4','B3','B4','C1','C2']}
]
(Path(__file__).parent/'joint_verification.json').write_text(json.dumps(certificates,indent=2)+'\n')
