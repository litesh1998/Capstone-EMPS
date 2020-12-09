'''
This file provides query-endpoints for other applications to send their
request.

MAIN REQUEST HADNLING LOGIC
'''

# IMPORTS
import os
from flask import Response, make_response
from musicapi.apiUtil import generate, getSongsList, getSong
from musicapi import app

@app.route('/', methods=['GET'])
def home():
    # req = request.args
    # print(req)
    response = {
        "msg": "OK",
        "as": "GET"
    }
    # RETURN RESPONSE
    return make_response(response)


@app.route('/api/<emotion>', methods=['GET'])
def Emotion(emotion):
    song_list = getSongsList(emotion)
    
    return make_response(song_list)

@app.route('/song/<song_id>')
def SendSong(song_id):
    song = getSong(song_id)
    if song:
        # print(song.path)
        # return song
        return Response(generate(song.path), mimetype="audio/m4a", headers={"song": song})
    else:
        return Response("Song Not found", status=404)
