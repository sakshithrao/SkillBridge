def student_menu():
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. View Courses")
        print("2. Enroll Course")
        print("3. Placement")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            from student.view_courses import view_courses
            view_courses()

        elif choice == "2":
            from student.enroll_course import enroll_course
            enroll_course()

        elif choice == "3":
            from student.placement import placement
            placement()

        elif choice == "4":
            print("Exiting Student Menu...")
            break

        else:
            print("Invalid choice. Please try again.")