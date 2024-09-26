#!/usr/bin/python3


"""
This script takes your GitHub credentials (username
and password) and uses the GitHub API to display your id.
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
