from bank import BankAccount
import pytest


#@pytest.fixture(scope="session") équivalent d'un Before All
@pytest.fixture # équivalent d'un Before Each
def account():
    return BankAccount()

def test_new_account_has_zero_balance():
    assert account.balance == 0

def test_deposit_increase_balance():
    account.deposite(100)
    assert account.balance == 100

def test_withdraw_decreases_balance():
    account.deposite(100)
    account.withdraw(40)
    assert account.balance == 60

def test_withdraw_cannot_go_negative():
    with pytest.raises(ValueError):
        account.withdraw(20)
