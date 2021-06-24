#!/usr/bin/python3

from scripts.utils import (
    get_account,
    get_verify_status
)

from brownie import (
    Storage,
    network,
    Contract
)


def main():
    account = get_account()
    print(f"You are using the account {account}")
    verify = get_verify_status()
    deployed_contract = Storage.deploy({"from": account}, publish_source=verify)
    if type(deployed_contract) is network.transaction.TransactionReceipt:
        deployed_contract.wait(3)
        deployed_contract = Contract.from_abi("Storage", deployed_contract.contract_address, Storage.abi)
    
    print(deployed_contract)