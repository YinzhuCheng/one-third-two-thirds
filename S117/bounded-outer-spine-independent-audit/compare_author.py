#!/usr/bin/env python3
"""Cross-compare the author's complete mask-DP ledger with independent output."""
import argparse,hashlib,json
from pathlib import Path
from audit import occupancy_count,check

def main(source,result,out):
    author=json.loads(source.read_text());ours=json.loads((result/'occupancy_counts.json').read_text());summary=json.loads((result/'summary.json').read_text())
    check(author['arrow_order']==ours['arrow_order'],'arrow_order')
    ar=author['per_vector'];ir=ours['records'];check(len(ar)==len(ir),'length')
    keys=('weights','extensions','ideal_states','all_18_numerators','four_analytic_event_numerators','failed_arrows')
    for a,b in zip(ar,ir):
        for key in keys:check(a[key]==b[key],'oracle_ledger_mismatch',key,b['weights'])
        check([x['name'] for x in a['balanced_endpoints']]==b['balanced_arrows'],'balanced_names',b['weights'])
        for pair in a['balanced_endpoints']:
            check(pair['numerator']==b['all_18_numerators'][ours['arrow_order'].index(pair['name'])],'balanced_count',b['weights'],pair)
    checked_pairs=0;full_results=[]
    for special in author['special_all_pair_results']:
        w=tuple(special['weights']);z,nums,_,pairs=occupancy_count(w,True);counts=dict(zip(pairs,nums))
        check(z==special['extensions'],'special_total')
        expected=[]
        for (x,y),n in counts.items():
            if x<y and 0<n<z:expected.append({'x':list(x),'y':list(y),'numerator_x_before_y':n})
        check(expected==special['all_incomparable_pairs'],'special_all_pairs')
        matching=next(x for x in summary['special_after_first_three_exact_filters'] if x['weights']==list(w))
        for key in ('delta','balanced_pairs','maximizing_pairs'):check(special[key]==matching[key],'special_result',key)
        checked_pairs+=len(expected);full_results.append({'weights':w,'extensions':z,'all_incomparable_pairs':expected})
    report={'status':'PASS','author_verification_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'independent_summary_sha256':hashlib.sha256((result/'summary.json').read_bytes()).hexdigest(),
        'matched_vectors':len(ir),'matched_endpoint_counts':18*len(ir),'matched_analytic_event_counts':4*len(ir),
        'matched_full_incomparable_pair_counts':checked_pairs,'special_all_incomparable_pairs':full_results}
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='special_all_incomparable_pairs'},indent=2,sort_keys=True))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--author',type=Path,required=True);p.add_argument('--independent',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.author,a.independent,a.output)
