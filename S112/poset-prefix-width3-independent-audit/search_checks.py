#!/usr/bin/env python3
"""Additional independent checks of the recorded exploratory search outputs."""
from independent_checks import *
import subprocess

def main():
    snapshot=HERE/'author_snapshot';rerun=HERE/'author_rerun'
    checks={}
    for filename in ['candidates.json','exact_templates.json']:
        require(json.loads((snapshot/filename).read_text())==json.loads((rerun/filename).read_text()),'reproduced '+filename)
        checks[filename]='exact JSON equality after copied author rerun'
    candidates=json.loads((snapshot/'candidates.json').read_text())
    analyzed=json.loads((snapshot/'analyzed.json').read_text())
    counts=[]
    for p,a in zip(candidates['candidates'],analyzed['candidates']):
        require(p['pred']==a['pred'],'analysis order')
        n=p['n'];rel=closure(n,p['covers_edges']);actual=profile(n,rel,p['r'])
        require(p['pred']==pred_from_rel(n,rel),'candidate predecessor closure')
        require(properties(n,rel)['width']==3,'candidate width')
        for key in ['maxima','ideals','pairs','F','A']:require(p[key]==actual[key],'candidate '+key)
        require(all(any(not Q(1,3)<=Q(v,f)<=Q(2,3) for v,f in zip(row,p['F'])) for row in p['A']),'no fixed candidate')
        covers=[]
        for pair_indices in combinations(range(len(p['A'])),2):
            A=[p['A'][i] for i in pair_indices]
            if all(geometric_two_row_optimum(cell_data(p['F'],A,pattern))[0]<=0 for pattern in product('LH',repeat=2)):
                covers.append(list(pair_indices))
        require(covers and a['minimum_cover_size']==2 and a['minimum_covers']==covers,'exact minimum pair covers')
        counts.append(dict(n=n,pred=p['pred'],F=p['F'],exact_minimum_cover_size=2,exact_minimum_covers=covers))
    require(len(counts)==28 and len(analyzed['candidates'])==28,'all 28 exploratory candidates checked')
    # Demonstrate the assertion-based author's verifier behavior, without modifying its files.
    probe="""import importlib.util,json,copy,sys
from pathlib import Path
p=Path(sys.argv[1]);spec=importlib.util.spec_from_file_location('author_certify',p/'certify.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
d=json.loads((p/'exact_templates.json').read_text())[0];c=copy.deepcopy(d['certificates'][0]);c['optimum']='999'
try:
 m.verify(d['F'],[d['A'][i] for i in d['selected_indices']],c)
 print('ACCEPTED invalid optimum')
except (AssertionError, RuntimeError) as e:
 print('REJECTED invalid optimum:',type(e).__name__)
"""
    probe_results={}
    for name,flags in [('normal',[]),('optimized',['-O'])]:
        run=subprocess.run([sys.executable,*flags,'-c',probe,str(snapshot)],capture_output=True,text=True)
        require(run.returncode==0,'author verifier probe ran')
        probe_results[name]=run.stdout.strip()
    require(probe_results['normal'].startswith('REJECTED') and probe_results['optimized'].startswith('ACCEPTED'),'recorded assertion caveat')
    output=dict(verdict='PASS for exact exported outputs; author verifier hardening recommended',reproduction=checks,recorded_search_stats=candidates['stats'],all_28_profiles_and_minimum_covers=counts,author_assertion_probe=probe_results)
    (HERE/'search_checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(verdict=output['verdict'],profiles_checked=len(counts),reproduction=checks,author_assertion_probe=probe_results),indent=2))
if __name__=='__main__':main()
