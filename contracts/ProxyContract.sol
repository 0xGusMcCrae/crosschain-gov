// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import "../node_modules/@openzeppelin/contracts/crosschain/arbitrum/CrossChainEnabledArbitrumL2.sol";
import "../node_modules/@openzeppelin/contracts/access/Ownable.sol";
import "./interfaces/ArbRetryableTx.sol";

contract ProxyContract is ERC1967Proxy, CrossChainEnabledArbitrumL2, Ownable {

    constructor(
        address implementation, 
        bytes memory initializerCall
        ) ERC1967Proxy(implementation, initializerCall) {}

    function setNewImplementation(
        address newImplementation, 
        bytes memory initializerCall
        ) public /*onlyCrossChainSender(address(100))*/ { //arbsys address
        _upgradeToAndCall(newImplementation, initializerCall, false);
    }

    function getL1Call(uint256 _ticketId) public onlyOwner {
        //arbchainId = arb goerli? which is 421613. Or mainnet?
        //_ticketId will come from the inbox contract on L1
        bytes32 ticketId = bytes32(abi.encodePacked(abi.encodePacked(uint(421613), _ticketId), uint(0) ));
        ArbRetryableTx(address(110)).redeem(ticketId);
    }

    function getImplmentation() external view returns (address) {
        _implementation();
    }

}
