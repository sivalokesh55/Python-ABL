
n = int(input("Enter number of student records: "))

branch_codes = {
    "CSE": "Computer Science",
    "AIM": "Artificial Intelligence",
    "ECE": "Electronics",
    "EEE": "Electrical",
    "MEC": "Mechanical"
}

valid_count = 0
invalid_count = 0

for i in range(n):
    print("\nStudent", i + 1)

    reg_id = input("Enter registration identifier: ").upper()

    if len(reg_id) != 9:
        print("Invalid: Identifier must contain 9 characters")
        invalid_count += 1

    elif not reg_id[:2].isdigit():
        print("Invalid: Admission year must contain digits")
        invalid_count += 1

    elif reg_id[2:5] not in branch_codes:
        print("Invalid: Unknown branch code")
        invalid_count += 1

    elif not reg_id[5:].isdigit():
        print("Invalid: Student number must contain digits")
        invalid_count += 1

    elif int(reg_id[:2]) < 20 or int(reg_id[:2]) > 26:
        print("Invalid: Admission year code out of range")
        invalid_count += 1

    elif int(reg_id[5:]) == 0:
        print("Invalid: Student number cannot be zero")
        invalid_count += 1

    else:
        year_code = reg_id[:2]
        branch_code = reg_id[2:5]
        student_number = reg_id[5:]

        print("Valid Registration Identifier")
        print("Admission Year: 20" + year_code)
        print("Branch Code:", branch_code)
        print("Branch Name:", branch_codes[branch_code])
        print("Student Number:", student_number)

        valid_count += 1

print("\n----- REGISTRATION SUMMARY -----")
print("Total Records:", n)
print("Valid Records:", valid_count)
print("Invalid Records:", invalid_count)
