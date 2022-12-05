// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

interface IOldContract {

    function initialize() external;

    function getIdentifier() external view returns (string memory);

    function getVersion() external view returns (uint8);

    function isInitializing() external view returns (bool);
}