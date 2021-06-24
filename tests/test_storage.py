import pytest

def test_init_number_of_value(storage):
    number_of_values = storage.getNumberOfValues()
    assert number_of_values == 0

def test_add_two_values(storage, account, halongbay):
    tx = storage.storeValue(1337, {'from': account})
    if halongbay:
        tx.wait(3)
    tx = storage.storeValue(2008, {'from': account})
    if halongbay:
        tx.wait(3)
    number_of_values = storage.getNumberOfValues()
    assert number_of_values == 2

def test_get_first_value(storage):
    first_value = storage.getValue(0)
    assert first_value == 1337