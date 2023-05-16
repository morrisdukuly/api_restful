from config import db

class Payment (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float, nullable = False)
    payment_mode = db.Column(db.String(12), nullable =  False)

    ## OneToMany de Order vers payment
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = False)
    order = db.relationship('Order', foreign_keys = [orderId])

    ## Methode pour rendre la classe Mere(Heritage)
    _mapper_args_ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': 'payment_mode'
    }
