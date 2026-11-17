import sqlite3
connection=sqlite3.connect("library.db")
# cursor=connection.execute("SELECT * FROM books")
# records=cursor.fetchall()
# for record in records:
#     print(record)
#------------------------
# cursor=connection.execute("SELECT * FROM books WHERE book_id=?",
#                           (2,))
# record=cursor.fetchone()
# print(record)
# cursor=connection.execute("SELECT * FROM books WHERE price>?",
#                            (18,))
# records=cursor.fetchall()
# for record in records:
#     print(record)