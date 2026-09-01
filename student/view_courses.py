from utils.file_handler import read_data


def view_courses():
    courses = read_data("data/courses.json")

    print("\n===== AVAILABLE COURSES =====")

    if not courses:
        print("No courses available.")
        return

    for course in courses:
        print("ID:", course["id"])
        print("Name:", course["name"].strip())
        print("Duration:", course["duration"])
        print("------------------------")