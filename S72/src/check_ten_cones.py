"""Optional exact checks of the six ten-parameter applications in S72."""
from explore_ten import distribution
from fractions import Fraction
import random,json,csv,time
from pathlib import Path

def main():
    rng=random.Random(720930);rows=[];start=time.time()
    for mode in range(6):
        for _ in range(12):
            s=[rng.randint(1,6) for _ in range(6)]
            a,b,c,d=[rng.randint(1,8) for _ in range(4)]
            if mode==0:b=2*sum(s[1:5])+rng.randrange(3)
            if mode==1:c=2*sum(s[1:5])+rng.randrange(3)
            if mode==2:s[1]=2*(b+c)+rng.randrange(3)
            if mode==3:s[4]=2*(b+c)+rng.randrange(3)
            if mode==4:a=2*(s[0]+s[1]+b)+rng.randrange(3)
            if mode==5:d=2*(s[5]+s[4]+c)+rng.randrange(3)
            st,H=distribution(tuple(s),(a,b,c,d));E=st['total']
            L=sum(s[1:5]);X=b+c
            ratios=[Fraction(L,L+b),Fraction(L,L+c),Fraction(X,X+s[1]),Fraction(X,X+s[4]),
                    Fraction(s[0]+s[1]+b,s[0]+s[1]+b+a),Fraction(s[5]+s[4]+c,s[5]+s[4]+c+d)]
            bound=(1-min(ratios))/2
            assert st['delta']>=Fraction(2,5) and st['delta']>=bound
            # Full position law for the actual witness orientation.
            if mode==0:q=H[0,2][s[0]]
            elif mode==1:q=H[0,2][sum(s[:5])-1][::-1]
            elif mode==2:
                full=H[2,0][0]; off=s[0]; n=L
                q=[sum(full[:off+1])]+full[off+1:off+n]+[sum(full[off+n:])]
            elif mode==3:
                full=H[2,0][b+c-1]; off=s[0]; n=L
                q=([sum(full[:off+1])]+full[off+1:off+n]+[sum(full[off+n:])])[::-1]
            elif mode==4:
                full=H[0,1][0];q=full[:a]+[sum(full[a:])]
            else:
                full=H[0,1][-1];q=([sum(full[:a+1])]+full[a+1:])[::-1]
            assert sum(q)==E and all(q[i]>=q[i+1] for i in range(len(q)-1)),(mode,s,(a,b,c,d),q)
            assert 5*sum(q[:2])<=3*E
            t=next(t for t in range(1,len(q)) if 5*sum(q[:t])>=2*E)
            N=sum(q[:t]);assert 5*N<=3*E
            rows.append(dict(mode=mode,main=' '.join(map(str,s)),outer=f'{a} {b} {c} {d}',
                             total=E,t=t,N=N,delta=str(st['delta']),bound=str(bound)))
    out=Path(__file__).resolve().parents[1]/'evidence'
    out.mkdir(exist_ok=True)
    with (out/'ten_cone_checks.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary=dict(instances=len(rows),cases_per_cone=12,min_delta=str(min(Fraction(r['delta']) for r in rows)),seconds=round(time.time()-start,3))
    print(json.dumps(summary,indent=2));(out/'ten_cone_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
if __name__=='__main__':main()
