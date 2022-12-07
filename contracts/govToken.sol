//SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";

contract GovToken is ERC20Votes {

    constructor(uint256 supply) ERC20('GovToken', 'GOV') ERC20Permit('Govtoken'){
        _mint(msg.sender, supply);
    }
}