import os
from nose.tools import nottest
from caloric.app import create_app
from caloric.db import db
from caloric.models.user import User
from caloric.tests import config

__author__ = 'marcusmccurdy'

BASE_PATH = os.path.dirname(__file__)


def setUp():
    test_db_path = os.path.join(BASE_PATH, 'test.db')
    if os.path.exists(test_db_path):
        os.unlink(test_db_path)
        
    app = create_app(config)

    with app.test_request_context():
        db.create_all(app=app)
        create_test_users()
        db.session.commit()


@nottest
def create_test_users():
    u = User('john@gmail.com', 'abc123')
    u.save()