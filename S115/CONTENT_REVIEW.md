# S115 content, provenance and scope review

Date: 2026-10-10. This is a local-only, bounded incremental research package. No GitHub, Notion, Library or other remote write was performed for this package.

## Mathematical scope

The two new independently reviewed results concern only the seven-point quotient with covers `0<3; 1<2,4; 2<3,6; 3<5; 4<5`, inflated by chains of weights `(u,a,b,1,t,1,v)`. All variable weights are positive integers. The v>=5 rank obstruction and the v=4 three-probability certificate jointly exclude v>=4, without bounds on u,a,b,t. Finite computations support the implementations; the unbounded conclusions are the proved analytic statements.

The prior v>=t+1 exclusion and the structural v=1 contradiction give the contextual remaining range v in {2,3}, v<=t. Neither v=2 nor v=3 is settled by this package. Its boundary describes only the included frozen proofs, not the status of later research. Their later exploration, general seven-weight claims, a solution of MAIN33, and claims of universally balanced fixed named pairs are excluded.

## Frozen review targets

- `residual-rank-independent-audit/MANIFEST.json` records PASS and binds every original file of `residual-rank-obstruction/` by SHA-256. Its `frozen/` files must also be byte-identical to those originals. Its independent theorem audit is `AUDIT.md`.
- `four-tail-independent-audit/SOURCE_INTEGRITY.json` records PASS and binds all six original files of `four-tail-rank-certificate/`. Its `source_snapshot/` files must also be byte-identical. The theorem audit is `PROOF_REVIEW.md`, which states PASS without mathematical correction.
- `AUDIT_BINDINGS.json` is executable provenance: the driver reads the actual preserved audit JSON, compares each cited source hash with current package bytes, verifies the nested audit manifests, and verifies all explicit source-copy equalities. It does not merely trust an earlier boolean receipt.
- All original documents, source code, output JSON, audit evidence and logs are copied unchanged. Historical status and scope language is retained. The Chinese guide resolves temporal differences without altering any frozen document.

## Minimal previous proof dependencies

Both new theorems externally depend only on Zaguia, arXiv:1610.00809, Definition 1 and Theorem 2, as checked by the independent reviewers. The two S112 reference documents preserve the prior structural-good-pair discussion and audit; the new claims use those structural sections, without adopting unrelated minimality hypotheses.

The two singleton-upper-spine documents already present under `residual-rank-independent-audit/dependencies/` preserve the earlier v>=t+1 theorem and its independent audit. They support only the contextual residual range. The frozen historical S114 SHA256SUMS binds those two documents and both S112 structural documents to their exact earlier package bytes. The S114 package itself is not re-created or fully re-executed here.

## Replay and integrity rules

The driver is standard-library-only and uses explicit exceptions rather than assertions; its checks remain active under Python optimization. Every computation is run from an independent disposable package copy, with its declared outputs removed first. Both author verifiers and both independent verifiers run normally and with -O. Summary and vector JSON are compared byte-for-byte. No JSON fields are ignored; wall-clock timings appear only in external replay receipts.

Package file inventory, per-file SHA-256, provenance classification, nested source/audit manifests, audit source hashes and prior-dependency hashes are checked before and after replay. The portability guard rejects accidental reads of original source directories; it is not a security sandbox. Receipts and execution logs produced by the top-level driver remain outside the immutable payload.

## Content and distribution boundary

The allowlist consists of the two author directories, their two complete frozen independent audit directories, three minimal prior-reference files, and package-authored guides/integrity/replay files. It excludes raw chats, internal notes, credentials, caches, compiled binaries, archives, third-party packages, unrelated research, and subsequent v=2/v=3 exploration. Original absolute source paths occurring in frozen audit metadata are historical provenance only. Reproduction requires no original workspace, network or installed third-party package.

Independent review here means separately conducted proof review and computation within this research workflow, not external peer review or a claim of literature novelty. The local inventory and ZIP are preparation artifacts, not evidence of remote publication or authority to publish.
