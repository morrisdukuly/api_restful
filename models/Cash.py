from config import db
from models.Payment import Payment


class Cash (Payment):
    
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    cashTendered = db.Column(db.Float, nullable = False)


    _mapper_args_ = {
        'polymorphic_identity' : 'cash'
    }
