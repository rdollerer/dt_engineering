import os
import requests

# API address and port
api_address = 'api'
api_port = 8000

def log_result(expected, actual):
    status = 'SUCCESS' if expected == actual else 'FAILURE'
    output = f"""
============================
    Authentication test
============================
expected result = {expected}
actual result = {actual}
==> {status}
"""
    print(output)
    if os.environ.get('LOG') == '1':
        with open('/logs/api_test.log', 'a') as file:
            file.write(output)

users = [{'username': 'alice', 'password': 'wonderland', 'expected_status': 200},
         {'username': 'bob', 'password': 'builder', 'expected_status': 200},
         {'username': 'clementine', 'password': 'mandarine', 'expected_status': 403}]

for user in users :
    print(f'http://{api_address}:{api_port}/permissions')
    print({'username': user['username'],'password': user['password']})
    r = requests.get(url=f'http://{api_address}:{api_port}/permissions',
                     params={'username': user['username'],'password': user['password']})
    log_result(user['expected_status'], r.status_code)

