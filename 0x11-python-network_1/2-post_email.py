#!/usr/bin/python3
"""
This module takes in a URL and email sends a POST
request and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
