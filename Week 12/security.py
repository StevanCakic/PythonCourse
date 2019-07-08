from user import User
from werkzeug.security import safe_str_cmp

'''
users = [
    {   
        "id": 1,
        "username": "marko",
        "password": "abc123"
    }
]

username_mapping = { 
    "marko": {
        "id": 1,
        "username": "marko",
        "password": "abc123"
    }
}

userid_mapping = {
    1: {
        "id": 1,
        "username": "marko",
        "password": "abc123"
    }
}'''

users = [
    User(1, "marko", "abc123")
]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# Zasto ovo radimo mapiranje?

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password): # sigurniji nacin za provjeru stringova
        return user

def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)

