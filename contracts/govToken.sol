//SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "../node_modules/@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";

///@title Governance token
///@author 0xGusMcCrae
///@notice supply is minted to deployer to test governance votes with the Sacred Council governor contract
contract GovToken is ERC20Votes {

    constructor(uint256 supply) ERC20('GovToken', 'GOV') ERC20Permit('Govtoken'){
        _mint(msg.sender, supply);
    }
}