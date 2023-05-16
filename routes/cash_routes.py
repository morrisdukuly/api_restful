from app import app
from config import db
from models.Cash import Cash
from flask import Flask, request, jsonify

from flask import Blueprint
cash_bp = Blueprint('cash', __name__)

#---------------------------------------------------------------------------------------------------------
#======================================================CASH===============================================
#---------------------------------------------------------------------------------------------------------


#======================================================POST===============================================

#Methode d'ajout cash

@app.route('/Cash/add', methods = ['POST'])
def cash_add():
    try:
        json = request.json
        print(json)
        cashTendered = json['cashTendered']
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if cashTendered and request.method == 'POST':
           
            print("******************")
           
            cashs = Cash(cashTendered = cashTendered, amount = amount, payment_mode = payment_mode, orderId = orderId)
            
            db.session.add(cashs)
            db.session.commit()
            resultat = jsonify('New Cash add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400,"message" : "Error" }
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#======================================================GET===============================================

#Methode GET pour Cash

@app.route('/cash', methods = ['GET'])
def get_cashs():
    try:
        cashsx = Cash.query.all()
        data = [
                {
                    "id":cashs.id, 
                    "cashTendered":cashs.cashTendered
                } 
                for cashs in cashsx
                ]

        resultat = jsonify({"status_code":200, "Cash" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

#====================================================== UPDATE ===============================================


@app.route('/cash/update', methods = ['POST', 'GET'])
def cash_update():
    try:
        data = request.json
        id = data["id"]
        cashTendered = data['cashTendered']
        amount = data['amount']
        payment_mode = data['payment_mode']
        orderId = data['orderId']

        cashs = Cash.query.filter_by(id=id).first()
        
        if id and cashTendered and amount and payment_mode and orderId and request.method == 'POST':

            cashs.cashTendered = cashTendered
            cashs.amount = amount
            cashs.payment_mode = payment_mode
            cashs.orderId = orderId
            db.session.commit()
            resultat = jsonify('Cash is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== DELETE ===============================================

###DELETE de cash
@app.route('/cash/delete', methods = ['POST'])
def delete_cash():
    try:
        json = request.json
        id = json['id']

        cash = Cash.query.filter_by(id=id).first()

        db.session.delete(cash)
        db.session.commit()
        resultat = jsonify('Cash is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
