import sqlite3
def create_database():
    connection=sqlite3.connect("library.db")
    connection.execute("""
                    CREATE TABLE IF NOT EXISTS books(
                        book_id Integer PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        price REAL CHECK(price > 0)
                    )
                    """)
    connection.commit()
    connection.close()