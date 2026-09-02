// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
error InsufficientBalance(string reason, address sender, uint256 amt);
error InsufficientDoantion(string reason , address sender);

contract donation {
    address owner;
    constructor(){
        owner = msg.sender;
    }
    modifier onlyOwner(){
        require(msg.sender == owner, "Not owner");
        _;
    }
    modifier onlyDonor(){
        require(msg.sender != owner , "Not donor");
        _;
    }
    function donate() public payable  onlyDonor{  
        if (msg.sender.balance < 90 ether){
            revert InsufficientBalance({reason:'Balance below 90 ETH',sender:msg.sender,amt:msg.sender.balance});
        }
        if (msg.value<5 ether){
            revert InsufficientDoantion({reason:'Donation below 5 eth',sender:msg.sender});
        }
    }
    function withdraw() public payable onlyOwner returns (bool){
        uint256 ctr_bal = address(this).balance;
        (bool success,) =  owner.call{value: ctr_bal}("");
        return success ;
    }
}
