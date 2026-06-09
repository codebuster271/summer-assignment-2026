import sqlite3


def print_rows(title, rows):
    print(title)
    for row in rows:
        print(row)
    print()


connection = sqlite3.connect("assignment5_practice.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS enrollments")
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS courses")

cursor.execute(
    """
    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
    """
)

cursor.execute(
    """
    CREATE TABLE courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        fee INTEGER
    )
    """
)

cursor.execute(
    """
    CREATE TABLE enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
    """
)

students = [
    (1, "Aman", 20, "Jaipur"),
    (2, "Priya", 21, "Bhopal"),
    (3, "Rahul", 22, "Indore"),
]

courses = [
    (1, "Python", 5000),
    (2, "Data Science", 7000),
    (3, "Web Development", 6000),
]

enrollments = [
    (1, 1, 1, "A"),
    (2, 2, 2, "B"),
    (3, 3, 3, "A"),
]

cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students)
cursor.executemany("INSERT INTO courses VALUES (?, ?, ?)", courses)
cursor.executemany("INSERT INTO enrollments VALUES (?, ?, ?, ?)", enrollments)

connection.commit()

cursor.execute("UPDATE students SET city = ? WHERE student_id = ?", ("Udaipur", 2))
cursor.execute("UPDATE enrollments SET grade = ? WHERE enrollment_id = ?", ("A+", 2))
connection.commit()

cursor.execute("DELETE FROM enrollments WHERE enrollment_id = ?", (3,))
connection.commit()

all_students = cursor.execute("SELECT * FROM students").fetchall()
print_rows("All students:", all_students)

students_from_city = cursor.execute(
    "SELECT name, city FROM students WHERE city = ?",
    ("Udaipur",),
).fetchall()
print_rows("Students from Udaipur:", students_from_city)

ordered_courses = cursor.execute(
    "SELECT course_name, fee FROM courses ORDER BY fee DESC"
).fetchall()
print_rows("Courses ordered by fee:", ordered_courses)

distinct_cities = cursor.execute(
    "SELECT DISTINCT city FROM students"
).fetchall()
print_rows("Distinct cities:", distinct_cities)

join_result = cursor.execute(
    """
    SELECT students.name, courses.course_name, enrollments.grade
    FROM enrollments
    JOIN students ON enrollments.student_id = students.student_id
    JOIN courses ON enrollments.course_id = courses.course_id
    """
).fetchall()
print_rows("Student course details:", join_result)

grade_count = cursor.execute(
    "SELECT grade, COUNT(*) FROM enrollments GROUP BY grade"
).fetchall()
print_rows("Grade count:", grade_count)

connection.close()
