from flask import Flask, request
from database import accounts

app = Flask(__name__)

# Python decorator that tells Flask to run functionality below when this URL is visited
@app.route("/accounts/<account_number>/balance", methods=["GET"])
def get_balance(account_number):
    account = accounts.get(account_number)
    if account:
        return {
                   "account_number": account.account_number,
                   "balance": account.get_balance()
               }, 200
    return {"error": "Account not found"}, 404


# Python decorator that tells Flask to run functionality below when this URL is visited
@app.route("/accounts/<account_number>/deposit", methods=["POST"])
def deposit(account_number):
    account = accounts.get(account_number)
    if not account:
        return {"error": "Account not found"}, 404

    data = request.get_json()
    amount = data.get("amount", 0)
    try:
        new_balance = account.deposit(amount)
        return {
                   "message": "Deposit successful",
                   "new_balance": new_balance
               }, 200
    except ValueError as e:
        return {"error": str(e)}, 400


# Python decorator that tells Flask to run functionality below when this URL is visited
@app.route("/accounts/<account_number>/withdraw", methods=["POST"])
def withdraw(account_number):
    account = accounts.get(account_number)
    if not account:
        return {"error": "Account not found"}, 404

    data = request.get_json()
    amount = data.get("amount", 0)
    try:
        new_balance = account.withdraw(amount)
        return {
                   "message": "Withdrawal successful",
                   "new_balance": new_balance
               }, 200
    except ValueError as e:
        return {"error": str(e)}, 400


if __name__ == "__main__":
    # default parameters are host="127.0.0.1", port=5000 - runs on local host
    app.run(host="0.0.0.0", port=5000)
