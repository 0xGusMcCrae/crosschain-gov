// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import '@openzeppelin/contracts/crosschain/arbitrum/CrossChainEnabledArbitrumL1.sol';

contract L1Relay is CrossChainEnabledArbitrumL1 {

    constructor() CrossChainEnabledArbitrumL1(0xaf4159A80B6Cc41ED517DB1c453d1Ef5C2e4dB72) {

    }
}

