
stock = {
    "Laptop": 20,
    "Mouse": 50,
    "Keyboard": 30
}

total_orders = 0
total_dispatched = 0
total_returns = 0
invalid_records = 0

n = int(input("Enter number of order records: "))

for i in range(n):
    print("\nOrder Record", i + 1)

    item = input("Enter product name: ").title()
    ordered = int(input("Enter ordered quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    returned = int(input("Enter returned quantity: "))

    if item not in stock:
        print("Invalid record: Unknown product")
        invalid_records += 1
        continue

    elif ordered <= 0 or dispatched < 0 or returned < 0:
        print("Invalid record: Incorrect quantity")
        invalid_records += 1
        continue

    elif dispatched > ordered:
        print("Invalid record: Dispatch exceeds order")
        invalid_records += 1
        continue

    elif returned > dispatched:
        print("Invalid record: Returns exceed dispatch")
        invalid_records += 1
        continue

    outstanding = ordered - dispatched
    net_delivered = dispatched - returned

    stock[item] += returned

    total_orders += ordered
    total_dispatched += dispatched
    total_returns += returned

    print("\nOrder Status")
    print("Product:", item)
    print("Ordered Quantity:", ordered)
    print("Dispatched Quantity:", dispatched)
    print("Returned Quantity:", returned)
    print("Outstanding Quantity:", outstanding)
    print("Net Delivered Quantity:", net_delivered)
    print("Updated Inventory:", stock[item])

    if outstanding > 0:
        print("Status: Order Pending")
    else:
        print("Status: Dispatch Completed")

print("\n===== RETAIL DISPATCH SUMMARY =====")
print("Total Ordered:", total_orders)
print("Total Dispatched:", total_dispatched)
print("Total Returns:", total_returns)
print("Invalid Records:", invalid_records)

print("\nOutstanding Orders:", total_orders - total_dispatched)

print("\n===== UPDATED INVENTORY =====")
for item in stock:
    print(item, ":", stock[item], "units")

print("\nAnalysis completed")
