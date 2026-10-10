# Guarded-prefix author verifier hardening

Date: 2026-10-10. Status: PASS in normal and optimized Python.

## Scope

Only `/workspace/shared/poset-prefix-width3-search/certify.py` was changed in the original project. The frozen independent audit, existing certificate outputs, count tables, mathematical results, and remote repositories were not changed. All tracked frozen-audit hashes verify. A before/after inventory confirms that the only modified file across the original project and frozen audit is the author verifier itself, with no added or missing files in either directory.

## Repair

- Replace every safety-critical assertion, including LP solver invariants and exporter checks, with explicit `Invalid(ValueError)` exceptions that remain active under `python -O`.
- Reject float, boolean, malformed, or otherwise non-integer/non-string rational input. Exact integer and string rational inputs remain accepted, matching the independent checker's boundary convention.
- Check positive integer denominators, bounded integer count rows, exact dimensions, mandatory fields, valid L/H orientations, primal/dual nonnegativity and normalization, primal feasibility, statewise dual identities, and equality of primal and dual values before accepting a cell.
- Add `verify_cells` to require every orientation exactly once. Add `verify_profile`, `verify_template`, and `verify_bundle` to reconstruct the Hasse order, predecessor closure, maximal omissions, rank states, observed pairs, and exact count tables, and to check selection and aggregate claims. The bundle entry point expects the same three-template export as the independent checker.
- Preserve the LP algorithm, valid certificate dictionary order, chosen primal/dual solutions, JSON export, and printed output. `verify` now returns the exact optimum on success; its former return was `None`. It never claims full-mask coverage from an isolated cell.

## Results

Both `python` and `python -O`:

- Reproduce `exact_templates.json` and `certify.log` byte-for-byte.
- Accept all three valid templates and all 12 selected cell certificates.
- Reject 267 malformed-input cases per mode: the frozen audit's 20 mutations plus 247 additional shape, type, field, mask, algebraic, profile, selection, and direct-entry-point checks.
- Reject the original optimum=999 exploit with `Invalid: primal feasible`.
- Accept the mathematically valid uncovered negative-control certificate with HH optimum 1/120, ensuring positive cell optima are not incorrectly treated as invalid proofs.
- Agree with the frozen independent cell checker on all 12 selected optima; that check includes its independent two-row geometry.
- Have zero AST `assert` nodes in the repaired source.

The baseline probe reproduces the prior bug: original source rejects optimum=999 normally and accepts it under optimized Python. The repaired source rejects it in both modes. Full details are in `optimum-999-probe.log`, `tests.normal.json`, and `tests.optimized.json`.

## SHA-256

- Original certify.py: `13baed71339b33e872bb5e81e91b815131f4dd69548776481b4452a0bd2a6c3a`
- Repaired certify.py: `4d35c66632ff9f1f89cecccf18e5aaf02f8a94a18c217f1823b5e9e01a721451`
- Unchanged exact_templates.json: `e1f07ca69cebe5ca816c0ed08835eb1c9b0581ec68ac4c9ba2cb7add1696c05c`
- Unchanged certify.log: `cf6368bc029ddcd20696ddb5d05bcdf44fb0d3d882567b5e1500842cee1797ee`
- Unified patch: `6c86266056295d25fdf65c9e85e800ec041374ae07df7cec10406298451813e2`

## Reproduction without changing the source project or frozen audit

Use a temporary output directory for exporter runs because the default author script writes its certificate output next to itself:

```sh
src=/workspace/shared/poset-prefix-width3-search
audit=/workspace/shared/poset-prefix-width3-independent-audit
work=$(mktemp -d)
cp "$src/certify.py" "$src/candidates.json" "$work/"
PYTHONDONTWRITEBYTECODE=1 python "$work/certify.py" > "$work/certify.log"
cmp "$src/exact_templates.json" "$work/exact_templates.json"
cmp "$src/certify.log" "$work/certify.log"
PYTHONDONTWRITEBYTECODE=1 python -O "$work/certify.py" > "$work/certify.log"
cmp "$src/exact_templates.json" "$work/exact_templates.json"
cmp "$src/certify.log" "$work/certify.log"
PYTHONDONTWRITEBYTECODE=1 python /tmp/prefix-verifier-hardening/test_hardening.py "$src" "$audit"
PYTHONDONTWRITEBYTECODE=1 python -O /tmp/prefix-verifier-hardening/test_hardening.py "$src" "$audit"
(cd "$audit" && sha256sum -c SHA256SUMS)
```

The regression harness accepts alternate project/audit directory arguments for a relocated package. It imports the frozen audit only read-only with bytecode writing disabled; it does not invoke the audit's report-writing main routine. During the original audit's mutation-harness replay, only an in-memory function binding is temporarily redirected to the repaired author verifier and is restored afterward.

This is a narrowly scoped implementation repair. It does not broaden any theorem, establish any new exhaustive classification, or change the frozen audit's historical verdict about the original snapshot.
