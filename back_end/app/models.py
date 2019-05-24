from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    googleId = db.Column(db.String(128))
    role = db.Column(db.Integer, default=10)

    def __init__(self, name, email, googleId):
        self.name = name
        self.email = email
        self.googleId = googleId

class Vacation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    fromDate = db.Column(db.String(64))
    toDate = db.Column(db.String(64))
    status = db.Column(db.Integer, default=0)

    def __init__(self, userId, fromDate, toDate):
        self.userId = userId
        self.fromDate = fromDate
        self.toDate = toDate
