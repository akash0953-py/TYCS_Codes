// SPDX-License-Identifier: MIT
pragma solidity <= 0.8.34;

error InsufficientFunds(string reason ,address sender , uint256 amount);
error InsufficientDonation(string reason ,address sender);

contract Donation{
    address owner;
    constructor(){
        owner = msg.sender;
    }

    modifier onlyOwner(){
        require(msg.sender == owner, "You are not owner");
        _;
    }
    modifier notowner(){
        require(msg.sender != owner, "You are not owner");
        _;
    }

    function donate() public payable notowner{
        if(msg.sender.balance <= 100000 gwei){
            revert InsufficientFunds("Balance be big",msg.sender,msg.sender.balance);
        }
        if (msg.value <= 5 gwei){
            revert InsufficientDonation("donation big than 5" , msg.sender);
        }
    }

    function withdraw() public payable onlyOwner returns (bool) {
        uint256 acc_bal = address(this).balance;
        if (acc_bal == 0){
            revert InsufficientFunds("Balcnce should be more" , msg.sender , acc_bal);
        }
        (bool success , ) = owner.call{value:acc_bal}("");
        return success ;
    }

}
