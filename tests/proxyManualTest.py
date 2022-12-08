from brownie import *
from dotenv import load_dotenv
load_dotenv()

old = interface.IOldContract('0x93AA8eA0944b384c224F84E40A821418122E09E7')
new = interface.INewContract('0xa4D68274649FEA4A74dC69D1fbCd924502dEAcB6')

#deploy proxy
proxyInitCall = old.initialize.encode_input()
proxy = ProxyContract.deploy(old.address,proxyInitCall,{'from': accounts[0]},publish_source=True)

#show that old contract has been set as implementation
proxyOld = interface.IOldContract(proxy.address)
proxyOld.getIdentifier() #should return 'Old Contract'
proxyOld.getVersion() #should return 1
proxy.getImplementation() #should return old address

#upgrade implementation to new contract
newProxyInitCall = new.initialize.encode_input(proxyOld.getVersion() + 1)
proxy.setNewImplementation(new.address,newProxyInitCall,{'from': accounts[0]}) 

#show that implementation has been upgraded to new contract
proxyOld.getIdentifier() #should return 'New Contract'
proxyOld.getVersion() #should return 2
proxy.getImplementation() #should return new address
