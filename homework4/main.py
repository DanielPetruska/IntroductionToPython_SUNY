filename = "expenses.txt"

while True:
    category = input("Enter expense category: ")
    amount = input("Enter amount: ")
    with open(filename, "a") as f:
        f.write(f"{category},{amount}\n")
    more = input("Add another expense? (y/n): ")
    if more.lower() != "y":
        break

expenses = {}
with open(filename, "r") as f:
    for line in f:
        cat, amt = line.strip().split(",")
        amt = float(amt)
        if cat in expenses:
            expenses[cat] += amt
        else:
            expenses[cat] = amt

sorted_expenses = dict(sorted(expenses.items(), key=lambda x: x[1], reverse=True))
print("\nTotal expenses by category (descending):")
for cat, total in sorted_expenses.items():
    print(f"{cat}: {total}")