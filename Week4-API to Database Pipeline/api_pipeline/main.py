from extract import extract_users
from transform import transform_users
from database import load_users
data=extract_users()
if data is not None:
    cleaned_users=transform_users(data)
    load_users(cleaned_users)