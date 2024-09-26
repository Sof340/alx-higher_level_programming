#!/usr/bin/python3

"""
this script takes 2 arguments in order to solve
the challenge.
"""


import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print("Failed to retrieve data")
