// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/proxy/utils/Initializable.sol";

contract OldContract is Initializable {

    string private IDENTIFIER;

    constructor() public {
        _disableInitializers(); //disables initalize function in the context of the implementation contract's state
    }

    function initialize() public initializer  {
        IDENTIFIER = 'Old Contract';
    }

    function getIdentifier() public view returns (string memory) {
        return IDENTIFIER;
    }

    function getVersion() external view returns (uint8) {
        return _getInitializedVersion();
    }

    // function isInitializing() external view returns (bool) {
    //     return _isInitializing();
    // }
}