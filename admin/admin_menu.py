from authentication.logout import logout_user
from admin.manage_users import manage_users
from admin.manage_courses import manage_courses
from admin.manage_trainers import manage_trainers


def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Manage Users")
        print("2. Manage Courses")
        print("3. Manage Trainers")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            manage_users()

        elif choice == "2":
            manage_courses()

        elif choice == "3":
            manage_trainers()
            
        elif choice == "4":
            logout_user()
            break

        else:
            print("Invalid choice. Please try again.")