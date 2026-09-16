// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.34;

import {Calculator} from "pr9cal.sol";

contract Main is Calculator{
    uint256 x;
    uint256 y;
    uint256 public r1;
    uint256 public r2;

    function accept_numbers(uint256 n1, uint256 n2) public {
        x = n1;
        y = n2;
        r1 = add(x,y);
        r2 = sub(x, y);
    }
}
