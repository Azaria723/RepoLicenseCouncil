# Architecture

```text
Council configuration
        ↓
Immutable Git comparison case
        ↓
Commit/tree/blob/raw verification
        ↓
Bounded semantic fact package
        ↓
Independent member ballots
        ↓
Deterministic quorum decision
```

The semantic assessment and governance decision are separate state transitions. `assess_change` cannot approve or reject a case. It only freezes provenance status, classification and policy-vocabulary characteristics. `vote` accepts ballots only from the immutable member set. `finalize_case` uses only quorum and stored vote counts.

This is not an evidence registry, monitoring journal, escrow or one-shot authorization protocol. Its persistent object is a council case whose fact-finding phase precedes multi-party governance.
