from config import db
from models.Payment import Payment

class WireTransfer (Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    bankID = db.Column(db.String(120), nullable = False)
    bankName = db.Column(db.String(120), nullable = False)

    _mapper_args_ = {
        'polymorphic_identity' : 'wireTransfer'
    }
