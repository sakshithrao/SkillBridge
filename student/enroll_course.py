from utils.file_handler import read_data, write_data


def enroll_course():
    courses = read_data("data/courses.json")
    students = read_data("data/students.json")

    print("\n===== ENROLL COURSE =====")

    if not courses:
        print("No courses available.")
        return

    print("\nAvailable Courses:")

    for course in courses:
        print(
            "ID:", course["id"],
            "| Name:", course["name"].strip(),
            "| Duration:", course["duration"]
        )

    try:
        course_id = int(input("Enter course ID to enroll: "))
    except ValueError:
        print("Invalid course ID.")
        return

    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    name = input("Enter your name: ")
    email = input("Enter your email: ")

    student = {
        "id": len(students) + 1,
        "name": name,
        "email": email,
        "course": selected_course["name"].strip()
    }

    students.append(student)

    write_data("data/students.json", students)

    print("\nCourse enrolled successfully.")
    print("Student:", name)
    print("Course:", selected_course["name"].strip())