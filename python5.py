
balance = float(input("Enter initial account balance: "))

daily_limit = 20000
total_withdrawn = 0
transactions = []
choice = 0

while choice != 5:
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid deposit amount")
        else:
            balance += amount
            transactions.append("Deposit: +" + str(amount))
            print("Deposit successful")
            print("Updated Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > balance:
            print("Insufficient balance")
        elif total_withdrawn + amount > daily_limit:
            print("Daily withdrawal limit exceeded")
        else:
            balance -= amount
            total_withdrawn += amount
            transactions.append("Withdrawal: -" + str(amount))
            print("Withdrawal successful")
            print("Updated Balance:", balance)

    elif choice == 3:
        print("Available Balance:", balance)
        print("Daily Withdrawal Limit:", daily_limit)
        print("Amount Withdrawn Today:", total_withdrawn)

    elif choice == 4:
        print("\n----- TRANSACTION SUMMARY -----")

        if len(transactions) == 0:
            print("No transactions available")
        else:
            for transaction in transactions:
                print(transaction)

        print("Current Balance:", balance)

    elif choice == 5:
        print("Thank you for using the ATM")
        print("Final Balance:", balance)

    else:
        print("Invalid menu choice")

print("\nATM session ended")
