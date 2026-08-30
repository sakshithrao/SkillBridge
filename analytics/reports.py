def generate_report():
    print("\n===== TRAINER REPORT =====")
    print("1. Student Report")
    print("2. Course Report")
    print("3. Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nStudent Report")
        print("No student data available.")

    elif choice == "2":
        print("\nCourse Report")
        print("No course data available.")

    elif choice == "3":
        return

    else:
        print("Invalid choice!")