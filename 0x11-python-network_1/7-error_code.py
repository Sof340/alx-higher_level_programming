#!/usr/bin/python3

"""
This module takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
