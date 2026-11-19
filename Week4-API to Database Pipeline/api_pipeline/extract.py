import requests
import logging
def extract_users():
    """Fetch user data from the API and return it."""
    try:
        url="https://jsonplaceholder.typicode.com/users"
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        data=response.json()
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None
