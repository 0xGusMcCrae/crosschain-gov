// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import "./interfaces/ArbRetryableTx.sol";

contract ProxyContract is ERC1967Proxy {

    constructor(
        address implementation, 
        bytes memory initializerCall
        ) ERC1967Proxy(implementation, initializerCall) {}

    function setNewImplementation(
        address newImplementation, 
        bytes memory initializerCall
        ) public {
        _upgradeToAndCall(newImplementation, initializerCall, false);
    }

    function getL1Call(bytes32 _ticketId) public {
        //_ticketId will come from event emitted by ArbRetryableTx on L2
        ArbRetryableTx(address(110)).redeem(_ticketId);
    }

    function getImplementation() external view returns (address) {
        return ERC1967Proxy._implementation();
    }

}
