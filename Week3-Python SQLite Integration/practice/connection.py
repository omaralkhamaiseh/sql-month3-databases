import sqlite3 
connection = sqlite3.connect("students.db")
connection.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id Integer PRIMARY KEY,
            name TEXT NOT NULL,
            age Integer
        )
                   """)
print("Table created successfully!")
# connection.execute("INSERT INTO students (name,age) VALUES(?,?)",
#                    ("Omar",20))
# connection.commit()
# cursor = connection.execute(
#     "SELECT * FROM students ORDER BY id "
#     )

# first_student=cursor.fetchone()
# print("First student:", first_student)
# remaining_students=cursor.fetchall()
# print("Remaining students:", remaining_students)
try:
    connection.execute(
        "UPDATE students SET age=? WHERE id=?",
        (25, 1)
    )

    connection.rollback()
    print("Changes canceled!")

except sqlite3.Error as error:
    connection.rollback()
    print("Database error:", error)
connection.close()