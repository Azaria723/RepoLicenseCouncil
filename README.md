# RepoLicenseCouncil

RepoLicenseCouncil is a GenLayer dApp for evidence-grounded repository license governance. Validators establish what changed between two immutable `LICENSE` revisions; council members—not the model—decide whether the project accepts that change.

## Protocol boundary

GitHub is authoritative only for repository identity and exact bytes at an immutable commit. Validator consensus classifies a bounded semantic relationship between verified license texts. It does not give legal advice and cannot approve a change. A final `APPROVED`, `REJECTED`, or `NO_QUORUM` decision is produced exclusively by council votes and deterministic quorum rules.

The files under `evidence/demo-project/` are synthetic public fixtures. They do not claim that any external project changed its license.

## Lifecycle

1. Create a council bound to one repository, one LICENSE path, a finite member set, quorum and bounded policy vocabulary.
2. A member proposes two distinct full Git commit SHAs and exact fetched-byte SHA-256 commitments.
3. Validators derive GitHub URLs, verify commit identity, complete trees, blob path/type/mode/size/Git SHA-1, raw bytes and SHA-256.
4. Consensus records one bounded assessment: `NO_MATERIAL_CHANGE`, `MORE_PERMISSIVE`, `MORE_RESTRICTIVE`, `OBLIGATION_CHANGED`, `AMBIGUOUS`, or `SOURCE_UNRESOLVED`.
5. Members cast one `ACCEPT`, `REJECT`, or `ABSTAIN` ballot each.
6. Deterministic quorum and vote counts create the final decision.

## Local verification

```bash
python -m pip install -r requirements.txt
python -m pytest -q
cd frontend
npm ci
npm run build
```

The deployer receives no implicit governance role. Membership exists only in council configuration. See [architecture](docs/ARCHITECTURE.md), [threat model](docs/THREAT_MODEL.md), and [deployment guide](docs/DEPLOYMENT.md).

## Verified deployment

- StudioNet contract: `0xfEa116bEa66ba7FF6F7Cc4573c949a22f2Fc1665`
- Chain ID: `61999`
- Deployed/local source SHA-256: `2f69ef79e77fd4b0d8bd84cec1d96954fd0084559d562014b8d583cc46f3240d`
- Live result: immutable GitHub provenance verified, semantic assessment recorded, duplicate ballot and premature finalization rejected, quorum finalized deterministically.

See [StudioNet verification](verification/studionet-verification.md) for the reproducible inputs, transaction hashes, and final readback.
