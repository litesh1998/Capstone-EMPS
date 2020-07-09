import mongoengine as mongo

db = mongo.connect(db='musicapi')



class User(mongo.Document):
    username = mongo.fields.StringField(required=True, unique=True, min_length=3, max_length=12)
    password = mongo.fields.StringField(required=True, min_length=5)

    meta = {
        'collection': 'users',
        'indexes': ['username']
    }

class Song(mongo.Document):
    name = mongo.fields.StringField(required=True)
    emotion = mongo.fields.StringField(default='Neutral', max_length=20)
    path = mongo.fields.StringField(required=True, unique=True)

    meta = {
        'collection': 'songs',
        'indexes': ['emotion']
    }

class PlayList(mongo.Document):
    name = mongo.fields.StringField(required=True, unique=True)
    song_list = mongo.fields.ListField(mongo.ReferenceField(Song))

    meta = {
        'collection': 'playlists',
        'indexes': ['name']
    }
