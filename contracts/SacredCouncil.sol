// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/governance/Governor.sol";
import "../node_modules/@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";
import "../node_modules/@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";
import "../node_modules/@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import "../node_modules/@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";

///@title Sacred Council
///@author 0xGusMcCrae
///@notice This contract is a basic governor contract made by the openzeppelin wizard
contract SacredCouncil is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction {

    constructor(IVotes _token)
        Governor("Sacred Council")
        GovernorSettings(1 /* 1 block */, 50 /* 10 minutes */, 0) //voting delay, voting period (in blocks --> ~12 seconds each), proposal threshold
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(4)
    {}

    // The following functions are overrides required by Solidity.

    function votingDelay()
        public
        view
        override(IGovernor, GovernorSettings)
        returns (uint256)
    {
        return super.votingDelay();
    }

    function votingPeriod()
        public
        view
        override(IGovernor, GovernorSettings)
        returns (uint256)
    {
        return super.votingPeriod();
    }

    function quorum(uint256 blockNumber)
        public
        view
        override(IGovernor, GovernorVotesQuorumFraction)
        returns (uint256)
    {
        return super.quorum(blockNumber);
    }

    function proposalThreshold()
        public
        view
        override(Governor, GovernorSettings)
        returns (uint256)
    {
        return super.proposalThreshold();
    }
    
}
