from student.view_courses import view_courses
from student.enroll_course import enroll_course
from student.placement import placement


def student_menu():
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. View Courses")
        print("2. Enroll Course")
        print("3. Placement Opportunities")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_courses()

        elif choice == "2":
            enroll_course()

        elif choice == "3":
            placement()

        elif choice == "4":
            print("Exiting Student Menu...")
            break

        else:
            print("Invalid choice. Please try again.")