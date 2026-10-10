// Independent audit: generate a natural order by choosing upward-closed rows
// from the already constructed suffix; test modules by pair-generated closure.
// No functions or data imported from the catalogue under audit.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
int n; array<unsigned,9> U{},D{}; uint64_t cnt[7]; vector<vector<unsigned>> survivors;
bool comparable(int a,int b){return ((U[a]>>b)|(U[b]>>a))&1;}
bool chain(unsigned m){while(m){int a=__builtin_ctz(m);m&=m-1; for(unsigned t=m;t;t&=t-1)if(!comparable(a,__builtin_ctz(t)))return false;}return true;}
int relation(int x,int y){return (U[x]>>y&1)?1:((U[y]>>x&1)?-1:0);}
bool prime(){unsigned full=(1u<<n)-1;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++){
 unsigned m=(1u<<a)|(1u<<b);bool changed=true;
 while(changed&&m!=full){changed=false;for(int x=0;x<n;x++)if(!(m>>x&1)){
  int first=__builtin_ctz(m),r=relation(x,first);bool split=false;
  for(unsigned t=m;t;t&=t-1)if(relation(x,__builtin_ctz(t))!=r){split=true;break;}
  if(split){m|=1u<<x;changed=true;}
 }}
 if(m!=full)return false;
}return true;}
bool width3(){for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)if(!comparable(a,b))for(int c=b+1;c<n;c++)if(!comparable(a,c)&&!comparable(b,c))return true;return false;}
bool cyclic(vector<vector<int>> g){int k=g.size();vector<int> indeg(k);for(auto row:g)for(int b:row)indeg[b]++;vector<int> q;for(int a=0;a<k;a++)if(!indeg[a])q.push_back(a);for(int j=0;j<(int)q.size();j++)for(int b:g[q[j]])if(--indeg[b]==0)q.push_back(b);return (int)q.size()!=k;}
void examine(){cnt[0]++;for(int a=0;a<n;a++){D[a]=0;for(int b=0;b<n;b++)if(U[b]>>a&1)D[a]|=1u<<b;}
 if(!prime())return;cnt[1]++;if(!width3())return;cnt[2]++;
 bool lower=false,upper=false;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++){
  if(D[a]==D[b]&&chain(U[a]&~U[b])&&chain(U[b]&~U[a]))lower=true;
  if(U[a]==U[b]&&chain(D[a]&~D[b])&&chain(D[b]&~D[a]))upper=true;
 }if(lower)cnt[3]++;if(upper)cnt[4]++;if(lower||upper)return;cnt[5]++;
 vector<vector<int>> g(2*n);
 for(int a=0;a<n;a++){g[2*a].push_back(2*a+1);for(int b=0;b<n;b++)if(a!=b){
  if(U[a]>>b&1)g[2*a+1].push_back(2*b);
  else if(!comparable(a,b)){
   if(!(D[a]&~D[b])&&chain(U[b]&~U[a]))g[2*a].push_back(2*b);
   if(!(U[b]&~U[a])&&chain(D[a]&~D[b]))g[2*a+1].push_back(2*b+1);
  }
 }}
 if(cyclic(g))return;cnt[6]++;survivors.emplace_back(U.begin(),U.begin()+n);
}
void generate(int row){if(row<0){examine();return;} unsigned suffix=((1u<<n)-1)^((1u<<(row+1))-1);
 for(unsigned s=suffix;;s=(s-1)&suffix){bool closed=true;for(unsigned t=s;t;t&=t-1)if(U[__builtin_ctz(t)]&~s){closed=false;break;}
  if(closed){U[row]=s;generate(row-1);}if(!s)break;
 }}
int main(int argc,char**argv){int maximum=argc>1?atoi(argv[1]):8;cout<<"{\"counts\":[";
 for(n=1;n<=maximum;n++){fill(begin(cnt),end(cnt),0);generate(n-1);if(n>1)cout<<",";cout<<"{\"n\":"<<n;const char* key[]={"natural","prime","prime_width3","lower_vgp","upper_vgp","post_vgp","post_ports"};for(int j=0;j<7;j++)cout<<",\""<<key[j]<<"\":"<<cnt[j];cout<<"}";cerr<<"n="<<n<<" natural="<<cnt[0]<<" prime="<<cnt[1]<<" survivors="<<cnt[6]<<endl;}
 cout<<"],\"survivor_masks\":[";bool first=true;for(auto p:survivors){if(!first)cout<<",";first=false;cout<<"[";for(int a=0;a<(int)p.size();a++){if(a)cout<<",";cout<<p[a];}cout<<"]";}cout<<"]}\n";
}
