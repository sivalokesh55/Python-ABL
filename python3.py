
n = int(input("Enter number of students: "))

valid_count = 0
invalid_count = 0

for i in range(n):
    print("\nStudent", i + 1)

    email = input("Enter student email: ")
    reg_id = input("Enter registration ID: ")

    email_valid = True
    id_valid = True

    # Email validation
    if "@" not in email:
        print("Email Error: Missing @ symbol")
        email_valid = False
    elif email.count("@") != 1:
        print("Email Error: Invalid @ separator")
        email_valid = False
    else:
        parts = email.split("@")
        username = parts[0]
        domain = parts[1]

        if username == "" or domain == "":
            print("Email Error: Missing component")
            email_valid = False
        elif "." not in domain:
            print("Email Error: Missing domain separator")
            email_valid = False
        elif domain.startswith(".") or domain.endswith("."):
            print("Email Error: Malformed separator")
            email_valid = False
        elif ".." in email:
            print("Email Error: Consecutive dots")
            email_valid = False
        else:
            allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._+-"
            for ch in username:
                if ch not in allowed:
                    print("Email Error: Invalid username character")
                    email_valid = False
                    break

            for ch in domain:
                if ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-":
                    print("Email Error: Invalid domain character")
                    email_valid = False
                    break

    # Registration ID validation
    # Expected format: CSE followed by 6 digits
    if len(reg_id) != 9:
        print("ID Error: Incorrect length")
        id_valid = False
    elif not reg_id.startswith("CSE"):
        print("ID Error: Missing CSE prefix")
        id_valid = False
    else:
        digits = reg_id[3:]
        if not digits.isdigit():
            print("ID Error: Invalid character group")
            id_valid = False

    # Final result
    if email_valid and id_valid:
        print("Result: Student details are valid")
        valid_count += 1
    else:
        print("Result: Student details are invalid")
        invalid_count += 1

print("\n----- VALIDATION SUMMARY -----")
print("Total students:", n)
print("Valid records:", valid_count)
print("Invalid records:", invalid_count)
