from transform import transform_users

test_list = [
    {"id": 1, "name": "Omar", "email": "omar@example.com"},
    {"id": -2, "name": "Ahmad", "email": "ahmad@example.com"},
    {"id": 3, "name": "", "email": "test@example.com"},
    {"id": 4, "name": "Sara", "email": ""}
]
result=transform_users(test_list)
print(result)
print(len(result))