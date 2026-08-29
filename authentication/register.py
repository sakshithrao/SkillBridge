from utils.file_handler import read_data, write_data
from utils.validators import is_valid_email, is_valid_password


def register_user():
    users = read_data("data/users.json")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    role = input("Enter your role (student/trainer): ").strip().lower()

    if name == "":
        print("Name cannot be empty.")
        return

    if not is_valid_email(email):
        print("Invalid email.")
        return

    if not is_valid_password(password):
        print("Password must contain at least 6 characters.")
        return

    if role not in ["student", "trainer"]:
        print("Invalid role.")
        return

    for user in users:
        if user["email"] == email:
            print("Email already registered.")
            return

    user_id = len(users) + 1

    new_user = {
        "id": user_id,
        "name": name,
        "email": email,
        "password": password,
        "role": role
    }

    users.append(new_user)

    write_data("data/users.json", users)

    print("Registration successful.")