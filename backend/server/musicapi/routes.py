'''
This file provides query-endpoints for other applications to send their
request.

MAIN REQUEST HADNLING LOGIC
'''

# IMPORTS
import os
from musicapi import app
from .apiUtil import generate
from flask import request, jsonify, make_response, Response


@app.route('/', methods=['GET'])
def home():
    req = request.args
    # print(req)
    response = {
        "msg": "OK",
        "as": "GET"
    }
    # RETURN RESPONSE
    return make_response(response)


@app.route('/api/<emotion>', methods=['GET'])
def streamwav(emotion):
    cwd = os.getcwd()
    loc = os.path.join(cwd, 'musicapi', 'static', 'songs', emotion)
    content = os.listdir(loc)
    songName = content[0]
    songPath = os.path.join(loc, songName)
    return Response(generate(songPath), mimetype="audio/m4a", headers={"name": songName})

#
