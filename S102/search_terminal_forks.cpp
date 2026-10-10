#include <bits/stdc++.h>
using namespace std; using U=unsigned long long;
mt19937_64 rng(990120261010ULL);
struct Check {
 int n,N; vector<int> pre,post,order; vector<U> g,f; U E; vector<vector<U>> m;
 Check(vector<int> p):n(p.size()),N(1<<n),pre(p),post(n),g(N),f(N) {
  for(int j=0;j<n;j++) for(int i=0;i<n;i++) if(pre[j]>>i&1) post[i]|=1<<j;
  g[N-1]=1; for(int mask=N-2;mask>=0;--mask){ bool ideal=true; for(int j=0;j<n;j++)if((mask>>j&1)&&((pre[j]&mask)!=pre[j])){ideal=false;break;} if(!ideal)continue; order.push_back(mask);for(int j=0;j<n;j++)if(!(mask>>j&1)&&((pre[j]&mask)==pre[j]))g[mask]+=g[mask|1<<j];}
  E=g[0];f[0]=1; for(auto it=order.rbegin();it!=order.rend();++it){int mask=*it;for(int j=0;j<n;j++)if(!(mask>>j&1)&&((pre[j]&mask)==pre[j]))f[mask|1<<j]+=f[mask];}
 }
 vector<U> before(int y){vector<U> r(n);for(int mask:order)if(!(mask>>y&1)&&((pre[y]&mask)==pre[y])){U w=f[mask]*g[mask|1<<y];for(int i=0;i<n;i++)if(mask>>i&1)r[i]+=w;}return r;}
 void matrix(){m.assign(n,vector<U>(n));for(int j=0;j<n;j++)m[j]=before(j);for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)swap(m[i][j],m[j][i]);}
};
vector<int> closure(vector<int> p){int n=p.size();for(int k=0;k<n;k++)for(int j=0;j<n;j++)if(p[j]>>k&1)p[j]|=p[k];return p;}
void output(Check &c,int y,int u,int s,int t,U d,string file){c.matrix();ofstream o(file);o<<"{\"n\":"<<c.n<<",\"y\":"<<y<<",\"u\":"<<u<<",\"s\":"<<s<<",\"t\":"<<t<<",\"E\":"<<c.E<<",\"d_count\":"<<d<<",\"pre\":[";for(int i=0;i<c.n;i++)o<<(i?",":"")<<c.pre[i];o<<"],\"counts\":[";for(int i=0;i<c.n;i++){o<<(i?",":"")<<"[";for(int j=0;j<c.n;j++)o<<(j?",":"")<<c.m[i][j];o<<"]";}o<<"]}\n";}
int main(int argc,char**argv){long long limit=argc>1?atoll(argv[1]):1000000;long long eligible=0;set<string> seen;int minN=99;
 // Five-point self-check, labels a,u,s,t,y.
 Check self({0,0,3,3,0});assert(self.E==20);auto r=self.before(4);assert(r[0]==14&&r[1]==14&&r[2]==6&&r[3]==6);U joint=0,one=0;for(int mask:self.order)if(!(mask&16)){U w=self.f[mask]*self.g[mask|16];if((mask&12)==12)joint+=w;if((mask&12)==4)one+=w;}assert(joint==4&&one==2);cerr<<"SELFTEST E20 joint4 single2 PASS\n";
 for(long long it=0;it<limit;it++){
  int n=5+rng()%8;vector<int> p(n);int mode=rng()%4;
  if(mode==0){ // y isolated, two randomly interleaved chains on rest.
   int last[2]={-1,-1};for(int i=0;i<n-1;i++){int c=rng()%2;if(last[c]>=0)p[i]|=1<<last[c];last[c]=i;} double q=(rng()%81)/100.;for(int j=1;j<n-1;j++)for(int i=0;i<j;i++)if((rng()%10000)<q*10000)p[j]|=1<<i;
  } else {int last[3]={-1,-1,-1};for(int i=0;i<n;i++){int c=rng()%3;if(last[c]>=0)p[i]|=1<<last[c];last[c]=i;} double q=(rng()%61)/100.;for(int j=1;j<n;j++)for(int i=0;i<j;i++)if((rng()%10000)<q*10000)p[j]|=1<<i;}
  p=closure(p);Check c(p);for(int y=0;y<n;y++)if(!p[y]){auto r=c.before(y);bool ok=true,hi=false;for(int z=0;z<n;z++)if(z!=y&&!(c.post[y]>>z&1)){if(3*r[z]>=c.E&&3*r[z]<=2*c.E){ok=false;break;}if(3*r[z]>2*c.E)hi=true;}if(!ok||!hi)continue;
   for(int u=0;u<n;u++)if(u!=y&&3*r[u]>2*c.E){bool max=true;for(int v=0;v<n;v++)if((c.post[u]>>v&1)&&3*r[v]>2*c.E)max=false;if(!max)continue;vector<int> cover;for(int v=0;v<n;v++)if((c.post[u]>>v&1)&&!(c.post[y]>>v&1)&&!(c.post[u]&p[v]))cover.push_back(v);assert(cover.size()==2);int s=cover[0],t=cover[1];assert(3*r[s]<c.E&&3*r[t]<c.E&&9*r[u]<7*c.E);U d=0;for(int mask:c.order)if(!(mask>>y&1)&&((p[u]&mask)==p[u]))d+=c.f[mask]*c.g[mask|1<<y];assert(9*d>18*r[u]-5*c.E);eligible++;auto rs=c.before(t);U st=rs[s];if(3*st<c.E||3*st>2*c.E){output(c,y,u,s,t,d,"terminal_fork_witness.json");cerr<<"FOUND iter="<<it<<" n="<<n<<" eligible="<<eligible<<" E="<<c.E<<" st="<<st<<"\n";return 0;}
   }
  }if(it%10000==0)cerr<<"tested="<<it<<" eligible="<<eligible<<"\n";
 }cerr<<"DONE sampled="<<limit<<" eligible="<<eligible<<" no witness\n";
}
