from authentication.login import login_user
from admin.admin_menu import admin_menu
from trainer.trainer_menu import trainer_menu
from student.student_menu import student_menu


print("Welcome to SkillBridge")

user = login_user()

if user:
    if user["role"] == "admin":
        admin_menu()

    elif user["role"] == "trainer":
        trainer_menu()

    elif user["role"] == "student":
        student_menu()

    else:
        print("Invalid user role.")