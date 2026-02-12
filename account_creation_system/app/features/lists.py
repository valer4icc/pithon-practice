from app.core.models import is_adult

def show_usernames(users):
    print("\n=== USERNAMES ===")

    if len(users) == 0:
        print("No users registered")
        return

    usernames = [user["username"] for user in users]

    for name in usernames:
        print(name)


def show_adults(users):
    print("\n=== ADULT USERS ===")

    if len(users) == 0:
        print("No users registered.")
        return

    adults = list(filter(is_adult, users))

    if len(adults) == 0:
        print("No adult users found.")
        return

    from app.reports.tables import show_users_table
    show_users_table(adults)


def show_emails(users):
    print("\n=== USER EMAILS ===")

    if len(users) == 0:
        print("No users registered.")
        return

    emails = list(map(lambda user: user["email"], users))

    for email in emails:
        print(email)
