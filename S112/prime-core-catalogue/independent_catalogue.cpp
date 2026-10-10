// Independent direct relation-bitmask enumerator, no ideal-extension generator.
// Build: c++ -O3 -std=c++17 independent_catalogue.cpp -o /tmp/prime_core_oracle
// Run: /tmp/prime_core_oracle 7 > independent_catalogue_n7.json
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using U=unsigned;
using V=std::vector<U>;
V transpose(const V& p){int n=p.size();V d(n);for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(p[a]&(1u<<b))d[b]|=1u<<a;return d;}
bool chain(const V&p,U m){for(U z=m;z;z&=z-1){int a=__builtin_ctz(z);for(U w=z&(z-1);w;w&=w-1){int b=__builtin_ctz(w);if(!(p[a]&(1u<<b))&&!(p[b]&(1u<<a)))return false;}}return true;}
bool prime(const V&p){int n=p.size();U full=(1u<<n)-1;for(U m=1;m<full;m++){if(__builtin_popcount(m)<2)continue;int a=__builtin_ctz(m);bool mod=true;for(int x=0;x<n&&mod;x++)if(!(m&(1u<<x))){int sa=(p[x]&(1u<<a))?1:((p[a]&(1u<<x))?-1:0);for(int y=0;y<n;y++)if(m&(1u<<y)){int sy=(p[x]&(1u<<y))?1:((p[y]&(1u<<x))?-1:0);if(sa!=sy){mod=false;break;}}}if(mod)return false;}return true;}
int width(const V&p){int n=p.size(),best=0;for(U m=0;m<(1u<<n);m++){if(__builtin_popcount(m)<=best)continue;bool a=true;for(int x=0;x<n;x++)if((m&(1u<<x))&&(p[x]&m)){a=false;break;}if(a)best=__builtin_popcount(m);}return best;}
bool very(const V&p){V d=transpose(p);for(int a=0;a<(int)p.size();a++)for(int b=a+1;b<(int)p.size();b++)if(d[a]==d[b]&&chain(p,p[a]&~p[b])&&chain(p,p[b]&~p[a]))return true;return false;}
V good(const V&p){int n=p.size();V d=transpose(p),g(n);for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(a!=b&&!(p[a]&(1u<<b))&&!(p[b]&(1u<<a))&&!(d[a]&~d[b])&&chain(p,p[b]&~p[a]))g[a]|=1u<<b;return g;}
bool cyclic(V p){int n=p.size();for(int k=0;k<n;k++)for(int a=0;a<n;a++)if(p[a]&(1u<<k))p[a]|=p[k];for(int a=0;a<n;a++)if(p[a]&(1u<<a))return true;return false;}
V join(V a,const V&b){for(int i=0;i<(int)a.size();i++)a[i]|=b[i];return a;}
int main(int argc,char**argv){int maxn=argc>1?atoi(argv[1]):7;std::cout<<"{\"enumerator\":\"All strict-relation masks, filtered by transitivity\",\"counts\":[";bool first=true;std::vector<V> survivors;
for(int n=1;n<=maxn;n++){uint64_t all=0,pr=0,w3=0,vg=0,sep=0,two=0;int bits=n*(n-1)/2;for(uint64_t mask=0;mask<(1ull<<bits);mask++){V p(n);int shift=0;for(int a=0;a<n;a++){int len=n-a-1;p[a]=((mask>>shift)&((1ull<<len)-1))<<(a+1);shift+=len;}bool trans=true;for(int a=0;a<n&&trans;a++)for(int b=a+1;b<n;b++)if((p[a]&(1u<<b))&&(p[b]&~p[a])){trans=false;break;}if(!trans)continue;all++;if(!prime(p))continue;pr++;if(width(p)<3)continue;w3++;V d=transpose(p);if(very(p)||very(d))continue;vg++;V g=good(p),h=good(d);if(cyclic(join(p,g))||cyclic(join(d,h)))continue;sep++;V ports(2*n);for(int a=0;a<n;a++){ports[2*a]|=1u<<(2*a+1);for(int b=0;b<n;b++){if(p[a]&(1u<<b)){ports[2*a]|=3u<<(2*b);ports[2*a+1]|=3u<<(2*b);}if(g[a]&(1u<<b))ports[2*a]|=1u<<(2*b);if(h[a]&(1u<<b))ports[2*b+1]|=1u<<(2*a+1);}}if(cyclic(ports))continue;two++;survivors.push_back(p);}
if(!first)std::cout<<",";first=false;std::cout<<"{\"n\":"<<n<<",\"naturally_labelled_posets\":"<<all<<",\"prime_cores\":"<<pr<<",\"prime_width_at_least_3\":"<<w3<<",\"after_very_good_both_sides\":"<<vg<<",\"after_separate_port_cycles\":"<<sep<<",\"after_all_uniform_filters\":"<<two<<"}";std::cerr<<"completed independent n="<<n<<" all="<<all<<" survive="<<two<<std::endl;}
std::cout<<"],\"survivor_masks\":[";first=true;for(auto p:survivors){if(!first)std::cout<<",";first=false;std::cout<<"[";for(int i=0;i<(int)p.size();i++){if(i)std::cout<<",";std::cout<<p[i];}std::cout<<"]";}std::cout<<"]}\n";}
