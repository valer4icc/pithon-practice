students = []
student_index = {}


def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return round(sum(grades) / len(grades), 2)


def determine_status(avg):
    return "PASS" if avg >= 5 else "FAIL"



def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    if student_id in student_index:
        print("Student with this ID already exists.")
        return

    attended = int(input("Enter attended lectures: "))
    total = int(input("Enter total lectures: "))

    student = {
        "id": student_id,
        "name": name,
        "grades": [],
        "courses": set(),
        "attendance": (attended, total)
    }

    students.append(student)
    student_index[student_id] = student

    print("Student added successfully.")


def add_grade():
    student_id = input("Enter student ID: ")

    if student_id not in student_index:
        print("Student not found.")
        return

    grade = int(input("Enter grade: "))
    student_index[student_id]["grades"].append(grade)

    print("Grade added.")


def add_course():
    student_id = input("Enter student ID: ")

    if student_id not in student_index:
        print("Student not found.")
        return

    course = input("Enter course name: ")
    student_index[student_id]["courses"].add(course)

    print("Course added.")

def generate_student_report(student):
    avg = calculate_average(student["grades"])
    status = determine_status(avg)

    return {
        "id": student["id"],
        "name": student["name"],
        "average": avg,
        "status": status
    }


def show_all_reports():
    if len(students) == 0:
        print("No students available.")
        return

    print("\n=== STUDENT REPORTS ===")
    print(f"{'ID':<8}{'Name':<15}{'Average':<10}{'Status'}")
    print("-" * 40)

    for student in students:
        report = generate_student_report(student)
        print(f"{report['id']:<8}{report['name']:<15}{report['average']:<10}{report['status']}")


def show_course_statistics():
    if len(students) == 0:
        print("No students available.")
        return

    course_stats = {}

    for student in students:
        for course in student["courses"]:
            course_stats[course] = course_stats.get(course, 0) + 1

    print("\n=== COURSE STATISTICS ===")
    for course, count in course_stats.items():
        print(f"{course}: {count} student(s)")


def show_failing_students():
    failing = []

    for student in students:
        avg = calculate_average(student["grades"])
        if avg < 5:
            failing.append(student["id"])

    print("\n=== FAILING STUDENTS ===")

    if len(failing) == 0:
        print("No failing students.")
    else:
        for sid in failing:
            print(sid)


def show_extremes():
    if len(students) == 0:
        print("No students available.")
        return

    averages = [calculate_average(s["grades"]) for s in students]

    if len(averages) == 0:
        print("No grade data available.")
        return

    print("\n=== EXTREME VALUES ===")
    print("Highest average:", max(averages))
    print("Lowest average:", min(averages))

def print_menu():
    print("\n=== STUDENT SYSTEM MENU ===")
    print("1. Add student")
    print("2. Add grade")
    print("3. Add course")
    print("4. Show all reports")
    print("5. Show course statistics")
    print("6. Show failing students")
    print("7. Show highest/lowest averages")
    print("8. Exit")



running = True

while running:
    print_menu()
    choice = input("Choose an option (1-8): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_grade()

    elif choice == "3":
        add_course()

    elif choice == "4":
        show_all_reports()

    elif choice == "5":
        show_course_statistics()

    elif choice == "6":
        show_failing_students()

    elif choice == "7":
        show_extremes()

    elif choice == "8":
        print("Program closed.")
        running = False

    else:
        print("Invalid option.")
