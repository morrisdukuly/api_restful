from config import db
from models.Payment import Payment

class Check (Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    name = db.Column(db.String(120), nullable = False)
    bankID = db.Column(db.String(120), nullable = False)
    
    _mapper_args_ = {
        'polymorphic_identity' : 'check'
    }
