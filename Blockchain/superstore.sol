// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.2 <0.9.0;

contract Store{
    uint public totalBill;

    //  regular function
    function purchase(uint amount) public {
        totalBill = amount;
    }

    // View function
    function getBill() public view returns (uint) {
        return totalBill;
    }

    // Pure function 
    function discount() public pure returns (uint) {
        return 500;
    }

    // View function
    function finalBill() public view returns (uint) {
        if (totalBill > 5000) {
            return totalBill - discount();
        } else {
            return totalBill;
        }
    }
}