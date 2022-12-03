// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import '@openzeppelin/contracts/crosschain/arbitrum/CrossChainEnabledArbitrumL1.sol';

contract ProxyContract is ERC1967Proxy, CrossChainEnabledArbitrumL1 {

    constructor(
        address implementation, 
        bytes memory initializerCall
        ) ERC1967Proxy(
            implementation, 
            initializerCall
            ) CrossChainEnabledArbitrumL1(0xaf4159A80B6Cc41ED517DB1c453d1Ef5C2e4dB72){}

    function setNewImplementation(
        address newImplementation, 
        bytes memory initializerCall
        ) public onlyCrossChainSender(/*address*/) { //need to figure out what address this is supposed to be
        _upgradeToAndCall(newImplementation, initializerCall, false);
    }
}
