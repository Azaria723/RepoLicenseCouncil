# Local verification

- Direct Mode: `12 passed`.
- Production frontend build: passed.
- Contract SHA-256: `2f69ef79e77fd4b0d8bd84cec1d96954fd0084559d562014b8d583cc46f3240d`.
- Strict web mocks and serialization checks are enabled.
- Coverage includes provenance success/failure, malformed semantic results, member-only proposal/vote, duplicate ballot, quorum pending, approval, rejection and protected-state preservation.
- Static checks ensure semantic assessment and council decision remain separate and previous registry/authorization/journal architecture is absent.

The first Studionet candidate used GitHub's larger combined `/commits/{sha}` response and correctly failed its 18 KB fetch bound with `SOURCE_UNRESOLVED`. The source now uses the canonical Git Data `/git/commits/{sha}` endpoint (observed public payload approximately 1 KB) while preserving commit-to-tree identity verification. A fresh deployment is required for live lifecycle evidence.
