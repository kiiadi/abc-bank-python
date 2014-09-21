from nose.tools import assert_equals

from account import Account, CHECKING, MAXI_SAVINGS, SAVINGS
from bank import Bank
from customer import Customer


def test_customer_summary():
    bank = Bank()
    john = Customer("John").openAccount(Account(CHECKING))
    bank.addCustomer(john)
    assert_equals(bank.customerSummary(),
                  "Customer Summary\n - John (1 account)")


def test_checking_account():
    bank = Bank()
    checkingAccount = Account(CHECKING)
    bill = Customer("Bill").openAccount(checkingAccount)
    bank.addCustomer(bill)
    checkingAccount.deposit(100.0)
    assert_equals(bank.totalInterestPaid(), 0.1)


def test_savings_account():
    bank = Bank()
    checkingAccount = Account(SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(1500.0)
    assert_equals(bank.totalInterestPaid(), 2.0)


def test_maxi_savings_account():
    bank = Bank()
    checkingAccount = Account(MAXI_SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(3000.0)
    assert_equals(bank.totalInterestPaid(), 170.0)