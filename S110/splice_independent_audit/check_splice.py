#!/usr/bin/env python3
"""Exact, independent full-ideal counting; no transfer matrices imported."""
import json, hashlib
from fractions import Fraction
from pathlib import Path

OUT=Path(__file__).resolve().parent

def serial(n, gaps):
    return [sum(1<<i for i in range(j) if j-i not in gaps) for j in range(n)]

def valid(pred):
    n=len(pred)
    for j,p in enumerate(pred):
        assert p>>j==0
        for i in range(j):
            if p>>i&1: assert pred[i]&~p==0
    return max((sum(1 for j in range(n) if j!=i and not ((pred[j]>>i)&1 if i<j else (pred[i]>>j)&1)) for i in range(n)),default=0)

def solve(pred):
    n=len(pred); full=(1<<n)-1
    layers=[{0:1}]; successors={}
    for r in range(n):
        nxt={}
        for mask,f in layers[-1].items():
            trans=[]
            for j,p in enumerate(pred):
                if not(mask>>j&1) and p&~mask==0:
                    m=mask|(1<<j); trans.append((j,m)); nxt[m]=nxt.get(m,0)+f
            successors[mask]=trans
        layers.append(nxt)
    back={full:1}
    for layer in reversed(layers[:-1]):
        for mask in layer: back[mask]=sum(back[m] for j,m in successors[mask])
    assert back[0]==layers[-1][full]
    return layers,successors,back,back[0]

def profile(sol,r,D,which,normalize=True):
    layers,succ,back,E=sol; n=len(layers)-1; result={}
    for mask,f in layers[r].items():
        assert mask&((1<<max(0,r-D))-1)==(1<<max(0,r-D))-1
        assert mask>>min(n,r+D)==0
        key=tuple(i-r for i in range(max(1,r-D+1),min(n,r+D)+1) if mask>>(i-1)&1)
        assert key not in result
        result[key]=f if which=='F' else back[mask]
    z=sum(result.values()); return {k:Fraction(v,z) for k,v in result.items()} if normalize else result

def relative(p,q):
    assert p.keys()==q.keys()
    return max(abs(q[k]/p[k]-1) for k in p)

def prob(sol,x,y):
    """1-based labels. Count each path when x appears with y still absent."""
    layers,succ,back,E=sol; total=0; xb=1<<(x-1); yb=1<<(y-1)
    for layer in layers[:-1]:
        for mask,f in layer.items():
            if mask&(xb|yb): continue
            for j,m in succ[mask]:
                if j==x-1: total+=f*back[m]
    return Fraction(total,E)

def splice(pred,a,b,R):
    L=b-a; np=[]
    for j in range(1,len(pred)-L+1):
        oldj=j if j<=a else j+L
        np.append(sum(1<<(i-1) for i in range(1,j) if j-i>R or (pred[oldj-1]>>(oldj-(j-i)-1))&1))
    return np

def fraction(x): return {'exact':str(x),'decimal':float(x)}

def case(n,gaps,a,b,negative=False):
    pred=serial(n,set(gaps)); D=valid(pred); R=2*D-1; h=3*D-1; K=4*D-1; L=b-a
    assert a>=K and b+K<=n
    for i in range(a-K+1,a+K+1):
        for j in range(i+1,a+K+1): assert (pred[j-1]>>(i-1)&1)==(pred[j+L-1]>>(i+L-1)&1)
    if not negative: assert L>=2*K+1
    new=splice(pred,a,b,R); dn=valid(new); assert dn<=D
    for y in range(1,len(new)+1):
        for x in range(1,y):
            if y<=a+K: assert (new[y-1]>>(x-1)&1)==(pred[y-1]>>(x-1)&1)
            if x>=a-K+1: assert (new[y-1]>>(x-1)&1)==(pred[y+L-1]>>(x+L-1)&1)
            if y<=a or x>a:
                ox=x if x<=a else x+L; oy=y if y<=a else y+L
                assert (new[y-1]>>(x-1)&1)==(pred[oy-1]>>(ox-1)&1)
    oldsol=solve(pred); newsol=solve(new)
    for r in (a-h,a+h):
        assert profile(newsol,r,D,'F',False)==profile(oldsol,r,D,'F',False)
        assert profile(newsol,r,D,'B',False)==profile(oldsol,r+L,D,'B',False)
    ef=relative(profile(oldsol,a-h,D,'F'),profile(oldsol,b-h,D,'F'))
    eb=relative(profile(oldsol,a+h,D,'B'),profile(oldsol,b+h,D,'B'))
    eta=max(ef,eb); assert eta<=Fraction(1,2)
    result={'n':n,'incomparable_gaps':gaps,'D':D,'a':a,'b':b,'L':L,'R':R,'h':h,'K':K,'new_n':len(new),'new_D':dn,'extension_count_old':str(oldsol[3]),'extension_count_new':str(newsol[3]),'forward_relative_error':fraction(ef),'backward_relative_error':fraction(eb),'eta':fraction(eta),'ideal_count_old':sum(map(len,oldsol[0])),'ideal_count_new':sum(map(len,newsol[0]))}
    if negative:
        x=a-1; oldy=a+2; newy=oldy-L
        assert not(pred[oldy-1]>>(x-1)&1)
        assert new[newy-1]>>(x-1)&1
        pp=prob(oldsol,x,oldy); qq=prob(newsol,x,newy)
        assert abs(qq-pp)>eta
        result.update({'preserved_identity_pair':[x,oldy],'new_labels':[x,newy],'old_probability':fraction(pp),'new_probability':fraction(qq),'error':fraction(abs(qq-pp)),'error_exceeds_eta':True,'classification':'negative control: fails cut separation; not a counterexample to stated theorem'})
    else:
        mx=Fraction(0); witness=None; left=right=cross=0
        for y in range(1,len(new)+1):
            for x in range(1,y):
                if new[y-1]>>(x-1)&1: continue
                if y<=a: ox,oy=x,y;left+=1
                elif x>a: ox,oy=x+L,y+L;right+=1
                else: ox,oy=x,y;cross+=1
                assert not(pred[oy-1]>>(ox-1)&1)
                pp=prob(oldsol,ox,oy); qq=prob(newsol,x,y); err=abs(pp-qq)
                assert err<=eta,(x,y,err,eta)
                assert 2*err<=eta*(1+err*err), 'sharp reweighting bound'
                if err>mx:mx=err;witness={'new_pair':[x,y],'original_witness':[ox,oy],'original_probability':fraction(pp),'new_probability':fraction(qq)}
        result.update({'same_side_left_pairs':left,'same_side_right_pairs':right,'new_cross_seam_pairs':cross,'maximum_probability_error':fraction(mx),'maximizing_witness':witness,'all_exact_inequalities_pass':True})
    return result

if __name__=='__main__':
    specs=[(29,[1],7,22),(61,[1],14,40),(121,[1,2],32,80),(121,[1,3],32,80),(181,[1,2,3],50,110)]
    data={'method':'Full ideal-mask path count with exact integers/Fractions; no imported transition matrices, no uniform deletion assumptions. Pair events counted when first endpoint is emitted while second absent.','positive_cases':[],'overlapping_cut_negative_control':None}
    for spec in specs:
        r=case(*spec);data['positive_cases'].append(r);print('PASS',spec,'eta',r['eta']['decimal'],'max error',r['maximum_probability_error']['decimal'],flush=True)
    data['overlapping_cut_negative_control']=case(101,[1,3],50,51,True)
    r=data['overlapping_cut_negative_control'];print('NEGATIVE_CONTROL',r['eta']['decimal'],r['error']['decimal'],flush=True)
    (OUT/'exact_checks.json').write_text(json.dumps(data,indent=2)+'\n')
