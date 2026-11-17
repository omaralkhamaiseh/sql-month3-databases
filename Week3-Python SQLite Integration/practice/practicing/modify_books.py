import sqlite3
connection=sqlite3.connect("library.db")
connection.execute("UPDATE books SET price=? WHERE book_id=?",
                   (18,1))
connection.execute("DELETE FROM books WHERE book_id=?",
                   (3,))
connection.commit()
cursor=connection.execute("SELECT * FROM books")
records=cursor.fetchall()
for record in records:
    print(record)