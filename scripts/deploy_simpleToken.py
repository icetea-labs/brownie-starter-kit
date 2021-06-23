#!/usr/bin/python3

from brownie import SimpleToken, accounts, config, network


def account_from_key():
    private_key = config["wallets"]["from_key"]
    account = accounts.add(private_key)
    return account


def deploy_token():
    # account = account_from_key()
    account = accounts.load('halongbay')
    simpleToken = SimpleToken.deploy({"from": account})
    return simpleToken


def main():
    deploy_token()
