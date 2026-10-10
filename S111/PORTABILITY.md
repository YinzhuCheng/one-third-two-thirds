# Publication paths and audit binding

This is a scoped, portable S111 publication. It does not replace any prior S109/S110 files. Original source snapshots remain unchanged outside this bundle. Private working paths, execution records and publication receipts are not included.

## Exact original audit bindings

- Core fiber audit `INDEPENDENT_AUDIT.md`: original SHA-256 `c0d04de956d0b72bd59490812ef5b8c266fcd214483ce828eaee644dadf0acdb`.
- Recurrence audit `SECTION5_AUDIT.md`: original SHA-256 `74c2d92f0060c8602fe94db0240a77687467e52e027ffe4d071612c39f1ed731`.
- Realizability/restricted-proof audit `AUDIT_REPORT.txt`: original SHA-256 `87f0d8f5ee9678cadb0e71fa61b4271f89083b9fb526af88134bbeed53e11aec`.
- Fiber source `REPORT.md`: original SHA-256 `23484a21f230c49b6a30a4436a97195e169052915e032b2f348e201ba35f2ad5`.
- Longer source `proof_route_partial.txt`: original SHA-256 `8f76bdb6efa2a089bbdbb2a3abe4ae2e89c8878d16b67cd0dbdccb2f89f27111`. **The complete longer note is not included or represented as fully audited.** Only its exact source sections 1 and 7 appear in `barrier_audit/source_snapshot/proof_route_audited_excerpt.txt`, following a neutral definitions/provenance introduction. Those sections give the known two-minima attribution and the one-wing injection theorem/equality proof. The published excerpt SHA-256 is `94542a4bc3c378a9abb35244ae82e32c0750bdb115da6c126188e72fa5fd7694`.

`SOURCE_PROVENANCE.json` records original and publication SHA-256 values using filenames/public paths only. Local checksum manifests bind the actual portable versions. They are relative to the directory containing the manifest, never to a private workspace. The root `SHA256SUMS` binds every public file except itself.

## Permitted publication transformations

1. Absolute output paths in two source scripts become paths relative to the script's directory. Two independent comparison scripts point to the sibling `actual_fiber/` directory. No arithmetic, enumeration, derivative, inequality or test predicate is changed.
2. One saved optional grid-result output filename becomes relative. Its mathematical fields remain unchanged.
3. Source prose uses portable reproduction paths and neutral references to an independent audit. Source mathematical statements, including the full original Section 5, remain unchanged.
4. The longer partial note is replaced by the explicitly identified two-section excerpt. Other omitted examples are not reproduced. The audit's mathematical statements are retained in their stated scope, with that omitted-material mention replaced by an exclusion sentence.
5. Audit metadata clearly distinguishes original source hashes from the portable publication binding. Source manifests and the exact checker's `source_sha256` result field are rebound to the included source files; no mathematical output is altered. Public reports carry a publication note rather than silently inheriting a verdict for an unrecorded source version.

The core audit does not certify Section 5. The separate recurrence audit certifies Section 5 only, with nonempty-downset hypotheses and explicit empty-downset terminal conventions. Publication rebinding does not enlarge either verdict. The original full proof-route hash provides provenance, not an assertion that all its sections were certified.

All checker reruns take place in a separate copy so the published certificate files retain fixed bytes. `PUBLICATION_CHECKS.md` states exactly which fields are ignored for runtime-only comparisons. The precise private transformation diff was retained for publication review; it is not part of the public artifact because it contains private paths.
