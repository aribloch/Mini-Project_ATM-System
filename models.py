from datetime import datetime
import threading

class Account:
    # default min_balance and credit_limits initialized
    def __init__(self, account_number, balance=0.0, min_balance=0.0, credit_limit=1000.0):
        self.account_number = account_number
        self.balance = balance
        self.min_balance = min_balance
        self.credit_limit = credit_limit
        self.monthly_withdrawn = 0.0
        self.last_withdraw_month = None  # stores the month of last withdrawal
        self.lock = threading.Lock() # lock to make operations atomic

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        with self.lock:
            self.balance += amount
        return self.balance

    def can_withdraw(self, amount):
        # Check if withdrawal is allowed based on balance, min_balance, and monthly credit_limit.
        # Reset monthly_withdrawn if month changed
        current_month = datetime.now().month
        if self.last_withdraw_month != current_month:
            self.monthly_withdrawn = 0
            self.last_withdraw_month = current_month

        if amount <= 0:
            return False
        # would go below min balance
        if self.balance - amount < self.min_balance:
            return False
        # would exceed max amount to withdraw per month
        if self.monthly_withdrawn + amount > self.credit_limit:
            return False
        return True

    def withdraw(self, amount):
        with self.lock:
            if not self.can_withdraw(amount):
                raise ValueError(
                    f"Cannot withdraw {amount}. "
                    f"Min balance: {self.min_balance}, "
                    f"Monthly credit limit: {self.credit_limit}, "
                    f"Already withdrawn this month: {self.monthly_withdrawn}"
                )
            self.balance -= amount
            self.monthly_withdrawn += amount
            return self.balance
