def trainer_menu():
    print("\n===== TRAINER MENU =====")
    print("1. Manage Students")
    print("2. Trainer Profile")
    print("3. View My Courses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        from trainer.manage_students import manage_students
        manage_students()

    elif choice == "2":
        from trainer.trainer_profile import trainer_profile
        trainer_profile()

    elif choice == "3":
        from trainer.view_my_courses import view_my_courses
        view_my_courses()

    elif choice == "4":
        print("Exiting Trainer Menu...")
        return

    else:
        print("Invalid choice!")