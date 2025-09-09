from bank import BankAccount
import pytest


#@pytest.fixture(scope="session") équivalent d'un Before All
@pytest.fixture # équivalent d'un Before Each
def account():
    return BankAccount()

@pytest.mark.parametrize("amount", [10, 50, 200])
def test_multiple_deposits(account, amount):
    account.deposite(amount)
    assert account.balance == amount

def test_new_account_has_zero_balance(account):
    assert account.balance == 0

def test_deposit_increase_balance(account):
    account.deposite(100)
    assert account.balance == 100

def test_withdraw_decreases_balance(account):
    account.deposite(100)
    account.withdraw(40)
    assert account.balance == 60

def test_withdraw_cannot_go_negative(account):
    with pytest.raises(ValueError):
        account.withdraw(20)
