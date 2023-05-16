from config import db

class Order (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    createDate = db.Column(db.Date, nullable = False)

    ## OneToMany de Customer vers Order
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = True)
    customer = db.relationship('Customer', foreign_keys = [customerId])
