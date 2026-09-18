# Deployment checklist

1. Run Direct Mode tests and production frontend build.
2. Push the repository with the baseline synthetic LICENSE fixture.
3. Record its full commit and SHA-256 of exact Git blob bytes.
4. Replace the same file with the synthetic network-copyleft fixture and push a second commit.
5. Deploy the exact contract to Studionet without constructor arguments.
6. Verify deployed/local source parity and zero initial counters before any write.
7. Create a council whose members are dedicated test accounts; the deployer need not be a member.
8. Propose the immutable commit pair, assess it and require authoritative readback before voting.
9. Exercise two distinct member votes, quorum finalization, outsider voting, double voting, source failure and premature finalization.
10. For every live write retain transaction finality, GenVM result, contract-level result and complete post-state readback.

Do not publish private keys or describe account orchestration in public evidence. Do not represent the synthetic fixture as an external real-world license event.
