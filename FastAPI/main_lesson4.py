from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

api = FastAPI(
    title="My API",
    description="My own API powered by FastAPI.",
    version="1.0.1")

class Computer(BaseModel):
    """
        a computer that is available in the store
    """
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float

@api.get('/')
def get_index():
    """Returns a random greeting message
    """
    return {'greetings': 'welcome'}

@api.get('/', name="Hello World")
def get_index():
    """Returns greetings
    """
    return {'greetings': 'welcome'}

class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None

@api.get('/typed')
def get_typed(argument1: int):
    return {
        'data': argument1 + 1
    }

@api.get('/addition')
def get_addition(a: int, b: Optional[int]=None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }

@api.post('/item')
def post_item(item: Item):
    return item


@api.put('/computer', name='Create a new computer')
def get_computer(computer: Computer):
    """Creates a new computer within the database
    """
    return computer

@api.get('/custom', name='Get custom header')
def get_content(custom_header: Optional[str] = Header(None, description='My own personal header')):
    return {
        'Custom-Header': custom_header
    }