from flask import jsonify
from serializator import *

from Model import Client, BaseModel
from app import app, engine


@app.route('/clients', methods=['GET'])
def main_route():
    entities = engine.session.query(Client.Client).all()
    data = jsonify(to_dict(entities))
    return data, 200
