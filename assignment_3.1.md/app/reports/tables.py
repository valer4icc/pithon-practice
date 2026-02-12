from app.core.models import is_adult

def show_users_table(users):
    print("\n=== REGISTERED USERS ===")

    if len(users) == 0:
        print("No users registered")
        return

    print(f"{'Username':<15} {'Email':<25} {'Age':>5} {'Status':>8}")
    print("-" * 55)

    for user in users:
        status = "Adult" if is_adult(user) else "Minor"
        print(f"{user['username']:<15} {user['email']:<25} {user['age']:>5} {status:>8}")
