#!/bin/bash

# Check if the API is alive
curl -X 'GET' \
  'http://127.0.0.1:8000/alive' \
  -H 'accept: application/json'

# Get questions with specific parameters
curl -X 'GET' \
  'http://127.0.0.1:8000/questions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -u 'alice:wonderland' \
  -d '{
  "subjects": [
    "Classification",
    "Distributed systems",
    "Automation"
  ],
  "use": "Validation test",
  "nr_questions": 5
}'

# Post a new question
curl -X 'POST' \
  'http://127.0.0.1:8000/questions' \
  -H 'accept: application/json' \
  -H 'admin-password: 4dm1N' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "What color is the sky?",
  "subject": "misc",
  "correct": [
    "A"
  ],
  "use": "misc",
  "answerA": "blue",
  "answerB": "yellow",
  "answerC": "green"
}'
