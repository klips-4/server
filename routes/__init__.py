import json

from flask import jsonify
from sqlalchemy import select


from Model import Client
from app import app, engine

@app.route('/clients', methods=['GET'])
def main_route():
    data =[]
    entities = engine.session.query(Client.Client).all()
    for product in entities:
        data.append(product.client_name)

    return data








