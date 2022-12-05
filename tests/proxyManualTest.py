from brownie import *

old = interface.IOldContract('0xee9e10004F2E3576D799F77C8c2bbAfAAfCC5478')
new = interface.INewContract('0x1Cd96dD820Aa2b618122BDCcF6C65557a29b9801')

proxyInitCall = old.initialize.encode_input()

proxy = ProxyContract.deploy(old.address,proxyInitCall,{'from': accounts[0]})

proxyOld = interface.IOldContract(proxy.address)

proxyOld.getIdentifier() #should return 'Old Contract'

newProxyInitCall = new.initialize.encode_input(205)

proxy.setNewImplementation(new.address,newProxyInitCall,{'from': accounts[0]}) 