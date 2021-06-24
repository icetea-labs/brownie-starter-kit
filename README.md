# Brownie Starter Kit
An example smart contract toolkit


## Installation

```bash
pip install --user pipx

pipx ensurepath

# restart your terminal
pipx install eth-brownie
```

## Basic Use

### Add network in brownie
Add Folkafoundry halongbay network

```bash
brownie networks add Polkafoundry halongbay host=https://rpc-halongbay.polkafoundry.com chainid=11
```

### Set environment variables

You'll need the following environment variables. You can set them all in your .env file:

```
export WEB3_INFURA_PROJECT_ID=YourProjectID
export ETHERSCAN_TOKEN=''
export PRIVATE_KEY="0xasdfasdfasdfasd..."
export MNEMONIC=''
```

* `WEB3_INFURA_PROJECT_ID`: Your connection to the blockchain. You can get a URL from a service like Infura
* `ETHERSCAN_TOKEN`:
* `PRIVATE_KEY`: Your Private Key from your Wallet. If using metamask, you'll have to add a 0x to the start of your private key.
* `MNEMONIC`: Your menemonic phasse

### Run source .env

This doesn't auto-pull in your .env file at the start, so you have to set your environment variables at the start.

```bash 
source .env
```

## Run Scripts

```bash
brownie run scripts/deploy.py
brownie run scripts/deploy.py --network kovan
brownie run scripts/deploy.py --network halongbay
```

## Testing

To run the tests:

```bash
brownie test
brownie test --network kovan
brownie test --network halongbay
```

## Testing
### Deploy and interact with the smart contracts via RPC

- [x] Hello World
- [x] Basic Storage
- [ ] ERC20 Token
- [ ] ERC-721 NFT
- [ ] ChainLink

## Contributing

Help is always appreciated! Feel free to open an issue if you find a problem, or a pull request if you've solved an issue.


## License

This project is licensed under the [MIT license](LICENSE).
