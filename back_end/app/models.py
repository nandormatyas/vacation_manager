from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    googleId = db.Column(db.String(128))
    role = db.Column(db.Integer, default=10)
    vacations = db.relationship('Vacation', backref='owner', lazy='dynamic')

class Vacation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromDate = db.Column(db.String(64))
    toDate = db.Column(db.String(64))
    status = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
