pragma solidity ^0.6.0;

// SPDX-License-Identifier: MIT

contract SimpleToken {
    uint256[] public list;

    function foo(uint256 a) public {
        list.push(a);
    }
}
