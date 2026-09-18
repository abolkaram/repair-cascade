from conftest import CONTRACT
def setup(vm,dep,ac):vm.warp('2035-01-01T00:00:00+00:00');vm.sender=ac[0];x=dep(CONTRACT);x.open_incident('i-1','Release integrity incident',['Freeze writes','Repair index','Reopen reads'],[-1,0,1],['0x'+a.hex() for a in ac[1:4]],3600);return x
def mock(vm,h):vm.mock_web(h,{'status':200,'body':'Node complete and safe.'});vm.mock_llm(r'.*RepairCascade node check.*','{"complete":true,"safe":true}')
def test_ordered_dag_closes(direct_vm,direct_deploy,direct_accounts):
 x=setup(direct_vm,direct_deploy,direct_accounts)
 for i in range(3):direct_vm.sender=direct_accounts[i+1];mock(direct_vm,rf'n{i}\.example');x.verify_node('i-1',i,f'https://n{i}.example/proof')
 assert x.get_cascade('i-1')['state']=='CLOSED'
def test_locked_child_rejected(direct_vm,direct_deploy,direct_accounts):
 x=setup(direct_vm,direct_deploy,direct_accounts);direct_vm.sender=direct_accounts[2];mock(direct_vm,r'n1\.example')
 with direct_vm.expect_revert('unlocked node'):x.verify_node('i-1',1,'https://n1.example/proof')
