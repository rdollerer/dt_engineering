import os
import requests

# API address and port
api_address = 'api'
api_port = 8000

def log_result(expected, actual):
    status = 'SUCCESS' if expected == actual else 'FAILURE'
    output = f"""
============================
    Authorization test
============================
expected result = {expected}
actual result = {actual}
==> {status}
"""
    print(output)
    if os.environ.get('LOG') == '1':
        with open('/logs/api_test.log', 'a') as file:
            file.write(output)

users = [{'username': 'alice', 'password': 'wonderland', 'v1_expected_status': 200, 'v2_expected_status': 200},
         {'username': 'bob', 'password': 'builder', 'v1_expected_status': 200, 'v2_expected_status': 403}]
    
for user in users:
    for version in ['v1', 'v2']:
        r = requests.get(url=f'http://{api_address}:{api_port}/{version}/sentiment',
                         params={'username': user['username'],
                                 'password': user['password'],
                                 'sentence': 'test'})
        expected_status = user[f'{version}_expected_status']
        log_result(expected_status, r.status_code)
