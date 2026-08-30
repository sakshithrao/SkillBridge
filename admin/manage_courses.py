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

        # View Courses
        if choice == "1":
            if len(courses) == 0:
                print("No courses found.")
            else:
                print("\n===== AVAILABLE COURSES =====")

                for course in courses:
                    print(
                        "ID:", course["id"],
                        "| Name:", course["name"],
                        "| Duration:", course["duration"]
                    )

        # Add Course
        elif choice == "2":
            name = input("Enter course name: ")
            duration = input("Enter course duration: ")

            # Generate a unique course ID
            if len(courses) == 0:
                course_id = 1
            else:
                course_id = max(course["id"] for course in courses) + 1

            new_course = {
                "id": course_id,
                "name": name,
                "duration": duration
            }

            courses.append(new_course)

            write_data("data/courses.json", courses)

            print("Course added successfully.")

        # Delete Course
        elif choice == "3":
            if len(courses) == 0:
                print("No courses found.")
                continue

            try:
                course_id = int(input("Enter course ID to delete: "))
            except ValueError:
                print("Please enter a valid course ID.")
                continue

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

        # Back
        elif choice == "4":
            break

        # Invalid choice
        else:
            print("Invalid choice. Please try again.")