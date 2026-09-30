"""S75 optional exact finite core, equal ten-module lengths 2 <= t <= 39.
The infinite tail t >= 40 is proved in notes/PROOF.md.
Two encodings of ideal counting share the template and domain; they are not
an external review or two independent mathematical reductions.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import csv, json, sys
sys.setrecursionlimit(10000)
PRED=(0,1,67,71,79,479,0,1,193,207)

def matrix(t:int):
    if t<1: raise ValueError('positive length required')
    end=(6*t,2*t,2*t)
    @lru_cache(None)
    def nxt(s):
        i,j,k=s; out=[]
        if i<6*t and (i!=2*t or j>=t) and (i!=5*t or k>=2*t):
            out.append((0,(i+1,j,k)))
        if j<t or (j<2*t and i>=4*t and k>=t):
            out.append((1,(i,j+1,k)))
        if (k<t and i>=t) or (t<=k<2*t and j>=t):
            out.append((2,(i,j,k+1)))
        return tuple(out)
    @lru_cache(None)
    def back(s):
        if s==end:return 1
        return sum(back(v) for _,v in nxt(s))
    E=back((0,0,0)); states=back.cache_info().currsize
    H=[[0]*(t+1) for _ in range(t)]
    layer={(0,0,0):1}
    for _ in range(10*t):
        new={}
        for s,f in layer.items():
            for q,v in nxt(s):
                new[v]=new.get(v,0)+f
                if q==1 and s[1]<t:
                    H[s[1]][min(s[0],t)]+=f*back(v)
        layer=new
    if layer!={end:E}:raise AssertionError('forward/backward totals differ')
    best=None
    for i,row in enumerate(H,1):
        if sum(row)!=E:raise AssertionError('distribution is not normalized')
        N=0
        for j in range(1,t+1):
            N+=row[j-1]
            item=(min(N,E-N),-i,-j,N)
            if best is None or item>best:best=item
    value,ni,nj,N=best
    nxt.cache_clear();back.cache_clear()
    return E,-ni,-nj,N,states

def module_count(t:int,witness:tuple[int,int]|None=None)->int:
    """Direct event count with ten module-prefix coordinates."""
    pred=[[j for j in range(10) if PRED[k]>>j&1] for k in range(10)]
    end=(t,)*10
    @lru_cache(None)
    def count(s):
        if s==end:return 1
        z=0
        for k in range(10):
            if s[k]>=t or any(s[j]!=t for j in pred[k]):continue
            if witness is not None and k==0 and s[0]==witness[1]-1 and s[6]<witness[0]:continue
            v=list(s);v[k]+=1;z+=count(tuple(v))
        return z
    z=count((0,)*10);count.cache_clear();return z

def main():
    root=Path(__file__).resolve().parents[1]/'evidence';root.mkdir(exist_ok=True)
    rows=[];low=None
    for t in range(2,40):
        E,i,j,N,states=matrix(t)
        if module_count(t)!=E or module_count(t,(i,j))!=N:raise AssertionError(('cross-check',t))
        if not 2*E<=5*N<=3*E:raise AssertionError(('not balanced',t))
        bal=Fraction(min(N,E-N),E)
        if low is None or bal<low[0]:low=(bal,t)
        rows.append(dict(t=t,i=i,j=j,E=str(E),N=str(N),E_minus_N=str(E-N),left_margin=str(5*N-2*E),right_margin=str(3*E-5*N),probability=str(Fraction(N,E)),balance=str(bal),states=states))
        print(t,i,j,str(Fraction(N,E)),flush=True)
    with (root/'equal_template_2_39.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    summary=dict(cases=38,domain='integer t=2,...,39',all_pass=True,smallest_selected_balance=str(low[0]),smallest_selected_at=low[1],shared_inputs='same template and domain; two encodings of ideal counting')
    (root/'finite_summary.json').write_text(json.dumps(summary,indent=2)+'\n')

if __name__=='__main__':main()
