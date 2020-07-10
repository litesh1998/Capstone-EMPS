from flask import Flask
from flask_mongoengine import MongoEngine
import sys, signal

app = Flask(__name__)

@app.teardown_appcontext
def handler(error):
    print('Terminating App')
    db.connection.close()
    print("Closing Connection")
    sys.exit(0)

app.config['MONGODB_HOST'] = 'mongodb+srv://dbUser:capstone123@cluster0.lcjsg.mongodb.net/songs?retryWrites=true&w=majority'

db = MongoEngine(app)
if db:
    print("Successfully connected to database!")

# signal.signal(signal.SIGINT, handler)
# signal.pause()

if __name__ == "__main__":
    app.run(debug=True)

