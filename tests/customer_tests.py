from nose.tools import assert_equals, nottest

from account import Account, CHECKING, SAVINGS
from customer import Customer


def test_statement():
    checkingAccount = Account(CHECKING)
    savingsAccount = Account(SAVINGS)
    henry = Customer("Henry").openAccount(checkingAccount).openAccount(savingsAccount)
    checkingAccount.deposit(100.0)
    savingsAccount.deposit(4000.0)
    savingsAccount.withdraw(200.0)
    assert_equals(henry.getStatement(),
                  "Statement for Henry" +
                  "\n\nChecking Account\n  deposit $100.00\nTotal $100.00" +
                  "\n\nSavings Account\n  deposit $4000.00\n  withdrawal $200.00\nTotal $3800.00" +
                  "\n\nTotal In All Accounts $3900.00")


def test_oneAccount():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    assert_equals(oscar.numAccs(), 1)


def test_twoAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 2)


@nottest
def test_threeAccounts():
    oscar = Customer("Oscar").openAccount(Account(SAVINGS))
    oscar.openAccount(Account(CHECKING))
    assert_equals(oscar.numAccs(), 3)