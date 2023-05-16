from app import app
from config import db
from models import WireTransfer
from models.WireTransfer import WireTransfer

from flask import Flask, request, jsonify, render_template

from flask import Blueprint
wireTransfer_bp = Blueprint('wireTransfer', __name__)

#---------------------------------------------------------------------------------------------------------
#======================================================WIRE TRANSFER===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout wireTransfer

@app.route('/wiretransfer/add', methods = ['POST'])
def wiretransfer_add():
    try:
        json = request.json
        print(json)
        bankID = json['bankID']
        bankName = json['bankName']
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if bankID and bankName and request.method == 'POST':
           
            print("******************")
            
            wiretransfer = WireTransfer(bankID = bankID, bankName = bankName, amount = amount, payment_mode = payment_mode, orderId = orderId)

            db.session.add(wiretransfer)
            db.session.commit()
            resultat = jsonify('New Wire Transfer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#======================================================GET===============================================

#Methode GET pour wireTransfer

@app.route('/wireTransfer', methods = ['GET'])
def get_wiretransfers():
    try:
        wiretransferx = WireTransfer.query.all()
        data = [
                {
                    "id":wireTransfer.id, 
                    "bankID":wireTransfer.bankID, 
                    "bankName":wireTransfer.bankName, 
                } 
                for wireTransfer in wiretransferx
                ]

        resultat = jsonify({"status_code":200, "Wire Transfer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()



#====================================================== UPDATE ===============================================


@app.route('/wiretransfer/update', methods = ['POST', 'GET'])
def wiretransfer_update():
    try:
        data = request.json
        id = data["id"]
        bankID = data['bankID']
        bankName = data['bankName']
        amount = data['amount']
        payment_mode = data['payment_mode']
        orderId = data['orderId']
        wiretransfer = WireTransfer.query.filter_by(id=id).first()
        
        if id and bankID and bankName and amount and payment_mode and orderId and request.method == 'POST':

            wiretransfer.bankID = bankID
            wiretransfer.bankName = bankName
            wiretransfer.amount = amount
            wiretransfer.payment_mode = payment_mode

            db.session.commit()
            resultat = jsonify('Wire Transfer is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()



#====================================================== DELETE ===============================================

###DELETE de wireTansfer
@app.route('/wireTansfer/delete', methods = ['POST'])
def delete_wire_transfer():
    try:
        json = request.json
        id = json['id']

        wire_transfer = WireTransfer.query.filter_by(id=id).first()

        db.session.delete(wire_transfer)
        db.session.commit()
        resultat = jsonify('WireTransfer is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


