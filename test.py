from msilib.schema import SelfReg
from typing import Self
import unittest
from flask import Flask, request
from flask.testing import FlaskClient
from app import app
from routes.customer_routes import customer_add

app.testing = True
# @app.route('/customer/add', methods = ['POST'])
# def customer_add():
#     try:
#         json = request.json
#         print(json)
#         name = json['name']
#         deliveryAddress = json['deliveryAddress']
#         contact = json['contact']
#         active = json['active']

#         if name and deliveryAddress and contact and active and request.method == 'POST':
#             return 'Valide'
#         else:
#             return 'error'
#     except Exception as e:
#         print(e)
#         return 'error'


class MyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_customer_add(self):
        customer_data = {
            "name": "Morris",
            "deliveryAddress": "Hedzranawoe",
            "contact": "97130480",
            "active": "True"
        }  
        response = self.app.post('/customer/add', json=customer_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Valide')

    
if __name__ == '__main__':
    unittest.main()
