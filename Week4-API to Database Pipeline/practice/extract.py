import requests
def extract_users():
    url="https://jsonplaceholder.typicode.com/users"
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    data=response.json()
    return data

