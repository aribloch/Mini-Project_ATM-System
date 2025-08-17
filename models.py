class Account:
    def __init__(self, account_number, balance=0.0, min_balance=0.0, credit_limit=1000.0):
        self.account_number = account_number
        self.balance = balance
        self.min_balance = min_balance
        self.credit_limit = credit_limit
        self.withdrawn_this_month = 0.0  # Tracks monthly withdrawals
