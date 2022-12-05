from brownie import *
from dotenv import load_dotenv
load_dotenv()

old = interface.IOldContract('0x93AA8eA0944b384c224F84E40A821418122E09E7')
new = interface.INewContract('0xa4D68274649FEA4A74dC69D1fbCd924502dEAcB6')

proxyInitCall = old.initialize.encode_input()

proxy = ProxyContract.deploy(old.address,proxyInitCall,{'from': accounts[0]},publish_source=True)

proxyOld = interface.IOldContract(proxy.address)

proxyOld.getIdentifier() #should return 'Old Contract'

proxyOld.getVersion() #should be 1, why is it 17

proxy.getImplementation() #should be old address

newProxyInitCall = new.initialize.encode_input(proxyOld.getVersion() + 1)

proxy.setNewImplementation(new.address,newProxyInitCall,{'from': accounts[0]}) 

############################################################################
################## Perform crosschain call from L1 #########################
############################################################################

#Get ticketId from ArbRetryableTx event
proxy.getL1Call(ticketId,{'from': accounts[0]})

proxyOld.getIdentifier() #should return 'New Contract'

proxyOld.getVersion() #does return 18, so it's updating but idk why it's starting at 17

