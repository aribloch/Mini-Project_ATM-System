from datetime import datetime
from repositories import AccountRepositoryInterface  # assuming your repo file is repositories.py
import threading

# this layer handles the BL (Business Logic)
class AccountService:
    def __init__(self, account_repo: AccountRepositoryInterface):
        self.account_repo = account_repo
        self.lock = threading.Lock() # Lock for atomic operations

    def get_balance(self, account_number):
        account = self.account_repo.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        return account.balance

    def deposit(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        with self.lock:
            account = self.account_repo.get_account(account_number)
            if not account:
                raise ValueError("Account not found")

            account.balance += amount
            self.account_repo.update_account(account)
            return account.balance

    def withdraw(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        with self.lock:
            account = self.account_repo.get_account(account_number)
            if not account:
                raise ValueError("Account not found")

            # 🔹 Reset monthly withdrawals if month changed
            current_month = datetime.now().month
            if getattr(account, "last_withdraw_month", None) != current_month:
                account.withdrawn_this_month = 0.0
                account.last_withdraw_month = current_month

            # 🔹 Check monthly credit limit
            if account.withdrawn_this_month + amount > account.credit_limit:
                raise ValueError("Withdrawal exceeds monthly credit limit")

            # 🔹 Check minimum balance
            if account.balance - amount < account.min_balance:
                raise ValueError("Insufficient funds to maintain minimum balance")

            # 🔹 Perform withdrawal
            account.balance -= amount
            account.withdrawn_this_month += amount

            self.account_repo.update_account(account)
            return account.balance
