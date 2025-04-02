from strike_app import db

class Striker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    strike = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Integer)