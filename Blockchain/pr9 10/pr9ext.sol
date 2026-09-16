// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.34;

import {Calculator} from "pr9cal.sol";

contract EC{
    uint256 x;
    uint256 y;
    uint256 public r1;
    uint256 public r2;

    function accept_numbers(uint256 n1, uint256 n2) public {
        Calculator cal = Calculator(0x1c91347f2A44538ce62453BEBd9Aa907C662b4bD);
        x = n1;
        y = n2;
        r1 = cal.div(x,y);
        r2 = cal.mul(x,y);
    }
    
}