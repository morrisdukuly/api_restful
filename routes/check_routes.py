from app import app
from config import db
from models.Check import Check
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
check_bp = Blueprint('check', __name__)




#---------------------------------------------------------------------------------------------------------
#======================================================CHECK===============================================
#---------------------------------------------------------------------------------------------------------



#======================================================POST===============================================


#Methode d'ajout check

@app.route('/check/add', methods = ['POST'])
def check_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        bankID = json['bankID']
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if name and bankID and request.method == 'POST':
           
            print("******************")
            
            checks = Check(name = name, bankID = bankID, amount = amount, payment_mode = payment_mode, orderId = orderId)

            db.session.add(checks)
            db.session.commit()
            resultat = jsonify('New Check add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour Check

@app.route('/check', methods = ['GET'])
def get_checks():
    try:
        checksx = Check.query.all()
        data = [
                {
                    "id":checks.id, 
                    "name":checks.name, 
                    "bankID":checks.bankID 
                } 
                for checks in checksx
                ]

        resultat = jsonify({"status_code":200, "Check" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== UPDATE ===============================================


@app.route('/check/update', methods = ['POST', 'GET'])
def check_update():
    try:
        data = request.json
        id = data["id"]
        name = data['name']
        bankID = data['bankID']
        amount = data['amount']
        payment_mode = data['payment_mode']
        orderId = data['orderId']

        checks = Check.query.filter_by(id=id).first()
        
        if id and name and bankID and amount and payment_mode and orderId and request.method == 'POST':

            checks.name = name
            checks.bankID = bankID
            checks.amount = amount
            checks.payment_mode = payment_mode
            checks.orderId = orderId
            db.session.commit()
            resultat = jsonify('Check is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== DELETE ===============================================


###DELETE de check
@app.route('/check/delete', methods = ['POST'])
def delete_check():
    try:
        json = request.json
        id = json['id']

        check = Check.query.filter_by(id=id).first()

        db.session.delete(check)
        db.session.commit()
        resultat = jsonify('Check is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
