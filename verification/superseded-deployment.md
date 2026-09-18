# Superseded deployment

- Address: `0x064e8396bC41E54e12E32aA9D9758453816E5C25`
- Source parity at deployment: true (`f9c6cc29f7496e0bdc1098e4f79ccc456d6089e6d77720668be4b24e8eb90f70`).
- Initial state: zero councils and zero cases.
- Council creation: `0xd59b6e41e8fe5f1ddeea1291bde93f45235684e05b786d42a3e332bcc87e0db2`.
- Case proposal: `0x7bb5da37e839bf0fc1707ca6bafc0a3832a6eb42ba51d024495ab9b2cc4de41c`.
- Assessment: `0xa6036afddfc29ca2d64b8f07e149f491deea58ca8bd3127217f2db3338eca2b7`.

The assessment finalized successfully at the VM level but returned the contract's safe `SOURCE_UNRESOLVED` outcome and set `BLOCKED_SOURCE`. Both immutable raw files were publicly reachable and matched their committed byte sizes. Diagnosis showed the combined GitHub `/commits/{sha}` response was approximately 64 KB, exceeding the deliberately bounded 18 KB response limit. No voting was opened and no governance decision was created.

The contract was corrected to use GitHub's canonical Git Data `/git/commits/{sha}` route, whose public response was approximately 1 KB and still provides the repository-scoped commit and tree identity needed by the proof. This address is superseded and must not be submitted as the final deployment.
