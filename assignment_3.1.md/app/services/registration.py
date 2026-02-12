from app.core.validators import validate_age, validate_password, validate_terms

def get_user_input():
    print("Welcome to the User Registration System v2")
    print("Follow the steps below to create your account.")

    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    age = int(input("Enter your age: "))
    terms_input = input("Do you accept the terms? (yes/no): ")

    return username, email, password, age, terms_input


def register_user():
    username, email, password, age, terms_input = get_user_input()

    if not validate_age(age):
        print("Error: You must be at least 18 years old.")
        return None
    elif not validate_password(password):
        print("Error: Password must be at least 8 characters long.")
        return None
    elif not validate_terms(terms_input):
        print("Error: You must accept the terms and conditions.")
        return None
    else:
        print("Registration successful")
        return {"username": username, "email": email, "age": age}
