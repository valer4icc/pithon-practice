from app.runtime.runner import start
from app.storage.json_store import load_users

def main():
    users = load_users()
    start(users)

if __name__ == "__main__":
    main()
