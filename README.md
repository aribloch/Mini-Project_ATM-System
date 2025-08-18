# ATM Banking API

##  Overview
This project is a simple **ATM banking system** built with **Flask** and deployed on the cloud (AWS EC2).  
It provides APIs for:
- Checking account balance  
- Depositing funds  
- Withdrawing funds (with monthly credit limit & minimum balance enforcement)  

The system follows a **layered architecture**:
- **Models layer** → defines the `Account` class (business entity).  
- **Repositories layer** → abstracts data access (e.g., in-memory today, could be a database tomorrow).  
- **Services layer** → contains business logic (deposit, withdraw, enforce rules).  
- **App layer** → Flask routes expose REST API endpoints.  

---

##  Design Decisions
1. **Separation of Concerns**  
   - Business logic is isolated from persistence via a repository interface.  
   - Switching from in-memory to SQL or NoSQL storage requires no change in the service layer.  

2. **Atomic Operations**  
   - Deposits and withdrawals are atomic to prevent inconsistent states.  

3. **Business Rules**  
   - Minimum balance enforcement.  
   - Monthly credit withdrawal limit.  
   - Automatic reset of monthly withdrawals.  

4. **Cloud-Ready**  
   - Deployable on **AWS EC2**.  

---

## ▶️ Execution (Linux)

Once your server is running (locally or on AWS), you can test the API with these **curl commands**.  
Replace `{server-ip}` with your EC2 public IP (or `localhost` if running locally), `{account_number}` with the account number, and `{amount}` with the amount to deposit/withdraw.  

---

### 1. Get Balance
```bash
curl -X GET http://{server-ip}:5000/accounts/{account_number}/balance
```
### 1. Deposit
```bash
curl -X POST http://{server-ip}:5000/accounts/{account_number}/deposit -H "Content-Type: application/json" -d '{"amount": {amount}}'
```

### 1. Withdraw
```bash
curl -X POST http://{server-ip}:5000/accounts/{account_number}/withdraw -H "Content-Type: application/json" -d '{"amount": {amount}}'
```

