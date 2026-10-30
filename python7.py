
# Each tuple contains:
# (Book ID, Borrowing Period, Return Delay in Days)

borrow_records = [
    ("B101", 7, 0),
    ("B102", 14, 3),
    ("B103", 10, 5),
    ("B104", 7, 0),
    ("B105", 14, 2)
]

available_books = ["B101", "B102", "B103", "B104", "B105"]

fine_per_day = 5
total_fine = 0
overdue_count = 0
returned_books = []

print("===== LIBRARY BORROWING REPORT =====")

for book_id, borrowing_period, delay in borrow_records:
    print("\nBook ID:", book_id)
    print("Borrowing Period:", borrowing_period, "days")
    print("Return Delay:", delay, "days")

    if delay > 0:
        fine = delay * fine_per_day
        total_fine += fine
        overdue_count += 1

        print("Status: Overdue")
        print("Fine Amount: Rs.", fine)
    else:
        fine = 0
        print("Status: Returned on time")
        print("Fine Amount: Rs. 0")

    returned_books.append(book_id)

    if book_id in available_books:
        available_books.remove(book_id)

print("\n===== FINE RECONCILIATION =====")
print("Total Overdue Books:", overdue_count)
print("Total Fine Collected/Due: Rs.", total_fine)

print("\n===== BOOK AVAILABILITY =====")
print("Borrowed Books:", returned_books)
print("Available Books:", available_books)
print("Number of Available Books:", len(available_books))
