from config import db
from models.Payment import Payment

class Credit (Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    number = db.Column(db.String(120), nullable = False)
    types = db.Column(db.String(120), nullable = False)
    expireDate = db.Column(db.Date, nullable = False)

    _mapper_args_ = {
        'polymorphic_identity' : 'credit'
    }
