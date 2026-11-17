import sqlite3

def add_book(title,author,price):
    connection=sqlite3.connect("library.db")
    connection.execute("INSERT INTO books(title,author,price) VALUES(?,?,?)",
                       (title,author,price))
    connection.commit()
    connection.close()
def get_all_books():
    connection=sqlite3.connect("library.db")
    cursor=connection.execute("SELECT * FROM books")
    records=cursor.fetchall()
    for record in records:
        print(record)
    connection.close() 
def find_book(book_id):
    connection=sqlite3.connect("library.db")
    cursor=connection.execute("SELECT * FROM books WHERE book_id=?",
                              (book_id,))   
    record=cursor.fetchone()
    if record is not None:
        print(record)
    else:
        print("Book not found!")
    connection.close()        
def update_book(book_id,new_price):
    connection=sqlite3.connect("library.db")
    cursor=connection.execute("UPDATE books SET price=? WHERE book_id=?",
                       (new_price,book_id))
    updated=cursor.rowcount
    connection.commit()
    connection.close()
    if updated > 0:
        return True
    else:
        return False
def delete_book(book_id):
    connection=sqlite3.connect("library.db")
    cursor=connection.execute("DELETE FROM books WHERE book_id=?",
                       (book_id,))
    deleted=cursor.rowcount
    connection.commit()
    connection.close()
    if deleted > 0:
        return True
    else:
        return False