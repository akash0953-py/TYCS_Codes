// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.34;

error inf(string ms,  address owner);

contract pr7{
    event donationMorethan10ETH(string MSG, address sender , uint256 amount);

    address owner ;
     
    function donate()public payable {
        if(msg.value <= 5 ether){
            revert inf("greater than 5" , owner);
        }
        if(msg.value > 10 ether){
        emit donationMorethan10ETH("thank you", owner, msg.value);
    }
}
}