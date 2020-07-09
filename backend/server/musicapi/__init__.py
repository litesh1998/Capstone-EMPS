'''
This is the MusicAPI.

This contains the API configurations and Database connections
'''

from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='../static')

from musicapi import routes
