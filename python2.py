
n = int(input("Enter number of chemical records: "))

max_quantities = {
    "Acid": 50,
    "Base": 40,
    "Solvent": 60
}

inventory = []
invalid_records = []

for i in range(n):
    print("\nRecord", i + 1)

    name = input("Enter chemical name: ")
    category = input("Enter category (Acid/Base/Solvent): ")
    quantity = float(input("Enter quantity in litres: "))
    storage = input("Enter storage category: ")

    valid = True
    reason = ""

    if category not in max_quantities:
        valid = False
        reason = "Invalid chemical category"

    elif quantity <= 0:
        valid = False
        reason = "Invalid quantity"

    elif quantity > max_quantities[category]:
        valid = False
        reason = "Maximum quantity exceeded"

    elif category == "Acid" and storage == "Base":
        valid = False
        reason = "Acid and base storage incompatibility"

    elif category == "Solvent" and storage == "Oxidizer":
        valid = False
        reason = "Solvent and oxidizer storage incompatibility"

    inventory.append([name, category, quantity, storage, valid])

    if not valid:
        invalid_records.append([name, reason])

print("\n----- INVENTORY VALIDATION REPORT -----")

for record in inventory:
    if record[4]:
        print(record[0], "- Valid record")
    else:
        print(record[0], "- Invalid record")

print("\n----- INVALID RECORDS -----")

if len(invalid_records) == 0:
    print("No invalid records found")
else:
    for record in invalid_records:
        print(record[0], ":", record[1])

print("\nTotal records:", n)
print("Valid records:", n - len(invalid_records))
print("Invalid records:", len(invalid_records))
