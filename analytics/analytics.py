def show_analytics():
    print("\n===== TRAINER ANALYTICS =====")

    print("1. Total Students")
    print("2. Course Performance")
    print("3. Student Attendance")
    print("4. Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nTotal Students: 0")

    elif choice == "2":
        print("\nCourse Performance")
        print("Python: No data available")

    elif choice == "3":
        print("\nStudent Attendance")
        print("No attendance data available")

    elif choice == "4":
        return

    else:
        print("Invalid choice!")