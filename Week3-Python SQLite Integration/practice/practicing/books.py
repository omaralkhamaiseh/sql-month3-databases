import sqlite3
connection=sqlite3.connect("library.db")
connection.execute("""
                   CREATE TABLE IF NOT EXISTS books(
                       book_id Integer PRIMARY KEY,
                       title TEXT NOT NULL,
                       author TEXT NOT NULL,
                       price REAL CHECK(price > 0)
                   )
                   """)
# print("Table created successfully!")
# connection.executemany("Insert INTO books (title,author,price) VALUES(?,?,?)",
#                    [
#                    ('Python Basics','Ahmad',15.5),
#                    ('SQL Mastery','Omar',20.0),
#                    ('AI Fundamentals','Sara',35.0)
#                    ]
#                    )
# connection.commit()
# print("books inserted successfully!")

connection.close()