categories = [
"Food & Groceries",
"Electronics",
"Clothing",
"Household items",
"Entertainment",
"Transportation",
"Health & Beauty",
"Other"
]
category = input("Enter item category: ")
if category in categories:
    print("Category accepted.")
else:
    print("Error: Category not supported.")

store_name = None
store_name = input("Enter store name: ")

if store_name is None or store_name == "":
    print("Error: Store name cannot be empty.")
else:
    if store_name is not None:
        print("Store name accepted.")
