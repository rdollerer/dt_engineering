from fastapi import FastAPI, HTTPException, Depends, Header, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List, Optional, Any
import pandas as pd
import random

api = FastAPI()
security = HTTPBasic()

df = pd.read_excel('questions_en.xlsx')

# Users dictionary provided 
users = {
    'alice': 'wonderland',
    'bob': 'builder',
    'clementine': 'mandarine',
    'admin': '4dm1N'
}

# Question Object - copies the structure of the file / DataFrame
class Question(BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    responseA: str
    responseB: str
    responseC: Optional[Any] = None
    responseD: Optional[Any] = None

# This function is used to authenticate the users for the get_questions
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_password = users.get(credentials.username)

    if correct_password is None or correct_password != credentials.password:
        raise HTTPException(status_code = 401, detail = 'Incorrect username or password')
    return credentials.username

# I created this function because I wanted the logic with the admin password to be a little bit cleaner 
def is_admin(user):
    return user == 'admin'

@api.get('/alive', name = 'Am I alive?')
def alive():
    """ 
        Enpoint to check if API is functional.
        No parameters required.  
    """
    return {'status': 'API is functional'}


@api.get('/questions', name = 'Get Questions', response_model = List[Question])
def get_questions(
    use: str = Query(...),
    subjects: List[str] = Query(...),
    nr_questions: int = Query(...),
    username: str = Depends(authenticate)
):
    """
        Please inform:

            1 use
            1 or more subjects
            number of questions: 5, 10 or 20
    """
    if nr_questions not in [5, 10, 20]:
        raise HTTPException(status_code = 400, detail = 'Nr questions must be 5, 10, or 20')
    
    filtered_df = df[(df['use'] == use) & (df['subject'].isin(subjects))]
    if filtered_df.empty:
        raise HTTPException(status_code = 404, detail = 'No questions found for the specified criteria')
    
    sampled_df = filtered_df.sample(n = min(nr_questions, len(filtered_df)))
    questions = sampled_df.to_dict(orient = 'records')
    return questions


@api.post('/questions', name = 'New Question', response_model = Question)
def create_question(question: Question, username: str = Depends(authenticate)):
    """
        If you are the admin, you can add new questions
    """
    if not is_admin(username):
        raise HTTPException(status_code = 401, detail = 'Unauthorized')
    
    global df
    df.loc[len(df.index)] = {
        'question': question.question,
        'subject': question.subject,
        'correct': question.correct,
        'use': question.use,
        'responseA': question.responseA,
        'responseB': question.responseB,
        'responseC': question.responseC,
        'responseD': question.responseD
    }
    return question

