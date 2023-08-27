import requests


API_URL = 'http://localhost:5000/users'

def create_user(user_data):
    response = requests.post(API_URL, json=user_data)
    return response