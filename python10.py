
days = int(input("Enter number of days: "))
stations = int(input("Enter number of monitoring stations per day: "))

readings = []

for i in range(days):
    daily_readings = []

    print("\nDay", i + 1)

    for j in range(stations):
        value = float(input(
            "Enter air quality reading for station "
            + str(j + 1) + ": "
        ))

        daily_readings.append(value)

    readings.append(daily_readings)

threshold = float(input("Enter acceptable threshold: "))

total = 0
count = 0
highest = readings[0][0]
lowest = readings[0][0]
high_count = 0

print("\n===== ENVIRONMENTAL REPORT =====")

for i in range(days):
    daily_total = 0

    print("\nDay", i + 1)

    for j in range(stations):
        value = readings[i][j]

        daily_total += value
        total += value
        count += 1

        if value > highest:
            highest = value

        if value < lowest:
            lowest = value

        if value > threshold:
            print("Station", j + 1, ":", value,
                  "- Threshold Exceeded")
            high_count += 1
        else:
            print("Station", j + 1, ":", value,
                  "- Acceptable")

    average = daily_total / stations
    print("Daily Average:", round(average, 2))

overall_average = total / count

print("\n===== FINAL SUMMARY =====")
print("Overall Average:", round(overall_average, 2))
print("Highest Reading:", highest)
print("Lowest Reading:", lowest)
print("Readings Exceeding Threshold:", high_count)
print("Total Readings:", count)
