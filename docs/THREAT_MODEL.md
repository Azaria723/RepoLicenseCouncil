# Threat model

| Threat | Control |
|---|---|
| Proposer supplies an arbitrary evidence URL | URLs are derived from the council-bound repository, commit and path. |
| Branch mutates after proposal | Only full 40-character commits are accepted. |
| Commit is from another repository | Commit API identity is checked under the bound repository route. |
| Manifest hides relevant repository state | The canonical Git commit tree is fetched; truncated trees fail closed. |
| Raw response differs from Git blob | Path, type, mode, size and Git blob SHA-1 are verified. |
| Submitted digest is unrelated to adjudicated bytes | SHA-256 is recomputed from the exact fetched bytes. |
| License text contains prompt injection | Evidence is labeled untrusted; output keys, enum and characteristics are allowlisted. |
| Model invents a policy characteristic | Only vocabulary stored in the council configuration is accepted. |
| AI silently approves a license | Assessment cannot update `decision`; only ballots and quorum can. |
| Outsider proposes or votes | Both operations require immutable membership. |
| Member votes twice | Ballot key is case ID plus sender address. |
| Early finalization bypasses quorum | Before deadline, finalization returns `QUORUM_PENDING` unless quorum is met. |
| Source cannot be verified | Case becomes `BLOCKED_SOURCE` and cannot receive votes. |
