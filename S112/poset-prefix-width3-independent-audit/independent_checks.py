#!/usr/bin/env python3
"""Independent exact audit. No author code is imported. Fail-closed under -O."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from collections import Counter
from pathlib import Path
import copy, json, sys
HERE=Path(__file__).resolve().parent

class Invalid(ValueError): pass
def require(ok, message):
    if not ok: raise Invalid(message)
def rat(x):
    require(type(x) in (int,str), 'rational input must be integer or string')
    try: return Q(x)
    except (ValueError,ZeroDivisionError): raise Invalid('invalid rational')
def dot(x,y):
    require(len(x)==len(y),'dot dimensions')
    return sum((a*b for a,b in zip(x,y)),Q())
def closure(n,edges):
    relation=set(map(tuple,edges))
    require(all(type(a)==type(b)==int and 0<=a<n and 0<=b<n for a,b in relation),'edge endpoints')
    for k in range(n):
        relation |= {(i,j) for i in range(n) for j in range(n) if (i,k) in relation and (k,j) in relation}
    require(all(a!=b for a,b in relation),'acyclic')
    return relation
def pred_from_rel(n,rel):
    return [sum(1<<a for a,b in rel if b==i) for i in range(n)]
def ideal_sets(n,rel,r=None):
    return [frozenset(i for i in range(n) if mask>>i&1) for mask in range(1<<n)
            if (r is None or mask.bit_count()==r) and all(not(mask>>b&1) or mask>>a&1 for a,b in rel)]
def enumerate_permutations(vertices,rel):
    v=set(vertices)
    induced=[(a,b) for a,b in rel if a in v and b in v]
    found=[]
    for perm in permutations(vertices):
        rank={x:i for i,x in enumerate(perm)}
        if all(rank[a]<rank[b] for a,b in induced): found.append(perm)
    return found

def properties(n,rel):
    minimum=[i for i in range(n) if not any(b==i for a,b in rel)]
    maximum=[i for i in range(n) if not any(a==i for a,b in rel)]
    ants=[list(s) for k in range(n+1) for s in combinations(range(n),k)
          if all((a,b) not in rel and (b,a) not in rel for a,b in combinations(s,2))]
    width=max(map(len,ants))
    visited={0}
    while True:
        new=visited|{b for a,b in rel if a in visited}|{a for a,b in rel if b in visited}
        if new==visited:break
        visited=new
    covers=sorted((a,b) for a,b in rel if not any((a,c) in rel and (c,b) in rel for c in range(n)))
    return dict(minima=minimum,maxima=maximum,width=width,maximum_antichains=[a for a in ants if len(a)==width],connected=len(visited)==n,cover_relations=covers)

def profile(n,rel,r):
    ideals=ideal_sets(n,rel,r)
    maxima=properties(n,rel)['maxima']
    expected=[frozenset(set(range(n))-{m}) for m in maxima]
    require(set(ideals)==set(expected),'rank states')
    common=set.intersection(*(set(j) for j in ideals))
    pairs=[list(p) for p in combinations(sorted(common),2) if p not in rel and p[::-1] not in rel]
    F=[];A=[[] for p in pairs]
    for state in expected:
        orders=enumerate_permutations(sorted(state),rel)
        F.append(len(orders))
        for row,(a,b) in zip(A,pairs):row.append(sum(p.index(a)<p.index(b) for p in orders))
    return dict(maxima=maxima,ideals=[sum(1<<x for x in j) for j in expected],common=sorted(common),pairs=pairs,F=F,A=A)

def cell_data(F,A,pattern):
    q=[[Q(a,f) for a,f in zip(row,F)] for row in A]
    return [[Q(1,3)-x if side=='L' else x-Q(2,3) for x in row] for row,side in zip(q,pattern)]
def geometric_two_row_optimum(h):
    """Vertices of two affine half-simplex pieces, rather than the author's active-basis solver."""
    require(len(h)==2 and len(h[0])==len(h[1]),'two-row shape')
    m=len(h[0]);verts=[tuple(Q(int(i==j)) for j in range(m)) for i in range(m)]
    d=[a-b for a,b in zip(*h)]
    for j,k in combinations(range(m),2):
        if d[j]!=d[k]:
            t=d[k]/(d[k]-d[j])
            if 0<=t<=1:
                v=[Q()]*m;v[j]=t;v[k]=1-t;verts.append(tuple(v))
    values=[min(dot(hh,v) for hh in h) for v in verts]
    best=max(values)
    return best,[v for v,z in zip(verts,values) if z==best]

def verify_certificate(F,A,c):
    require(type(F)==list and F and all(type(f)==int and f>0 for f in F),'F positive integers')
    m=len(F);k=len(A)
    require(k>0 and all(type(row)==list and len(row)==m for row in A),'A dimensions')
    require(all(type(a)==int and 0<=a<=f for row in A for a,f in zip(row,F)),'A range')
    require(type(c)==dict,'cell dictionary')
    pattern=c.get('pattern')
    require(type(pattern)==str and len(pattern)==k and set(pattern)<=set('LH'),'cell pattern')
    for key,size in [('mu',m),('lambda_pairs',k),('eta',m)]:
        require(type(c.get(key))==list and len(c[key])==size,key+' dimensions')
    mu=list(map(rat,c['mu']));lam=list(map(rat,c['lambda_pairs']));eta=list(map(rat,c['eta']))
    nu=rat(c['nu']);opt=rat(c['optimum']);h=cell_data(F,A,pattern)
    require(all(x>=0 for x in mu+lam+eta),'nonnegative multipliers')
    require(sum(mu)==1 and sum(lam)==1,'normalizations')
    require(all(dot(row,mu)>=opt for row in h),'primal feasible')
    require(all(sum(lam[i]*h[i][j] for i in range(k))+eta[j]==nu for j in range(m)),'dual identity')
    require(opt==nu,'primal dual equality')
    if k==2: require(geometric_two_row_optimum(h)[0]==opt,'independent geometric optimum')
    return opt

def verify_bundle(data):
    require(type(data)==list and len(data)==3,'three templates')
    require(len({p.get('name') for p in data})==len(data),'unique templates')
    for p in data:
        n=p['n'];r=p['r'];require(type(n)==type(r)==int and r==n-1,'cut')
        rel=closure(n,p['covers_edges']);actual=profile(n,rel,r)
        require(p['pred']==pred_from_rel(n,rel),'predecessor closure')
        require(sorted(map(tuple,p['covers_edges']))==properties(n,rel)['cover_relations'],'Hasse edges')
        for key in ['maxima','ideals','pairs','F','A']:require(p[key]==actual[key],'recomputed '+key)
        sel=p['selected_indices'];require(type(sel)==list and len(sel)>0 and len(set(sel))==len(sel),'selection')
        require(all(type(i)==int and 0<=i<len(p['A']) for i in sel),'selected indices')
        require(p['selected_pairs']==[p['pairs'][i] for i in sel],'selected endpoints')
        A=[p['A'][i] for i in sel]
        cells=p['certificates'];require(type(cells)==list,'certificate list')
        masks=[''.join(v) for v in product('LH',repeat=len(A))]
        require(len(cells)==len(masks) and sorted(c.get('pattern','') for c in cells)==sorted(masks),'complete unique masks')
        opts=[verify_certificate(p['F'],A,c) for c in cells]
        require(type(p.get('covered'))==bool and p['covered']==all(v<=0 for v in opts),'aggregate coverage')
        require(p['covered'] and p.get('covers') is True,'successful template')
        nonfixed=all(any(not Q(1,3)<=Q(a,f)<=Q(2,3) for a,f in zip(row,p['F'])) for row in p['A'])
        require(p.get('all_observed_pairs_nonfixed') is nonfixed and nonfixed,'fixed-pair status')
    return True

def linear_extensions(n,rel):
    predecessors=[{a for a,b in rel if b==i} for i in range(n)]
    def visit(prefix,unused):
        if not unused:
            yield tuple(prefix);return
        for v in sorted(unused):
            if not(predecessors[v]&unused):yield from visit(prefix+[v],unused-{v})
    yield from visit([],set(range(n)))

def guarded_witness(p,pair_index,target_column,chain_length):
    n=p['n'];r=p['r'];m=p['maxima'][target_column];N=n+chain_length
    edges=list(map(tuple,p['covers_edges']))+[(v,n) for v in range(n) if v!=m]+[(i,i+1) for i in range(n,N-1)]
    rel=closure(N,edges);orders=list(linear_extensions(N,rel))
    states=[frozenset(i for i in range(n) if i!=omitted) for omitted in p['maxima']]
    actual=set(frozenset(order[:r]) for order in orders)
    require(actual==set(states),'guarded actual cut support')
    require(all(sum(b==v for a,b in rel)>=r for v in range(n,N)),'outside predecessor guard')
    require(not any(a>=n and b<n for a,b in rel),'initial core ideal')
    B=[len(list(linear_extensions_induced(set(range(N))-state,rel))) for state in states]
    require(B==[chain_length+1 if j==target_column else 1 for j in range(3)],'tail B formula')
    total=len(orders);counts=[sum(order.index(a)<order.index(b) for order in orders) for a,b in p['pairs']]
    require(total==dot(p['F'],B),'total transfer')
    require(all(count==dot(row,B) for count,row in zip(counts,p['A'])),'pair transfer')
    probability=Q(counts[pair_index],total)
    require(not Q(1,3)<=probability<=Q(2,3),'actual fixed-pair failure')
    return dict(pair_index=pair_index,pair=p['pairs'][pair_index],omitted=m,chain_length=chain_length,total_vertices=N,B=B,total_extensions=total,direction_counts=counts,probabilities=[str(Q(v,total)) for v in counts],failed_pair_probability=str(probability),verified_exact_cut_states=p['ideals'])

def linear_extensions_induced(vertices,rel):
    v=sorted(vertices);rename={x:i for i,x in enumerate(v)}
    rel2={(rename[a],rename[b]) for a,b in rel if a in vertices and b in vertices}
    yield from linear_extensions(len(v),rel2)

def all_nonfixed_witnesses(p):
    result=[]
    for i,row in enumerate(p['A']):
        j=next(j for j,(a,f) in enumerate(zip(row,p['F'])) if not Q(1,3)<=Q(a,f)<=Q(2,3))
        k=1
        while Q(1,3)<=Q(sum(row)+k*row[j],sum(p['F'])+k*p['F'][j])<=Q(2,3):k+=1
        result.append(guarded_witness(p,i,j,k))
    return result

def mutation_tests(data):
    results=[]
    def reject(name,fn):
        x=copy.deepcopy(data);fn(x)
        try: verify_bundle(x)
        except (Invalid,KeyError,TypeError,IndexError,ValueError):results.append(name);return
        raise Invalid('mutation accepted: '+name)
    reject('missing mask',lambda x:x[0]['certificates'].pop())
    reject('duplicate mask',lambda x:x[0]['certificates'].__setitem__(1,copy.deepcopy(x[0]['certificates'][0])))
    reject('wrong pattern length',lambda x:x[0]['certificates'][0].__setitem__('pattern','L'))
    reject('invalid pattern letter',lambda x:x[0]['certificates'][0].__setitem__('pattern','XL'))
    reject('negative multiplier',lambda x:x[0]['certificates'][0]['lambda_pairs'].__setitem__(0,'-1'))
    reject('bad dual equality',lambda x:x[0]['certificates'][0]['eta'].__setitem__(0,'1'))
    reject('bad primal normalization',lambda x:x[0]['certificates'][0]['mu'].__setitem__(0,'1'))
    reject('truncated eta',lambda x:x[0]['certificates'][0]['eta'].pop())
    reject('extra multiplier',lambda x:x[0]['certificates'][0]['lambda_pairs'].append('0'))
    reject('float rational',lambda x:x[0]['certificates'][0].__setitem__('nu',-1/3))
    reject('false optimum',lambda x:x[0]['certificates'][0].__setitem__('optimum','0'))
    reject('false aggregate',lambda x:x[0].__setitem__('covered',False))
    reject('empty pair menu',lambda x:x[0].__setitem__('selected_indices',[]))
    reject('wrong selected pair',lambda x:x[0]['selected_pairs'].__setitem__(0,[0,5]))
    reject('wrong count row',lambda x:x[0]['A'][0].__setitem__(0,4))
    reject('wrong denominator',lambda x:x[0]['F'].__setitem__(0,8))
    reject('wrong cut state',lambda x:x[0]['ideals'].__setitem__(0,54))
    reject('nontransitive predecessor table',lambda x:x[0]['pred'].__setitem__(5,6))
    reject('false nonfixed claim',lambda x:x[0].__setitem__('all_observed_pairs_nonfixed',False))
    reject('missing template',lambda x:x.pop())
    return results

def negative_controls(data):
    p=data[0];n=p['n'];rel=closure(n,p['covers_edges'])
    # An independent extra point retains the core as an initial ideal but changes support.
    states=ideal_sets(n+1,rel,p['r']);extra=[s for s in states if n in s]
    require(extra,'unguarded extra states exist')
    two_outside=ideal_sets(n+2,rel,p['r'])
    lost=[s for s in two_outside if any(a not in s or b not in s for a,b in p['selected_pairs'])]
    require(lost,'two unguarded points can break pair observation')
    neg=json.loads((HERE/'author_snapshot/genuine_vertex_negative.json').read_text())
    N=neg['n'];rr={(a,b) for b,mask in enumerate(neg['pred']) for a in range(N) if mask>>a&1}
    require(closure(N,rr)==rr,'negative closure')
    prof=profile(N,rr,N-1)
    for k in ['F','A','pairs','ideals','maxima']:require(prof[k]==neg[k],'negative actual '+k)
    F=neg['F'];A=neg['A']
    require(all(any(Q(1,3)<=Q(row[j],F[j])<=Q(2,3) for row in A) for j in range(3)),'negative vertex coverage')
    opt={c['pattern']:str(verify_certificate(F,A,c)) for c in neg['certificates']}
    require(opt['HH']=='1/120','negative uncovered cell')
    B=[1,4,5];den=dot(F,B);probs=[dot(row,B)/den for row in A]
    require(all(p>Q(2,3) for p in probs),'negative positive-cone hole')
    return dict(unguarded_core_initial_ideal_extra_cut_states=[sorted(s) for s in extra],two_unguarded_points_unobserved_pair_states=[sorted(s) for s in lost],vertex_only_genuine_core=dict(F=F,A=A,all_cells=opt,positive_B=B,probabilities=list(map(str,probs)),note='This B is an abstract positive continuation vector. No completion realizing this vector is asserted.'))

def independent_natural_counts():
    # Every new last label is specified uniquely by its predecessor order ideal.
    # Enumerate ideals as down-closures of antichains, not subset eligibility tests.
    levels=[()];counts={0:1}
    for n in range(1,8):
        nxt=[]
        for pred in levels:
            old=n-1;ideals=set()
            for mask in range(1<<old):
                members=[i for i in range(old) if mask>>i&1]
                if any(pred[b]>>a&1 for a,b in combinations(members,2)):continue
                down=mask
                for i in members:down|=pred[i]
                require(down not in ideals,'unique antichain downsets')
                ideals.add(down)
            nxt.extend(pred+(i,) for i in sorted(ideals))
        levels=nxt;counts[n]=len(levels)
    require([counts[i] for i in [5,6,7]]==[357,4824,96428],'natural enumeration counts')
    return counts

def main():
    path=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'author_snapshot/exact_templates.json'
    data=json.loads(path.read_text());verify_bundle(data)
    report=dict(verdict='PASS',independent_methods=['full core permutations','exact rational two-row simplex subdivision','exact primal and dual identities','recursive full guarded-completion enumeration','antichain-generated naturally labeled posets'],templates=[])
    for p in data:
        n=p['n'];rel=closure(n,p['covers_edges']);stats=properties(n,rel)
        require(stats['width']==3 and stats['connected'],'width three and connected')
        full=enumerate_permutations(range(n),rel)
        require(len(full)==sum(p['F']),'core total decomposition')
        selected=[p['A'][i] for i in p['selected_indices']]
        q=[[Q(a,f) for a,f in zip(row,p['F'])] for row in selected]
        opts={c['pattern']:str(verify_certificate(p['F'],selected,c)) for c in p['certificates']}
        # Extend selected dual weights by zero to certify all full-menu masks.
        extended=[]
        for mask in product('LH',repeat=len(p['A'])):
            projection=''.join(mask[i] for i in p['selected_indices'])
            cert=copy.deepcopy(next(c for c in p['certificates'] if c['pattern']==projection))
            weights=['0']*len(p['A'])
            for index,weight in zip(p['selected_indices'],cert['lambda_pairs']):weights[index]=weight
            cert['pattern']=''.join(mask);cert['lambda_pairs']=weights
            # Feasible matching primal is not guaranteed for extra constraints; only use dual upper bound.
            h=cell_data(p['F'],p['A'],cert['pattern']);lam=list(map(rat,weights));eta=list(map(rat,cert['eta']));nu=rat(cert['nu'])
            require(sum(lam)==1 and all(x>=0 for x in lam+eta),'extended multipliers')
            require(all(sum(lam[i]*h[i][j] for i in range(len(lam)))+eta[j]==nu for j in range(3)) and nu<=0,'extended full-menu dual')
            extended.append(dict(pattern=cert['pattern'],nu=str(nu),lambda_pairs=weights,eta=cert['eta']))
        common_max,points=geometric_two_row_optimum(q)
        lower=min(v for row in q for v in row)
        determinant=(q[0][1]-q[0][0])*(q[1][2]-q[1][0])-(q[0][2]-q[0][0])*(q[1][1]-q[1][0])
        require(common_max=={'W3-six-boundary':Q(2,3),'W3-six-triangle':Q(15,23),'W3-seven-three-minima':Q(131,215)}[p['name']],'sharp envelope')
        report['templates'].append(dict(name=p['name'],properties=stats,full_core_extensions=len(full),profile=profile(n,rel,p['r']),selected_pairs=p['selected_pairs'],q=[[str(v) for v in row] for row in q],all_selected_cell_optima=opts,all_full_menu_duals=extended,sharp_max_min=str(common_max),sharp_mu=[[str(v) for v in point] for point in points],common_lower_bound=str(lower),affine_determinant=str(determinant),guarded_fixed_pair_witnesses=all_nonfixed_witnesses(p)))
    report['mutation_tests_rejected']=mutation_tests(data)
    report['negative_controls']=negative_controls(data)
    report['natural_label_counts']=independent_natural_counts()
    report['optimized_python']=not __debug__
    dest=HERE/('independent_checks_optimized.json' if not __debug__ else 'independent_checks.json')
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(verdict='PASS',output=str(dest),templates=[dict(name=p['name'],core_extensions=p['full_core_extensions'],sharp_max_min=p['sharp_max_min'],witnesses=len(p['guarded_fixed_pair_witnesses']),full_masks=len(p['all_full_menu_duals'])) for p in report['templates']],rejected_mutations=len(report['mutation_tests_rejected']),natural_counts=report['natural_label_counts'],optimized=report['optimized_python']),indent=2))
if __name__=='__main__':main()
