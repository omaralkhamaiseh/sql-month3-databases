import sqlite3
connection=sqlite3.connect("library.db")
try:
    connection.execute(
    "INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
    ("Deep Learning", "Ahmad", 45.0)
    )
    connection.commit()
    print("Book added successfully!")
except sqlite3.Error as error:
    connection.rollback()
    print("Database error:",error)
finally:
    connection.close()