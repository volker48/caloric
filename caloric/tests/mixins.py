import json
from unittest import TestCase
from flask import url_for
from caloric.app import create_app
from caloric.models.user import User
from caloric.tests import config

__author__ = 'marcusmccurdy'


class CaloricTest(TestCase):

    def setUp(self):
        self.app = create_app(config)
        self.test_app = self.app.test_client()

    def json_post(self, url, data=None):
        if data:
            data = json.dumps(data)
        return self.test_app.post(url, data=data, headers={'Content-Type': 'application/json'})


class RequestContextMixin(object):

    def setUp(self):
        super(RequestContextMixin, self).setUp()
        self.ctx = self.app.test_request_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()
        super(RequestContextMixin, self).tearDown()


class LoginMixin(object):
    username = 'john@gmail.com'
    password = 'abc123'

    def setUp(self):
        super(LoginMixin, self).setUp()
        url = url_for('jwt')
        data = {'username': self.username, 'password': self.password}
        res = self.test_app.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        payload = json.loads(res.data)
        self.token = payload['token']
        self.user = User.query.filter_by(email=self.username).one()
        self.headers = {'Authorization': 'Bearer {}'.format(self.token)}


