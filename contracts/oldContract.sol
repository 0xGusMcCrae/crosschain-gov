// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "@openzeppelin/contracts/proxy/utils/Initializable.sol";

contract OldContract is Initializable {

    string private immutable IDENTIFIER;

    function initialize() initializer public {
        IDENTIFIER = 'Old Contract';
    }

    function getIdentifier() public pure returns (string memory) {
        return IDENTIFIER;
    }
}