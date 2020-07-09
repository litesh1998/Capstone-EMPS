'''
Caller Module that makes a call to server.

Before running this module, run the localhost server first.

Move to the server folder and use command:
    -> python run.py

This will start the local server.

Now Run this file in a new shell
'''

import requests as req

URL = "http://localhost:5000/api/happy"

response = None

try:
    print("\nRequesting Song! Waiting for response...")
    response = req.get(URL, stream=True)
except Exception as e:
    print("\nCould not establish connection!")


if response and response.status_code == 200:
    print("Response recieved with status: ", response.status_code)
    print("Response is:", response)
else:
    print("\nNo Response!\n")
