#!/usr/bin/env python3
"""Independent labelled-poset ideal DP: validate every weight vector in {1,2}^8.
This script imports no catalogue/filter implementation and tests no larger core.
"""
from pathlib import Path
from collections import defaultdict
import itertools,json,time
HERE=Path(__file__).parent

def oracle(R,w):
 V=[(i,k) for i in range(len(w)) for k in range(w[i])];N=len(V);end=(1<<N)-1
 relation={(a,b) for a,(i,k) in enumerate(V) for b,(j,l) in enumerate(V) if (i,j) in R or (i==j and k<l)}
 pred=[sum(1<<a for a,b in relation if b==v) for v in range(N)]
 tail={end:1}
 def count(M):
  if M not in tail:tail[M]=sum(count(M|1<<a) for a in range(N) if not M>>a&1 and pred[a]&~M==0)
  return tail[M]
 total=count(0);prefix=defaultdict(int);prefix[0]=1;pairs=[[0]*N for _ in V]
 for M in sorted(tail,key=int.bit_count):
  for a in range(N):
   if M>>a&1 or pred[a]&~M:continue
   nxt=M|1<<a;prefix[nxt]+=prefix[M];ways=prefix[M]*tail[nxt]
   for b in range(N):
    if b!=a and not M>>b&1:pairs[a][b]+=ways
 assert prefix[end]==total
 return V,relation,total,pairs,len(tail)

def main():
 start=time.monotonic();Q=json.loads((HERE/'input_cores.json').read_text());catalogue={q['class_id']:q for q in json.loads((HERE/'weight_filter_catalogue.json').read_text())['cores']}
 counts={'inflations':0,'general_bottom_insertion_bounds':0,'general_top_insertion_bounds':0,'actual_good_pair_lifts':0,'linear_rejections':0,'port_rejections':0,'balanced_witnesses':0,'ideal_states':0};per=[]
 for q in Q:
  n=8;R={(i,j) for i in range(n) for j in range(n) if q['strict_up_masks'][i]>>j&1};C=catalogue[q['class_id']]
  D=[{a for a,b in R if b==i} for i in range(n)];U=[{b for a,b in R if a==i} for i in range(n)]
  inc=[{j for j in range(n) if j!=i and (i,j) not in R and (j,i) not in R} for i in range(n)]
  record={'class_id':q['class_id'],'inflations':0,'linear_pass':0,'port_and_linear_pass':0,'smallest_balanced_example':None}
  for w in itertools.product((1,2),repeat=n):
   V,P,Z,pairs,states=oracle(R,w);N=len(V);index={v:k for k,v in enumerate(V)}
   pd=[{a for a,b in P if b==i} for i in range(N)];pu=[{b for a,b in P if a==i} for i in range(N)]
   def chain(S):return all((a,b) in P or (b,a) in P for a,b in itertools.combinations(S,2))
   counts['ideal_states']+=states
   # General event bound: only one downset/upset inclusion is required.
   for i in range(n):
    den=w[i]+sum(w[j] for j in inc[i])
    for j in inc[i]:
     if D[i]<=D[j]:
      assert den*pairs[index[i,0]][index[j,0]]>=w[i]*Z
      counts['general_bottom_insertion_bounds']+=1
     if U[i]<=U[j]:
      assert den*pairs[index[j,w[j]-1]][index[i,w[i]-1]]>=w[i]*Z
      counts['general_top_insertion_bounds']+=1
   for rule in C['rules']:
    i=rule['target']
    for j in rule['bottom_witnesses']:
     a,b=index[j,0],index[i,0]
     assert pd[a]<=pd[b] and chain(pu[b]-pu[a]);counts['actual_good_pair_lifts']+=1
    for j in rule['top_witnesses']:
     a,b=index[i,w[i]-1],index[j,w[j]-1]
     assert pu[b]<=pu[a] and chain(pd[a]-pd[b]);counts['actual_good_pair_lifts']+=1
   linear=all(2*w[r['target']]<sum(w[j] for j in r['incomparable_indices']) for r in C['rules'])
   port=all(w[i]>=2 for i in C['port_forced_nonsingleton_indices'])
   counts['linear_rejections']+=not linear;counts['port_rejections']+=not port
   balanced=[(a,b) for a in range(N) for b in range(a+1,N) if (a,b) not in P and (b,a) not in P and Z<=3*pairs[a][b]<=2*Z]
   assert balanced,('finite check only',q['class_id'],w)
   counts['balanced_witnesses']+=1
   if record['smallest_balanced_example'] is None:
    a,b=balanced[0];record['smallest_balanced_example']={'weights':list(w),'pair':[V[a],V[b]],'numerator':pairs[a][b],'denominator':Z}
   record['inflations']+=1;record['linear_pass']+=linear;record['port_and_linear_pass']+=linear and port;counts['inflations']+=1
  per.append(record);print(q['class_id'],record['port_and_linear_pass'],flush=True)
 out={'status':'PASS','scope':'Exactly 17 input cores, all 256 positive weight vectors in {1,2}^8 for each core; actual inflation order 8 through 16','method':'Independent labelled-vertex predecessor-mask ideal DP; exact integer pair counts; no uniform quotient/outside law used','counts':counts,'by_class':per,'elapsed_seconds':round(time.monotonic()-start,3),'limitations':'Finite implementation checks are not all-weight proofs. Passing linear and port filters does not imply a counterexample.'}
 (HERE/'inflation_validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
