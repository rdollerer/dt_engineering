from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

api = FastAPI(
    title='Users API'
)

class User(BaseModel):
    user_id: int
    name: str
    subscription: Optional[str] = None

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

@api.get('/')
def get_index():
    return {'msg': 'Welcome!'}

@api.get('/users/}')
def get_users():
    return users_db

@api.get('/users/userid/{userid:int}')
def get_one_user(userid):
    for user in users_db:
        if user['user_id'] == userid:
            return user
    return {}

@api.get('/users/userid/{userid:int}/name')
def get_one_name(userid):
    for user in users_db:
        if user['user_id'] == userid:
            return {'name': user['name']}
    return {}

@api.get('/users/userid/{userid:int}/subscription')
def get_one_subscription(userid):
    for user in users_db:
        if user['user_id'] == userid:
            return {'subscription': user['subscription']}
    return {}

@api.put('/users')
def put_user(userdata:User):
    users_db.append(userdata)
    return userdata

@api.post('/users/userid/{userid:int}')
def post_user(user: User, userid):
    try:
        old_user = list(
            filter(lambda x: x.get('user_id') == userid, users_db)
            )[0]
        users_db.remove(old_user)
        old_user['name'] = user.name
        old_user['subscription'] = user.subscription
        users_db.append(old_user)
        return old_user
    except IndexError:
        return {}
    

@api.delete('/users/{userid:int}')
def delete_users(userid):
    try:
        old_user = list(
            filter(lambda x: x.get('user_id') == userid, users_db)
            )[0]
        users_db.remove(old_user)
        return {
            'userid': userid,
            'deleted': True
            }
    except IndexError:
        return {}