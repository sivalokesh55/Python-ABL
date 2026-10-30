
days = int(input("Enter number of days: "))
waste_limit = float(input("Enter acceptable wastage percentage: "))

total_prepared = 0
total_served = 0
total_leftovers = 0
exceeded_days = 0

records = []

for i in range(days):
    print("\nDay", i + 1)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))
    leftovers = int(input("Enter leftover meals: "))

    if prepared <= 0 or served < 0 or leftovers < 0:
        print("Invalid meal quantities")
        continue

    if served + leftovers != prepared:
        print("Invalid record: Prepared meals must equal served meals plus leftovers")
        continue

    wastage = (leftovers / prepared) * 100

    records.append([i + 1, prepared, served, leftovers, wastage])

    total_prepared += prepared
    total_served += served
    total_leftovers += leftovers

    print("Wastage Percentage:", round(wastage, 2), "%")

    if wastage > waste_limit:
        print("Status: Wastage limit exceeded")
        exceeded_days += 1
    else:
        print("Status: Acceptable")

print("\n===== FOOD WASTE REPORT =====")

for record in records:
    print("\nDay:", record[0])
    print("Prepared:", record[1])
    print("Served:", record[2])
    print("Leftovers:", record[3])
    print("Wastage:", round(record[4], 2), "%")

if total_prepared > 0:
    overall_wastage = (total_leftovers / total_prepared) * 100

    print("\n===== OVERALL SUMMARY =====")
    print("Total Meals Prepared:", total_prepared)
    print("Total Meals Served:", total_served)
    print("Total Leftovers:", total_leftovers)
    print("Overall Wastage:", round(overall_wastage, 2), "%")
    print("Days Exceeding Limit:", exceeded_days)
else:
    print("No valid records available")
