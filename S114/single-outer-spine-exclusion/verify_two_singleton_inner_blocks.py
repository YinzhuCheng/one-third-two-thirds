"""Bounded, standard-library independent labelled-DP checks for the five-parameter theorem."""
from itertools import product
from math import comb
from pathlib import Path
import json
from verify_single_outer_spine import z, terms, dual, oracle

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def main():
    vectors=oracles=ranks=bounds=0
    for u,a,t,d,v in product(range(1,5),repeat=5):
        w=(u,a,1,1,t,d,v);den=z(w)
        require(den==oracle(w), 'den==oracle(w)');oracles+=1
        qa=[den];qd=[den]
        for i in range(1,a+1):
            value=z((u,a-i,1,1,t,d,v))
            require(value==oracle(w,((1,i),(0,1))), 'value==oracle(w,((1,i),(0,1)))')
            qa.append(value);oracles+=1;ranks+=1
        for i in range(1,d+1):
            value=z((u,a,1,1,t,d-i,v))
            require(value==oracle(w,((6,v),(5,d-i+1))), 'value==oracle(w,((6,v),(5,d-i+1)))')
            qd.append(value);oracles+=1;ranks+=1
        for values in (qa,qd):
            gaps=[values[i]-values[i+1] for i in range(len(values)-1)]
            require(all(gaps[i]>=gaps[i+1] for i in range(len(gaps)-1)), 'all(gaps[i]>=gaps[i+1] for i in range(len(gaps)-1))')
        K=1+t+v;Kp=1+t+u
        require(qa[-1]*comb(K+a+u,u)<=den*comb(K+u,u), 'qa[-1]*comb(K+a+u,u)<=den*comb(K+u,u)')
        require(qd[-1]*comb(Kp+d+v,v)<=den*comb(Kp+v,v), 'qd[-1]*comb(Kp+d+v,v)<=den*comb(Kp+v,v)');bounds+=2
        if a>=2:
            require(qa[-1]*(K+u+1)*(K+u+2)<=den*(K+1)*(K+2), 'qa[-1]*(K+u+1)*(K+u+2)<=den*(K+1)*(K+2)');bounds+=1
        if d>=2:
            require(qd[-1]*(Kp+v+1)*(Kp+v+2)<=den*(Kp+1)*(Kp+2), 'qd[-1]*(Kp+v+1)*(Kp+v+2)<=den*(Kp+1)*(Kp+2)');bounds+=1
        lower=sum(n for _,j,n in terms(w) if j==0)
        upper=sum(n for _,j,n in terms(dual(w)) if j==0)
        require(lower==oracle(w,((2,1),(4,1))), 'lower==oracle(w,((2,1),(4,1)))')
        require(upper==oracle(w,((4,t),(3,1))), 'upper==oracle(w,((4,t),(3,1)))');oracles+=2
        require(lower*(v+t+2)<den*(v+2), 'lower*(v+t+2)<den*(v+2)')
        require(upper*(u+t+2)<den*(u+2), 'upper*(u+t+2)<den*(u+2)')
        vectors+=1
    alg=0
    for u in range(2,101):
        for v in range(u,101):
            for t in range(1,(u+1)//2+1):
                Kp=1+t+u
                require(2*Kp<=3*v+3, '2*Kp<=3*v+3')
                require(3*(Kp+1)*(Kp+2)<2*(Kp+v+1)*(Kp+v+2), '3*(Kp+1)*(Kp+2)<2*(Kp+v+1)*(Kp+v+2)')
                require(23*v*v+12*v-35>0, '23*v*v+12*v-35>0')
                alg+=1
    result={
        'status':'PASS',
        'weight_family':'(u,a,1,1,t,d,v)',
        'exact_grid':'u,a,t,d,v independently in {1,2,3,4}',
        'weight_vectors':vectors,
        'independent_labelled_ideal_DP_counts':oracles,
        'endpoint_rank_probabilities_checked':ranks,
        'rank_product_bound_checks':bounds,
        'strict_middle_bound_checks':2*vectors,
        'algebra_grid':'2<=u<=v<=100; 1<=t<=floor((u+1)/2)',
        'algebra_grid_points':alg,
        'infinite_claim_status':'Direct proof in TWO_SINGLETON_INNER_BLOCKS_EXCLUSION.md, with stated structural and shuffle dependencies.'
    }
    Path(__file__).with_name('two_singleton_inner_blocks_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
