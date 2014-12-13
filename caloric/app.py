from flask import Flask
from caloric import blueprints
from caloric.auth import login_manager
from caloric.db import db


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_pyfile('config_default.py')

    if config:
        app.config.from_object(config)

    blueprints.register(app)

    db.init_app(app)

    login_manager.init_app(app)

    return app
