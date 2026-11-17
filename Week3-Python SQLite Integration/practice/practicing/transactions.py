import sqlite3
connection=sqlite3.connect("library.db")
try:
    connection.execute("INSERT INTO books(title,author,price)  VALUES(?,?,?)",
                       ('Data Engineer','Omar',30.0))
    connection.execute("INSERT INTO books(title,author,price) VALUES(?,?,?) ",
                       ('Cloud Computing','Ahmad',-15.0))
    connection.commit()
except sqlite3.Error as error:
    connection.rollback()
    print("Transaction failed:", error)
finally:
    connection.close() 