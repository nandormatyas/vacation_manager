from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    googleId = db.Column(db.String(128))
    googleAccessToken = db.Column(db.String(128))
    role = db.Column(db.Integer, default=10)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Vacation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    fromDate = db.Column(db.Date)
    toDate = db.Column(db.Date)
    status = db.Column(db.Integer, default=0)
