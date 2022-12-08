// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/proxy/utils/Initializable.sol";

///@title Proxy Contract
///@author 0xGusMcCrae
///@notice This contract exists to show that it is not 'New Contract'
contract OldContract is Initializable {

    ///@notice Will contain 'Old Contract' after initialized by proxy
    string private IDENTIFIER;

    constructor() public {
        _disableInitializers(); //disables initalize function in the context of the implementation contract's state
    }

    ///@notice Initializes state when called by proxy
    function initialize() public initializer  {
        IDENTIFIER = 'Old Contract';
    }

    ///@notice Getter function for IDENTIFIER
    ////@return Identifier - 'Old Contract'
    function getIdentifier() public view returns (string memory) {
        return IDENTIFIER;
    }

    ///@notice Getter function for intialization version
    ///@return Version - will be 1 when called by proxy or 255 when called directly
    function getVersion() external view returns (uint8) {
        return _getInitializedVersion();
    }

}