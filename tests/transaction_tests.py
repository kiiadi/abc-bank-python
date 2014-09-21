from nose.tools import assert_is_instance

from transaction import Transaction


def test_type():
    t = Transaction(5)
    assert_is_instance(t, Transaction, "correct type")