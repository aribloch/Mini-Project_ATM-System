from flask import Flask, request
from models import Account
from repositories import InMemoryAccountRepository
from services import AccountService

app = Flask(__name__)

# Initialize repositories and services
account_repo = InMemoryAccountRepository()
account_service = AccountService(account_repo)

# Create some sample accounts
account_repo.update_account(Account(1001, balance=500.0, min_balance=50.0, credit_limit=1000.0))
account_repo.update_account(Account(1002, balance=2000.0, min_balance=100.0, credit_limit=1500.0))

@app.route("/accounts/<int:account_number>/balance", methods=["GET"])
def get_balance(account_number):
    try:
        balance = account_service.get_balance(account_number)
        return {"balance": balance}
    except ValueError as e:
        return {"error": str(e)}, 404

@app.route("/accounts/<int:account_number>/deposit", methods=["POST"])
def deposit(account_number):
    data = request.get_json()
    amount = data.get("amount")
    try:
        new_balance = account_service.deposit(account_number, amount)
        return {"balance": new_balance}
    except ValueError as e:
        return {"error": str(e)}, 400

@app.route("/accounts/<int:account_number>/withdraw", methods=["POST"])
def withdraw(account_number):
    data = request.get_json()
    amount = data.get("amount")
    try:
        new_balance = account_service.withdraw(account_number, amount)
        return {"balance": new_balance}
    except ValueError as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run()
