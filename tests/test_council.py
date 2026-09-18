import hashlib,json,time
import pytest

pytestmark=pytest.mark.filterwarnings("ignore:Web mock never matched")
OWNER="Azaria723";REPO="RepoLicenseCouncil";PATH="/evidence/demo-project/LICENSE"
OLD=b"MIT License\nPermission is hereby granted, free of charge, to any person obtaining a copy.\n"
NEW=b"GNU AFFERO GENERAL PUBLIC LICENSE Version 3\nNetwork interaction requires corresponding source availability.\n"
C1="1"*40;C2="2"*40
POLICY={"allowed":["permissive"],"requires_vote":["copyleft"],"prohibited_characteristics":["network-copyleft"]}
def sha(x):return hashlib.sha256(x).hexdigest()
def blob(x):return hashlib.sha1((f"blob {len(x)}\0").encode()+x).hexdigest()
def addr(x):return "0x"+x.hex()
def deploy(vm,direct_deploy,actor):
    vm.strict_mocks=True;vm.check_pickling=True
    with vm.prank(actor):return direct_deploy("contracts/RepoLicenseCouncil.py")
def create(vm,c,creator,a,b):
    with vm.prank(creator):return c.create_council(OWNER,REPO,PATH,json.dumps([addr(a),addr(b)]),2,json.dumps(POLICY))
def propose(vm,c,actor):
    with vm.prank(actor):return c.propose_change(0,C1,sha(OLD),C2,sha(NEW),int(time.time())+3600)
def mock(vm,items,bad_blob=False,truncated=False):
    api=f"https://api.github.com/repos/{OWNER}/{REPO}";raw="https://raw.githubusercontent.com/"
    for i,(commit,body) in enumerate(items):
        tree=str(i+4)*40
        vm.mock_web((api+"/commits/"+commit).replace(".",r"\.")+"$",{"status":200,"body":json.dumps({"sha":commit,"commit":{"tree":{"sha":tree}}}).encode()})
        entry={"path":PATH[1:],"mode":"100644","type":"blob","size":len(body),"sha":"0"*40 if bad_blob else blob(body)}
        vm.mock_web((api+"/git/trees/"+tree+r"\?recursive=1$").replace(".",r"\."),{"status":200,"body":json.dumps({"truncated":truncated,"tree":[entry]}).encode()})
        vm.mock_web((raw+OWNER+"/"+REPO+"/"+commit+PATH).replace(".",r"\.")+"$",{"status":200,"body":body})
def case(c):return json.loads(c.get_case(0))

def test_full_assess_vote_finalize(direct_vm,direct_deploy,direct_alice,direct_bob):
    c=deploy(direct_vm,direct_deploy,direct_alice);assert create(direct_vm,c,direct_alice,direct_alice,direct_bob)==0;assert propose(direct_vm,c,direct_alice)==0;mock(direct_vm,[(C1,OLD),(C2,NEW)])
    direct_vm.mock_llm(r"Compare two repository license.*",json.dumps({"classification":"MORE_RESTRICTIVE","characteristics":["copyleft","network-copyleft"]}))
    assert c.assess_change(0)=="MORE_RESTRICTIVE" and case(c)["decision"]=="PENDING"
    with direct_vm.prank(direct_alice):assert c.vote(0,"ACCEPT")=="VOTE_RECORDED"
    with direct_vm.prank(direct_bob):assert c.vote(0,"REJECT")=="VOTE_RECORDED"
    assert c.finalize_case(0)=="REJECTED" and case(c)["decision"]=="REJECTED"

def test_ai_does_not_decide_governance(direct_vm,direct_deploy,direct_alice,direct_bob):
    c=deploy(direct_vm,direct_deploy,direct_alice);create(direct_vm,c,direct_alice,direct_alice,direct_bob);propose(direct_vm,c,direct_alice);mock(direct_vm,[(C1,OLD),(C2,NEW)])
    direct_vm.mock_llm(r"Compare two repository license.*",json.dumps({"classification":"MORE_RESTRICTIVE","characteristics":["network-copyleft"]}))
    assert c.assess_change(0)=="MORE_RESTRICTIVE" and case(c)["decision"]=="PENDING"

@pytest.mark.parametrize("output",[
 {"classification":"ALLOW","characteristics":[]},
 {"classification":"MORE_RESTRICTIVE","characteristics":["invented"]},
 {"classification":"MORE_RESTRICTIVE","characteristics":[],"reason":"extra"},
])
def test_malformed_semantics_become_ambiguous(direct_vm,direct_deploy,direct_alice,direct_bob,output):
    c=deploy(direct_vm,direct_deploy,direct_alice);create(direct_vm,c,direct_alice,direct_alice,direct_bob);propose(direct_vm,c,direct_alice);mock(direct_vm,[(C1,OLD),(C2,NEW)]);direct_vm.mock_llm(r"Compare two repository license.*",json.dumps(output))
    assert c.assess_change(0)=="AMBIGUOUS" and case(c)["decision"]=="PENDING"

def test_provenance_failure_blocks_voting(direct_vm,direct_deploy,direct_alice,direct_bob):
    c=deploy(direct_vm,direct_deploy,direct_alice);create(direct_vm,c,direct_alice,direct_alice,direct_bob);propose(direct_vm,c,direct_alice);mock(direct_vm,[(C1,OLD),(C2,NEW)],bad_blob=True)
    assert c.assess_change(0)=="SOURCE_UNRESOLVED" and case(c)["decision"]=="BLOCKED_SOURCE"
    with direct_vm.prank(direct_alice):assert c.vote(0,"ACCEPT")=="CASE_NOT_OPEN"

def test_truncated_tree_blocks(direct_vm,direct_deploy,direct_alice,direct_bob):
    c=deploy(direct_vm,direct_deploy,direct_alice);create(direct_vm,c,direct_alice,direct_alice,direct_bob);propose(direct_vm,c,direct_alice);mock(direct_vm,[(C1,OLD),(C2,NEW)],truncated=True)
    assert c.assess_change(0)=="SOURCE_UNRESOLVED"

def test_roles_double_vote_and_quorum(direct_vm,direct_deploy,direct_alice,direct_bob,direct_charlie):
    c=deploy(direct_vm,direct_deploy,direct_alice);create(direct_vm,c,direct_alice,direct_alice,direct_bob)
    with direct_vm.prank(direct_charlie):assert c.propose_change(0,C1,sha(OLD),C2,sha(NEW),int(time.time())+3600)=="MEMBER_ONLY"
    propose(direct_vm,c,direct_alice);mock(direct_vm,[(C1,OLD),(C2,NEW)]);direct_vm.mock_llm(r"Compare two repository license.*",json.dumps({"classification":"OBLIGATION_CHANGED","characteristics":["copyleft"]}));c.assess_change(0)
    with direct_vm.prank(direct_charlie):assert c.vote(0,"ACCEPT")=="MEMBER_ONLY"
    with direct_vm.prank(direct_alice):assert c.vote(0,"ACCEPT")=="VOTE_RECORDED";assert c.vote(0,"ACCEPT")=="ALREADY_VOTED"
    assert c.finalize_case(0)=="QUORUM_PENDING"
    with direct_vm.prank(direct_bob):assert c.vote(0,"ACCEPT")=="VOTE_RECORDED"
    assert c.finalize_case(0)=="APPROVED"

def test_invalid_config_preserves_counts(direct_vm,direct_deploy,direct_alice,direct_bob):
    c=deploy(direct_vm,direct_deploy,direct_alice)
    with direct_vm.prank(direct_alice):
        assert c.create_council(OWNER,REPO,"/../LICENSE",json.dumps([addr(direct_alice),addr(direct_bob)]),2,json.dumps(POLICY))=="INVALID_REPOSITORY"
        assert c.create_council(OWNER,REPO,PATH,json.dumps([addr(direct_alice)]),2,json.dumps(POLICY))=="INVALID_MEMBERS"
    assert json.loads(c.get_counts())=={"case_count":0,"council_count":0}
