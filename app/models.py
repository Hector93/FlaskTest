from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    ghid = db.Column(db.Integer)
    image_url = db.Column(db.String)
    ghtype = db.Column(db.String)
    ghid = db.Column(db.Integer)
    link = db.Column(db.String)

    def __repr__(self):
        return '<user %r>' % self.id
