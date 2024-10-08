#!/usr/bin/python3

"""
This module fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    body = response.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
