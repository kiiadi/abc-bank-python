from datetime import datetime


class Transaction:
    def __init__(self, amount):
        self.amount = amount
        self.transactionDate = datetime.now()