#!/usr/bin/env python3
"""Regenerate the author census with Python standard-library integers only.
The compiled C++ count program is an optional accelerator for the count step.
"""
import argparse,json,time
from pathlib import Path
import explore
from verify_exact import exact
import summarize
P=Path(__file__).parent

def main(domain_only):
 explore.main()
 ws=json.loads((P/'analytic_survivors.json').read_text())
 (P/'analytic_survivors.txt').write_text(''.join(' '.join(map(str,w))+'\n' for w in ws))
 if domain_only:return
 start=time.time()
 with (P/'exact_counts.txt').open('w') as out:
  for k,w in enumerate(ws,1):
   out.write(' '.join(map(str,(*w,*exact(w))))+'\n')
   if k%2000==0:print('counted',k,'seconds',round(time.time()-start,3),flush=True)
 summarize.main()
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--domain-only',action='store_true');main(p.parse_args().domain_only)
