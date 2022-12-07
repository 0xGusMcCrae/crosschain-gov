from brownie import *

govToken = GovToken.at('0x2b06e3E7a863d2B5ED0dD4cFE89768ad74b2c062')

governor = SacredCouncil.at('0x3B3263618aD58Ee805A917798c5E5C00e7cEf621')

#delegate my tokens via the ERC20 contract (only once)
govToken.delegate(accounts[0].address,{'from': accounts[0]})
#then Propose() on the governor
proposal = governor.propose(
    #address[] targets
    #uint256[] values (msg.values of calls)
    #bytes[] calldatas (b'' for empty)
    #string description
    {'from': accounts[0]} #you DONT need to include msg.value here - that's handled during execute()
)
#then castVote() on the governor
#proposal id can be gotten from an emitted event from proposal submission (first item on etherscan, convert to decimal) or proposal.events
#be sure to save the Tx to a variable so I can check events
proposalId = proposal.events['ProposalCreated'][0][0]['proposalId']

vote = governor.castVote(
    proposalId,   #proposal Id
    1,           #vote - 1 = FOR, 2 = ABSTAIN, 0 for AGAINST
    {'from': accounts[0]}
) 
#once it passes, execute()
description = proposal.events['ProposalCreated'][0][0]['description']
descriptionHash = web3.keccak(text=description)

execution = governor.execute(
    #address[] targets
    #uint256[] values (msg.values of calls)
    #bytes[] calldatas (b'' for empty)
    #bytes32 descriptionHash --> use web3.keccak(text=description)
    {'from': accounts[0], 'value': 0}
)

#and if you have a timelock, you need to wait for the queue period to execute
