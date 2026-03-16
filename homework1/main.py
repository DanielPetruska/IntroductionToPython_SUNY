# Part 1: Ask for birth date and print it
day = input("Enter day of birth: ")
month = input("Enter month of birth: ")
year = input("Enter year of birth: ")
print(f"{day}/{month}/{year}")

# Part 2: Ask for income and calculate tax
income = float(input("Enter your yearly income: "))
if income < 10000:
    tax = income * 0.08
elif 10001 <= income <= 26000:
    tax = income * 0.12
else:
    tax = income * 0.24
print(f"Tax: {tax}")

# Part 3: Print numbers from a to b
a = int(input("Give a: "))
b = int(input("Give b: "))
if a > b:
    print("Error, a must be less than b")
else:
    for num in range(a, b + 1):
        print(num, end=" ")
    print()

# Part 4: Print even numbers up to a given number
n = int(input("Give a number: "))
for i in range(2, n + 1, 2):
    print(i, end=" ")
print()

# Part 5: Supermarket self-checkout total
total = 0
while True:
    price = float(input("Item price: "))
    total += price
    more = input("Have more items? (y/n): ")
    if more.lower() != 'y':
        break
print(f"TOTAL: {total}")