import pytest
from brownie import network, HelloWorld

def test_call_get(hello_world):
    message = hello_world.get()
    assert message == "Hello world"
