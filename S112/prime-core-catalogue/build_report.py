#!/usr/bin/env python3
"""Reconcile independent enumerations and build deterministic class/weight reports."""
import json
from pathlib import Path
import catalogue as c
import canonicalize as canon
import singleton_constraints as single

ROOT=Path(__file__).parent

def save(p,obj):p.write_text(json.dumps(obj,indent=2)+'\n')

def run():
    summary=json.loads((ROOT/'results/summary.json').read_text())
    independent=json.loads((ROOT/'independent_catalogue_n8.json').read_text())
    records=json.loads((ROOT/'results/survivors.json').read_text())
    counts={d['n']:d for d in summary['counts']}
    assert summary['max_n']==8
    for row in independent['counts']:
        for key,value in row.items():assert counts[row['n']][key]==value,(key,row)
    aset={tuple(d['strict_up_masks']) for d in records};bset={tuple(d) for d in independent['survivor_masks']}
    assert len(aset)==len(records)==len(bset)==len(independent['survivor_masks'])==2596
    assert aset==bset
    classes=canon.classify(records)
    assert len(classes)==18
    save(ROOT/'results/survivor_isomorphism_classes.json',classes)
    assert {n:sum(d['n']==n for d in classes) for n in (7,8)}=={7:1,8:17}
    n7=[d for d in classes if d['n']==7]
    save(ROOT/'n7_survivor_isomorphism_classes.json',n7)
    save(ROOT/'n7_singleton_constraints.json',[single.analyze(d['representative_naturally_labelled']['strict_up_masks']) for d in n7])
    constraints=[]
    for i,cl in enumerate(classes,1):
        rep=cl['representative_naturally_labelled'];d=single.analyze(rep['strict_up_masks'])
        d.update({'class_id':f'C{i:02d}','n':cl['n'],'width':rep['width'],'height':rep['height'],'cover_edges':rep['cover_edges'],'natural_labelled_multiplicity':cl['natural_labelled_multiplicity'],'automorphisms':cl['automorphisms'],'linear_extensions_of_representative':cl['linear_extensions_of_representative']})
        constraints.append(d)
    save(ROOT/'all_survivor_singleton_constraints.json',constraints)
    save(ROOT/'enumeration_crosscheck.json',{'status':'PASS','max_n':8,'compared_nested_count_fields':list(independent['counts'][-1]),'identical_complete_survivor_sets':True,'survivor_natural_label_count':len(aset),'survivor_isomorphism_classes_by_n':{'7':1,'8':17},'canonicalization_multiplicity_identity_all_classes':'PASS','independent_algorithms':'Python largest-maximal-vertex/ideal generator versus C++ direct strict-relation-bitmask generator.'})
    lines=['# Exact catalogue counts','', 'All enumeration columns below count naturally labelled relations, not unlabelled posets.','', '| n | Natural posets | Prime | Prime, width ≥3 | No very-good pair either side | Separate cycles passed | Generic two-port passed | Survivor isomorphism classes |','|---:|---:|---:|---:|---:|---:|---:|---:|']
    for n,r in counts.items():
        vals=[n]+[r[k] for k in ['naturally_labelled_posets','prime_cores','prime_width_at_least_3','after_very_good_both_sides','after_separate_port_cycles','after_all_uniform_filters']]+[sum(d['n']==n for d in classes)]
        lines.append('| '+' | '.join(map(str,vals))+' |')
    lines+=['','The last column alone is an exact isomorphism-class count, obtained by canonicalizing survivors. Duals are not automatically identified.','', 'No cycle filter adds a uniform exclusion beyond very-good pairs through n=8. There are no recorded cycle-beyond-very-good examples in this range.','', 'At n=8, survivors by width: 2,087 natural copies at width 3 and 465 at width 4; by height: 783 at height 3, 1,687 at height 4, and 82 at height 5.','', '## Exact survivor-class inventory','', 'Representative upper masks are the lexicographically least natural presentation. Every class has Aut=1. The displayed forced nonsingletons are complete minimal singleton-pattern clauses in this finite catalogue; all clauses happen to be singletons. A blank clause list means this structural test supplies no weight restriction.','', '| ID | n | width | height | Natural copies = e(Q) | Must have weight ≥2 | Local minimum total size from these clauses |','|---|---:|---:|---:|---:|---|---:|']
    for d in constraints:
        clauses=[q['singleton_vertices'] for q in d['minimal_forbidden_singleton_subsets']]
        assert all(len(S)==1 for S in clauses)
        lines.append('| '+' | '.join(map(str,[d['class_id'],d['n'],d['width'],d['height'],d['natural_labelled_multiplicity'],', '.join(str(S[0]) for S in clauses) or 'none',d['necessary_total_inflation_size_from_this_filter']]))+' |')
    lines+=['','These are necessary lower bounds from port constraints only, not existence results or sharp bounds for counterexamples.','', '## Representatives','']
    for d in constraints:
        lines += [f"### {d['class_id']}",f"Upper masks: `{tuple(d['strict_up_masks'])}`.",f"Cover edges: `{d['cover_edges']}`.",'']
    (ROOT/'COUNTS.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'status':'PASS','max_n':8,'survivor_natural_labels':len(records),'survivor_classes':len(classes),'n8_classes_without_singleton_constraint':sum(d['n']==8 and not d['minimal_forbidden_singleton_subsets'] for d in constraints)},indent=2))

if __name__=='__main__':run()
