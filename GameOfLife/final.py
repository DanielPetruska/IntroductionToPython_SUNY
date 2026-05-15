import csv

FILE = "orders.csv"


# Create the file with header if it doesn't exist
def initialize_file():
    try:
        with open(FILE, "r") as f:
            pass
    except FileNotFoundError:
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "address", "description", "date", "total", "delivered"])


def add_order():
    name = input("Customer name: ")
    address = input("Address: ")
    description = input("Description: ")
    date = input("Date (YYYY/MM/DD): ")
    total = input("Total amount: ")

    # Get next ID
    try:
        with open(FILE, "r") as f:
            rows = list(csv.reader(f))
            next_id = len(rows)  # since we have header, this works as ID
    except:
        next_id = 1

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([next_id, name, address, description, date, total, "False"])

    print("Order added successfully!\n")


def mark_delivered():
    order_id = input("Enter order ID: ")

    rows = []
    found = False

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for row in rows:
        if row[0] == order_id:
            row[6] = "True"
            found = True
            break

    if found:
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print("Order marked as delivered!\n")
    else:
        print("Order ID not found!\n")


def orders_by_customer():
    name = input("Customer name: ").strip().lower()
    count = 0

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["name"].strip().lower() == name:
                count += 1

    print(f"Total orders for {name.title()}: {count}\n")


def pending_orders():
    print("Pending orders:")
    print("-" * 50)

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        found = False
        for row in reader:
            if row["delivered"] == "False":
                print(f"ID: {row['id']} | {row['name']} | {row['description']} | {row['date']} | ${row['total']}")
                found = True
        if not found:
            print("No pending orders!")
    print()


# Initialize file
initialize_file()

# Main menu
while True:
    print("=== Order Management System ===")
    print("1. Add order")
    print("2. Mark order as delivered")
    print("3. Orders by customer")
    print("4. Show pending orders")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        add_order()
    elif choice == "2":
        mark_delivered()
    elif choice == "3":
        orders_by_customer()
    elif choice == "4":
        pending_orders()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.\n")