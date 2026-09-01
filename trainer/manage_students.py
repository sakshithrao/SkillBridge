import json

STUDENTS_FILE = "data/students.json"


def load_students():
    try:
        with open(STUDENTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(STUDENTS_FILE, "w") as file:
        json.dump(students, file, indent=4)


def manage_students():
    while True:
        print("\n--- Manage Students ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            course = input("Enter course name: ")

            students = load_students()

            student = {
                "id": len(students) + 1,
                "name": name,
                "email": email,
                "course": course
            }

            students.append(student)
            save_students(students)

            print("\nStudent added successfully!")
            print("Name:", name)
            print("Email:", email)
            print("Course:", course)

        elif choice == "2":
            students = load_students()

            print("\n--- Students ---")

            if not students:
                print("No students available.")
            else:
                for student in students:
                    print("\nID:", student["id"])
                    print("Name:", student["name"])
                    print("Email:", student["email"])
                    print("Course:", student["course"])

        elif choice == "3":
            return

        else:
            print("Invalid choice!")