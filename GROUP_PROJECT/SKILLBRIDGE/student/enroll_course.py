from utils.file_handler import read_data, write_data


def enroll_course():
    courses = read_data("data/courses.json")
    students = read_data("data/students.json")

    print("\n===== ENROLL COURSE =====")

    if len(courses) == 0:
        print("No courses available.")
        return

    print("Available Courses:")

    for course in courses:
        print(
            "ID:", course["id"],
            "| Name:", course["name"],
            "| Duration:", course["duration"]
        )

    course_id = int(input("Enter course ID to enroll: "))

    found = False

    for course in courses:
        if course["id"] == course_id:
            found = True

            name = input("Enter your name: ")
            email = input("Enter your email: ")

            student = {
                "id": len(students) + 1,
                "name": name,
                "email": email,
                "course": course["name"]
            }

            students.append(student)

            write_data("data/students.json", students)

            print("Course enrolled successfully.")
            break

    if not found:
        print("Course not found.")