from math import comb
import json
from pathlib import Path

def counts(m,r,s):
 M=m+2;R=r+1;N=M+R
 rows=[]
 for i in range(3):
  for j in range(s+1):
   if i==0 and j>1:continue
   if i==0 and j==0:
    cnt=comb(N,M)-comb(N-2,M);ay=comb(N-1,M-1);by=comb(N-2,M-2)
   elif i==0:cnt=comb(N-2,M-1);ay=by=0
   else:
    suf=comb(N-i-j,M-i);pre=1 if j==0 else (2 if i==1 else 2*j+1);cnt=pre*suf;ay=cnt if j==0 else (1 if i==1 else j+1)*suf
    by=comb(N-2,M-2) if i==1 and j==0 else (cnt if j==0 else suf) if i==2 else 0
   rows.append((i,j,cnt,ay,by))
 E=sum(q for i,j,q,ay,by in rows);K=[sum(q for i,j,q,ay,by in rows if i>=1),sum(ay for i,j,q,ay,by in rows),sum(q for i,j,q,ay,by in rows if i==2),sum(by for i,j,q,ay,by in rows),sum(q for i,j,q,ay,by in rows if j==0)]
 return E,K,rows
if __name__=='__main__':
 for r in range(2,300):
  for m in range(1,8*r):
   E,K,_=counts(m,r,2)
   if min(3*K[0]-2*E,3*K[1]-2*E,3*K[4]-2*E)>0 and 3*K[2]<E:
    print('L FAIL',m,r,2,'n',m+r+4,'E',E,'K',K,'p',[k/E for k in K],flush=True)
    open(Path(__file__).with_name('L_family_counterexample.json'),'w').write(json.dumps(dict(m=m,r=r,s=2,n=m+r+4,E=E,K=K,rows=counts(m,r,2)[2]),indent=2));raise SystemExit
 print('NO COUNTEREXAMPLE')
