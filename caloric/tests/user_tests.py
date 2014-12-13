import json
from flask import url_for
from caloric.tests.mixins import CaloricTest, RequestContextMixin

__author__ = 'marcusmccurdy'


class ViewTests(RequestContextMixin, CaloricTest):

    def setUp(self):
        super(ViewTests, self).setUp()
        self.url = url_for('user.login')

    def valid_login_test(self):
        res = self.json_post(self.url, {'email': 'john@gmail.com', 'password': 'abc123'})
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(json.loads(res.data), {'success': 'Logged in'})

    def bad_password_test(self):
        res = self.json_post(self.url, {'email': 'john@gmail.com', 'password': 'badpassword'})
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(json.loads(res.data), dict(error='Invalid email/password'))

    def non_existing_user_test(self):
        res = self.json_post(self.url, {'email': 'idontexist@gmail.com', 'password': 'password'})
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(json.loads(res.data), dict(error='Invalid email/password'))
