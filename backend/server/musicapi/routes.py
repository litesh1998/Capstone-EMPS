'''
This file provides query-endpoints for other applications to send their
request.

MAIN REQUEST HADNLING LOGIC
'''

# IMPORTS
import os
from musicapi import app
from flask import request, jsonify, make_response, Response


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


@app.route('/api/<emotion>', methods=['GET'])
def streamwav(emotion):
    cwd = os.getcwd()
    loc = os.path.join(cwd, 'musicapi', 'static', 'songs', emotion)
    content = os.listdir(loc)
    songName = content[0]
    songPath = os.path.join(loc, songName)
    # selectedSong = open(songPath, 'r')
    def generate():
        with open(songPath, "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/m4a")

# @app.route('/api/<emotion>', methods=['GET'])
# def Song(emotion):
#     cwd = os.getcwd()
#     # loc = f'/songs/{emotion}'
#     # loc = cwd + '\\musicapi\\static\\songs\\' + emotion
#     loc = os.path.join(cwd, 'musicapi', 'static', 'songs', emotion)
#     content = os.listdir(loc)
#     songName = content[0]
#     songPath = os.path.join(loc, songName)
#     selectedSong = open(songPath, 'r')
#     response = {
#         "media": selectedSong,
#         "as": "GET"
#     }
#     # RETURN RESPONSE
#     return make_response(response)
