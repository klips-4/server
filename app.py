from flask import Flask
from classes.EngineConnect import EngineConnect

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

engine = EngineConnect()

app = Flask(__name__)
CORS(app)
app.config.from_object('Config.common')
db = SQLAlchemy(app)
Model = db.Model
migrate = Migrate(app, db)


from routes import *


if __name__ == '__main__':
    app.run()
