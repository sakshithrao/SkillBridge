from authentication.login import login_user
from admin.admin_menu import admin_menu


user = login_user()

if user:
    if user["role"] == "admin":
        admin_menu()

    elif user["role"] == "trainer":
        print("Trainer menu will be added soon.")

    elif user["role"] == "student":
        print("Student menu will be added soon.")

    else:
        print("Invalid user role.")