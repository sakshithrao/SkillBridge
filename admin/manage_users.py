from utils.file_handler import read_data, write_data


def manage_users():
    while True:
        users = read_data("data/users.json")

        print("\n===== MANAGE USERS =====")
        print("1. View Users")
        print("2. Delete User")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            if len(users) == 0:
                print("No users found.")
            else:
                for user in users:
                    print(
                        "ID:", user["id"],
                        "| Name:", user["name"],
                        "| Email:", user["email"],
                        "| Role:", user["role"]
                    )

        elif choice == "2":
            user_id = int(input("Enter user ID to delete: "))

            found = False

            for user in users:
                if user["id"] == user_id:
                    users.remove(user)
                    found = True
                    break

            if found:
                write_data("data/users.json", users)
                print("User deleted successfully.")
            else:
                print("User not found.")

        elif choice == "3":
            break

        else:
            print("Invalid choice.")