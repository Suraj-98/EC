from wsgi import db
from uuid import uuid4

class students(db.Model):
    id = db.Column('studentid',db.Integer, primary_key=True, default=uuid4)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, default=uuid4)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    contact_number = db.Column(db.String(11))
    email = db.Column(db.String(100))
    password = db.Column(db.String(1000))

