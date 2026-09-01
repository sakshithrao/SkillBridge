from utils.file_handler import read_data


def view_my_courses():
    courses = read_data("data/courses.json")

    print("\n===== MY COURSES =====")

    if len(courses) == 0:
        print("No courses found.")
        return

    for course in courses:
        print(
            "ID:", course["id"],
            "| Name:", course["name"],
            "| Duration:", course["duration"]
        )