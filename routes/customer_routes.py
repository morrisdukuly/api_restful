from app import app
from config import db
from models.Customer import Customer
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
customer_bp = Blueprint('customer', __name__)



#---------------------------------------------------------------------------------------------------------
#======================================================CUSTOMER===============================================
#---------------------------------------------------------------------------------------------------------


#======================================================POST===============================================


#Methode d'ajout customer

@app.route('/customer/add', methods = ['POST'])
def customer_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']

        if name and deliveryAddress and contact and active and request.method == 'POST':
           
            print(" ****************** ")
            customers = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)

            db.session.add(customers)
            db.session.commit()
            resultat = jsonify('Customer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#======================================================GET===============================================

#Methode GET pour Customer

@app.route('/customers', methods = ['GET'])
def get_customers():
    try:
        customersx = Customer.query.all()
        data = [
                {
                    "id":customers.id, 
                    "name":customers.name, 
                    "deliveryAddress":customers.deliveryAddress, 
                    "contact":customers.contact, 
                    "active":customers.active
                } 
                for customers in customersx
                ]

        resultat = jsonify({"status_code":200, "Customer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== UPDATE ===============================================


@app.route('/customer/update', methods = ['POST', 'GET'])
def customer_update():
    try:
        data = request.json
        id = data["id"]
        name = data["name"]
        deliveryAddress = data["deliveryAddress"]
        contact = data["contact"]
        active = data["active"]

        customers = Customer.query.filter_by(id=id).first()
        
        if id and name and deliveryAddress and contact and active and request.method == 'POST':

            customers.name = name
            customers.deliveryAddress = deliveryAddress
            customers.contact = contact
            customers.active = active
            db.session.commit()
            resultat = jsonify('Customer is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()

#====================================================== DELETE ===============================================

###DELETE de customer
@app.route('/customer/delete', methods = ['POST'])
def delete_customer():
    try:
        json = request.json
        id = json['id']

        customers = Customer.query.filter_by(id=id).first()

        db.session.delete(customers)
        db.session.commit()
        resultat = jsonify('Customer is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

