// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.2 <0.9.0;

contract Nss{
    uint sid = 1;
    uint marks;
    uint nss = 1;

    // regular function
    function putmarks(uint mks) public{
            marks = mks;
    }

    // pure function
    function nss_marks() public pure returns(uint){
        return 10;
    }
    
    // view function
    function get_marks() public view returns(uint){
        return marks;
    }

    // regular function
    function store_marks() public returns(uint) {
        if (nss == 1){
            marks += nss_marks();
        }
        return marks;
    }
}

