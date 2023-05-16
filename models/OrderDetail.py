from config import db

class OrderDetail (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    qty = db.Column(db.Integer, nullable = False)
    taxStatus = db.Column(db.String(120), nullable = False)

    ## OneToMany de Item vers OrderDetail
    itemId = db.Column(db.Integer, db.ForeignKey('item.id'), nullable = True)
    item = db.relationship('Item', foreign_keys = [itemId])

    ## OneToMany de Order vers OrderDetail
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])
