// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleBank {
    mapping(address => uint256) private balances;

    // Deposit money to the contract
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // Withdraw money from the contract
    function withdraw(uint256 amount) public {
        require(amount <= balances[msg.sender], "Insufficient funds");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Get the balance of the user
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
