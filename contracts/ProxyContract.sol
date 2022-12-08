// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import "./interfaces/ArbRetryableTx.sol";

///@title Proxy Contract
///@author 0xGusMcCrae
///@notice Do not use in pruduction!
contract ProxyContract is ERC1967Proxy {

    constructor(
        address implementation, 
        bytes memory initializerCall
        ) ERC1967Proxy(implementation, initializerCall) {}

    ///@notice update pointer to new implementation contract
    ///@param newImplementation address of new implementation contract
    ///@param initializerCall payload containing initializer function call
    function setNewImplementation(
        address newImplementation, 
        bytes memory initializerCall
        ) public {
        _upgradeToAndCall(newImplementation, initializerCall, false);
    }

    ///@notice Retrieve L1 message from ArbRetryableTx
    ///@dev can also be called directly on ArbRetryableTx from any account 
    ///@param _ticketId ticketId for the call being retrieved
    function getL1Call(bytes32 _ticketId) public {
        //_ticketId will come from event emitted by ArbRetryableTx on L2
        ArbRetryableTx(address(110)).redeem(_ticketId);
    }

    ///@notice get implementation contract address
    ///@return address of implementaiton contract
    function getImplementation() external view returns (address) {
        return ERC1967Proxy._implementation();
    }

}
