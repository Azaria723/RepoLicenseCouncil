from pathlib import Path
S=Path("contracts/RepoLicenseCouncil.py").read_text()
def test_genlayer_semantics_and_provenance():
    for x in ["gl.eq_principle.strict_eq(evaluate)","gl.nondet.web.get","gl.nondet.exec_prompt","/git/commits/","/git/trees/","_blob_sha1"]:assert x in S
def test_governance_is_separate_from_assessment():
    for x in ["def assess_change","def vote","def finalize_case","QUORUM_PENDING"]:assert x in S
def test_not_prior_architecture():
    for x in ["consume_authorization","append_snapshot","register_service","escrow"]:assert x not in S
