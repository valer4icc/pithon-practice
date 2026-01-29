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
user_category = input("Enter item category: ")
if user_category in categories:
    print("Category accepted.")
else:
    print("Error: Category not supported.")
