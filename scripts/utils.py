from brownie import (
    network, 
    accounts,
    config
)


def get_account():
    actived_network = network.show_active()
    print(f"The active network is {actived_network}")
    if actived_network == "development":
        return accounts[0]
    if actived_network in config["networks"]:
        private_key = config["wallets"]["from_key"]
        return accounts.add(private_key)


def get_verify_status():
    actived_network = network.show_active()
    verify = (
        config["networks"][actived_network]["verify"]
        if config["networks"][actived_network].get("verify")
        else False
    )
    return verify

def is_halongbay():
    if network.show_active() == 'halongbay':
        return True
    return False