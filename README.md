# Brownie Starter Kit
An example smart contract toolkit


## Installation


## Basic Use

This mix provides a [simple ERC20 Token Template](contracts/Token.sol) upon which you can build your own token.

To interact with a deployed contract in a local environment, start by opening the console:

```bash
brownie console
```

Next, deploy a test token:

```python
>>> token = Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})

Transaction sent: 0x4a61edfaaa8ba55573603abd35403cf41291eca443c983f85de06e0b119da377
  Gas price: 0.0 gwei   Gas limit: 12000000
  Token.constructor confirmed - Block: 1   Gas used: 521513 (4.35%)
  Token deployed at: 0xd495633B90a237de510B4375c442C0469D3C161C
```

You now have a token contract deployed, with a balance of `1e21` assigned to `accounts[0]`:

```python
>>> token
<Token Contract '0xd495633B90a237de510B4375c442C0469D3C161C'>

>>> token.balanceOf(accounts[0])
1000000000000000000000

>>> token.transfer(accounts[1], 1e18, {'from': accounts[0]})
Transaction sent: 0xb94b219148501a269020158320d543946a4e7b9fac294b17164252a13dce9534
  Gas price: 0.0 gwei   Gas limit: 12000000
  Token.transfer confirmed - Block: 2   Gas used: 51668 (0.43%)

<Transaction '0xb94b219148501a269020158320d543946a4e7b9fac294b17164252a13dce9534'>
```

## Testing

To run the tests:

```bash
brownie test
```

## Resources


## License

This project is licensed under the [MIT license](LICENSE).
