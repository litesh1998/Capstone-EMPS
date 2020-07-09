from musicapi import db

# print(db)

class User(db.Document):
    username = db.StringField(required=True, unique=True, min_length=3, max_length=12)
    password = db.StringField(required=True, min_length=5)

    meta = {
        'collection': 'users',
        'indexes': ['username']
    }

class Song(db.Document):
    name = db.StringField(required=True)
    emotion = db.StringField(default='Neutral', max_length=20)
    path = db.StringField(required=True, unique=True)

    meta = {
        'collection': 'songs',
        'indexes': ['emotion']
    }

class PlayList(db.Document):
    name = db.StringField(required=True, unique=True)
    song_list = db.ListField(db.ReferenceField(Song))

    meta = {
        'collection': 'playlists',
        'indexes': ['name']
    }
