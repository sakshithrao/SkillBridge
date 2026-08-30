def manage_students():
    print("\n--- Manage Students ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        course = input("Enter course name: ")

        print("\nStudent added successfully!")
        print("Name:", name)
        print("Email:", email)
        print("Course:", course)

    elif choice == "2":
        print("\n--- Students ---")
        print("No students available.")

    elif choice == "3":
        return

    else:
        print("Invalid choice!")