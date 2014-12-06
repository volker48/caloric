from flask import Flask
from caloric import blueprints


def create_app():
    app = Flask(__name__)
    blueprints.register(app)
    return app
