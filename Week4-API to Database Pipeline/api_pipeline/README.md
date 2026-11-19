
# API-to-SQLite ETL Pipeline

## Project Description
This project is part of Month 3, Week 4 of my AI/DevOps (MLOps) Engineering learning roadmap.

It is a Python ETL pipeline that extracts user data from a public REST API, transforms and validates the data, and loads it into an SQLite database.

## Features
- Extracts user data from the JSONPlaceholder API
- Cleans names and email addresses
- Validates user IDs, names, and emails
- Stores valid users in an SQLite database
- Uses UPSERT to prevent duplicate records and update existing users
- Handles API and database errors
- Uses logging to track database operations

## Technologies Used
- Python
- SQLite
- Requests
- REST APIs
- SQL
- Logging

## Project Structure
- `main.py` - Runs the complete ETL pipeline
- `extract.py` - Retrieves users from the API
- `transform.py` - Cleans and validates user data
- `database.py` - Saves users into SQLite using UPSERT
- `test_transform.py` - Tests the data validation logic
- `README.md` - Project documentation

## How to Run

1. Install Python.
2. Install the Requests library:

```bash
pip install requests
```

3. Open a terminal inside the `api_pipeline` folder.
4. Run the pipeline:

```bash
python main.py
```

The application creates `user.db` and stores the validated users.

## Testing

Run the transformation test:

```bash
python test_transform.py
```

The test checks whether invalid user records are rejected.

## What I Learned
Through this project, I practiced:
- Building a modular ETL pipeline
- Integrating REST APIs with SQLite
- Cleaning and validating JSON data
- Using SQL UPSERT to handle duplicates
- Implementing logging and error handling
- Organizing a Python project for GitHub

## Future Improvements
- Add automated unit tests
- Add retry logic for failed API requests
- Support additional API endpoints
- Schedule automatic data updates
