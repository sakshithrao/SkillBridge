from utils.file_handler import read_data


def login_user():
    users = read_data("data/users.json")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful.")
            print("Welcome", user["name"])

            return user

    print("Invalid email or password.")
    return None