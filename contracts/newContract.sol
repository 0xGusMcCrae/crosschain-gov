// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "@openzeppelin/contracts/proxy/utils/Initializable.sol";

contract NewContract {

    string private immutable IDENTIFIER;

    function initialize() reinitializer(2) public {
        IDENTIFIER = 'New Contract';
    }

    function getIdentifier() public pure returns (string memory) {
        return IDENTIFIER;
    }
}
