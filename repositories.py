from abc import ABC, abstractmethod

# Repository interface
# Data Layer (Interface + In-Memory Implementation)
class AccountRepositoryInterface(ABC):
    @abstractmethod
    def get_account(self, account_number):
        pass

    @abstractmethod
    def update_account(self, account):
        pass


# In-memory implementation
class InMemoryAccountRepository(AccountRepositoryInterface):
    def __init__(self):
        self.accounts = {}
# Retreives Account Object from DB
    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Returns updated Account object to DB
    def update_account(self, account):
        self.accounts[account.account_number] = account
