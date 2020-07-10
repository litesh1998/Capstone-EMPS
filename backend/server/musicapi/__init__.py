'''
This is the MusicAPI.

This contains the API configurations and Database connections
'''
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__, static_url_path='', static_folder='../static')
app.config.from_pyfile('config.cfg')

db = MongoEngine(app)

# from musicapi.dbutils import scanAndUpdateDB
# scanAndUpdateDB()

from musicapi import routes