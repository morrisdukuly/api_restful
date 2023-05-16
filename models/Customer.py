from config import db

class Customer (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    deliveryAddress = db.Column(db.String(120), nullable = False)
    contact = db.Column(db.String(120), nullable = True)
    active = db.Column(db.Boolean, nullable = False)
