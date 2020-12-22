"""
FLASK API:

This file in responsible to start the server

The main API is present inside the "musicapi" module
"""
from musicapi import app

if __name__ == '__main__':
    app.run()
