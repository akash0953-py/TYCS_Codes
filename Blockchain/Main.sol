// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import {Calculator} from './cal.sol';
contract Main is Calculator{
    uint256 x;
    uint256 y;
    function accept_numbers(uint256 a,uint256 b) public {
        x = a;
        y = b;
        add(x, y);
        sub(x, y);
        // mul(x, y);
        // div(x, y);
    }
}