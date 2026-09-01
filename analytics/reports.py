from utils.file_handler import read_data


def generate_report():
    students = read_data("data/students.json")
    courses = read_data("data/courses.json")

    print("\n===== REPORT =====")

    print("Student Report")
    print("Total Students:", len(students))

    print("\nCourse Report")
    print("Total Courses:", len(courses))