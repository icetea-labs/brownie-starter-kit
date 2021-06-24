// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.0;

contract Storage {
    uint[] private values;

    function storeValue(uint value) public {
        values.push(value);
    }

    function getValue(uint initial) public view returns(uint) {
        return values[initial];
    }

    function getNumberOfValues() public view returns(uint) {
        return values.length;
    }
}
