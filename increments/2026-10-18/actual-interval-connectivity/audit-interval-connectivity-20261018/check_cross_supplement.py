"""Read-only full certificate diagnostics; recount only the fixed maximum-beta object."""
import json
from pathlib import Path
from fractions import Fraction
from collections import Counter
from math import comb
BASE=Path('/workspace/shared');OUT=BASE/'audit-interval-connectivity-20261018';C=BASE/'cross-pair-valley-test-20261018'
frozen=json.loads((BASE/'disconnected-balance-interval-test-20261018/frozen_cases.json').read_text())
manifest=json.loads((C/'candidate_manifest.json').read_text());rows=json.loads((C/'all_counts.json').read_text())
summary=json.loads((C/'summary.json').read_text());stats=Counter();certs=[];ratios=[]
for k,(f,r) in enumerate(zip(frozen,rows)):
    assert (r['p'],r['q'],r['y'],r['z'])==(f['p'],f['q'],f['y'],f['z'])
    expected=[]
    for chain,length in [('A',f['p']),('B',f['q'])]:
      for I in ['y','z']:
        expected.append((chain,I,f[I][0 if chain=='A' else 1]==length))
    for idx,(e,sel) in enumerate(zip(r['events'],expected)):
        chain,I,skip=sel; label=f"{chain}{f['p'] if chain=='A' else f['q']}<{I}"
        m=manifest[4*k+idx]
        assert (e['D_chain'],e['I'],e['skip_comparable'],e['label'])==(chain,I,skip,label)
        assert all(e[a]==m[a] for a in m)
        og=f['z' if I=='y' else 'y']
        ordinal=og in [[0,0],[f['p'],f['q']]]
        assert e['other_I_ordinal_cut']==ordinal==False
        if skip:stats['skipped']+=1;continue
        stats['tested']+=1
        t=r['total'];n=e['event'];fail=[x-y for x,y in zip(t,n)];alpha,beta,_=fail;a,b,c=t
        assert fail==e['failure'] and n[2]==c and fail[2]==0
        ratio=Fraction(beta,c);ratios.append((ratio,k+1,label))
        assert str(ratio)==e['B_fail_over_c']
        covered=beta<=6*c;assert covered==e['covered_beta_le_6c'];stats['covered' if covered else 'over']+=1
        def twice(v):
            x,y,z=v;return [z,2*y+3*z,2*(x+y+z)]
        low=twice([x-3*y for x,y in zip(t,n)]);high=twice([3*y-2*x for x,y in zip(t,n)])
        assert low==e['low'] and high==e['high']
        A,B,D=twice(t);aa,bb,dd=twice(n)
        q2=aa*B-bb*A;q1=q2+2*(aa*D-dd*A);q0=(aa+bb)*D-dd*(A+B)
        assert [q2,q1,q0]==e['discrete_difference'] and min(q2,q1,q0)>0
        assert e['difference_positive']==[[1,None]] and e['difference_negative']==[]
        if not covered:
            v=e['vertex_check'];zstar=max(2,(3*beta-2*b)//(2*c));F2=3*alpha+6*beta-2*a-4*b-6*c
            assert zstar==v['maximizer_z']==2 and F2==v['failure_low_first_F2']==v['failure_low_integer_max']>0
            assert v['low_concave']['integer_extreme_m']==[1] and v['low_concave']['twice_extreme']==2*F2
            H=e['H_high_nonpositive'];L=e['L_low_positive'];bal=e['balanced']
            assert len(H)==len(L)==1 and H[0][0]==L[0][0]==1
            h=H[0][1];l=L[0][1]
            val=lambda p,x:(p[0]*x+p[1])*x+p[2]
            assert high[0]>0 and val(high,1)<=0 and val(high,h)<=0<val(high,h+1)
            assert low[0]<0 and val(low,1)>0 and val(low,l)>0>=val(low,l+1)
            assert l<h and bal==[[l+1,h]]
            # Independently check saved convex minimum candidates, allowing ties.
            fl=(-high[1])//(2*high[0]);cand={1,max(1,fl),max(1,fl+1)}
            minimum=min(val(high,j) for j in cand);at=sorted(j for j in cand if val(high,j)==minimum)
            assert v['high_convex']['integer_extreme_m']==at and v['high_convex']['twice_extreme']==minimum
            certs.append(dict(case=k+1,event=label,beta_over_c=str(ratio),F2=F2,zstar=zstar,H=H,L=L,balanced=bal))
assert len(manifest)==384 and len(rows)==96
assert stats==dict(tested=308,skipped=76,covered=278,over=30)
assert len(certs)==30
assert max(ratios)==(Fraction(1206163158146871,125608995203104),96,'B31<z')

# New independent algorithm: D-word reward-moment DP, with no I insertion states.
# A completed D word has L_y=sum(active_y), L_z=sum(active_z),
# min(L_y,L_z)=sum(active_y & active_z) over its 58 proper prefixes.
def moments(p,q,y,z):
    # count, sum Ly, sum Lz, sum Ly*Lz, sum min(Ly,Lz)
    dp=[[[0]*5 for j in range(q+1)] for i in range(p+1)];dp[0][0][0]=1
    for i in range(p+1):
      for j in range(q+1):
        if i==p and j==q:continue
        n,sy,sz,prod,both=dp[i][j]
        uy=int(i>=y[0] and j>=y[1]);uz=int(i>=z[0] and j>=z[1])
        v=[n,sy+uy*n,sz+uz*n,prod+uy*sz+uz*sy+uy*uz*n,both+uy*uz*n]
        for ni,nj in [(i+1,j)]*(i<p)+[(i,j+1)]*(j<q):
            for h,x in enumerate(v):dp[ni][nj][h]+=x
    n,sy,sz,prod,both=dp[p][q];assert n==comb(p+q,p)
    return [prod+both,sy+sz,2*n]
r=rows[95];total=moments(27,31,[9,21],[18,11])
# B31<z simply adds the B31 predecessor gate for z.
event=moments(27,31,[9,21],[18,31]);saved=next(e for e in r['events'] if e['label']=='B31<z')
assert total==r['total'] and event==saved['event']
out=dict(selection_and_skips='PASS',statistics=dict(stats),ordinal_cut_covered=0,maximum_beta_control=dict(case=96,event_label='B31<z',algorithm='D-word reward-moment DP; no I insertion states',total=total,event=event,failure=[x-y for x,y in zip(total,event)],ratio=str(max(ratios)[0])),thirty_exact_interval_certificates=certs)
(OUT/'cross_supplement_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='thirty_exact_interval_certificates'},ensure_ascii=False,indent=2))
print('PASS: saved 30 certificates checked; only fixed case96 independently recounted')
