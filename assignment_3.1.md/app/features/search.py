def search_user_by_username(users):
    print("\n=== SEARCH USER ===")

    if len(users) == 0:
        print("No users registered")
        return

    search_name = input("Enter username to search: ")

    for user in users:
        if user["username"] == search_name:
            print("User found:")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"Age: {user['age']}")
            return

    print("User not found")
