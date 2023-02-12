from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=robohash&s={}'.format(
            digest, size)

class Content(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    body=db.Column(db.String)

    def __repr__(self):
        return '<Content {}'.format(self.topic)

class UserHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, primary_key=True)
    contentID = db.Column(db.Integer, primary_key=True)
    time_done = db.Column(db.DateTime)
    def __repr__(self): 
        return '<UserHistory {}'.format(self.username)


