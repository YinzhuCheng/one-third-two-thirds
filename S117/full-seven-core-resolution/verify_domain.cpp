// Independent direct prerequisite replay: broad global rectangle, no author
// generator, product binary search, rank threshold table, or c-min formula.
#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using Z=mpz_class;
int V(int k){return k==1?3:k==2?9:k==3?29:k==4?43:108;}
Z rising(int x,int k){Z z=1;for(int r=0;r<k;++r)z*=x+r;return z;}
bool product_ok(int a,int u,int b){return 3*rising(b,a+1)<rising(b+u,a+1);}
bool rank_ok(int a,int u,int s){return 3*rising(s+1,a)>2*rising(s+u+1,a);}
int main(int argc,char**argv){
 if(argc!=2)return 2;std::ofstream out(argv[1]);if(!out)return 3;
 long ports=0,old=0,nonempty_ports=0,intervals=0,total=0;int maxn=0;
 std::map<std::pair<int,int>,int> bounds;
 for(int a=1;a<=181;++a)for(int d=a;d<=181;++d){
  if(a+d>184)continue;
  if(a<=3&&d>(a==1?50:a==2?92:181))continue;
  if(a==4&&d>36)continue;
  if(a>=5&&a+d>41)continue;
  for(int u=2;u<=V(a);++u)for(int v=2;v<=V(d);++v){
   if(u+v>110)continue;
   if(16*(a*u+d*v)>=60*(u+v)+25*std::min(u,v)+25*(a+d))continue;
   if(a<=4&&d>=5&&(16*d-60)*v>=25*d+25*a+(85-16*a)*u)continue;
   ++ports;if(d<=3){++old;continue;}
   auto bound=[&](int k,int q){auto key=std::make_pair(k,q);if(bounds.count(key))return bounds[key];int m=0;for(int b=1;b<(k+1)*q;++b)if(product_ok(k,q,b))m=b;return bounds[key]=m;};
   int bm=bound(a,u),cm=bound(d,v);bool any=false;
   for(int b=1;b<=bm;++b)for(int c=1;c<=cm;++c){
    int high=(b+c+std::min(u,v)-1)/2;
    int low=std::max({1,2*u-a-b-v+1,2*v-u-c-d+1});
    if(low>high)continue;
    if(!rank_ok(a,u,b+high+v)||!rank_ok(d,v,c+high+u))continue;
    while(low<=high&&(!rank_ok(a,u,b+low+v)||!rank_ok(d,v,c+low+u)))++low;
    if(low>high)return 4;
    out<<u<<' '<<a<<' '<<b<<' '<<c<<' '<<d<<' '<<v<<' '<<low<<' '<<high<<'\n';
    any=true;++intervals;total+=high-low+1;maxn=std::max(maxn,u+a+b+c+high+d+v);
   }
   if(any)++nonempty_ports;
  }
 }
 std::cout<<"ports "<<ports<<" old "<<old<<" nonempty_ports "<<nonempty_ports<<" intervals "<<intervals<<" vectors "<<total<<" maximum_order "<<maxn<<'\n';
}
