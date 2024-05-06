from flask import jsonify
from flask_sqlalchemy.session import Session

from Model import Client
from app import app, engine

@app.route('/clients', methods=['GET'])
def main_route():
    return 'Hello'







