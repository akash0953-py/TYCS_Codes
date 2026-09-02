// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Calculator{
    uint256 result;

    function add(uint256 a,uint256 b) internal  returns (uint256) {
        result = a+b;
        return result;
    }

    function sub(uint256 a,uint256 b) internal  returns (uint256) {
        result = a-b;
        return result;
    }

    function mul(uint256 a,uint256 b) external  returns (uint256) {
        result = a*b;
        return result;
    }

    function div(uint256 a,uint256 b) external  returns (uint256) {
        result = a/b;
        return result;
    }

}