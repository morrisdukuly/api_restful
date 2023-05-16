from app import app
from config import db
from models.OrderStatus import OrderStatus
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
orderStatus_bp = Blueprint('orderStatus', __name__)


#---------------------------------------------------------------------------------------------------------
#======================================================ORDER STATUS===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout orderStatus

@app.route('/orderStatus/add', methods = ['POST'])
def orderstatus_add():
    try:
        json = request.json
        print(json)
        CREATE = json['CREATE']
        SHIPPING = json['SHIPPING']
        DELIVERED = json['DELIVERED']
        PAID = json['PAID']

        if CREATE and SHIPPING and DELIVERED and PAID and request.method == 'POST':
           
            print("******************")

            orderStatus = OrderStatus(CREATE = CREATE, SHIPPING = SHIPPING, DELIVERED = DELIVERED, PAID = PAID)

            db.session.add(orderStatus)
            db.session.commit()
            resultat = jsonify('Order Status add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour orderStatus

@app.route('/orderStatus', methods = ['GET'])
def get_orderstatus():
    try:
        orderstatusx = OrderStatus.query.all()
        data = [
                {
                    "id":orderStatus.id, 
                    "CREATE":orderStatus.CREATE, 
                    "SHIPPING":orderStatus.SHIPPING, 
                    "DELIVERED":orderStatus.DELIVERED, 
                    "PAID":orderStatus.PAID
                } 
                for orderStatus in orderstatusx
                ]

        resultat = jsonify({"status_code":200, "Order status" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== UPDATE ===============================================


@app.route('/order-status/update', methods = ['POST', 'GET'])
def orderstatus_update():
    try:
        data = request.json
        id = data["id"]
        CREATE = data['CREATE']
        SHIPPING = data['SHIPPING']
        DELIVERED = data['DELIVERED']
        PAID = data['PAID']

        orderstatus = OrderStatus.query.filter_by(id=id).first()
        
        if id and CREATE and SHIPPING and DELIVERED and PAID and request.method == 'POST':

            orderstatus.CREATE = CREATE
            orderstatus.SHIPPING = SHIPPING
            orderstatus.DELIVERED = DELIVERED
            orderstatus.PAID = PAID

            db.session.commit()
            resultat = jsonify('Order status is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()



#====================================================== DELETE ===============================================

###DELETE de orderStatus
@app.route('/orderStatus/delete', methods = ['POST'])
def delete_order_status():
    try:
        json = request.json
        id = json['id']

        order_status = OrderStatus.query.filter_by(id=id).first()

        db.session.delete(order_status)
        db.session.commit()
        resultat = jsonify('Order status is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()



