from config import db

class OrderStatus (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    CREATE = db.Column(db.Integer)
    SHIPPING = db.Column(db.Integer, nullable = True)
    DELIVERED = db.Column(db.Integer, nullable = True)
    PAID = db.Column(db.Integer, nullable = True)
