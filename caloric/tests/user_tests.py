import json
from flask import url_for
from nose.tools import nottest
from caloric.models.user import User
from caloric.tests.mixins import CaloricTest, RequestContextMixin

__author__ = 'marcusmccurdy'


class LoginTests(RequestContextMixin, CaloricTest):

    def setUp(self):
        super(LoginTests, self).setUp()
        self.url = url_for('jwt')

    def valid_login_test(self):
        res = self.json_post(self.url, {'username': 'john@gmail.com', 'password': 'abc123'})
        self.assertEqual(res.status_code, 200)
        payload = json.loads(res.data)
        self.assertTrue('token' in payload)

    def bad_password_test(self):
        res = self.json_post(self.url, {'username': 'john@gmail.com', 'password': 'badpassword'})
        self.assertEqual(res.status_code, 400)

    def non_existing_user_test(self):
        res = self.json_post(self.url, {'username': 'idontexist@gmail.com', 'password': 'password'})
        self.assertEqual(res.status_code, 400)


class UserApiTests(RequestContextMixin, CaloricTest):

    @nottest
    def get_user_test(self):
        test_user = User.query.filter_by(email='john@gmail.com').one()
        url = url_for('user.user', user_id=test_user.id)
        res = self.test_app.get(url)
        self.assertEqual(res.status_code, 200)
        loaded = json.loads(res.data)
        self.assertEqual(test_user.email, loaded['email'])


