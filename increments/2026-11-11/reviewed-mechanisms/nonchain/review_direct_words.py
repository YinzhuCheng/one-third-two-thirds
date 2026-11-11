"""Independent audit: build covers, list all original words, filter real fibres."""
import hashlib,json
from pathlib import Path


def relation(n,orientation=None):
 names=['a','b','c','u','v','x','d']+[f'z{i}' for i in range(1,n+1)]
 edges=[('a','u'),('a','v'),('b','c'),('a','x'),('c','x'),('a','d'),('c','d'),('u','z1'),('v','z1'),('d','z1'),('x',f'z{n}')]
 edges += [(f'z{i}',f'z{i+1}') for i in range(1,n)]
 if orientation:edges.append(orientation)
 index={x:i for i,x in enumerate(names)}
 mat=[[False]*len(names) for _ in names]
 for a,b in edges:mat[index[a]][index[b]]=True
 for k in range(len(names)):
  for i in range(len(names)):
   for j in range(len(names)):mat[i][j] |= mat[i][k] and mat[k][j]
 assert not any(mat[i][i] for i in range(len(names)))
 pred={x:{names[i] for i in range(len(names)) if mat[i][j]} for j,x in enumerate(names)}
 succ={x:{names[j] for j in range(len(names)) if mat[i][j]} for i,x in enumerate(names)}
 return names,pred,succ


def words(names,pred):
 out=[]
 def extend(prefix,remaining):
  if not remaining:out.append(tuple(prefix));return
  placed=set(prefix)
  for x in names:
   if x in remaining and pred[x]<=placed:
    extend(prefix+[x],remaining-{x})
 extend([],set(names))
 return out


def stats(ws):
 def k(*pairs):return sum(all(w.index(a)<w.index(b) for a,b in pairs) for w in ws)
 N=len(ws);Kba=k(('b','a'));Kvc=k(('v','c'));Kxv=k(('x','v'));Kdv=k(('d','v'));Kcvx=k(('c','v'),('v','x'))
 union=sum(min(w.index('d'),w.index('x'))<w.index('v') for w in ws)
 return dict(N=N,Kba=Kba,Kvc=Kvc,Kxv=Kxv,Kdv=Kdv,Kcvx=Kcvx,K_union=union,Bx=Kba+Kvc+Kxv-N,Bd=Kba+Kvc+Kdv-N,B_union=Kba+Kvc+union-N)

out=[]
for n in range(5,9):
 names,pred,succ=relation(n);ws=words(names,pred);s=stats(ws)
 expected=dict(N=38*n+86,Kba=18*n+46,Kvc=14*n+20,Kxv=45,Kdv=12*n+33,Kcvx=24*n+21,K_union=12*n+48,Bx=25-6*n,Bd=6*n+13,B_union=6*n+28)
 assert s==expected,(n,s,expected)
 degrees={x:len(set(names)-{x}-pred[x]-succ[x]) for x in names}
 expecteddeg={'a':2,'b':3,'c':3,'u':5,'v':5,'x':n+2,'d':3}|{f'z{i}':1 if i<n else 0 for i in range(1,n+1)}
 assert degrees==expecteddeg
 assert max(degrees.values())==n+2
 assert {x for x in names if x not in succ['a']|{'a'}}=={'b','c'}
 O=succ['c']&succ['u']&succ['v'];assert O=={f'z{i}' for i in range(1,n+1)}
 assert len(set(names)-O)==7
 assert pred['u']==pred['v']=={'a'}
 Dc={x for x in names if x not in {'a','b','c','u','v'}|O and x in succ['c'] and x not in succ['u']|succ['v']}
 assert Dc=={'d','x'} and pred['d']==pred['x']=={'a','b','c'}
 plus=[w for w in ws if w.index('x')<w.index('d')];minus=[w for w in ws if w.index('d')<w.index('x')]
 assert len(plus)+len(minus)==len(ws)
 # Rebuild both orientation posets, and compare their entire word SETS to real cells.
 orientation_degrees={}
 for pair,fibre in [(('x','d'),plus),(('d','x'),minus)]:
  nam,pred_or,succ_or=relation(n,pair)
  assert set(words(nam,pred_or))==set(fibre)
  deg_or={x:len(set(nam)-{x}-pred_or[x]-succ_or[x]) for x in nam}
  orientation_degrees['<'.join(pair)]={'Delta':max(deg_or.values()),'degrees':deg_or}
 assert orientation_degrees['x<d']['Delta']==5
 assert orientation_degrees['d<x']['Delta']==max(5,n+1)
 sp,sm=stats(plus),stats(minus)
 assert (sp['N'],sp['Kba'],sp['Kvc'],sp['Kxv'],sp['Kdv'],sp['Bx'])==(62,32,17,30,15,17)
 assert (sm['N'],sm['Kba'],sm['Kvc'],sm['Kxv'],sm['Kdv'],sm['Bx'],sm['Bd'])==(38*n+24,18*n+14,14*n+3,15,12*n+18,8-6*n,6*n+11)
 assert sp['Bx']+sm['Bd']==s['B_union']
 assert sp['Bx']+sm['Bx']==s['Bx']
 assert s['B_union']-s['Bx']==12*n+3
 assert 3*s['Kba']-s['N']==16*n+52>0 and 2*s['N']-3*s['Kba']==22*n+34>0
 assert sum(w.index('u')<w.index('v') for w in ws)*2==len(ws)
 out.append(dict(n=n,Delta=max(degrees.values()),whole=s,x_before_d=sp,d_before_x=sm,degrees=degrees,orientation_degrees=orientation_degrees,physical_names=names,full_downsets={x:sorted(pred[x]) for x in names},O=sorted(O),Q_size=7,full_word_list=[list(w) for w in ws]))
proof=Path('research-review/nonchain-D10-true-bank-20261111/PROOF.md')
result=dict(status='PASS_WITH_EXACT_SCOPE',method='Explicit-cover transitive closure plus direct listing of every full original extension; independently rebuilt oriented posets exactly match filtered word sets.',proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),proof_bytes=proof.stat().st_size,cases=out)
path=Path(__file__).with_name('INDEPENDENT_DIRECT_WORDS.json');path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
for row in out:
 print(json.dumps({k:v for k,v in row.items() if k in ['n','Delta','whole','x_before_d','d_before_x','Q_size']},indent=2))
