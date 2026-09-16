// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
error InsufficientPrice(string reason, address sender, uint256 amt);
error InsufficientDoantion(string reason , address sender);

contract ott {
    address owner;
    constructor(){
        owner = msg.sender;
    }
    modifier onlyOwner(){
        require(msg.sender == owner, "Not owner");
        _;
    }
    modifier onlybuyer(){
        require(msg.sender != owner , "Not a buyer");
        _;
    }
    function basic_plan() public payable  onlybuyer{  
        if (msg.value != 2 ether){
            revert InsufficientPrice({reason:'Plan price should 2 eth',sender:msg.sender,amt:msg.sender.balance});
        }
    }
    function pro_plan() public payable  onlybuyer{  
        if (msg.value != 10 ether){
            revert InsufficientPrice({reason:'Plan price should be only 10 eth',sender:msg.sender,amt:msg.sender.balance});
        }
    }
    function withdraw_subscription() public payable onlyOwner returns (bool){
        uint256 ctr_bal = address(this).balance;
        (bool success,) =  owner.call{value: ctr_bal}("");
        return success ;
    }
}
