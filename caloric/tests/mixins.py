import json
from unittest import TestCase
from caloric.app import create_app
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

