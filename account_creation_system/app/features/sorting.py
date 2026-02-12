from app.reports.tables import show_users_table

def show_users_sorted_by_age(users):
    print("\n=== USERS SORTED BY AGE ===")

    if len(users) == 0:
        print("No users registered.")
        return

    sorted_users = sorted(users, key=lambda user: user["age"])
    show_users_table(sorted_users)
