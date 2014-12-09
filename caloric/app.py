from flask import Flask
from caloric import blueprints
from caloric.db import db


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config_default.py')

    blueprints.register(app)

    db.init_app(app)

    return app
