from utils.file_handler import read_data


def view_courses():
    courses = read_data("data/courses.json")

    print("\n===== AVAILABLE COURSES =====")

    if len(courses) == 0:
        print("No courses available.")
        return

    for course in courses:
        print(
            "ID:", course["id"],
            "| Name:", course["name"],
            "| Duration:", course["duration"]
        )