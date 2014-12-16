from flask import Flask
from caloric import blueprints
from caloric.auth import jwt
from caloric.db import db


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_pyfile('config_default.py')

    if config:
        app.config.from_object(config)

    blueprints.register(app)

    db.init_app(app)

    jwt.init_app(app)

    return app
