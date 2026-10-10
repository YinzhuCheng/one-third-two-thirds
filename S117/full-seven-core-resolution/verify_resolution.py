#!/usr/bin/env python3
"""Independent exact replay for all 6,088 new full-domain residuals.
Uses factorial-built binomial rows and reverse summation order, importing no author code.
Run verify_domain.cpp first to independently regenerate interval coverage.
"""
from math import factorial,prod
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,time
P=Path(__file__).resolve().parent

def demand(ok,msg):
    if not ok:raise RuntimeError(msg)

def main():
    start=time.time()
    raw=(P/'domain_intervals.txt').read_text();other=(P/'independent_intervals.txt').read_text()
    demand(raw==other,'Independent interval domain differs')
    intervals=[tuple(map(int,line.split())) for line in raw.splitlines()]
    expected=[]
    for u,a,b,c,d,v,lo,hi in intervals:
        demand(1<=lo<=hi,'Invalid interval')
        for t in range(lo,hi+1):expected.append((u,a,b,c,t,d,v))
    demand(len(expected)==len(set(expected))==6088,'Domain missing or duplicate vectors')
    maxn=max(map(sum,expected));facts=[factorial(i) for i in range(maxn+1)]
    C=[[facts[n]//facts[k]//facts[n-k] for k in range(n+1)] for n in range(maxn+1)]
    rows=[tuple(map(int,line.split())) for line in (P/'exact_counts.txt').read_text().splitlines()]
    demand([r[:7] for r in rows]==expected,'Counts order/membership differs')
    minimum=Fraction(1);minweights=[];by_outer=Counter();checks=0
    for r in rows:
        u,a,b,c,t,d,v,z,n02=r
        demand(3*prod(range(b,b+a+1))<prod(range(b+u,b+u+a+1)),'Product 1 failed')
        demand(3*prod(range(c,c+d+1))<prod(range(c+v,c+v+d+1)),'Product 2 failed')
        demand(2*u<a+b+t+v and 2*v<u+c+t+d and 2*t<b+c+min(u,v),'Shuffle failed')
        demand(3*C[b+t+v+u][u]>2*C[a+b+t+v+u][u],'Rank 1 failed')
        demand(3*C[c+t+u+v][v]>2*C[d+c+t+u+v][v],'Rank 2 failed')
        zz=nn=0
        for j in range(t+1):
            head=C[b+j-1][j]
            for i in range(u+1):
                term=head*C[a+b+i+j-1][i]*C[u-i+c+t-j][t-j]*C[u-i+c+t-j+d+v][v]
                zz+=term
                if i==u:nn+=term
        demand((zz,nn)==(z,n02),f'Integer count mismatch {r[:7]}')
        demand(2*n02>z,'Stronger rejection >1/2 failed')
        ratio=Fraction(n02,z)
        if ratio<minimum:minimum=ratio;minweights=[r[:7]]
        elif ratio==minimum:minweights.append(r[:7])
        by_outer[a,d]+=1;checks+=2
    report={'status':'PASS','scope':'Exact new complementary-domain certificate; prerequisite audits are separate dependencies','port_domain_replay':'Independent broad rectangle and direct products identical to threshold intervals','intervals':len(intervals),'weight_vectors':len(rows),'integer_counts_cross_checked':checks,'maximum_order':maxn,'all_T0_before_T2_probabilities_gt_one_half':True,'minimum_probability':str(minimum),'minimum_weights':minweights,'by_outer_weights':{f'{a},{d}':n for (a,d),n in sorted(by_outer.items())},'elapsed_seconds':round(time.time()-start,3)}
    (P/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
