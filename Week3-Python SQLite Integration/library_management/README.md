# Library Management System

A command-line Library Management System built with Python and SQLite as part of my AI/DevOps (MLOps) Engineering learning roadmap.

## Features

- Add new books to the database
- View all available books
- Search for books by ID
- Update book prices
- Delete books
- Handle invalid inputs and database errors
- Store data persistently using SQLite

## Technologies

- Python 3
- SQLite
- Python `sqlite3` library

## Project Structure

- `main.py` — Interactive command-line menu
- `books.py` — Book management functions
- `database.py` — Database initialization
- `library.db` — SQLite database

## How to Run

1. Install Python 3.
2. Open a terminal inside the `library_management` folder.
3. Run `python main.py`.
4. Select an option from the interactive menu.

SQLite support is included with standard Python installations.

## What I Learned

- Connecting Python applications to SQLite databases
- Implementing CRUD operations
- Writing parameterized SQL queries
- Using Python functions to organize database operations
- Handling exceptions and validating user inputs
- Working with commits, rollbacks, and database constraints

## Future Improvements

- Automated tests
- Better input validation
- More detailed book information
- Improved error handling and connection management
