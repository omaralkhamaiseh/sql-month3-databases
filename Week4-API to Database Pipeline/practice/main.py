from extract import extract_users
from transform import transform_users
from load import load_users
data=extract_users()
cleaned_users=transform_users(data)
load_users(cleaned_users)
print(len(cleaned_users))
print(len(data))