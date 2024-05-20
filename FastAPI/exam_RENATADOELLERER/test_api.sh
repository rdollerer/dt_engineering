#!/bin/bash

# Check if the API is alive
curl -X 'GET' \
  'http://127.0.0.1:8000/alive' \
  -H 'accept: application/json'

# Get questions with specific parameters
curl -X 'GET' \
  'http://127.0.0.1:8000/questions?use=Validation%20test&subjects=Classification&subjects=Automation&nr_questions=10' \
  -H 'accept: application/json' \
  -u 'alice:wonderland' 

# Post a new question
curl -X 'POST' \
  'http://127.0.0.1:8000/questions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -u 'admin:4dm1N' \
  -d '{
  "question": "is the sky blue?",
  "subject": "misc",
  "correct": "A",
  "use": "misc",
  "responseA": "yes",
  "responseB": "no"
}'
