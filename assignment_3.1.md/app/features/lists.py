from app.core.models import is_adult
from app.reports.tables import show_users_table

def show_usernames(users):
    print("\n=== USERNAMES ===")
    if len(users) == 0:
        print("No users registered")
        return
    for user in users:
        print(user["username"])

def show_adults(users):
    print("\n=== ADULT USERS ===")
    if len(users) == 0:
        print("No users registered.")
        return
    adults = list(filter(is_adult, users))
    if len(adults) == 0:
        print("No adult users found.")
        return
    show_users_table(adults)

def show_emails(users):
    print("\n=== USER EMAILS ===")
    if len(users) == 0:
        print("No users registered.")
        return
    for user in users:
        print(user["email"])
