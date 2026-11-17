import sqlite3
connection=sqlite3.connect("library.db")
def add_book(title,author,price):
    connection.execute("INSERT INTO books(title,author,price) VALUES(?,?,?)",
                       (title,author,price))
    connection.commit()
def get_all_books():
    cursor=connection.execute("SELECT * FROM books")
    records=cursor.fetchall()
    for record in records:
        print(record)
def find_book(book_id):
        cursor=connection.execute("SELECT * FROM books Where book_id=?",
                                (book_id,))
        record=cursor.fetchone()
        if record is not None:
            print(record)
        else:
            print("Book not found!")            
find_book(2)
find_book(99)

connection.close()