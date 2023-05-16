from app import app
from config import db
from models.Item import Item
from models.Order import Order
from models.OrderDetail import OrderDetail
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
orderDetail_bp = Blueprint('orderDetail', __name__)


#---------------------------------------------------------------------------------------------------------
#======================================================ORDER DETAIL===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout orderDetail

@app.route('/orderDetail/add', methods = ['POST'])
def orderdetail_add():
    try:
        json = request.json
        print(json)
        qty = json['qty']
        taxStatus = json['taxStatus']
        orderId = json['orderId']
        itemId = json['itemId']

        if qty and taxStatus and request.method == 'POST':
           
            print("******************")

            orderDetail = OrderDetail(qty = qty, taxStatus = taxStatus)

            if orderId :
                order = Order.query.filter_by(id = orderId).first()
                print(order)
                orderDetail.order = order

            if itemId :
                item = Item.query.filter_by(id = itemId).first()
                print(item)
                orderDetail.item = item

            db.session.add(orderDetail)
            db.session.commit()
            resultat = jsonify('New Order Detail add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour orderDetail

@app.route('/orderDetail', methods = ['GET'])
def get_orderdetails():
    try:
        order_detailsx = OrderDetail.query.all()
        data = [
                {
                    "id":orderDetail.id, 
                    "qty":orderDetail.qty, 
                    "taxStatus":orderDetail.taxStatus, 
                    "orderId" : orderDetail.orderId,
                    "itemId" : orderDetail.itemId
                } 
                for orderDetail in order_detailsx
                ]

        resultat = jsonify({"status_code":200, "Order details" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()



#====================================================== UPDATE ===============================================


@app.route('/order-detail/update', methods = ['POST', 'GET'])
def orderdetail_update():
    try:
        data = request.json
        id = data["id"]
        qty = data['qty']
        taxStatus = data['taxStatus']
        orderId = data['orderId']
        itemId = data['itemId']

        orderdetails = OrderDetail.query.filter_by(id=id).first()
        
        if id and qty and taxStatus and orderId and itemId and request.method == 'POST':

            orderdetails.qty = qty
            orderdetails.taxStatus = taxStatus
            orderdetails.orderId = orderId
            orderdetails.itemId = itemId

            db.session.commit()
            resultat = jsonify('Order detail is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()



#====================================================== DELETE ===============================================

###DELETE de orderDetail
@app.route('/orderDetail/delete', methods = ['POST'])
def delete_order_detail():
    try:
        json = request.json
        id = json['id']

        orderdetail = OrderDetail.query.filter_by(id=id).first()

        db.session.delete(orderdetail)
        db.session.commit()
        resultat = jsonify('Order detail is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


