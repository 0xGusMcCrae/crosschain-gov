// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

interface IProxyContract {

   function setNewImplementation(
        address newImplementation, 
        bytes memory initializerCall
        ) external;

}