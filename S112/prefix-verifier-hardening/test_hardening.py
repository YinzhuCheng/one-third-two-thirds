#!/usr/bin/env python3
"""Focused fail-closed regression harness for the author verifier repair."""
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path('/workspace/shared/poset-prefix-width3-search')
AUDIT = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path('/workspace/shared/poset-prefix-width3-independent-audit')

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

v = load('repaired_certify', ROOT / 'certify.py')
audit = load('frozen_independent_checks', AUDIT / 'independent_checks.py')
data = json.loads((ROOT / 'exact_templates.json').read_text())
rejections = []

def check(ok, message):
    if not ok:
        raise RuntimeError(message)

def reject(name, call):
    try:
        call()
    except v.Invalid as exc:
        rejections.append({'name': name, 'error': str(exc)})
    else:
        raise RuntimeError('malformed input accepted: ' + name)

def change(path, value, source=data):
    x = copy.deepcopy(source)
    p = x
    for key in path[:-1]:
        p = p[key]
    p[path[-1]] = value
    return x

def mutate(name, path, value):
    reject(name, lambda: v.verify_bundle(change(path, value)))

check(v.verify_bundle(data), 'original bundle failed')
check(audit.verify_bundle(data), 'frozen independent checker failed')
check(not any(isinstance(node, ast.Assert) for node in ast.walk(
    ast.parse((ROOT / 'certify.py').read_text()))), 'assert remains in repaired source')

# Replay the frozen auditor's exact 20 negative controls against the new verifier.
saved = audit.verify_bundle
audit.verify_bundle = v.verify_bundle
try:
    audit_cases = audit.mutation_tests(data)
finally:
    audit.verify_bundle = saved
check(len(audit_cases) == 20, 'unexpected audit mutation count')

# Every supported cell field is present and has its exact expected JSON shape.
for key in ['pattern', 'optimum', 'mu', 'lambda_pairs', 'eta', 'nu']:
    def missing(key=key):
        x = copy.deepcopy(data)
        del x[0]['certificates'][0][key]
        v.verify_bundle(x)
    reject('missing cell ' + key, missing)
for field, bads in {
    'pattern': [None, False, 0, [], ['L', 'L'], '', 'L', 'LLL', 'XL'],
    'mu': [None, '001', [], ['0', '1'], ['0', '0', '1', '0']],
    'lambda_pairs': [None, '01', [], ['1'], ['1', '0', '0']],
    'eta': [None, '000', [], ['0', '0'], ['0', '0', '0', '0']],
}.items():
    for idx, value in enumerate(bads):
        mutate('cell shape ' + field + ' ' + str(idx), [0, 'certificates', 0, field], value)
for field in ['nu', 'optimum', 'mu', 'lambda_pairs', 'eta']:
    for idx, value in enumerate([True, False, 0.0, -1 / 3, None, [], {}, '1/0', 'bad', 'NaN']):
        path = [0, 'certificates', 0, field] + ([0] if field in ['mu', 'lambda_pairs', 'eta'] else [])
        mutate('rational ' + field + ' ' + str(idx), path, value)
mutate('optimum 999', [0, 'certificates', 0, 'optimum'], '999')
mutate('negative primal weight', [0, 'certificates', 0, 'mu'], ['-1', '1', '1'])
mutate('negative dual pair weight', [0, 'certificates', 0, 'lambda_pairs'], ['-1', '2'])
mutate('negative state residual', [0, 'certificates', 0, 'eta', 0], '-1')
mutate('wrong dual normalization', [0, 'certificates', 0, 'lambda_pairs'], ['0', '0'])
mutate('wrong primal normalization', [0, 'certificates', 0, 'mu'], ['0', '0', '0'])
mutate('false nu', [0, 'certificates', 0, 'nu'], '999')
mutate('null cell', [0, 'certificates', 0], None)
mutate('null cell list', [0, 'certificates'], None)
mutate('empty cell list', [0, 'certificates'], [])
mutate('extra cell', [0, 'certificates'], data[0]['certificates'] + [data[0]['certificates'][0]])
mutate('missing cell', [0, 'certificates'], data[0]['certificates'][:-1])
mutate('duplicate mask', [0, 'certificates', 1], data[0]['certificates'][0])

# Profile and selected-menu validation cannot be bypassed using bool == int.
for key in data[0]:
    def missing(key=key):
        x = copy.deepcopy(data)
        del x[0][key]
        v.verify_bundle(x)
    reject('missing template ' + key, missing)
for name, path, value in [
    ('null template', [0], None),
    ('bool n', [0, 'n'], True), ('negative n', [0, 'n'], -1),
    ('string r', [0, 'r'], '5'), ('wrong r', [0, 'r'], 4),
    ('null pred', [0, 'pred'], None), ('truncated pred', [0, 'pred'], [0]),
    ('negative pred', [0, 'pred', 0], -1), ('bool pred', [0, 'pred', 0], False),
    ('out of range pred', [0, 'pred', 0], 64), ('unclosed pred', [0, 'pred', 5], 6),
    ('null edges', [0, 'covers_edges'], None),
    ('edge self loop', [0, 'covers_edges', 0], [0, 0]),
    ('edge wrong size', [0, 'covers_edges', 0], [0, 2, 3]),
    ('edge bool endpoint', [0, 'covers_edges', 0], [False, 2]),
    ('edge out of range', [0, 'covers_edges', 0], [0, 6]),
    ('edge cycle', [0, 'covers_edges'], data[0]['covers_edges'] + [[2, 0]]),
    ('duplicate edge', [0, 'covers_edges'], data[0]['covers_edges'] + [data[0]['covers_edges'][0]]),
    ('redundant Hasse edge', [0, 'covers_edges'], data[0]['covers_edges'] + [[0, 4]]),
    ('null maxima', [0, 'maxima'], None), ('wrong maxima', [0, 'maxima'], [2, 4, 5]),
    ('wrong ideals', [0, 'ideals', 0], 54), ('bool ideal', [0, 'ideals', 0], True),
    ('null pairs', [0, 'pairs'], None), ('bool pair endpoint', [0, 'pairs', 0], [False, True]),
    ('wrong pair', [0, 'pairs', 0], [0, 5]), ('missing pair', [0, 'pairs'], [[0, 1]]),
    ('null F', [0, 'F'], None), ('empty F', [0, 'F'], []),
    ('zero F', [0, 'F', 0], 0), ('negative F', [0, 'F', 0], -1),
    ('float F', [0, 'F', 0], 7.0), ('string F', [0, 'F', 0], '7'),
    ('bool F', [0, 'F', 0], True), ('wrong F', [0, 'F', 0], 8),
    ('null A', [0, 'A'], None), ('empty A', [0, 'A'], []),
    ('null A row', [0, 'A', 0], None), ('truncated A row', [0, 'A', 0], [5, 5]),
    ('extra A row entry', [0, 'A', 0], [5, 5, 6, 0]),
    ('out of range A', [0, 'A', 0, 0], 8), ('negative A', [0, 'A', 0, 0], -1),
    ('float A', [0, 'A', 0, 0], 5.0), ('bool A', [0, 'A', 0, 0], True),
    ('wrong A', [0, 'A', 0, 0], 4),
    ('null selection', [0, 'selected_indices'], None), ('empty selection', [0, 'selected_indices'], []),
    ('bool selection', [0, 'selected_indices'], [False, 1]),
    ('duplicate selection', [0, 'selected_indices'], [0, 0]),
    ('negative selection', [0, 'selected_indices'], [-1, 1]),
    ('out of range selection', [0, 'selected_indices'], [0, 2]),
    ('bool selected endpoints', [0, 'selected_pairs', 0], [False, True]),
    ('wrong selected endpoints', [0, 'selected_pairs', 0], [0, 5]),
    ('false coverage', [0, 'covered'], False), ('integer coverage', [0, 'covered'], 1),
    ('false discovery claim', [0, 'covers'], False), ('integer discovery claim', [0, 'covers'], 1),
    ('false nonfixed', [0, 'all_observed_pairs_nonfixed'], False),
    ('integer nonfixed', [0, 'all_observed_pairs_nonfixed'], 1),
    ('null name', [0, 'name'], None), ('empty name', [0, 'name'], ''),
    ('duplicate name', [1, 'name'], data[0]['name']),
]:
    mutate(name, path, value)
reject('null bundle', lambda: v.verify_bundle(None))
reject('empty bundle', lambda: v.verify_bundle([]))
reject('missing template', lambda: v.verify_bundle(data[:-1]))
reject('extra template', lambda: v.verify_bundle(data + [data[0]]))

# Verify the direct single-cell entry point, bypassing bundle/profile checks.
p = data[0]
F, A, c = p['F'], [p['A'][i] for i in p['selected_indices']], p['certificates'][0]
check(v.verify(F, A, c) == v.Q(-1, 3), 'valid cell optimum')
for f in [None, [], [7, 8], [0, 8, 9], [True, 8, 9], [7.0, 8, 9]]:
    reject('direct bad F ' + repr(f), lambda f=f: v.verify(f, A, c))
for a in [None, [], [A[0]], [[5, 5], A[1]], [[5, 5, 6, 0], A[1]], [[5.0, 5, 6], A[1]]]:
    reject('direct bad A ' + repr(a), lambda a=a: v.verify(F, a, c))
reject('direct false optimum 999', lambda: v.verify(F, A, dict(c, optimum='999')))
reject('dot truncated vector', lambda: v.dot([1], [1, 2]))
reject('solve missing row', lambda: v.solve([[1]], [1, 2]))
reject('solve extra row', lambda: v.solve([[1], [2]], [1]))
for pattern in [None, 1, 'XH', 'L', 'LLL', ['LH'], [False, 'H']]:
    reject('LP invalid pattern ' + repr(pattern), lambda pattern=pattern: v.lp(F, A, pattern))
reject('LP invalid table', lambda: v.lp([0], [[0]], 'L'))

# Positive controls: valid cells are accepted regardless of uncovered positivity;
# upper-bound failure is a bundle property, not an individual proof invalidity.
negative = json.loads((ROOT / 'genuine_vertex_negative.json').read_text())
check(v.verify_cells(negative['F'], negative['A'], negative['certificates'])[-1]
      == v.Q(1, 120), 'valid positive-optimum negative control was rejected')
for template in data:
    selected = [template['A'][i] for i in template['selected_indices']]
    for cell in template['certificates']:
        check(v.verify(template['F'], selected, cell) ==
              audit.verify_certificate(template['F'], selected, cell), 'independent mismatch')
        check(v.lp(template['F'], selected, cell['pattern']) == cell,
              'LP changed a valid certificate')
        integer_cell = copy.deepcopy(cell)
        for field in ['mu', 'lambda_pairs', 'eta']:
            integer_cell[field] = [int(x) if '/' not in x else x for x in cell[field]]
        for field in ['nu', 'optimum']:
            if '/' not in cell[field]: integer_cell[field] = int(cell[field])
        check(v.verify(template['F'], selected, integer_cell) == v.Q(cell['optimum']),
              'exact integer rational input rejected')

# Scalar JSON type fuzzing at every mandatory template and cell field.
# Retain only genuinely changed values; well-formed replacement cases are already
# covered above, so this sweep focuses on incompatible types.
for field in ['n', 'r', 'pred', 'covers_edges', 'maxima', 'ideals', 'pairs', 'F', 'A',
              'selected_indices', 'selected_pairs', 'certificates', 'name', 'covered',
              'covers', 'all_observed_pairs_nonfixed']:
    for value in [None, {}, []]:
        if value == data[0][field]: continue
        mutate('schema sweep ' + field + ' ' + repr(value), [0, field], value)

result = dict(verdict='PASS', optimized=not __debug__,
              author_sha256=hashlib.sha256((ROOT / 'certify.py').read_bytes()).hexdigest(),
              audit_mutations_rejected=audit_cases,
              additional_mutations_rejected=rejections,
              total_rejections=len(audit_cases) + len(rejections),
              valid_templates=3, valid_selected_cells=12,
              negative_control_HH='1/120', assertions_in_repaired_source=0)
print(json.dumps(result, indent=2))
