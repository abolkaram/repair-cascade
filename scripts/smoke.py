import json,time,secrets
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];E=(R.parents[3]/'accounts.env').read_text();key=next(x.split('=',1)[1].strip().strip('"').strip("'") for x in E.splitlines() if x.startswith('ACCOUNT_5_GENLAYER_PRIVATE_KEY='));owner=create_account(account_private_key=key);vs=[create_account(account_private_key='0x'+secrets.token_hex(32)) for _ in range(3)];cs=[create_client(chain=studionet,account=x) for x in [owner]+vs];a='0x2E7aE45015257396Dd097735ad8B24a711A8Ee85';i='LIVE-'+str(int(time.time()));b='4c9912f';urls=[f'https://raw.githubusercontent.com/abolkaram/repair-cascade/{b}/evidence/node-zero.txt',f'https://cdn.jsdelivr.net/gh/abolkaram/repair-cascade@{b}/evidence/node-one.txt',f'https://github.com/abolkaram/repair-cascade/raw/{b}/evidence/node-two.txt'];tx=[]
def send(cl,fn,args):
 h=cl.write_contract(address=a,function_name=fn,args=args);r=cl.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';tx.append(h)
send(cs[0],'open_incident',[i,'Release integrity incident',['Freeze writes','Repair index','Reopen reads'],[-1,0,1],[x.address for x in vs],3600]);
for n in range(3):send(cs[n+1],'verify_node',[i,n,urls[n]])
print(json.dumps({'id':i,'state':'CLOSED','transactions':tx}),flush=True)
