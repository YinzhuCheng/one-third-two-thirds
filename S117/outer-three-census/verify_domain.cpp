#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
int cap(int a){return a==1?3:a==2?9:29;}
int64_t rising(int x,int n){int64_t v=1;for(int k=0;k<n;++k)v*=x+k;return v;}
int main(int argc,char**argv){
 if(argc!=2)return 2;std::ofstream out(argv[1]);if(!out)return 3;
 for(int a=1;a<=3;++a)for(int d=1;d<=3;++d){
  if(a!=3&&d!=3)continue;
  int64_t raw=0,upper1=0,upper2=0;int maxn=0;
  for(int u=2;u<=29;++u)for(int v=2;v<=29;++v){
   if(u>cap(a)||v>cap(d))continue;
   for(int b=1;b<=90;++b){
    if(3*rising(b,a+1)>=rising(b+u,a+1))continue;
    for(int c=1;c<=90;++c){
     if(3*rising(c,d+1)>=rising(c+v,d+1))continue;
     for(int t=1;t<=104;++t){
      if(2*u>=a+b+t+v||2*v>=u+c+t+d||2*t>=b+c+u||2*t>=b+c+v)continue;
      ++raw;maxn=std::max(maxn,u+a+b+c+t+d+v);
      if(3*rising(b+t+v+1,a)<=2*rising(b+t+v+u+1,a))continue;
      ++upper1;
      if(3*rising(c+t+u+1,d)<=2*rising(c+t+u+v+1,d))continue;
      ++upper2;
      out<<u<<' '<<a<<' '<<b<<' '<<c<<' '<<t<<' '<<d<<' '<<v<<'\n';
     }
    }
   }
  }
  std::cout<<a<<' '<<d<<' '<<raw<<' '<<upper1<<' '<<upper2<<' '<<maxn<<'\n';
 }
}
