"""Exact rejection counts in the previously validated {1,2,3}^7 box."""
from weighted_core_formula import *
from fractions import Fraction

names=['singleton_ports','linear_0','linear_6','linear_4','binomial_0','binomial_6','endpoint_first1','endpoint_last5','endpoint_top0_top2','endpoint_bottom3_bottom6']
standalone={name:0 for name in names}
cumulative={name:0 for name in names}
survivors=[]
for w in product(range(1,4),repeat=7):
    u,a,b,c,t,d,v=w
    q=endpoint_counts(w);z=q['extensions']
    tests=[u>=2 and v>=2,
      2*u<a+b+t+v,2*v<u+c+t+d,2*t<u+b+c+v,
      3*comb(a+b+u-1,u)<comb(a+b+t+v+u,u),
      3*comb(d+c+v-1,v)<comb(d+c+t+u+v,v),
      3*q['bottom1_before_bottom0']>2*z,
      3*q['top6_before_top5']>2*z,
      3*q['top0_before_top2']<z,
      3*q['bottom3_before_bottom6']<z]
    alive=True
    for name,test in zip(names,tests):
        standalone[name]+=bool(test)
        alive=alive and test
        cumulative[name]+=bool(alive)
    if alive:survivors.append(w)
survivors.sort(key=lambda w:(sum(w),w))
smallest=survivors[0] if survivors else None
witness=None
if smallest:
    w=smallest;z=count_formula(w)
    pairs=[]
    for i in range(7):
      for j in range(i+1,7):
        for r in range(1,w[i]+1):
          for s in range(1,w[j]+1):
            n=dp_oracle(w,((i,r),(j,s)))
            if 0<n<z:pairs.append(((i,r),(j,s),n))
    delta=max(min(n,z-n) for _,_,n in pairs)
    maximizers=[{'x':x,'y':y,'numerator_x_before_y':n} for x,y,n in pairs if min(n,z-n)==delta]
    balanced=[{'x':x,'y':y,'numerator_x_before_y':n} for x,y,n in pairs if z<=3*n<=2*z]
    witness={'weights':w,'order':sum(w),'extensions':z,'delta_numerator':delta,'delta_denominator':z,
      'delta_reduced':str(Fraction(delta,z)),'maximizing_pairs':maximizers,'balanced_pairs':balanced,
      'endpoint_counts':endpoint_counts(w)}
out={'weight_box':'each wi in {1,2,3}','vectors':3**7,'test_order':names,'standalone_surviving_counts':standalone,
    'cumulative_surviving_counts':cumulative,'survivors':survivors,'smallest_menu_survivor':witness,
    'interpretation':'Every surviving vector is only a failure of this short rejection menu. No claim that it is a counterexample.'}
Path(__file__).with_name('screen_tested_box.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='survivors'},indent=2))
print('all survivors:',survivors)
