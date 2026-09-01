from utils.file_handler import read_data


def show_analytics():
    students = read_data("data/students.json")
    courses = read_data("data/courses.json")
    attendance = read_data("data/attendance.json")

    print("\n===== ANALYTICS =====")

    print("Total Students:", len(students))
    print("Total Courses:", len(courses))
    print("Total Attendance Records:", len(attendance))