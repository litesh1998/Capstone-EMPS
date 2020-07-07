'''
This file provides query-endpoints for other applications to send their
request.

MAIN REQUEST HADNLING LOGIC
'''

# IMPORTS
from musicapi import app
from flask import request, jsonify, make_response


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        req = request.args
        #LOGIC HERE
        print("\nRequeted data: ", req)
        response = {
            "msg": "OK",
            "as": "POST"
        }
        # RETURN RESPONSE
        return make_response(response)
    if request.method == 'GET':
        req = request.args
        # LOGIC HERE
        print(req)
        response = {
            "msg": "OK",
            "as": "GET"
        }
        # RETURN RESPONSE
        return make_response(response)
