from pathlib import Path
T=Path('contracts/contract.py').read_text(encoding='utf-8');P=Path('docs/index.html').read_text(encoding='utf-8')
def test_surface():
 for n in ('open_incident','verify_node','expire','get_cascade'):assert 'def '+n in T and n in P
 assert "status:'FINALIZED'" in P and 'id="faultMap"' in P and 'id="nodeProof"' in P
