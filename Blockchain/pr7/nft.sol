// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

error InsufficentDontaion(string reason, address sender , uint256 amount);
error InsufficentBalance(string reason , address sender); 

contract NFT{
    event dontaionMorethan10ETH(string MSG , address sender ,uint256 amount);
    address owner;
    constructor (){
        owner=msg.sender;
    }

    function donation () public payable {
        if (msg.value >= 20 ether){
            revert InsufficentBalance('balance not sufficent',owner);
        }
        if (msg.value > 10 ether){
            emit dontaionMorethan10ETH("Thank You for Donation", owner , msg.value);
        }
    }
}