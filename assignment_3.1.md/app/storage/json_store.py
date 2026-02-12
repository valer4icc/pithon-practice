import json

def save_users(users):
    with open("data/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

def load_users():
    with open("data/users.json", "r", encoding="utf-8") as file:
        return json.load(file)
