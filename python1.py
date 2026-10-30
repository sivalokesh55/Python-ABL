
balance = float(input("Enter initial balance: "))
transactions = []
withdrawal_limit = 10000

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")
    choice = int(input("Enter your choice: "))
    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        print("Invalid transaction amount")
        transactions.append("Transaction rejected: Invalid amount")

    elif choice == 1:
        balance += amount
        print("Deposit successful")
        transactions.append("Deposit: +" + str(amount))

    elif choice == 2:
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
            transactions.append("Withdrawal rejected: Limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
            transactions.append("Withdrawal rejected: Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")
            transactions.append("Withdrawal: -" + str(amount))

    else:
        print("Invalid transaction choice")
        transactions.append("Transaction rejected: Invalid choice")

print("\n----- TRANSACTION SUMMARY -----")
for transaction in transactions:
    print(transaction)

print("Final Balance:", balance)
print("Maximum Withdrawal Per Transaction:", withdrawal_limit)
