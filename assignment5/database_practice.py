import os
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), 'practice.db')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, course_name TEXT, fees INTEGER)')

cur.execute("INSERT INTO students (name, age) VALUES ('Ravi', 20)")
cur.execute("INSERT INTO students (name, age) VALUES ('Sneha', 21)")
cur.execute("INSERT INTO courses (course_name, fees) VALUES ('Python', 5000)")
cur.execute("INSERT INTO courses (course_name, fees) VALUES ('SQL', 4000)")

print('All students:')
for row in cur.execute('SELECT * FROM students'):
    print(row)

print('Student names and age:')
for row in cur.execute('SELECT name, age FROM students'):
    print(row)

cur.execute("UPDATE students SET age = 22 WHERE name = 'Ravi'")
cur.execute("DELETE FROM courses WHERE course_name = 'SQL'")

print('After update:')
for row in cur.execute('SELECT * FROM students'):
    print(row)

print('Remaining courses:')
for row in cur.execute('SELECT * FROM courses'):
    print(row)

conn.commit()
conn.close()
