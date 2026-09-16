// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.34;

contract Marks{
    uint finalmarks;
    function nss_marks() public pure returns(uint){
        return 10;
    }
    function enter_marks(uint marks , bool nss) public {
        if (nss == true){
            marks += nss_marks();
        }
        finalmarks = marks;
    }

    function getmarks() public view returns (uint) {
        return finalmarks;
    }
}