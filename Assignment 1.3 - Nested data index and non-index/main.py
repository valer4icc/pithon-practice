name = input("Enter your name: ")
print(f"Welcome to Python Bistro\n")

menu = [
    {"name": "Burger", "price": 8.50},
    {"name": "Pizza", "price": 10.00},
    {"name": "Cola", "price": 2.50}
]

print(f"{'Item':<20}{'Price':>10}")
print("-" * 27)

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item['name']:<17}{item['price']:>10.2f}")

print()

choice = int(input("Choose an item (1-3): "))

if 1 <= choice <= len(menu):
    selected_item = menu[choice - 1]
    print(f"You selected: {selected_item['name']} (€{selected_item['price']:.2f})")
else:
    print("Error: Invalid menu choice.")
