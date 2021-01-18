from flask import Flask
from flask_sqlalchemy import SQLAlchemy
appInstance = Flask(__name__)
appInstance.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
appInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(appInstance)

import app.views
