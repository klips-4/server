from flask import Flask
from classes.EngineConnect import EngineConnect
from sqlalchemy.orm import Session

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

engine = EngineConnect()

app = Flask(__name__)
CORS(app)
app.config.from_object('Config.common')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Model import Client
from routes import *

def get_clients():
    entities = engine.session.query(Client.Client).all()





if __name__ == '__main__':
    get_clients()
    app.run()
