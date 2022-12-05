// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

interface INewContract {

    function initialize(uint8 version) external;

    function getIdentifier() external view returns (string memory);

    function getVersion() external view returns (uint8);
}