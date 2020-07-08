'''
This is the MusicAPI.

This contains the API configurations and Database connections
'''

from flask import Flask

app = Flask(__name__)

from musicapi import routes
