# atm_client.py
import requests

BASE_URL = "http://127.0.0.1:5000/accounts"

def get_balance(account_number):
    url = f"{BASE_URL}/{account_number}/balance"
    response = requests.get(url)
    if response.status_code == 200:
        print("Current balance:", response.json()["balance"])
    else:
        print("Error:", response.text)

def deposit(account_number, amount):
    url = f"{BASE_URL}/{account_number}/deposit"
    response = requests.post(url, json={"amount": amount})
    if response.status_code == 200:
        print("Deposit successful. New balance:", response.json()["new_balance"])
    else:
        print("Error:", response.text)

def withdraw(account_number, amount):
    url = f"{BASE_URL}/{account_number}/withdraw"
    response = requests.post(url, json={"amount": amount})
    if response.status_code == 200:
        print("Withdrawal successful. New balance:", response.json()["new_balance"])
    else:
        print("Error:", response.text)

def main():
    print("=== ATM Client ===")
    account_number = input("Enter account number: ")
    while True:
        print("\nChoose operation:")
        print("1. Get Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            get_balance(account_number)
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            deposit(account_number, amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            withdraw(account_number, amount)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
