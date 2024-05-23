import os
import requests

# API address and port
api_address = 'api'
api_port = 8000

def log_result(expected, actual):
    if expected < 0 and actual < 0:
        status = 'SUCCESS'
        expected = '< 0'
    elif expected > 0 and actual > 0:
        status = 'SUCCESS'
        expected = '> 0'
    else:
        status = 'FAILURE'
    output = f"""
============================
    Content test
============================
expected result = {expected}
actual result = {actual}
==> {status}
"""
    print(output)
    if os.environ.get('LOG') == '1':
        with open('/logs/api_test.log', 'a') as file:
            file.write(output)

users = [{'username': 'alice', 'password': 'wonderland'}]

test_cases = [{'sentence': 'life is beautiful', 'expected_v1': 1, 'expected_v2': 1},
              {'sentence': 'that sucks', 'expected_v1': -1, 'expected_v2': -1}]

for user in users:
    for test_case in test_cases:
        for version in ['v1', 'v2']:
            r = requests.get(url=f'http://{api_address}:{api_port}/{version}/sentiment',
                             params={'username': user['username'],
                                     'password': user['password'],
                                     'sentence': test_case['sentence']})
            
            expected = test_case[f'expected_{version}']
            actual = r.json().get('score', 0)
            log_result(expected, actual)


