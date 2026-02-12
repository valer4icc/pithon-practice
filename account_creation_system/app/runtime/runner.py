from app.cli.menu import show_menu
from app.cli.actions import get_actions

def start():
    users = []
    running = True
    actions = get_actions()

    while running:
        show_menu()
        choice = int(input("Choose an option (1-9): "))

        if choice == 10:
            print("Exiting program.")
            running = False
            continue

        action = actions.get(choice)

        if action is None:
            print("Invalid option. Please choose 1-9")
            continue

        if action.__name__ == "register_user":
            user = action()
            if user is not None:
                users.append(user)
        else:
            action(users)
