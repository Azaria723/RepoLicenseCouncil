# StudioNet verification

Verified on GenLayer StudioNet (chain ID `61999`) against contract
[`0xfEa116bEa66ba7FF6F7Cc4573c949a22f2Fc1665`](https://explorer-studio.genlayer.com/address/0xfEa116bEa66ba7FF6F7Cc4573c949a22f2Fc1665).

## Source parity

- Deployment source SHA-256: `2f69ef79e77fd4b0d8bd84cec1d96954fd0084559d562014b8d583cc46f3240d`
- Repository source SHA-256: `2f69ef79e77fd4b0d8bd84cec1d96954fd0084559d562014b8d583cc46f3240d`
- Result: exact match.

## Immutable public inputs

- Repository: `Azaria723/RepoLicenseCouncil`
- Path: `/evidence/demo-project/LICENSE`
- Baseline commit: `c878c76bc61df05994fae03ed7179a0e71d95c32`
- Baseline bytes SHA-256: `4082305f60ac8e8128aad196c4150c2a3967e94ec736d80fe65b583d380d94e8`
- Candidate commit: `6b66919f42b94c71728232162ff7877ddc9db795`
- Candidate bytes SHA-256: `ed1cfd34802baa7159d8af86f169e2ba907192a4e3fafe52b6abf1818c7a9888`

The contract derives every GitHub URL. Validators verify the requested full commit SHA through Git Data, walk the complete tree, require a regular blob at the council-bound path, verify Git blob identity and size, then recompute SHA-256 from the fetched bytes before semantic comparison.

## Lifecycle transactions

| Operation | Transaction | Verified effect |
|---|---|---|
| Create council | [`0xd6ba…8983`](https://explorer-studio.genlayer.com/tx/0xd6ba0e0e2a16d536f27581ef64237307c400536162795fcb0f33b55af8b38983) | Council 0, two members, quorum 2 |
| Propose change | [`0xcfaa…55c`](https://explorer-studio.genlayer.com/tx/0xcfaabc6b8bcdb44827eef71a800cb00885ddd03781a3c8d8cf1159815b4c455c) | Case 0 created from two immutable revisions |
| Assess change | [`0xebcb…48c1`](https://explorer-studio.genlayer.com/tx/0xebcb4469028a59d98378ea3d436a72ad85be7cb4ab23a2b2f7df39cf3d1548c1) | Provenance true; `MORE_RESTRICTIVE`; characteristic `network-copyleft` |
| First ballot | [`0x0e62…aad4`](https://explorer-studio.genlayer.com/tx/0x0e624d5f3436efd8fcbb00cf3b6b52450465914d523ec3c0fce2db8872beaad4) | `ACCEPT`; total becomes 1 |
| Duplicate ballot attempt | [`0x5ac4…d34b`](https://explorer-studio.genlayer.com/tx/0x5ac49bb60b7b77631fe6746e3318141a6f25f2bbc13ec11e57255877da3ed34b) | Protected state unchanged |
| Premature finalize attempt | [`0xdb1f…94b9`](https://explorer-studio.genlayer.com/tx/0xdb1fda100168e3a573ee8d019f9f73fb19c542973fb20e23ca908eb60a8994b9) | Decision remains `PENDING` below quorum |
| Second ballot | [`0x050a…6b04`](https://explorer-studio.genlayer.com/tx/0x050a1f25910d4ad4c722c7ba9475518cb11c368a25d6bc4a509381bdec286b04) | `REJECT`; total becomes 2 |
| Finalize | [`0xece1…f9a2`](https://explorer-studio.genlayer.com/tx/0xece1ec993a3acbde86b01d5a165c47544d652214be51b7945b19b891f364f9a2) | Tie deterministically resolves to `REJECTED` |

## Final authoritative readback

```json
{
  "assessment": "MORE_RESTRICTIVE",
  "diagnostics": {
    "provenance_ok": true,
    "classification": "MORE_RESTRICTIVE",
    "characteristics": ["network-copyleft"]
  },
  "accept_votes": 1,
  "reject_votes": 1,
  "total_votes": 2,
  "decision": "REJECTED",
  "ballots": ["ACCEPT", "REJECT"]
}
```

This result demonstrates the protocol boundary: validator consensus records a bounded fact about the verified texts; it cannot approve the proposal. The council's authenticated ballots and deterministic quorum rules alone produce the final decision.

## Additional negative-path coverage

Direct Mode tests also cover non-member proposal and voting attempts, invalid repository/path/commit/digest inputs, same-revision proposals, fetch and provenance failures, malformed model output, replay protection, all decision branches, and protected-state preservation. Run `python -m pytest -q` to reproduce all 12 tests.
