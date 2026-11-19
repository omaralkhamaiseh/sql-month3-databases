import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
def load_users(cleaned_users):
    logging.info("Database loading started")
    connection=sqlite3.connect("user.db")
    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
            )
                        """)
        user_records=[]
        
        for cleaned_user in cleaned_users:
            record=(cleaned_user['user_id'],cleaned_user['name'],cleaned_user['email'])
            user_records.append(record)
        length=len(user_records)
        logging.info(f"Prepared {length} users")
        connection.executemany("""INSERT INTO users(user_id,name,email) 
                            VALUES (?,?,?)
                            ON CONFLICT(user_id) 
                            DO UPDATE SET 
                            name=excluded.name,
                            email=excluded.email""",
                            user_records)
        connection.commit()
        logging.info(f"Successfully loaded {length} users")
    except sqlite3.Error as e:
        connection.rollback()
        logging.error(f"Database error: {e}")
    finally:
        connection.close()