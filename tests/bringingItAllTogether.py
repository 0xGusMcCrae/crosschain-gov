from brownie import *
from dotenv import load_dotenv
load_dotenv()

#this is a collection of commands for manual testing via brownie 
#console - the full script is not meant to be executed!

####################################################################
############################## On L2 ###############################
####################################################################

#load account - replace with your own
accounts.load('fcc-test')

#deploy proxy implementation contracts
old = OldContract.deploy({'from': accounts[0]}, publish_source=True)
new = NewContract.deploy({'from': accounts[0]}, publish_source=True)

#deploy proxy
proxyInitCall = old.initialize.encode_input()
proxy = ProxyContract.deploy(old.address,proxyInitCall,{'from': accounts[0]}, publish_source=True)

#check proxy initialization version - should be 1
proxyImplementation = interface.IOldContract(proxy.address)
proxyImplementation.getVersion()
#check proxy identifier - should be 'Old Contract'
proxyImplementation.getIdentifier()
#check implementation address - shoould be the same as old.address
proxy.getImplementation()

####################################################################
############################## On L1 ###############################
####################################################################
from dotenv import load_dotenv
load_dotenv()

#load account - replace with your own
accounts.load('fcc-test')

#Deploy governance token and Governor
govToken = GovToken.deploy(10000*10**18,{'from': accounts[0]},publish_source=True)
governor = SacredCouncil.deploy(govToken.address, {'from': accounts[0]}, publish_source=True)

#delegate token votes to yourself
govToken.delegate(accounts[0].address,{'from': accounts[0]})

#generate proxy upgrade call payload - using interfaces on inbox.address as a placeholder - not making actual function calls so it doesn't really matter
inbox = interface.IInbox('0x6BEbC4925716945D46F0Ec336D5C2564F419682C')
proxyAddress = '0xDa9990359FC9Bf4e8539e47DD8e9Fe00c5f25aFa' #insert your deployed proxy address here
new = interface.INewContract(inbox.address)
newAddress = '0x1eaF21433bd28daD5C014fA505c1BE2C8156F34A' #use your deployed New Contract address here
newProxyInitCall = new.initialize.encode_input(2)
proxy = interface.IProxyContract(inbox.address)
payload = proxy.setNewImplementation.encode_input(newAddress,newProxyInitCall)
#The fee and value below are overestimations for ease of testing
fee = inbox.calculateRetryableSubmissionFee(175,0) 
value = accounts[0].balance()/4


#propose a crosschain call to upgrade the proxy
target = inbox.address
#gas/value parameters below are imprecise for ease of testing
calldata = inbox.createRetryableTicket.encode_input(proxyAddress,0,1000000,accounts[0].address,accounts[0].address,1000000,fee*2,payload)
description = 'I am manually testing'
proposal = governor.propose([target], [value], [calldata], description, {'from': accounts[0]})

#Cast vote FOR the above proposal - can be done via Tally or onchain as below
proposalId = proposal.events['ProposalCreated'][0][0]['proposalId']
vote = governor.castVote(proposalId, 1, {'from': accounts[0]})

#wait for vote period to run out - should be ~10 min total

#execute passed proposal
descriptionHash = web3.keccak(text=description)
execution = governor.execute([target],[value],[calldata],descriptionHash,{'from': accounts[0],'value': value})
####################################################################
######################### On L2 Websocket ##########################
####################################################################
from dotenv import load_dotenv
load_dotenv()

#load account - replace with your own
accounts.load('fcc-test')

#Set event listener to listen for ticketId to manually redeem if tx isn't executed automatically
arbRetryableTx = interface.ArbRetryableTx('0x000000000000000000000000000000000000006E')
ticketCreatedFilter = web3.eth.contract(address=arbRetryableTx.address, abi=arbRetryableTx.abi).events.TicketCreated.createFilter(fromBlock='latest')
ticketCreatedFilter.get_new_entries()

#event listener loop
import time
events = []
while(True):
    time.sleep(5)
    try: 
        result = ticketCreatedFilter.get_new_entries()
    except:
        ticketCreatedFilter = web3.eth.contract(address=arbRetryableTx.address, abi=arbRetryableTx.abi).events.TicketCreated.createFilter(fromBlock='latest')
        result =ticketCreatedFilter.get_new_entries()
    if result:
        events.append(result)
        print('we got one!')

ticketId = events[0][0]['args']['ticketId']

#call redeem
arbRetryableTx.redeem(ticketId, {'from': accounts[0]})

#check proxy initialization version - should now be 2
proxyImplementation = interface.IOldContract(proxy.address)
proxyImplementation.getVersion()
#check proxy identifier - should now be 'New Contract'
proxyImplementation.getIdentifier()
#check implementation address - should now be the same as new.address
proxy.getImplementation()

