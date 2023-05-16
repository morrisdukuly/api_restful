from app import app
from config import db
from models.Customer import Customer
from models.Order import Order
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
order_bp = Blueprint('order', __name__)


#---------------------------------------------------------------------------------------------------------
#======================================================ORDER===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout order

@app.route('/order/add', methods = ['POST'])
def order_add():
    try:
        json = request.json
        print(json)
        createDate = json['createDate']
        customerId = json['customerId']

        if createDate and request.method == 'POST':
           
            print("******************")

            orders = Order(createDate = createDate)

            if customerId :
                customer = Customer.query.filter_by(id = customerId).first()
                print(customer)
                orders.customer = customer

            db.session.add(orders)
            db.session.commit()
            resultat = jsonify('Order add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#======================================================GET===============================================

#Methode GET pour Cash

@app.route('/order', methods = ['GET'])
def get_orders():
    try:
        ordersx = Order.query.all()
        data = [
                {
                    "id":orders.id, 
                    "createDate":orders.createDate, 
                    "customerId":orders.customerId, 
                } 
                for orders in ordersx
                ]

        resultat = jsonify({"status_code":200, "Order" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== UPDATE ===============================================


@app.route('/order/update', methods = ['POST', 'GET'])
def order_update():
    try:
        data = request.json
        id = data["id"]
        createDate = data['createDate']
        customerId = data['customerId']

        orders = Order.query.filter_by(id=id).first()
        
        if id and createDate and customerId and request.method == 'POST':

            orders.createDate = createDate
            orders.customerId = customerId

            db.session.commit()
            resultat = jsonify('Order is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== DELETE ===============================================

###DELETE de order
@app.route('/order/delete', methods = ['POST'])
def delete_order():
    try:
        json = request.json
        id = json['id']
        # customerId = json ['customerId']

        orders = Order.query.filter_by(id=id).first()

        db.session.delete(orders)
        db.session.commit()
        resultat = jsonify('Order is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

