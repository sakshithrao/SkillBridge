from utils.file_handler import read_data, write_data


def manage_students():
    while True:
        students = read_data("data/students.json")

        print("\n===== MANAGE STUDENTS =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")

            if len(students) == 0:
                student_id = 1
            else:
                student_id = max(student["id"] for student in students) + 1

            new_student = {
                "id": student_id,
                "name": name,
                "email": email
            }

            students.append(new_student)

            write_data("data/students.json", students)

            print("Student added successfully.")

        elif choice == "2":
            if len(students) == 0:
                print("No students found.")
            else:
                print("\n===== STUDENTS =====")

                for student in students:
                    print(
                        "ID:", student["id"],
                        "| Name:", student["name"],
                        "| Email:", student["email"]
                    )

        elif choice == "3":
            break

        else:
            print("Invalid choice.")