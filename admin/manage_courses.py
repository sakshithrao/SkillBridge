from utils.file_handler import read_data, write_data


def manage_courses():
    while True:
        courses = read_data("data/courses.json")

        print("\n===== MANAGE COURSES =====")
        print("1. View Courses")
        print("2. Add Course")
        print("3. Delete Course")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            if len(courses) == 0:
                print("No courses found.")
            else:
                for course in courses:
                    print(
                        "ID:", course["id"],
                        "| Name:", course["name"],
                        "| Duration:", course["duration"]
                    )

        elif choice == "2":
            name = input("Enter course name: ")
            duration = input("Enter course duration: ")

            course_id = len(courses) + 1

            new_course = {
                "id": course_id,
                "name": name,
                "duration": duration
            }

            courses.append(new_course)

            write_data("data/courses.json", courses)

            print("Course added successfully.")

        elif choice == "3":
            course_id = int(input("Enter course ID to delete: "))

            found = False

            for course in courses:
                if course["id"] == course_id:
                    courses.remove(course)
                    found = True
                    break

            if found:
                write_data("data/courses.json", courses)
                print("Course deleted successfully.")
            else:
                print("Course not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")