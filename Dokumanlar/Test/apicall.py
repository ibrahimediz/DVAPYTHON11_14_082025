import requests

def get_user_data(user_id):
    response = requests.get(fr"http://api.example.com/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None