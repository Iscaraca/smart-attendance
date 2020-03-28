from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    classno = db.Column(db.String(255), unique=True)
    attendanceTime = db.Column(db.String(255))

    def __init__(self, name, classno, attendanceTime):
        self.name = name
        self.classno = classno
        self.attendanceTime = attendanceTime

    def __repr__(self):
        return '<User %r>' % self.name

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(255))
    username = db.Column(db.String(255))

    def __init__(self, fullname, username):
        self.fullname = fullname
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username
