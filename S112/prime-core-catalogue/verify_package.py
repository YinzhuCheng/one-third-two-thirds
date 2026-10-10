#!/usr/bin/env python3
"""Verify saved witnesses/count crosscheck; optionally verify frozen SHA-256 bytes."""
import argparse,hashlib,json
from pathlib import Path
import catalogue as c
import canonicalize as canon
import singleton_constraints as single
ROOT=Path(__file__).parent

def run(check_hashes=False):
    report=json.loads((ROOT/'enumeration_crosscheck.json').read_text());assert report['status']=='PASS'
    records=json.loads((ROOT/'results/survivors.json').read_text());classes=json.loads((ROOT/'results/survivor_isomorphism_classes.json').read_text())
    source=json.loads((ROOT/'independent_catalogue_n8.json').read_text())
    assert {tuple(x) for x in source['survivor_masks']}=={tuple(d['strict_up_masks']) for d in records}
    for d in records:
        up=d['strict_up_masks'];assert not c.proper_module(up) and c.width(up)>=3
        assert not c.very_good_pairs(up) and not c.very_good_pairs(c.dual(up))
        assert not c.directed_cycle(c.forced_graph(up)) and not c.directed_cycle(c.forced_graph(c.dual(up)))
        assert not c.directed_cycle(c.two_port_graph(up));assert json.loads(json.dumps(c.describe(up)))==d
    assert canon.classify(records)==classes
    for d in json.loads((ROOT/'all_survivor_singleton_constraints.json').read_text()):
        recomputed=single.analyze(d['strict_up_masks'])
        for k,v in recomputed.items():assert d[k]==v
    assert json.loads((ROOT/'independent_test_results.json').read_text())['status']=='PASS'
    if check_hashes:
        manifest=json.loads((ROOT/'MANIFEST.json').read_text())
        for d in manifest['files']:
            p=ROOT/d['path'];assert p.is_file();assert hashlib.sha256(p.read_bytes()).hexdigest()==d['sha256'],d['path']
    print(json.dumps({'status':'PASS','complete_survivor_records':len(records),'exact_classes':len(classes),'all_minimal_singleton_clauses_recomputed':True,'frozen_hashes_checked':check_hashes},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--hashes',action='store_true');a=p.parse_args();run(a.hashes)
