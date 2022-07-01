from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
ws = SocketIO(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
CORS(app, resources={r'/*': {'origins': '*'}})
