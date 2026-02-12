def search_user_by_username(users):
    print("\n=== SEARCH USER ===")

    if len(users) == 0:
        print("No users registered")
        return

    search_name = input("Enter username to search: ")

    found = False

    for user in users:
        if user["username"] != search_name:
            continue

        print("User found:")
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"Age: {user['age']}")
        found = True
        break

    if not found:
        print("User not found")
