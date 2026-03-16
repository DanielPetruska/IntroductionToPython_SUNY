import random

list1 = [random.randint(1, 100) for _ in range(20)]
print("List 1:", list1)

even_numbers = [num for num in list1 if num % 2 == 0]
print("Even numbers in list 1:", even_numbers)
print("TOTAL of even numbers:", sum(even_numbers))

list2 = [random.randint(1, 100) for _ in range(20)]
print("List 2:", list2)

common_elements = [num for num in list2 if num in list1]
print("Elements in list 2 that are also in list 1:", common_elements)

sales_data = [
    [2020, 2.3, 2.2, 1.8, 3.1],
    [2021, 2.4, 2.0, 1.7, 3.0],
    [2022, 1.7, 1.2, 1.0, 1.8],
    [2023, 1.9, 1.0, 0.7, 2.0],
    [2024, 2.0, 2.4, 2.0, 3.2]
]

print("\nTotal sales per year:")
for year_data in sales_data:
    print(f"{year_data[0]}: {sum(year_data[1:])} million $")

print("\nAverage sales per quarter per year:")
for year_data in sales_data:
    print(f"{year_data[0]}: {sum(year_data[1:])/4:.2f} million $")

max_sale = float('-inf')
min_sale = float('inf')
for year_data in sales_data:
    year = year_data[0]
    for q, sale in enumerate(year_data[1:], start=1):
        if sale > max_sale:
            max_sale = sale
            max_year = year
            max_quarter = q
        if sale < min_sale:
            min_sale = sale
            min_year = year
            min_quarter = q

print(f"\nMaximum sale: {max_sale} million $ in Q{max_quarter} {max_year}")
print(f"Minimum sale: {min_sale} million $ in Q{min_quarter} {min_year}")