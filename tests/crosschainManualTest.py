from brownie import *

#mainnet eth goerli
proxyAddress = '0x3fd61c6e97f180943A0E1d0719a20a4c1010D76B'
inbox = interface.IInbox('0x6BEbC4925716945D46F0Ec336D5C2564F419682C')

#issues with copy/pasting bytecode, so going to interface on inbox to generate correct bytecode on mainnet goerli 
new = interface.INewContract(inbox.address)
newAddress = '0xa4D68274649FEA4A74dC69D1fbCd924502dEAcB6'
newProxyInitCall = new.initialize.encode_input(27)
proxy = interface.IProxyContract(inbox.address)
proxyOld = interface.IOldContract(inbox.address)
payload = proxy.setNewImplementation.encode_input(newAddress,newProxyInitCall)
fee = inbox.calculateRetryableSubmissionFee(200,0) 

tx = inbox.createRetryableTicket(proxyAddress,0,1000000,accounts[0].address,accounts[0].address,10000000,fee*3,payload,{'from': accounts[0], 'value':accounts[0].balance()/4})


##### The below should be done via arbitrum goerli websocket ####
# gonna need to set an event filter up with this format:
# self.borrowFilter = web3.eth.contract(address=self.pool.address,abi=self.pool.abi).events.Borrow.createFilter(fromBlock='latest')
# but gotta figure out the abi to use
arbRetryableTx = interface.ArbRetryableTx('0x000000000000000000000000000000000000006E')
ticketCreatedFilter = web3.eth.contract(address=arbRetryableTx.address, abi=arbRetryableTx.abi).events.TicketCreated.createFilter(fromBlock='latest')
ticketCreatedFilter.get_new_entries()

#event listener loop
import time
events = []
while(True):
    time.sleep(5)
    print('werkin on it')
    try: 
        result = ticketCreatedFilter.get_new_entries()
        print(result)
    except:
        ticketCreatedFilter = web3.eth.contract(address=arbRetryableTx.address, abi=arbRetryableTx.abi).events.TicketCreated.createFilter(fromBlock='latest')
        result =ticketCreatedFilter.get_new_entries()
        print(result)
    if result:
        events.append(result)
        print('we got one!')

ticketId = events[0][0]['args']['ticketId']

#then call redeem on arbRetryableTx and it DOES work with the function call as is above.