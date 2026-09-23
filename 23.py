import csv

filename = "expenses.csv"


# Add expense
def add_expense():
    date = input("Enter expense date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# Display all expenses
def show_expenses():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)

            print("\n--- All Expenses ---")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No expense file found.")


# Spending summary
def spending_summary():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)

            total = 0
            categories = {}

            for row in reader:
                amount = float(row[3])
                category = row[1]

                total += amount

                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

            print("\n--- Spending Summary ---")
            print("Total Spending:", total)

            print("\nCategory-wise Spending:")

            for category, amount in categories.items():
                print(category, ":", amount)

    except FileNotFoundError:
        print("No expense file found.")


# Main menu
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Spending Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        spending_summary()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")